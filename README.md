# archer
This playbook tries to make it easier to install arch linux :tada:

Some caveats I should mention.
* This only works with EFI boot.
* I dont use swap space. It's 2020 and we have gobs of memory.
* I dont really have a good way to handle the arch-chroot. As a result we have and init and post script.

#### Default packages
Here is a list of the default packages if you do not edit them.
- ansible
- git
- gnome
- gdm
- neovim
- networkmanager
- mumble
- signal-desktop
- google-chrome
- pamac-aur

**Note:** This is not meant to cover everyone's use case. If you want to make this better that would be awesome.

### Arch ISO settings
:warning: **do not forget this step or packages wont install**

Hit `E` at the boot screen and add `cow_spacesize=1G` at the end of the boot parameters.

### Fork the repo
Fork this repo so its easier to edit the variables.

### Edit the variables
Edit the variables in [inventory/host_vars/localhost.yml](inventory/host_vars/localhost.yml)

:warning: I wouldn't change the `pacstrapped` variable.

### Get the init script from your forked repo.
```
curl https://raw.githubusercontent.com/{YOUR_USERNAME}/archer/master/init.sh > init.sh
```

Here is a short link incase you dont fork
```
curl https://git.io/JUFcb > init.sh
```

### Source the script so it runs in the same shell process
```
source init.sh
```

### Follow the prompts
You will need to run some commands manually. These revolve around moving into and out of chroot environment.

:warning: **Pick the correct drive to install on! I am not responsible for your lost data** :warning:
