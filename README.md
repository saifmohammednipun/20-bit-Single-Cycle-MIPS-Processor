## Complete Datapath based on IAS with assigned bits and operations

Here you will be implementing your own CPU based on the "Machine Code Bits" mentioned in the pdf file, submitted by individuals. The CPU must be able to execute the instructions stored in the memory one after another. Implement your datapath and control units properly so that your Datapath can execute instructions automatically. You have to submit the Complete Datapath based on IAS with your assigned bits  and operations.

**Submission must include:**

One logisim file containing the whole Complete Datapath. (register file design, ALU design, control unit and ALU control, instruction and data memory)
**Project Report:**
A document containing the table of Control Unit and ALU control.
The final version of your ISA based on the operations assigned to you in the pdf in same order.  You should mention:
1) How many operands
2) Types of operand? (Register based or Memory based??)
3) How many operations? (Note that your ISA must be based on what instructions you were given and in which order they were given.)
4) Types of operations? (Arithmetic, logical, branch type?? How many from each category? List the opcodes and respective binary values
5) No. of the format of instruction (how many different formats?)
6) Describe each of the formats (fields and field length)

**Note:**
It is difficult and error-prone to write machine code manually. The problem can be addressed by writing an assembler, which can automatically generate a machine code from an assembly file. In this project,  you might write an assembler for your ISA. The assembler reads a program written using assembly language in a text file, then translates it into binary code and generates an output file(.txt) containing machine code. The generated output files will be useful to run a program when you develop your actual CPU. 

**Language:**
You can use any high-level language. A demo assembler created with Python is attached here for your reference. You are strongly advised to use them to save your time. You might need to modify the existing functions/classes according to your need.