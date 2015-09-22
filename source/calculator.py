import os
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.dates import strpdate2num

def clear():
	os.system(['clear','cls'][os.name == 'nt'])

def start():
	tempFile = 'temp.txt'
	open(tempFile,'w+') # Open and clear any previous data	

	print("Enter stock symbol")
	stock = input(">")

	print("Quantity Purchasing")
	quantity = input(">")

	print("Commission Paid")
	commission = input(">")

	try:
		bloomberg = urllib.request.urlopen('http://www.bloomberg.com/markets/watchlist/recent-ticker/'+stock+':US').read()
		price = str(bloomberg).split('"last_price":')[1].split(",")[0]
		companyName = str(bloomberg).split('"disp_name":"')[1].split('",')[0]
		breakEven = ((float(price) * float(quantity)) + float (commission)) / (float(quantity))

		clear()
		print("\n=============================")
		print(stock.upper())
		print("=============================")		
		print("Price        |      $ %s" %price)
		print("=============================")
		print("Shares       |        %s" %quantity)
		print("=============================")
		print("Commission   |      $ %s" %commission)		
		print("=============================")		
		print("Break-Even   |      $",round(breakEven,4))
		print("=============================\n")		
		
		url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
		with urllib.request.urlopen(url) as f:
			sourceCode = f.read().decode('utf-8')
		splitSource = sourceCode.split('\n')

		for line in splitSource:
			splitLine = line.split(',')
			if len(splitLine) == 6:
				if 'values' not in line:
					saveFile = open(tempFile,'a')
					breakEven = str(breakEven) # Save as string to write to temp.txt
					linetoWrite = line+","+breakEven+'\n'
					saveFile.write(linetoWrite)

		# For converting dates:			
		def bytespdate2num(fmt, encoding='utf-8'):
			strconverter = strpdate2num(fmt)
			def bytesconverter(b):
				s = b.decode(encoding)
				return strconverter(s)
			return bytesconverter

		date, close, high, low, openPrice, volume, breakEven = np.loadtxt("temp.txt", delimiter=',', unpack=True,
																converters={0:bytespdate2num('%Y%m%d')})
		fig = plt.figure(figsize=(12, 8))
		#fig.patch.set_facecolor('white')
		ax1 = plt.subplot(1,1,1)
		ax1.plot(date, close, lw=2, color='#2C3E50', label="Closing")
		ax1.plot(date, high, color='#3498DB', label="High")
		ax1.plot(date, low, color='#E74C3C', label="Low")
		ax1.plot(date, breakEven, lw=2, color='#468966', linestyle='--', label="Break-Even")
		ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
		ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
		ax1.yaxis.set_ticks_position('right')
		plt.title(companyName+" ("+stock.upper()+")")
		plt.grid(True)

		plt.legend(loc=2, ncol=5)

		# For ticker symbol on graph:
		left, width = .25, .5
		bottom, height = .25, .5
		right = left + width
		top = bottom + height

		ax1.text(0.5*(left+right), 0.5*(bottom+top), stock.upper(),
			horizontalalignment='center',
			verticalalignment='center',
			fontsize=55, color='grey', alpha=0.4,
			transform=ax1.transAxes)

		plt.show()

		clear()
		start()

	except:
		clear()
		print ("Could not find: ", stock)
		start()

start()

"""
----------------------------------------------------------------------

Development Name: Plancials
Author: Nawaz Gafar
Permission is hereby granted to any user, the ability to use, copy, 
modify, and distribute, free of any charge, subject to the agreement 
of the following conditions: 

- This project is licensed under the Creative Commons 
  Attribution-ShareAlike 4.0 International License. Further information 
  regarding this license and usage may be found by visiting:
  http://creativecommons.org/licenses/by-sa/4.0/

- The notice above (starting with "Development Name") will appear in 
  any iterations of this file, or any further files that are a result 
  of the modification of this file. 

Please also note that this application is distributed without any 
expressed or implied warrant. As such no liability shall be incurred 
by the author for any subsequent event(s) that should occur as a result 
of information acquired through usage of this application.   

----------------------------- Tamam Shud -----------------------------
"""
