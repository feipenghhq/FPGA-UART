/* ---------------------------------------------------------------
 * Copyright (c) 2022. Heqing Huang (feipenghhq@gmail.com)
 *
 * Author: Heqing Huang
 * Date Created: 07/10/2022
 * ---------------------------------------------------------------
 * Uart
 * ---------------------------------------------------------------
 * Testbench
 * ---------------------------------------------------------------
*/


module tb (
    input               clk,
    input               rst,

    input               avn_read,
    input               avn_write,
    input [4:0]         avn_address,
    input [31:0]        avn_writedata,
    output reg [31:0]   avn_readdata,
    output              avn_waitrequest,

    output              uh_avn_read,
    output              uh_avn_write,
    output [31:0]       uh_avn_address,
    output [3:0]        uh_avn_byte_enable,
    output [31:0]       uh_avn_writedata,

    output              int_txwm,
    output              int_rxwm
);

    logic               uart_txd;
    logic               uart_rxd;

    logic [31:0]        uh_avn_readdata;
    logic               uh_avn_waitrequest;

    assign uh_avn_readdata = 0;
    assign uh_avn_waitrequest = 0;

    avalon_uart         avalon_uart(.*);

    avalon_uart_host
    u_avalon_uart_host(
        .clk            (clk),
        .rst            (rst),
        .uart_rxd       (uart_txd),
        .cfg_rxen       (1'b1),
        .cfg_div        (10),
        .avn_read       (uh_avn_read),
        .avn_write      (uh_avn_write),
        .avn_address    (uh_avn_address),
        .avn_writedata  (uh_avn_writedata),
        .avn_byte_enable(uh_avn_byte_enable),
        .avn_readdata   (uh_avn_readdata),
        .avn_waitrequest(uh_avn_waitrequest)
    );

endmodule
