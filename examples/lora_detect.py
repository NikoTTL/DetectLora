#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lora Detect
# Generated: Fri Oct 19 14:52:15 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import es
import lora
import math
import time
import wx


class lora_detect(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Lora Detect")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.spreading_factor = spreading_factor = 8
        self.samp_rate = samp_rate = 1e6
        self.rx_gain = rx_gain = 12
        self.offset = offset = -250e3
        self.ldr = ldr = True
        self.header = header = False
        self.frequency = frequency = 868.1e6
        self.code_rate = code_rate = 4
        self.bw = bw = 1.2e6

        ##################################################
        # Blocks
        ##################################################
        _rx_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rx_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rx_gain_sizer,
        	value=self.rx_gain,
        	callback=self.set_rx_gain,
        	label="rx_gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rx_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rx_gain_sizer,
        	value=self.rx_gain,
        	callback=self.set_rx_gain,
        	minimum=0,
        	maximum=89,
        	num_steps=90,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rx_gain_sizer)
        _offset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	label="offset",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._offset_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	minimum=-samp_rate/2,
        	maximum=samp_rate/2,
        	num_steps=999,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_offset_sizer)
        self._frequency_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.frequency,
        	callback=self.set_frequency,
        	label="frequency",
        	converter=forms.float_converter(),
        )
        self.Add(self._frequency_text_box)
        self._bw_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.bw,
        	callback=self.set_bw,
        	label="bw",
        	converter=forms.float_converter(),
        )
        self.Add(self._bw_text_box)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=frequency,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_center_freq(frequency, 0)
        self.uhd_usrp_source_1.set_gain(rx_gain, 0)
        self.uhd_usrp_source_1.set_antenna("RX2", 0)
        self.uhd_usrp_source_1.set_bandwidth(bw, 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(25000)
        self.uhd_usrp_sink_0.set_center_freq(frequency, 0)
        self.uhd_usrp_sink_0.set_gain(45, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_bandwidth(bw, 0)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  bw/samp_rate,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        	
        self.lora_lora_detect_0 = lora.lora_detect(8, False, 25.0, 2)
        self.es_trigger_edge_f_0 = es.trigger_edge_f(0.99,5000,0,gr.sizeof_gr_complex,0)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(0.3, 1, 0)
        self.blocks_rotator_cc_0 = blocks.rotator_cc((2 * math.pi * offset) / samp_rate)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, 1, 0, 8192)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.es_trigger_edge_f_0, 1))    
        self.connect((self.blocks_rotator_cc_0, 0), (self.pfb_arb_resampler_xxx_0, 0))    
        self.connect((self.blocks_threshold_ff_0, 0), (self.es_trigger_edge_f_0, 0))    
        self.connect((self.es_trigger_edge_f_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.es_trigger_edge_f_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.lora_lora_detect_0, 0), (self.blocks_threshold_ff_0, 0))    
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.lora_lora_detect_0, 0))    
        self.connect((self.uhd_usrp_source_1, 0), (self.blocks_rotator_cc_0, 0))    

    def get_spreading_factor(self):
        return self.spreading_factor

    def set_spreading_factor(self, spreading_factor):
        self.spreading_factor = spreading_factor

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_rotator_cc_0.set_phase_inc((2 * math.pi * self.offset) / self.samp_rate)
        self.pfb_arb_resampler_xxx_0.set_rate(self.bw/self.samp_rate)
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self._rx_gain_slider.set_value(self.rx_gain)
        self._rx_gain_text_box.set_value(self.rx_gain)
        self.uhd_usrp_source_1.set_gain(self.rx_gain, 0)
        	

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self._offset_slider.set_value(self.offset)
        self._offset_text_box.set_value(self.offset)
        self.blocks_rotator_cc_0.set_phase_inc((2 * math.pi * self.offset) / self.samp_rate)

    def get_ldr(self):
        return self.ldr

    def set_ldr(self, ldr):
        self.ldr = ldr

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self._frequency_text_box.set_value(self.frequency)
        self.uhd_usrp_sink_0.set_center_freq(self.frequency, 0)
        self.uhd_usrp_source_1.set_center_freq(self.frequency, 0)
        self.wxgui_fftsink2_0.set_baseband_freq(self.frequency)

    def get_code_rate(self):
        return self.code_rate

    def set_code_rate(self, code_rate):
        self.code_rate = code_rate

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self._bw_text_box.set_value(self.bw)
        self.pfb_arb_resampler_xxx_0.set_rate(self.bw/self.samp_rate)
        self.uhd_usrp_sink_0.set_bandwidth(self.bw, 0)
        self.uhd_usrp_source_1.set_bandwidth(self.bw, 0)


def main(top_block_cls=lora_detect, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
