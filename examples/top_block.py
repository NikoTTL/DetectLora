#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Oct 25 21:42:03 2018
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import lora


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.spreading_factor = spreading_factor = 8
        self.samp_rate = samp_rate = 250e3
        self.ldr = ldr = True
        self.header = header = False
        self.code_rate = code_rate = 4

        ##################################################
        # Blocks
        ##################################################
        self.lora_mod_0 = lora.mod(spreading_factor, 0x12)
        self.lora_encode_0 = lora.encode(spreading_factor, code_rate, ldr, header)
        self.lora_demod_0 = lora.demod(spreading_factor, ldr, 25.0, 2)
        self.lora_decode_0 = lora.decode(spreading_factor, code_rate, ldr, header)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_socket_pdu_0_0 = blocks.socket_pdu("UDP_CLIENT", "127.0.0.1", "52002", 10000, False)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_SERVER", "127.0.0.1", "52001", 10000, False)
        self.blocks_message_debug_0 = blocks.message_debug()

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0, 'pdus'), (self.lora_encode_0, 'in'))    
        self.msg_connect((self.lora_decode_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))    
        self.msg_connect((self.lora_decode_0, 'out'), (self.blocks_socket_pdu_0_0, 'pdus'))    
        self.msg_connect((self.lora_demod_0, 'out'), (self.lora_decode_0, 'in'))    
        self.msg_connect((self.lora_encode_0, 'out'), (self.lora_mod_0, 'in'))    
        self.connect((self.blocks_throttle_0_0, 0), (self.lora_demod_0, 0))    
        self.connect((self.lora_mod_0, 0), (self.blocks_throttle_0_0, 0))    

    def get_spreading_factor(self):
        return self.spreading_factor

    def set_spreading_factor(self, spreading_factor):
        self.spreading_factor = spreading_factor

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_ldr(self):
        return self.ldr

    def set_ldr(self, ldr):
        self.ldr = ldr

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def get_code_rate(self):
        return self.code_rate

    def set_code_rate(self, code_rate):
        self.code_rate = code_rate


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
