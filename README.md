# FPGA-UART

## Memory Map

Reference: <https://static.dev.sifive.com/SiFive-E300-platform-reference-manual-v1.0.1.pdf>


| Address | Name   | Description               |
| ------- | ------ | ------------------------- |
| 0x000   | txdata | Transmit data register    |
| 0x004   | rxdata | Receive data register     |
| 0x008   | txctrl | Transmit control register |
| 0x00C   | rxctrl | Receive control register  |
| 0x010   | ie     | interrupt enable          |
| 0x014   | ip     | Interrupt pending         |
| 0x018   | div    | rate divisor              |
