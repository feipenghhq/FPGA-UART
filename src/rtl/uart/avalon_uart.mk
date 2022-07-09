REPO_ROOT = $(shell git rev-parse --show-toplevel)
UART_PATH = $(REPO_ROOT)/src/rtl/uart

VERILOG_SOURCES += $(UART_PATH)/uart_fifo.sv
VERILOG_SOURCES += $(UART_PATH)/uart_baud.sv
VERILOG_SOURCES += $(UART_PATH)/uart_rx.sv
VERILOG_SOURCES += $(UART_PATH)/uart_tx.sv
VERILOG_SOURCES += $(UART_PATH)/uart_core.sv
VERILOG_SOURCES += $(UART_PATH)/avalon_uart.sv

