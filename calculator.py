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
		print "\n========================="
		print "Price        |      $%s" %price
		print "========================="
		print "Shares       |       %s" %shares
		print "========================="
		print "Commission   |      $%s" %commission		
		print "========================="		
		print "Break-Even   |      $%s" %breakEven
		print "=========================\n"		
		start()
		
	elif selection == "2":
		print "Stock Symbol (ex. AAPL or BAC)"
		symbol = raw_input("> ")
		
		print "Shares Purchased"
		shares = raw_input("> ")
		
		print "Commission Paid"
		commission = raw_input("> ")
		
		#Stock Price lookup
		yahooFinance = urllib2.urlopen("http://finance.yahoo.com/q?s="+symbol).read()
		price = yahooFinance.split('<span id="yfs_l84_'+symbol.lower()+'">' )[1].split("</span>")[0]
		
		breakEven = ((float(price) * float(shares)) + float (commission)) / (float(shares))
		
		try:
			os.system('cls') #Clears the screen (Windows).
		except:
			os.system('clear') #Linux /OS X
		print "\n========================="
		print symbol.upper()
		print "========================="		
		print "Price        |      $%s" %price
		print "========================="
		print "Shares       |       %s" %shares
		print "========================="
		print "Commission   |      $%s" %commission		
		print "========================="		
		print "Break-Even   |      $%s" %breakEven
		print "=========================\n"		
		start()		
		
	elif selection == "help" or "HELP" or "Help":
		try:
			os.system('cls') #Clears the screen (Windows).
		except:
			os.system('clear') #Linux /OS X
		print "Confused? Curious? A bit of both? Well your in the right place."
		print "\nHow to use"
		print "========================="
		print "Simply type in the number that corresponds with the option you would like to choose. This is either '1' or '2' (without quotation marks)."
		print "\nWhat do the options mean?"
		print "========================="
		print ">Option 1 is to calculate the break-even price of a stock by typing in the price paid, shares purchased, and commission paid.\n"
		print ">Option 2 will take a stock symbol and find its current price to calculate the break-even price."
		print "\nWhy do I need this?"
		print "========================="
		print "Trading stocks is often associated with transaction costs in the from of commission. It is beneficial to know at what price when selling a stock, you will have covered any transaction costs and started to make profits."
		print "\n=========================\n"
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