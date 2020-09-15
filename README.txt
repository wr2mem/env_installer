# BlackArch Env Installer --
# This script sets up and slick working Awesome WM 4.x exploitation enviromment.
# It is tailored for those that are very command line saavy.

# About --
- oh-my-zsh: 
-   custom exploitation based .zshrc
-   docker msf v6 intergation
-   zsh-autosuggestions 
-   zsh-syntax-highlighting 
-   zsh large paste fix:
      -> https://gist.github.com/magicdude4eva/2d4748f8ef3e6bf7b1591964c201c1ab
      
# Setup --
- fzf - term based fuzzy finder
- the_silver-searcher ( advanced grep )
- fd-find ( advanced find w/ fzf integration )
- extended grc.zsh
- themed terminator configurations
- themed termite
- nerd-fonts
- BMZ-cursor
- awesome wm autorun.sh - not working.
-   -> manual fix: /bin/echo -n 'awful.spawn.with_shell("~/.config/awesome/autorun.sh")' | /sbin/sudo \
    tee -a /etc/xdg/awesome/rc.lua
- rofi simple switcher - drun / combi
- picom transprancy
- golang / gotop default install
- lxdm login manager

- neovim dev IDE w/ CoC language engine plugins
- manual setup link --
    -> https://github.com/vadersecurity/env_installer/tree/master/config/editor/nvim

- screenshots included

- needs testing --
