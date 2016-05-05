// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@i
M=1  //i=1
@2
M=0   //D=RAM[2]
(LOOP)
@i
D=M  //D=i
@1
M=M-D  //RAM[1]=RAM[1]-1
@1
D=M    //D=RAM[1]
@END
D;JLT
@0
D=M  //D=RAM[0]
@2
D=D+M  //RAM[0]=RAM[0]+RAM[2]
@2
M=D  //RAM[2]=RAM[0]
@LOOP
0;JMP
(END)
@END
0;JMP
