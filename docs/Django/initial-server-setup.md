# Initial Server Setup

In this blog, we will be going through initial server setup on Centos7. This is generally recommended before diving straight into production. Centos is an open source Linux distribution under RHEL(Red Hat Enterprise Linux). The reason why Centos is preferred over Ubuntu is because of its stability. Its updates can take about more than 7-8 years to come.

## 1. Configuring Centos 7

After purchasing a server, login into it using the ssh command in the terminal. Remember to use your public ip and the password given by the administrator.

```bash
ssh root@your_ip_here
```

If you are getting a warning like “LC_CTYPE: cannot change locale (UTF-8): No such file or directory”, then enter the following command in your local terminal by logging out. The LC variables determine the language of encoding the characters. So, we need to export this variable.

```bash
logout
export LC_ALL="en_US.UTF-8"
ssh root@your_ip_here
```

### Updating centos

```bash
sudo yum update
sudo yum upgrade
```

### Setting up hostname

```bash
hostnamectl set-hostname centos-server
hostname # to check the hostname
```

### Setting up hostname in the hosts file

```bash
sudo nano /etc/hosts
```

Add your ip followed by tab and then type centos-server which is the hostname. Then hit CTRL+x to exit and enter to save the changes.

## 2. Adding a new user

Root has the most privileges in the OS. It can be destructive to operate the server under root user. To limit the scope, we will be creating a new user. In future, if any need arises, we will change the permissions for this user.

```bash
adduser user_name
passwd user_name #setting up password for new user
gpasswd -a user_name wheel #adding sudo privileges
logout
```

## 3. Securing the server

There are bots all around trying to find vulnerabilities in the servers. Till now, we have used password based authentication which is highly exploitable. These bots try brute force attacks to enter our server. So to fix this, we will disable password based authentication and setup ssh keys. These ssh keys will be stored in the local machine and the server. After this whenever we try to ssh into our server, it will analyse the keys and give access. So, setting up ssh keys for authentication in the local machine in home directory. Hit enter for default actions –

```bash
ssh-keygen -t rsa #generating keys
ssh-copy-id user_name@your_ip_here #coping the keys to the server
logout
```

Now you can ssh login without password for the new user –

```bash
ssh user_name@your_ip_here
```

Change configuration in `/etc/ssh/sshd_config`, thereby making our server more secure –

```none
PermitRootLogin no
PasswordAuthentication no
```

```bash
sudo nano /etc/ssh/sshd_config
sudo systemctl restart sshd
```

Up next – Deploy Django Applications on Centos
Thanks for reading!
