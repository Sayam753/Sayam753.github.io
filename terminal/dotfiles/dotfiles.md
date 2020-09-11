# Dotfiles

This blog post contains my daily used dotfiles which I do not wish to lose.

## .gitconfig

```none
[user]
	name = Sayam753
	email = sayamkumar753@yahoo.in
	signingkey = 69184FFA974E07E4
[core]
	excludesfile = /Users/user/.gitignore_global
[commit]
	gpgsign = true
[gpg]
	program = gpg2
```

## .gitignore_global

```none
.history
.vscode
.mypy_cache
.DS_Store
```

## .pylintrc

```none
[DEFAULT]
init-hook=
    import pylint_venv
    pylint_venv.inithook()
```

## .tmux.conf

```none
  
set -g default-terminal "xterm-256color"
set -g prefix C-z
unbind C-b
bind C-z send-prefix
```

## .vscode_settings.json

```json
{
    // Editor options
    "editor.wordWrap": "off",
    "editor.minimap.enabled": false,
    "editor.detectIndentation": false,
    "editor.suggestSelection": "first",
    // Workbench options
    "workbench.settings.editor": "json",
    "workbench.sideBar.location": "left",
    "workbench.iconTheme": "vscode-icons",
    "workbench.settings.openDefaultSettings": true,
    // Terminal options
    "terminal.integrated.shell.osx": "/bin/zsh",
    "terminal.integrated.fontFamily": "Inconsolata-g for Powerline",
    // Python options
    "python.pythonPath": "/usr/local/bin/python3",
    "python.venvPath": "/Users/user/Env",
    // Autopep8 options
    "python.languageServer": "Microsoft",
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.formatting.blackPath": "/usr/local/bin/black",
    "python.formatting.blackArgs": [
        "--line-length=100"
    ],
    // Pylint options
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.pylintUseMinimalCheckers": false,
    "python.linting.pylintPath": "/usr/local/bin/pylint",
    "python.linting.pylintCategorySeverity.refactor": "Information",
    "python.linting.pylintArgs": [
        "--enable=F, E, C, R, W",
    ],
    // Pydocstyle options
    "python.linting.pydocstyleEnabled": true,
    "python.linting.pydocstylePath": "/usr/local/bin/pydocstyle",
    "python.linting.pydocstyleArgs": [
        "--convention=numpy"
    ],
    // Mypy options
    "python.linting.mypyEnabled": true,
    "python.linting.mypyPath": "/usr/local/bin/mypy",
    "python.linting.mypyArgs": [
        "--ignore-missing-imports"
    ],
    // Misc
    "git.confirmSync": false,
    "C_Cpp.updateChannel": "Insiders",
    "files.exclude": {
        "**/.classpath": true,
        "**/.project": true,
        "**/.settings": true,
        "**/.factorypath": true,
        "**/.history": true,
        "**/.idea": true,
        "**/.mypy_cache": true,
        "**/__pycache__": true
    },
}
```

## .zshrc

```bash
# Customizing prompt
autoload -Uz vcs_info
autoload -U colors && colors
precmd() { vcs_info }

zstyle ':vcs_info:git:*' formats '%F{011}( %b)%f'

setopt PROMPT_SUBST
PROMPT='%F{166}Sayam%f:%F{040}%1~%f ${vcs_info_msg_0_}%{$reset_color%}$ '

# Personal configurations
source /usr/local/bin/virtualenvwrapper.sh
export WORKON_HOME=~/Env
alias p=python3
alias jn="jupyter notebook"

## Exports to deal with servers
export LANG="en_US.UTF-8"
export LC_COLLATE="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
export LC_MESSAGES="en_US.UTF-8"
export LC_MONETARY="en_US.UTF-8"
export LC_NUMERIC="en_US.UTF-8"
export LC_TIME="en_US.UTF-8"
```
