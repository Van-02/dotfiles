# Dotfiles & Configs

![Qtile](.screenshots/qtile.png)

## Information

- **OS: [Arch Linux](https://wiki.archlinux.org/title/Installation_guide)**
- **WM: [Qtile](https://qtile.org/)**
- **Login [LightDM](https://github.com/canonical/lightdm)**
- **Terminal: [Alacritty](https://alacritty.org/)**
- **Shell: [Zsh](https://zsh.sourceforge.io/)**
- **Prompt: [Powerlevel10k](https://github.com/romkatv/powerlevel10k)**
- **Editor: [Neovim](https://neovim.io/)/[VScode](https://code.visualstudio.com/)**
- **Compositor: [Picom](https://github.com/yshui/picom)**
- **Application Launcher: [Rofi](https://github.com/davatorium/rofi)**
- **Browser: [Firefox](https://www.mozilla.org/en-US/firefox/new/)**
- **File Manager: [Ranger](https://github.com/ranger/ranger)/[Thunar](https://docs.xfce.org/xfce/thunar/start)**

## How to install my setup

This guide begins after a clean installation of [Arch Linux](https://wiki.archlinux.org/title/Installation_guide). The first thing we need to do is install [NetworkManager](https://wiki.archlinux.org/title/NetworkManager), a program that provides system detection and configuration to automatically connect to networks.

```
pacman -S networkmanager reflector
systemctl enable NetworkManager
```

Now, with [Reflector](https://wiki.archlinux.org/title/reflector), we are going to update and configure the mirrorlist.

```
reflector --latest 10 --sort rate --save /etc/pacman.d/mirrorlist
```

We will install [Grub](https://www.gnu.org/software/grub/) as the boot manager.

```
pacman -S grub efibootmgr os-prober
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=Arch
```

If you want to have dual boot, run os-prober and check if it recognizes the operating system. Then, generate the configuration file for Grub.

```
os-prober
grub-mkconfig -o /boot/grub/grub.cfg
```

Now, create the user and assign a password. Replace "username" with the name of your user.

```
useradd -m username
passwd username
usermod -aG wheel,video,audio,storage username
```

Also, we need to install [sudo](https://wiki.archlinux.org/title/sudo) to have superuser privileges.

```
pacman -S sudo vim nano
```

Uncomment and add the following line in `/etc/sudoers`

```
## User privilege specification
root ALL=(ALL:ALL) ALL
username ALL=(ALL:ALL) ALL  <-- Add this line

## Uncomment to allow members of group wheel to execute any command
# %wheel ALL=(ALL:ALL) ALL  <-- Uncomment this line
```

I install [Paru](https://github.com/Morganamilo/paru) to have more options when downloading packages.

```
sudo pacman -S git
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
```

Now reboot

```
exit
reboot
```

Now we will install [Xorg](https://wiki.archlinux.org/title/Xorg), which will allow us to have a graphical environment at our disposal.

```
sudo pacman -S xorg xorg-server
```

## Login and windows display manager

After finishing the installation of Arch Linux, it's time to install a Login Display Manager that will allow us to log in to our desktop environment. I will use [LightDM](https://github.com/canonical/lightdm), but you can use any other. Also, install what is necessary to enter the desktop environment.

```
sudo pacman -S lightdm lightdm-gtk-greeter lightdm-webkit2-greeter qtile xterm firefox
paru -S lightdm-webkit-theme-aether
sudo systemctl enable lightdm
reboot
```

Now you should be able to log in to Qtile from LightDM. Afterwards, we will modify the theme and configuration of LightDM and Grub.

## Features of Qtile

- Simple, small and extensible. It’s easy to write your own layouts, widgets and commands.
- Configured in Python.
- Command shell that allows all aspects of Qtile to be managed and inspected.
- Complete remote scriptability - write scripts to set up workspaces, manipulate windows, update status bar widgets and more.
- Qtile’s remote scriptability makes it one of the most thoroughly unit-tested window managers around.

## How to install Qtile

With `Mod + Enter` open a Terminal

Install Qtile and dependencies:

```
sudo pacman -S qtile pacman-contrib cbatticon volumeicon udiskie picom network-manager-applet feh thunar ranger alacritty rofi which pulseaudio pavucontrol pamixer brightnessctl arandr libnotify notification-daemon p7zip lxappearance imv redshift scrot zsh
```

Clone and copy this repository

```
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.config/* ~/.config/.
cp dotfiles/.xsession ~/.
chmod u+x .xsession
```

Reload with `Mod + Ctrl + q`
