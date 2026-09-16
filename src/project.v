/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_fullladder (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // Inputs
    wire [3:0] A;
    wire [3:0] B;

    // Outputs
    wire [3:0] Result;
    wire Carry;
    wire Zero;

    // Pin mapping
    assign A = ui_in[3:0];
    assign B = ui_in[7:4];

    // 4-bit addition
    assign {Carry, Result} = A + B;

    // Zero flag
    assign Zero = (Result == 4'b0000);

    // Output pin mapping
    assign uo_out[0] = Result[0];
    assign uo_out[1] = Result[1];
    assign uo_out[2] = Result[2];
    assign uo_out[3] = Result[3];
    assign uo_out[4] = Carry;
    assign uo_out[5] = Zero;

    // Unused outputs
    assign uo_out[6] = 1'b0;
    assign uo_out[7] = 1'b0;

    // Bidirectional pins unused
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

endmodule
