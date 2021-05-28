# -*- coding: utf-8 -*-
"""
Created on Fri May 25 19:31:20 2021

@author: Joko Susilo
"""

import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best'
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/eastwood_lawyers.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/edison.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/graham_any_nation.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/harvey_gonads.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/hawking01.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/hawking02.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/houdini_goodnight.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/ireland_ouch.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/jackson_allegations.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/king_injustice.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/king_nonviolence.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/king_war_no_more.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/leary.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/lewis_prime-time_ratings.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/ll_cool_j_ya_know.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/macarthur_return.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/malcolm_x_by_any_means1.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/manson_believe_me.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/manson_devil.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/mother_teresa.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/nimoy_spock.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/patton_no_fun.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/swaggart_sinned.wav',
                  'https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/tutu_mandela.wav'])