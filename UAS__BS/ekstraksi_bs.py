# -*- coding: utf-8 -*-
"""
Created on Fri May 23 15:09:21 2021

@author: Joko Susilo
"""

import requests as req
from bs4 import BeautifulSoup as bs	       

header={"Host":"www.wavsource.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
halaman=req.get("https://www.wavsource.com/people/famous.htm",headers=header)
data_halaman=bs(halaman.text,"html.parser")
data_c1=data_halaman.find_all("td",class_="c1")
for ic in data_c1:
	data_script=ic.find_all("script")
	if(len(data_script)>0):
		ambil_data=str(data_script[0])
		ambil_data=ambil_data.replace("<script type=\"text/javascript\">","")
		ambil_data=ambil_data.replace("</script>","")
		ambil_data=ambil_data.replace("s2p(","")
		ambil_data=ambil_data.replace(")","")
		ambil_data=ambil_data.replace("\'","")
		ambil_data=ambil_data.split(",")
		print("-"*10)
		print("Judul             :{}".format(ambil_data[4]))
		print("Tahun ditambahkan:{}{}".format(ambil_data[2].replace("added ",""),ambil_data[3]))
		print("link lagu        :{}/{}/{}".replace(" ", " ").format('https://www.wavsource.com/snds_2020-10-01_3728627494378403',
                                                              ambil_data[0],ambil_data[1]))
		print("-"*10)
        