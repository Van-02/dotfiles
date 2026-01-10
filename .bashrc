#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Custom aliases
#----------------------------------------------------
# ls
alias ls='exa --group-directories-first'
alias ll='exa -l'
alias la='exa -a'
alias lla='exa -la --group-directories-first'
alias tree='exa -T'

#grep
alias grep='grep --color=auto'

# bat
alias cat='bat --style=plain --paging=never'
alias dotfiles="git --git-dir $HOME/.dotfiles/ --work-tree $HOME"

# nvim
alias nvim='/opt/nvim/bin/nvim'

[ -f ~/.fzf.bash ] && source ~/.fzf.bash

# Plugins
#----------------------------------------------------

# Git Prompt
# https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh
. ~/.git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1
export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[33m\]$(__git_ps1 "(%s)")\[\033[37m\]\$\[\033[00m\] '

# Bash Completion
# Enable bash programmable completion features in interactive shells
if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi

eval "$(starship init bash)"
