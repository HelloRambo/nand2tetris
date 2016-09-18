#!/usr/bin/python
import sys
import Parser
import Code
import SymbolTable

filename = sys.argv[1]
symboldict = SymbolTable.Constructor()
rfile = open(filename, 'r')
i = 0
linepre = rfile.readline()
flag = Parser.hasMoreCommands(linepre)

while flag:
    while linepre == '\r\n' or linepre.startswith('//'):
        linepre = rfile.readline()

    if linepre.find('(') >= 0:
        linepre = linepre.strip()
        symbol = linepre.strip('()\n')
        if not SymbolTable.contains(symbol, symboldict):
            symboldict = SymbolTable.addEntry(symbol, i, symboldict)
    else:
        i += 1

    linepre = Parser.advance(rfile, linepre)
    flag = Parser.hasMoreCommands(linepre)

rfile.close()


j = 0
rfile = open(filename, 'r')
wfile = open('prog.hack', 'w')

line = rfile.readline()
flag = Parser.hasMoreCommands(line)

while flag:
    while line == '\n' or line.startswith('//'):
        line = rfile.readline()

    ctype = Parser.commandType(line)

    if ctype is 'A_COMMAND':
        AS = Parser.symbol(line)
        if not AS.isdigit():
            if not SymbolTable.contains(AS, symboldict):
                symboldict = SymbolTable.addEntry(AS, j + 16, symboldict)
                j += 1
            binAS = bin(SymbolTable.GetAddress(AS, symboldict))[2:]

        else:
            binAS = bin(int(AS))[2:]

        AString = binAS.zfill(15)
        wfile.write('0'+AString+'\n')

    elif ctype is 'C_COMMAND':
        DestString = Code.dest(line)
        CompString = Code.comp(line)
        JumpString = Code.jump(line)
        wfile.write('111' + CompString + DestString + JumpString + '\n')

    line = Parser.advance(rfile, line)
    flag = Parser.hasMoreCommands(line)
    
rfile.close()
wfile.close()
