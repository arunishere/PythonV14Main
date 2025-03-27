'''
Question No: 41

Stock Trading System - Create the below classes. 
Stock - Attributes: symbol, price_per_share
Methods: - update_price(new_price)  & get_price()
Trader - Attributes: name, portfolio (dictionary of stocks & quantities), balance, transaction_history.
Methods:
buy_stock(stock, quantity): Purchases stock if the trader has enough balance.
sell_stock(stock, quantity): Sells stock if available in the portfolio.
view_portfolio(): Displays all stocks owned and their total value.
view_transaction_history(): Displays past buy/sell transactions.

StockMarket
Attributes: stocks (list of available stocks).
Methods:
list_stocks(): Displays available stocks and their prices

'''

# S.No.	Name	CMP Rs.	P/E	Mar Cap Rs.Cr. 	Div Yld %	NP Qtr Rs.Cr.	Qtr Profit Var %	Sales Qtr Rs.Cr.	Qtr Sales Var %	ROCE %
# 1.	Reliance Industr	1273.05	24.90	1722805.27	0.39	21930.00	7.38	239986.00	6.62	9.61
# 2.	HDFC Bank	1806.55	19.87	1382357.66	1.08	18340.11	2.31	85040.17	9.01	7.67
# 3.	TCS	3635.80	26.98	1315482.24	1.51	12444.00	5.16	63973.00	5.60	64.28
# 4.	Bharti Airtel	1738.55	52.00	1039731.25	0.46	16134.60	230.71	45129.30	19.08	13.13
# 5.	ICICI Bank	1335.90	

class Stock:

    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def updatePrice(self, newPrice):
        self.price = newPrice

    def getPrice(self):
        return self.price
    
    def getSymbol(self):
        return self.symbol
    

class Trader: 

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.porfolio = {}
        self.transaction = []

    def buyStock(self, stock, quantity):
        total_cost = stock.getPrice() * quantity
        if self.balance >= total_cost:
            #Updating the balance
            self.balance -= total_cost
            if stock.getSymbol() in self.porfolio:
                self.porfolio[stock.getSymbol()] += quantity
            else:
                self.porfolio[stock.getSymbol()] = quantity
            self.transaction.append(f'Bought {quantity} of {stock.getSymbol()} at INR {stock.getPrice()}')
        else:
            print('Insufficent Balance')

    def getPortfolio(self):
        return self.porfolio

    def displayDetails(self):
        print(f'Name: {self.name}')
        print(f'Current Balance: {self.balance}')
        print('Transactions:')
        if len(self.transaction) == 0:
            print('No Transactions to show')
        else:
            print(self.transaction)


Reliance = Stock("REL", 1273.05)
HDFC = Stock("HDFCBK", 1806.55)
TCS = Stock("TCSIN", 3635.80)
Airtel = Stock("AIR", 1738.55)
ICICI = Stock("ICI", 1335.90)

John = Trader('John Deck', 10000)
Mike = Trader('Michael', 0)


# John.buyStock(Reliance, 3)
# John.buyStock(HDFC, 2)
# John.buyStock(Airtel, 3)

Mike.buyStock(Reliance, 3)

# John.displayDetails()

