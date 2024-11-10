#python version: 3.12.7
#no dependencies

'''
product price as an input, I first kept it as in int but then realized
that the price could also have cents in it so I converted it to float instead.
'''
pp: float = float(input('Price of the product: '))

#cash also as float since it can also contain cents
cash: float = float(input('Cash: '))

'''
checking a condition if cash is less than the product price, if yes, then 
there should be no calculation, since it does not make sense in the real
world, even though one could argue that the result in - would also be helpful
and show that how much amount is less but I preferred to do this way.
'''
if cash >= pp:
    change: float = round(cash - pp, 2) #round function because it was printing alot of decimal numbers
    print(change)
else:
    print('Not enough cash')


