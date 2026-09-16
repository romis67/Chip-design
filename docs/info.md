<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a 4-bit binary adder.

The 8 input pins are divided into two 4-bit numbers:
- `ui[3:0]` = A
- `ui[7:4]` = B

The circuit adds A and B and produces:
- `uo[3:0]` = 4-bit Result
- `uo[4]` = Carry
- `uo[5]` = Zero flag

The addition is performed as:

A + B = {Carry, Result}

The remaining output pins are unused and set to 0.

## How to test

The design is tested using Cocotb.

The testbench applies different combinations of the 4-bit inputs A and B and checks:
- Result
- Carry
- Zero flag

All 256 possible combinations of A and B are tested.

For each combination, the expected result is calculated and compared with the output of the design.

## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any
