# CHECK THE VERSION OF THE VMWARE WORKSTATION

Look the log files.

```
cd /tmp/vmware-vanquisher
```

We are downloading the patches from the github and repository to retrieve the module
source, build modules and install them

# Follow these commands

```
wget https://github.com/mkubecek/vmware-host-modules/archive/workstation-14.1.1.tar.gz
  
tar -xzf workstation-14.1.1.tar.gz
  
cd vmware-host-modules-workstation-14.1.1
  
make
  
make install
```

Replace 14.1.1 with the version of your product.


# If you get error like this then follow these steps.
```
Could not open /dev/vmmon: No such file or directory.
Please make sure that the kernel module `vmmon' is loaded.
```

[How to fix ?](https://askubuntu.com/questions/1096052/vmware-15-error-on-ubuntu-18-4-could-not-open-dev-vmmon-no-such-file-or-dire)

# Remove Vmware workstation from system.

[Uninstall](https://kb.vmware.com/s/article/38)
