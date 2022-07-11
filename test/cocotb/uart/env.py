# ------------------------------------------------------------------------------------------------
# Copyright 2022 by Heqing Huang (feipenghhq@gamil.com)
# Author: Heqing Huang
#
# Date Created: 07/04/2022
# ------------------------------------------------------------------------------------------------
# Avalon Standard Bus
# ------------------------------------------------------------------------------------------------
# Environment
# ------------------------------------------------------------------------------------------------

from collections import deque

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
from cocotb_bus.drivers.avalon import AvalonMaster

class Env:

    def __init__(self, dut):
        self.dut = dut
        self.avalon = AvalonMaster(dut, "avn", dut.clk)

    async def clock_gen(self, period=10):
        """ Generate Clock """
        c = Clock(self.dut.clk, period, units="ns")
        await cocotb.start(c.start())

    async def reset_gen(self, time=100):
        """ Reset the design """
        self.dut.rst.value = 1
        await Timer(time, units="ns")
        await RisingEdge(self.dut.clk)
        self.dut.rst.value = 0
        await RisingEdge(self.dut.clk)
        self.dut._log.info(f"Reset Done!")

    async def uart_setup(self, nstop=0, txcnt=4, rxcnt=4, div=867):
        txctrl = 1 | nstop << 1 | txcnt << 16
        rxctrl = 1 | rxcnt << 16
        ie = 3
        await self.avalon.write(0x8, txctrl)
        await self.avalon.write(0xC, rxctrl)
        await self.avalon.write(0x10, ie)
        await self.avalon.write(0x18, div)
        await Timer(100, units="ns")

    async def setup(self, nstop=0, txcnt=4, rxcnt=4, div=867):
        await self.clock_gen()
        await self.reset_gen()
        await self.uart_setup(nstop, txcnt, rxcnt, div)