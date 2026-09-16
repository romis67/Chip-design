# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer


@cocotb.test()
async def test_project(dut):

    dut._log.info("Start Full Adder Test")

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

    # Test all possible combinations
    for A in range(16):
        for B in range(16):

            # ui[3:0] = A
            # ui[7:4] = B
            dut.ui_in.value = (B << 4) | A

            # Allow combinational logic to settle
            await Timer(1, unit="us")

            # Expected result
            total = A + B

            expected_result = total & 0xF
            expected_carry = (total >> 4) & 0x1
            expected_zero = 1 if expected_result == 0 else 0

            # Read outputs
            result = int(dut.uo_out.value) & 0xF
            carry = (int(dut.uo_out.value) >> 4) & 0x1
            zero = (int(dut.uo_out.value) >> 5) & 0x1

            # Check result
            assert result == expected_result, (
                f"Result error: A={A}, B={B}, "
                f"Expected={expected_result}, Got={result}"
            )

            # Check carry
            assert carry == expected_carry, (
                f"Carry error: A={A}, B={B}, "
                f"Expected={expected_carry}, Got={carry}"
            )

            # Check zero
            assert zero == expected_zero, (
                f"Zero error: A={A}, B={B}, "
                f"Expected={expected_zero}, Got={zero}"
            )

    dut._log.info("All 256 combinations passed!")
