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
