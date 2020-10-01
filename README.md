# archer
my attempt at a arch linux installer


### Arch ISO settings 
:warning: **do not forget this step or packages wont install**

Hit `E` at the boot screen and add `cow_spacesize=1G` at the end of the boot parameters.

### Get the init script
```
curl https://raw.githubusercontent.com/rhwendt/archer/master/init.sh > init.sh
```

### Source the script so it runs in the same shell process
```
source init.sh
```
