import sys, os, urllib2

def start():
	print "[1] Calculate the break even price for a stock you own"
	print "[2] Calculate the break even price for a stock using it's ticker symbol\n"
	print "Please select an option by typing the number"
	selection = raw_input("> ")

	if selection == "1":
		print "Price Paid"
		price = raw_input("> ")

		print "Shares Purchases"
		shares = raw_input("> ")

		print "Commission Paid"
		commission = raw_input("> ")

		breakEven = ((float(price) * float(shares)) + float (commission)) / (float(shares))
		
		try:
			os.system('cls') #Clears the screen (Windows).
		except:
			os.system('clear') #Linux /OS X
		print "\n============================="
		print "Price        |      $ %s" %price
		print "============================="
		print "Shares       |        %s" %shares
		print "============================="
		print "Commission   |      $ %s" %commission		
		print "============================="		
		print "Break-Even   |      $",round(breakEven,4)
		print "=============================\n"		
		start()
		
	elif selection == "2":
		print "Stock Symbol (ex. AAPL or BAC)"
		symbol = raw_input("> ")
		
		print "Shares Purchased"
		shares = raw_input("> ")
		
		print "Commission Paid"
		commission = raw_input("> ")
		
		#Stock Price lookup
		try:
			yahooFinance = urllib2.urlopen("http://finance.yahoo.com/q?s="+symbol).read()
			price = yahooFinance.split('<span id="yfs_l84_'+symbol.lower()+'">' )[1].split("</span>")[0]
		
			breakEven = ((float(price) * float(shares)) + float (commission)) / (float(shares))
		
			try:
				os.system('cls') #Clears the screen (Windows).
			except:
				os.system('clear') #Linux /OS X
			print "\n============================="
			print symbol.upper()
			print "============================="		
			print "Price        |      $ %s" %price
			print "============================="
			print "Shares       |        %s" %shares
			print "============================="
			print "Commission   |      $ %s" %commission		
			print "============================="		
			print "Break-Even   |      $",round(breakEven,4)
			print "=============================\n"		
			start()	
		except:
			print "\n========================="
			print "\nCould not find %s. Typo?\n" %symbol.upper()
			print "=========================\n"		
			start()			
		
	elif selection == "help":
		import webbrowser
		url = "https://github.com/ngafar/Plancials#help"
		webbrowser.open(url)
		start()	
		
	else:
		try:
			os.system('cls') #Clears the screen (Windows).
		except:
			os.system('clear') #Linux /OS X
		print "\n========================="
		print "\nNot a valid value\n"
		print "=========================\n"		
		start()
		
start()

"""
----------------------------------------------------------------------

Development Name: Plancials
Author: Nawaz Gafar
Permission is hereby granted to any user, the ability to use, copy, 
modify, and distribute, free of any charge, subject to the agreement 
of the following 
conditions: 

- The notice above (starting with "Development Name") will appear in 
  any iterations of this file, or any further files that are a result 
  of modification of this file. 

Please also not that this application is distributed without any 
expressed or implied warrant. As such no liability shall be incurred 
by the author for any subsequent event that should occur as a result 
of information  acquired using this application.   

----------------------------- Tamam Shud -----------------------------
"""