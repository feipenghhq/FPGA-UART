# ==================================================================================
# Makefile
# ==================================================================================

GIT_ROOT = $(shell git rev-parse --show-toplevel)
PWD 	 = $(shell pwd)

# defaults
SIM ?= verilator
TOPLEVEL_LANG ?= verilog

include $(GIT_ROOT)/src/rtl/uart/avalon_uart.mk
VERILOG_SOURCES += $(GIT_ROOT)/src/rtl/uart_host/avalon_uart_host.sv
VERILOG_SOURCES += $(PWD)/tb.sv
TOPLEVEL = tb

MODULE = test

DUMP ?= 0

ifeq ($(SIM),verilator)
ifeq ($(DUMP), 1)
	EXTRA_ARGS += --trace-fst --trace-structs
endif
endif

# Other variable
export COCOTB_RESOLVE_X=RANDOM
export PYTHONPATH = $(GIT_ROOT)/cocotb

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
