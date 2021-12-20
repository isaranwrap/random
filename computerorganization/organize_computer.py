import os, sys

print(os.listdir())

delimiters = [" ", "\t", "\n", "_", os.sep, "/"]

dataFolders = ["Automobile Records", "Bank Records", "Budget", "Credit Cards", "Dental Records", "Expenses", "Income", "Insurance", "Investments", "Legal", "Loans", "Medical Records", "Mortgage Rent", "Personal", "Real Estate", "Receipts", "Schools", "Taxes", "Utilities", "Warranties"]

def mkOrganize(*args, **kwargs):
	for folder in dataFolders:
		print(folder)
	return None
