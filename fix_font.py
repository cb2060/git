#!/usr/bin/env python3

import subprocess

f_inp = open("index.html", 'r')
f_out = open("tmp_index.html", 'w')

for line in f_inp:

    if r'    <style type="text/css">' in line:
        fonts = 'Droid+Serif|Yanone+Kaffeesatz|Ubuntu+Mono:400,700,400italic'
        css_line = '    <link rel="stylesheet" '
        css_line += 'href="https://fonts.googleapis.com/css?family='
        css_line += fonts + '">\n'
        css_line += '    <style>\n'
        f_out.write(css_line)

    elif r'@import url(http://fonts.googleapis.com/css?family=' in line:
        pass

    else:
        f_out.write(line)

f_inp.close()
f_out.close()

subprocess.call("mv tmp_index.html index.html".split())
