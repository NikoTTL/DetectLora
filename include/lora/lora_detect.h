/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_LORA_LORA_DETECT_H
#define INCLUDED_LORA_LORA_DETECT_H

#include <lora/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace lora {

    /*!
     * \brief <+description of block+>
     * \ingroup lora
     *
     */
    class LORA_API lora_detect : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<lora_detect> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of lora::lora_detect.
       *
       * To avoid accidental use of raw pointers, lora::lora_detect's
       * constructor is in a private implementation
       * class. lora::lora_detect::make is the public interface for
       * creating new instances.
       */
      static sptr make(unsigned short spreading_factor,bool  low_data_rate,  float beta,unsigned short fft_factor);
    };

  } // namespace lora
} // namespace gr

#endif /* INCLUDED_LORA_LORA_DETECT_H */

