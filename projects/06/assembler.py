#!/usr/bin/env python

import sys
import Parser
import Code

filename=sys.argv[1]
rfile = open(filename,'r')
wfile = open('prog.asm','w')


line=rfile.readline()
flag=Parser.hasMoreCommands(line)

while flag:
    while line == '\n' or line.startswith('//'):
        line=rfile.readline()

    ctype=Parser.commandType(line)
    if ctype is 'A_COMMAND':
	AS=Parser.symbol(line)
	ASb=bin(int(AS))[2:]
	AString=ASb.zfill(15)
	wfile.write('0'+AString+'\n')
    elif ctype is 'L_COMMAND':
	LString=Parser.symbol(line)
	wfile.write('0'+LString+'\n')
    if ctype is 'C_COMMAND':
	DestString=Code.dest(line)
	CompString=Code.comp(line)
	JumpString=Code.jump(line)
 	wfile.write('111'+CompString+DestString+JumpString+'\n')

    line=Parser.advance(rfile, line)
    flag=Parser.hasMoreCommands(line)

rfile.close()
wfile.close()
