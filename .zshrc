# Fix the Java Problem
export _JAVA_AWT_WM_NONREPARENTING=1

setopt histignorealldups sharehistory

# Use emacs keybindings even if our EDITOR is set to vi
bindkey -e

# Keep 1000 lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zsh_history

# Initialize TMUX
if command -v tmux &> /dev/null && [ -z "$TMUX" ]; then
    tmux attach-session -t default || tmux new-session -s default
fi

# Use modern completion system
autoload -Uz compinit
compinit

zstyle ':completion:*' uto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete _correct _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' menu select=2
eval "$(dircolors -b)"
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true

zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'

# Manual configuration

PATH=/root/.local/bin:/snap/bin:/usr/sandbox/:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/usr/share/games:/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games

# Custom aliases
#-------------------------------------------------------------------------------
# bat
alias cat='bat'
alias catn='bat --style=plain'
alias catnp='bat --style=plain --paging=never'

# ls
alias ls='exa --group-directories-first'
alias ll='exa -l --group-directories-first'
alias la='exa -a --group-directories-first'
alias l='exa --group-directories-first'
alias lla='exa -la --group-directories-first'
alias tree='exa -T'

# fzf
alias fzfbat='fzf --preview="bat --theme=Dracula --color=always {}"'
alias fzfnvim='nvim $(fzf --preview="bat --theme=Dracula --color=always {}")'

# nvim

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# Plugins
# -----------------------------------------------------------------------------
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/sudo/sudo.plugin.zsh
source /usr/share/zsh/plugins/starship/starship.plugin.zsh

eval "$(zoxide init zsh)"

export EDITOR='nvim'
export VISUAL='nvim'

# Functions
# -----------------------------------------------------------------------------
# Set 'man' colors
function man() {
    env \
    LESS_TERMCAP_mb=$'\e[01;31m' \
    LESS_TERMCAP_md=$'\e[01;31m' \
    LESS_TERMCAP_me=$'\e[0m' \
    LESS_TERMCAP_se=$'\e[0m' \
    LESS_TERMCAP_so=$'\e[01;44;33m' \
    LESS_TERMCAP_ue=$'\e[0m' \
    LESS_TERMCAP_us=$'\e[01;32m' \
    man "$@"
}


bindkey "^[[H" beginning-of-line
bindkey "^[[F" end-of-line
bindkey "^[[3~" delete-char
bindkey "^[[1;3C" forward-word
bindkey "^[[1;3D" backward-word

eval "$(starship init zsh)" 

# Created by `pipx` on 2026-01-23 00:12:06
export PATH="$PATH:/home/van/.local/bin"
