#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# install.py
# dualfade[at]vadersecurity.com

# import --
import os
import sys
import time
import shutil
import subprocess
from os import path
from pyfiglet import Figlet

# about --
# this installer will setup BlackArch Awesome WM 4.x
# the env will have all the necassary configurations for quick exploitation
# and cli access.

# deps --
# install before running this script --
# sudo pacman -Syu git python-pyfiglet
# git clone https://github.com/vadersecurity/env_installer.git
# cd env_installer ; python env_install.py

# definitions --
def splash_screen():
    custom_fig = Figlet(font='graffiti')
    print(custom_fig.renderText('VADER SECURITY'))
    print('\t\tAwesome WM 4.x penetration testing env install\n')
    print('[i] This program requires root or sudo access.')
    print('[?] Do you wish to proceed with the env_install ?')
    t = input('[?] selection [y/N]: ')
    if ( t == 'y' ):
        print('[+] Rock n Roll! let\'s do this...')
        time.sleep(1)
        return
    else:
        print('[!] Boo.. Exiting now.')
        sys.exit()

def start_package_installer():
    """ Starting env_installer -- """
    """ aur access needs to be setup """
    print('[+] Starting required package installation:')
    try:
        pac_update = subprocess.run(['/sbin/sudo', '/sbin/pacman', '-Syu'])
        pac_p_installer = subprocess.run(['/sbin/sudo', '/sbin/pacman', '-S', 'yay', 'picom', 'rofi', 'zsh', 'lxdm', 'grc', 'neovim', 'termite', \
                                          'terminator', 'fzf', 'the_silver_searcher',  'fd', 'amass', 'gospider', 'go', \
                                          'httpx', 'waybackurls', 'subfinder', 'zdns', 'hakrawler', 'screen'])
        print('[+] Starting System update: %d' %pac_update.returncode)
        print('[+] Installing packages: %d' %pac_p_installer.returncode)
        return
    except subprocess.CalledProcessError as err:
        print('[!] Installation failed.')
        print('[?] please review the error.')
        print('ERROR:', err)

def zsh_install():
    """ oh-my-zsh installation -- """
    try:
        print('[+] Installing oh-my-zsh:')
        home = str(path.dirname('/home/%s/') % arg2)
        repo = "".join([home, '/.oh-my-zsh/'])
        """ clone oh-my-zsh -- """
        om_zsh_clone = subprocess.check_call(['/sbin/git', 'clone', 'https://github.com/ohmyzsh/ohmyzsh.git', repo])
        print('[+] Cloning repository: %d' %om_zsh_clone)

        """ check for existing .zshrc / back it up -- """
        """ copy new .zshrc into place -- """
        src = './config/shell/zsh/zshrc'
        dst = "".join([home, '/.zshrc'])

        e_zshrc = os.path.isfile('%s/.zshrc' % home)
        if e_zshrc == True:
            print('[i] Backing up existing .zshrc')
            shutil.copy(dst, '%s/.zshrc.backup' % home)
        shutil.copy(src, dst)

        """ update local shell -- """
        update_shell = ('/sbin/sudo /sbin/chsh -s /usr/bin/zsh %s' % arg2)
        shell_update = subprocess.Popen(update_shell, shell=True)
        resp = shell_update.wait()
        print(resp)
        return(home) 
    except subprocess.CalledProcessError as err:
        print('[!] Installation failed.')
        print('ERROR:', err)

def start_local_config_setup():
    """ install config files for awesome wm 4.x """
    d_cnf_dirs = ['termite', 'terminator', 'rofi', 'picom', 'nvim', 'awesome']
    try:
        print('[+] Installing configuarion files:')
        dot_config = "".join([home, '/.config'])
        os.mkdir(dot_config, mode=0o755)
        for cnf_dir in d_cnf_dirs:
            c_cnf_dir = "".join([home, '/.config/', cnf_dir])
            """ not a type-o / pythons dumb way of permissions -- """
            os.mkdir(c_cnf_dir, mode=0o755)

        """ copy config to ~/.config/<dir> -- """
        print('[+] Copying local configs into place.')
        shutil.copy('./config/termite/config', '%s/.config/termite/' % home)
        shutil.copy('./config/terminator/config', '%s/.config/terminator/' % home)
        shutil.copy('./config/rofi/config.rasi', '%s/.config/rofi/' % home)
        shutil.copy('./config/picom/picom.conf', '%s/.config/picom/' % home)
        shutil.copy('./config/editor/nvim/init.vim', '%s/.config/nvim/' % home)
        shutil.copy('./config/wm/awesome/autorun.sh', '%s/.config/awesome/' % home)
        shutil.copy('./config/x11/Xdefaults', '%s/.Xdefaults' % home)
        shutil.copy('./config/screen/screenrc', '%s/.screenrc' % home)
        print('\n[i] neovim IDE installation --')
        print('[i] ref: https://github.com/vadersecurity/env_installer/tree/master/config/editor/nvim')
        print('[i] ref: https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions')
        print('[i] This will be automated; but until then...\n')
        time.sleep(2)

        """ create github / nmap_auto script directory -- """
        c_github = subprocess.check_call(['/bin/mkdir', '-p', '%s/Github/Misc/nmapAutomator' % home]) 
        print('[+] Creating Github directory: %d' %c_github)
        shutil.copy('./config/scan/nmap/nmap_auto.sh', '%s/Github/Misc/nmapAutomator/' % home)

        """ create templates / cherrytree script directory -- """
        c_templates = subprocess.check_call(['/bin/mkdir', '-p', '%s/Github/Misc/Templates/Cherrytree' % home]) 
        shutil.copy('./config/templates/cherrytree/default_target_teplate.ctb', '%s/Github/Misc/Templates/Cherrytree/' % home)
        print('[+] Creating Templates directory: %d' %c_templates)

        """ add $HOME/go -- """
        c_godir = subprocess.check_call(['/bin/mkdir', '-p', '%s/go' % home]) 
        print('[+] Creating go directory: %d' %c_godir)
    except OSError as err:
        print('[!] Config installation failed.')
        print('ERROR:', err)

def start_priv_config_setup():
    """ install privilges configurations -- """
    print('\n[i] Installing privileged config files.')
    time.sleep(2)
    try:
        grc = subprocess.check_call(['/sbin/sudo','/bin/cp', '-Rvp', './config/syntax/grc/grc.zsh', '/etc/grc.zsh']) 
        print('[+] Installing grc.zsh: %d' %grc)
        grc_perms = subprocess.check_call(['/sbin/sudo','/sbin/chown', '-R', 'root:root', '/etc/grc.zsh']) 
        print('[+] Setting grc.zsh permissions: %d' %grc_perms)
        lxdm = subprocess.check_call(['/sbin/sudo','/bin/cp', '-Rvp', './config/wm/lxdm/lxdm.conf', '/etc/lxdm/lxdm.conf']) 
        print('[+] Installing lxdm.conf: %d' %lxdm)
        lxdm_perms = subprocess.check_call(['/sbin/sudo','/sbin/chown', '-R', 'root:root', '/etc/lxdm/lxdm.conf']) 
        print('[+] Setting lxdm.conf permissions: %d' %lxdm_perms)

        """ installing wallpaper -- """
        mkdir_custom = subprocess.check_call(['/sbin/sudo','/bin/mkdir', '/usr/share/backgrounds/custom']) 
        print('[+] Installing lxdm.conf: %d' %mkdir_custom)
        cp_wallpaper = subprocess.check_call(['/sbin/sudo','/bin/cp', '-Rvp', './config/wallpaper/vader_security.png', '/usr/share/backgrounds/custom/']) 
        print('[+] Setting lxdm.conf permissions: %d' %cp_wallpaper)
        wp_perms = subprocess.check_call(['/sbin/sudo','/sbin/chown', '-R', 'root:root', '/usr/share/backgrounds/custom/vader_security.png']) 
        print('[+] Setting lxdm.conf permissions: %d' %wp_perms)

        """ add autorun.sh -- """
        """ update /etc/xdg/awesome/rc.lua -- """
        time.sleep(2)
        """ need to check this ?? """
        """ not working right -- """
        rc_lua_autorun = subprocess.check_call(['/bin/echo', '-n', '"awful.spawn.with_shell(\"~/.config/awesome/autorun.sh\")"', \
                                                '|', '/sbin/sudo', 'tee', '-a', '/etc/xdg/awesome/rc.lua']) 
        print('\n[+] Adding autorun.sh to rc.lua: %d' %rc_lua_autorun)

    except subprocess.CalledProcessError as err:
        print('[!] Installation failed.')
        print('ERROR:', err)

def install_missing_apps():
    """ install cherrytree-git / bmz-cursor-theme-git after yay is installed """
    """ add yaccl aliaes cache cleanup -- """
    try:
        yay_p_update = subprocess.check_call(['/sbin/yay', '-Syu'])
        print('[+] Updating packages: %d' %yay_p_update)
        yay_p_installer = subprocess.check_call(['/sbin/yay', '-S', 'cherrytree', 'bmz-cursor-theme-git', 'nerd-fonts-complete', 'virtualbox', 'docker', 'gotop'])
        print('\n[+] Installing aur packages: %d' %yay_p_installer)
        print('[i] yay zsh archlinux plugin cmd ref:')
        print('[i] https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/archlinux\n')
        print('[i] enable docker: sudo systemctl enable docker')
        print('[i] ref: https://gist.github.com/dualfade/fea1b8efcc6125c2c7b11cb92ac1a90c')
        time.sleep(2)
        print('[+] Adding gotop --')
        i_gotop = subprocess.check_call(['/usr/lib/go/bin/go', 'get', 'github.com/cjbassi/gotop'])
        print('\n[+] Fetching gotop latest src: %d' %i_gotop)
        print('[+] Creating go directory struct')
    except subprocess.CalledProcessError as err:
        print('[!] Installation failed.')
        print('ERROR:', err)

def clean_local_cache():
    """ clean local repo cache -- """
    try:
        yay_c_cache = subprocess.check_call(['/sbin/yay', '-Sc', '<<<y'])
        print('[+] Cleaning local repo cache: %d' %yay_c_cache)
        time.sleep(2)
    except subprocess.CalledProcessError as err:
        print('[!] Installation failed.')
        print('ERROR:', err)


# main --
if __name__ == '__main__':
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    except IndexError:
        print("[-] Usage: %s install user" % sys.argv[0])
        print("[-] Usage: python env_install.py install vagrant")
        sys.exit(-1)

# start installer --
if ( arg1 == 'install' ):
    splash_screen()
    start_package_installer()
    time.sleep(2)
    home = zsh_install()
    start_local_config_setup()
    start_priv_config_setup()
    install_missing_apps()
    clean_local_cache() 
    print('\n[i] Installation Done.')
    print('[+] logout out or reboot.')
    sys.exit(-1)
else:
    print('[!] Exiting now.')
    sys.exit(-1)

# __EOF__
