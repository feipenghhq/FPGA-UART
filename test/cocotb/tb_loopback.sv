/* ---------------------------------------------------------------
 * Copyright (c) 2022. Heqing Huang (feipenghhq@gmail.com)
 *
 * Author: Heqing Huang
 * Date Created: 07/08/2022
 * ---------------------------------------------------------------
 * Uart
 * ---------------------------------------------------------------
 * Testbench loopback
 * ---------------------------------------------------------------
*/


module tb_loopback (
    input               clk,
    input               rst,

    input               avn_read,
    input               avn_write,
    input [4:0]         avn_address,
    input [31:0]        avn_writedata,
    output reg [31:0]   avn_readdata,
    output              avn_waitrequest,

    output              int_txwm,
    output              int_rxwm
);

    logic               uart_txd;
    logic               uart_rxd;

    avalon_uart DUT(.*);

    assign uart_rxd = uart_txd;

endmodule
