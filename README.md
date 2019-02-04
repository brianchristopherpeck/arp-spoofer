# arp-spoofer

## Help
```
python arp_spoof.py --help
```

## Options
```
Options:
  -t, --target			Target IP Address
  -g, --gateway			Gateway IP Address
```

## Example command for MacOSX
```
sudo python arp_spoof.py  -t 127.0.0.1 -g 127.0.0.4
```

## Example command for Linux
```
sudo python arp_spoof.py  -target 127.0.0.1 -gateway 127.0.0.4
```

### Currently does NOT work with Python3
### Optparse while still widely used is considered deprecated to argparse

#### ToDo:
1. Upgrade to Python3
2. Upgrade to Argparse