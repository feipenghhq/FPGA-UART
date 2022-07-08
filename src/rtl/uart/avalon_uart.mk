REPO_ROOT = $(shell git rev-parse --show-toplevel)
UART_PATH = $(REPO_ROOT)/src/rtl/uart

VERILOG_SOURCE += $(UART_PATH)/avalon_uart.sv
VERILOG_SOURCE += $(UART_PATH)/uart_baud.sv
VERILOG_SOURCE += $(UART_PATH)/uart_core.sv
VERILOG_SOURCE += $(UART_PATH)/uart_fifo.sv
VERILOG_SOURCE += $(UART_PATH)/uart_rx.sv
VERILOG_SOURCE += $(UART_PATH)/uart_tx.sv

