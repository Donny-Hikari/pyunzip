#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import zipfile as zipper

# Chinese Charset: GBK(936), Big5(950)
# Japanese Charset: Shift_JIS(932), JIS(50220), EUC(51932)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Unzipper for vary Charsets")
    parser.add_argument('zipfile', help='Path to zip file.')
    parser.add_argument('-c', '--charset', type=str, default='utf-8',
        help='Charset of the zip file. Default is utf-8.')
    parser.add_argument('-e', '--encode', type=str, default='cp437',
        help="Correction for name encoding. It can be either utf-8 or cp437. Default is cp437.")
    parser.add_argument('-o', '--overwrite', action="store_true",
        help='Overwrite existing files.')
    args = parser.parse_args()

    print(("Processing File " + args.zipfile).encode('utf-8'))

    dirname = os.path.dirname(args.zipfile) + '/'
    zipfile = zipper.ZipFile(args.zipfile,"r")

    for filename in zipfile.namelist():

        dcname = ""
        try:
            dcname = dirname + filename.encode(args.encode).decode(args.charset)
        except Exception as e:
            print(e)
            continue
            pass

        print(("Extracting " + dcname).encode('utf-8'))
        pathname = os.path.dirname(dcname)
        if (not os.path.exists(pathname)) and (pathname != ""):
            os.makedirs(pathname)
        data = zipfile.read(filename)
        if args.overwrite or (not os.path.exists(dcname)):
            fo = open(dcname, "wb")
            fo.write(data)
            fo.close()
        else:
            print('File already exist.')

    zipfile.close()