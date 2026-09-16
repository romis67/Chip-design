# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer


@cocotb.test()
async def test_project(dut):

    dut._log.info("Start")

    # Start clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Enable
    dut.ena.value = 1

    # Reset
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    await Timer(20, unit="us")

    dut.rst_n.value = 1

    dut._log.info("Testing 4-bit adder")

    # ------------------------------------------------
    # Test 1
    # A = 0, B = 0
    # Result = 0, Carry = 0, Zero = 1
    # ------------------------------------------------

    dut.ui_in.value = 0b00000000
    await Timer(1, unit="us")

    assert dut.uo_out.value & 0x3F == 0b100000
    dut._log.info("Test 1 Passed")

    # ------------------------------------------------
    # Test 2
    # A = 1, B = 1
    # Result = 2, Carry = 0, Zero = 0
    # ------------------------------------------------

    dut.ui_in.value = 0b00010001
    await Timer(1, unit="us")

    assert dut.uo_out.value & 0x3F == 0b000010
    dut._log.info("Test 2 Passed")

    # ------------------------------------------------
    # Test 3
    # A = 3, B = 5
    # Result = 8
    # ------------------------------------------------

    dut.ui_in.value = 0b01010011
    await Timer(1, unit="us")

    assert dut.uo_out.value & 0x3F == 0b001000
    dut._log.info("Test 3 Passed")

    # ------------------------------------------------
    # Test 4
    # A = 7, B = 8
    # Result = 15
    # ------------------------------------------------

    dut.ui_in.value = 0b10000111
    await Timer(1, unit="us")

    assert dut.uo_out.value & 0x3F == 0b001111
    dut._log.info("Test 4 Passed")

    # ------------------------------------------------
    # Test 5
    # A = 15, B = 1
    # Result = 0, Carry = 1, Zero = 1
    # ------------------------------------------------

    dut.ui_in.value = 0b00011111
    await Timer(1, unit="us")

    assert dut.uo_out.value & 0x3F == 0b110000
    dut._log.info("Test 5 Passed")

    # ------------------------------------------------
    # Test 6
    # A = 15, B = 15
    # Result = 14, Carry = 1, Zero = 0
    # ------------------------------------------------

    dut.ui_in.value = 0b11111111
    await Timer(1, unit="us")

    assert dut.uo_out.value & 0x3F == 0b011110
    dut._log.info("Test 6 Passed")

    dut._log.info("All tests passed!")
