# ------------------------------------------------------------------------------------------------
# Copyright 2022 by Heqing Huang (feipenghhq@gamil.com)
# Author: Heqing Huang
#
# Date Created: 07/10/2022
# ------------------------------------------------------------------------------------------------
# Avalon Standard Bus
# ------------------------------------------------------------------------------------------------
# Direct test bus matrix
# ------------------------------------------------------------------------------------------------

from collections import deque

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
from env import Env
from random import randint


@cocotb.test()
async def test_loopback_1(dut):
    """ send single request """
    env = Env(dut)
    # Addr = 0xbeefcafe, Data = 0xabcd1234
    dl = [0xfe, 0xca, 0xef, 0xbe, 0x34, 0x12, 0xcd, 0xab]
    await env.setup(div=10)
    for i in range(8):
        data = dl[i]
        dut._log.info(f"Sending data: {hex(data)}")
        await env.avalon.write(0x0, data)
        await Timer(100, units = "us")
