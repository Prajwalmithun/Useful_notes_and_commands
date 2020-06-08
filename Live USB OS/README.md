Replace /path/to/archlinux.iso with the path to the downloaded ISO file and /dev/sdx with your USB drive name

```
dd bs=4M if=/path/to/archlinux.iso of=/dev/sdx status=progress oflag=sync
```
