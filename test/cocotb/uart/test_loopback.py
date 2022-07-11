# ------------------------------------------------------------------------------------------------
# Copyright 2022 by Heqing Huang (feipenghhq@gamil.com)
# Author: Heqing Huang
#
# Date Created: 07/04/2022
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
async def test_cfg(dut):
    env = Env(dut)
    await env.setup()
    txdata  = await env.avalon.read(0x0)
    rxdata  = await env.avalon.read(0x4)
    txctrl  = await env.avalon.read(0x8)
    rxctrl  = await env.avalon.read(0xC)
    ie      = await env.avalon.read(0x10)
    div     = await env.avalon.read(0x18)

    dut._log.info(hex(txdata))
    dut._log.info(hex(rxdata))
    dut._log.info(hex(txctrl))
    dut._log.info(hex(rxctrl))
    dut._log.info(hex(ie))
    dut._log.info(hex(div))

@cocotb.test()
async def test_loopback_1(dut, n=10):
    """ send single request """
    env = Env(dut)
    await env.setup()
    for i in range(n):
        data = randint(0, 255)
        dut._log.info(f"Sending data: {hex(data)}")
        await env.avalon.write(0x0, data)
        await Timer(100, units = "us")
        rxdata = await env.avalon.read(0x4)
        if rxdata == data:
            dut._log.info(f"Received data: {hex(rxdata)}")
        else:
            dut._log.info(f"Received wrong data: {hex(rxdata)}. Expected: {hex(data)}")

@cocotb.test()
async def test_loopback_2(dut, n=4):
    """ send multiple request """
    env = Env(dut)
    await env.setup()
    data = []
    rxdata = []
    for i in range(n):
        data.append(randint(0, 255))
        dut._log.info(f"Sending data: {hex(data[i])}")
        await env.avalon.write(0x0, data[i])
    await Timer(100*n, units = "us")
    for i in range(n):
        rxdata.append(await env.avalon.read(0x4))
    for i in range(n):
        if rxdata[i] == data[i]:
            dut._log.info(f"Received data: {hex(rxdata[i])}")
        else:
            dut._log.error(f"Received wrong data: {hex(rxdata[i])}. Expected: {hex(data[i])}")
            raise ValueError()

@cocotb.test()
async def test_loopback_3(dut, n=4):
    """ txwm & rxwm """
    env = Env(dut)
    await env.setup()
    assert dut.int_txwm.value == 1
    assert dut.int_rxwm.value == 0
    for i in range(4):
        await env.avalon.write(0x0, 0xAB)
        assert dut.int_txwm.value == 1
    await env.avalon.write(0x0, 0xAB)
    await Timer(100, units = "ns")
    assert dut.int_txwm.value == 0
    await Timer(100*4, units = "us")
    assert dut.int_rxwm.value == 0
    await Timer(100, units = "us")
    assert dut.int_rxwm.value == 1
    """
    for i in range(n):
        rxdata.append(await env.avalon.read(0x4))
    for i in range(n):
        if rxdata[i] == data[i]:
            dut._log.info(f"Received data: {hex(rxdata[i])}")
        else:
            dut._log.error(f"Received wrong data: {hex(rxdata[i])}. Expected: {hex(data[i])}")
            raise ValueError()
    """