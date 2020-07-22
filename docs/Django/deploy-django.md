# Deploy Django

In this blog, we will learn how to deploy Django Application with uWSGI and nginx on CentOS’7. Django is the most popular python based backend framework with the aim of rapid web development. Before installing anything, I recommend to read my [previous post](/django/initial-server-setup) where I have discussed about initial server setup with ssh keys.

## 1. Installing the prerequisites

### Installing python3.6

First install the latest packages from EPEL and RPM. EPEL(Extra Packages for Enterprise Linux) is an open source repository that contains the latest packages for Red Hat Linux distributions. RPM is also an open source package management system from Red Hat. After all this, lets install python3 –

```bash
sudo yum install -y epel-release
sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
sudo yum update
sudo yum install -y python36u python36u-libs python36u-devel python36u-pip python-devel
```

### Upgrading pip and installing virtualenv

Pip is the most popular python package installer. Virtual environments are used for separating the different versions of any package for different projects.

```bash
sudo pip3.6 install --upgrade pip
sudo pip install virtualenv virtualenvwrapper
```

### Configuring the shell

We will use Env directory to hold all our virtual environments. This can be configured in `.bashrc` file.

```bash
echo "export WORKON_HOME=~/Env" >> ~/.bashrc
echo "source /usr/bin/virtualenvwrapper.sh" >> ~/.bashrc
```

Now, open `/usr/bin/virtualenvwrapper.sh` with either vim or nano. Find the line –

```none
VIRTUALENVWRAPPER_PYTHON="$(command \which python)"
```

and replace python with python3.6 as –

```none
VIRTUALENVWRAPPER_PYTHON="$(command \which python3.6)"
```

Now, lets reflect these changes –

```bash
source ~/.bashrc
```

## 2. Configuring Django project

### Creating virtual environments

```bash
mkvirtualenv env_1
```

The environment env_1 gets automatically activated. The same can be verified by –

```bash
which pip
# Output: ~/Env/env_1/bin/pip
```

### Copying Django project from local to remote

Since, we have activated our virtual env, now we will copy our django project to remote server using scp. If you have uploaded it on github, just install git via yum and then git clone the project. But before doing this, lets grab all the requirements of the project. If your project already contains a requirements file, then you can skip this part. “cd” into your project’s directory and after activating virtual env in your local machine, use the following command to list out requirements in requirements.txt file in your local terminal-

```bash
pip freeze > requirements.txt
```

Now, to copy the project, use the following command in your local terminal. Do remember to put your ip and user_name configured in previous post. Write the complete path of your django project from root in local machine. This will copy the project in the home directory of the server.

```bash
scp -r /path/to/project user_name@your_ip_here:~
```

Now, connect to your server and activate the virtual env.

```bash
ssh user_name@your_ip_here
workon env_1
```

Let’s install all the requirements for the project. Use the path to requirements.txt file.

```bash
pip install -r /path/to/requirements.txt
```

### Installing MySQL from rpm

```bash
sudo rpm -ivh https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm
```

Check if Mysql repo has been enabled –

```bash
sudo yum repolist all | grep mysql | grep enabled
# Output : enabled
```

Install and enable mysql –

```bash
sudo yum -y install mysql-community-server
sudo systemctl start mysqld
sudo systemctl enable mysqld
sudo systemctl status mysqld
```

Copy the mysql temporary root password from the command given below and paste this while secure installation of mysql. Change the root password and hit Enter for default actions.

```bash
cat /var/log/mysqld.log | grep -i 'temporary password'
mysql_secure_installation
```

We have successfully installed mysql and now, we need a database to run our project. First, open the mysql interface and enter the root password –

```bash
mysql -u root -p
```

Now, in mysql, create a database –

```bash
mysql> CREATE DATABASE first_db;
mysql> SHOW DATABASES;
mysql> exit
```

After this, we need to install a client to communicate with mysql –

```bash
sudo yum install -y mysql-connector-python.x86_64 mysql-community-devel.x86_64 mysql-cluster-community-client.x86_64 mysql-shell.x86_64 mysql-router.x86_64 gcc
pip install mysqlclient # inside the virtual environment
```

### Changing settings.py file

With everything installed, let’s change some settings for the project –

```bash
sudo nano ~/project_name/project_name/settings.py
```

Add the following line to the last of the file. As we will be using nginx to deploy the application, this line tells django to place our static files in ‘static’ directory. This helps nginx to easily serve these static files.

```python
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
```

Do not forget to change the default database configurations to –

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'first_db',
        'USER': 'root',
        'PASSWORD': 'your-root-password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

And also add your ip in the allowed hosts –

```python
ALLOWED_HOSTS = ['your_ip_here']
```

### Opening port 8000

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-port=8000/tcp
sudo firewall-cmd --complete-reload
sudo firewall-cmd --list-all
```

### Running the application

First, flush out the initial migrations and delete the sqlite database. “cd” into your project’s directory and use the following commands –

```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
rm -f db.sqlite3
```

Run the migrations to sync up with database –

```bash
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
```

So, finally we can run the server and see the application accessible globally –

```bash
python manage.py runserver 0.0.0.0:8000
```

Go to the web browser and enter your_ip:8000 to access the django application.

## 3. Setting up uWSGI and nginx

### Configuring uWSGI globally

Store all the configuration files to /etc/uwsgi/sites. You should use your project name for all configurations –

```bash
sudo pip install uwsgi
sudo mkdir -p /etc/uwsgi/sites
cd /etc/uwsgi/sites
sudo nano project_name.ini
```

Add the following lines to the .ini file. Do remember to use your project and user name.

```bash
[uwsgi]
project = project_name
username = user_name
base = /home/%(username)

chdir = %(base)/%(project)
home = %(base)/Env/env_1
module = %(project).wsgi:application

master = true
processes = 5

uid = %(username)
socket = /run/uwsgi/%(project).sock
chown-socket = %(username):nginx
chmod-socket = 660
vacuum = true
```

Ctrl+x to exit and press y to save the changes. Base and home contain the full path for the home directory and virtual environment respectively. We have created a master process for loading our app server. Here, we have used Unix Socket. This socket uses uWSGI protocol which helps nginx to reverse proxy.

```bash
sudo nano /etc/systemd/system/uwsgi.service
```

Add the following lines. Do remember to use your user name in ExecStartPre of Service section.

```bash
[Unit]
Description=uWSGI Emperor service

[Service]
ExecStartPre=/usr/bin/bash -c 'mkdir -p /run/uwsgi; chown user_name:nginx /run/uwsgi'
ExecStart=/usr/bin/uwsgi --emperor /etc/uwsgi/sites
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

[Unit] section describes our service. [Service] section manages various applications. [Install] section ties up multi-user system state.

### Configuring Nginx

Installing Nginx -

```bash
sudo yum -y install nginx
sudo nano /etc/nginx/nginx.conf
```

Add the following lines. Do remember to use your user name and project name in root and uwsgi_pass.

```bash
server {
    listen 8000;
    server_name localhost;

    location = favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/user_name/project_name;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/run/uwsgi/project_name.sock;
    }
}
```

Above, we have set up a server block, with an open port to listen from. We have also specified the static file location and passed all the traffic to unix socket. Make sure the syntax of nginx file is correct and change permissions of the user.

```bash
sudo nginx -t
sudo usermod -a -G user_name nginx
chmod 710 /home/user_name
```

Start and enable the nginx and uwsgi.

```bash
sudo systemctl start nginx
sudo systemctl start uwsgi
sudo systemctl enable nginx
sudo systemctl enable uwsgi
```

Now you can directly access the django application from the ip with an open port.
Thanks for reading!
