def corrector(string, width, symbol):
    print("{string:{symbol}^{width}s}.".format(string=string, width=width, symbol=symbol))

corrector(string=input("Your text: "), width=input("Your width: "), symbol=input("Your symbol: "))
