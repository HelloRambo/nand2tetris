#!/usr/bin/python

import sys
import Parser
import Code
import SymbolTable

filename = sys.argv[1]
rfile = open(filename, 'r')
wfile = open('dprog.asm', 'w')

line = rfile.readline()
flag = Parser.hasMoreCommands(line)

while flag:
    while line == '\n' or line.startswith('//'):
        line = rfile.readline()

    ctype = Parser.commandType(line)

    if ctype is 'A_COMMAND':
        dline = Parser.symbol(line)
        wfile.write(dline+'\n')

    line = Parser.advance(rfile, line)
    flag = Parser.hasMoreCommands(line)
    
rfile.close()
wfile.close()
