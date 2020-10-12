# archer
My Arch Linux installer using Ansible

Only EFI booting is supported now.

## Arch ISO settings
**do not forget this step or packages wont install**

Hit `E` at the boot screen and add `cow_spacesize=1G` at the end of the boot parameters.

## Get the init script and source it.
```
curl -L https://git.io/JUFcb > init.sh
source init.sh
```
