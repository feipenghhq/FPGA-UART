/* ---------------------------------------------------------------
 * Copyright (c) 2022. Heqing Huang (feipenghhq@gmail.com)
 *
 * Author: Heqing Huang
 * Date Created: 07/08/2022
 * ---------------------------------------------------------------
 * Uart
 * ---------------------------------------------------------------
 * C Header file for avalon uart driver
 * ---------------------------------------------------------------
 */

#ifndef __AVALON_UART_H__
#define __AVALON_UART_H__

#include "avalon_uart_reg.h"

typedef struct _avalon_uart_init_s {
    uint8_t     txen;
    uint8_t     nstop;
    uint8_t     txcnt;
    uint8_t     rxen;
    uint8_t     rxcnt;
    uint8_t     ie_txwm;
    uint8_t     ie_rxwm;
    uint16_t    div;
} avalon_uart_init_s;

void avalon_uart_init(uint32_t base, avalon_uart_init_s* init_cfg);

int avalon_uart_open(uint32_t base);
int avalon_uart_close(uint32_t base);

void avalon_uart_write_byte_blocking(uint32_t base, const char* ptr);
int  avalon_uart_read_byte_blocking(uint32_t base);


#endif /* __AVALON_UART_H__ */
