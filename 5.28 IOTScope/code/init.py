#!/usr/bin/env python
# coding=utf-8

import os
import sys

def usage():
    print("[*] Usage:")
    print ("\tpython3 %s vendor brand" % sys.argv[0])
    print("[*] Example:")
    print ("\tpython3 %s D-Link DIR816L" % sys.argv[0])

def init():
    #IoTScope Ready
    vendor = sys.argv[1]
    brand = sys.argv[2]
    binfile = brand + ".bin"
    #binfile = brand + ".chk"
    #binfile = brand + ".trx"
    #print (binfile)
    if not os.path.exists(vendor):
        print ("[!] vendor <%s> paths is not exist" % vendor)
        return 1
    os.system("cp %s %s/" % (binfile, vendor))
    os.system("binwalk -Me %s/%s" % (vendor, binfile))
    os.system("mkdir %s/%s" % (vendor, brand))
    os.system("cp -R %s/_%s.extracted/squashfs-root/* %s/%s" % (vendor, binfile, vendor, brand))
    os.system("mkdir %s/%s/firmware" % (vendor, brand))
    os.system("cp -R %s/%s/* %s/%s/firmware" % (vendor, brand, vendor, brand))
    os.system("rm %s/%s" % (vendor, binfile))
    os.system("rm -rf %s/_%s.extracted/" % (vendor, binfile))
    #FirmAE copy files
    os.system("cp %s ~/Desktop/DIR600/FirmAE/firmwares/" % (binfile))

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        usage()
    else:
        init()
