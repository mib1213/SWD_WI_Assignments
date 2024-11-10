#python version: 3.12.7
#no dependencies

'''
Setting up variable names for given length and width,
I would not prefer to give full names because they
are harder to write but also not very short names 
as they will be harder to understand so I think 
names like rect_len is a good combination of size
and clarity.
'''

rect_len: int = 4 #in m
rect_wid: int = 3 #in m

#calculating the rectangle area with the formula l x b
rect_area: int = rect_len * rect_wid #in sqm

#since the value of rect_area is in sqm I can multiple by price per sqm
net_price: int = rect_area * 50 #in Euros/sqm 

purchase_tax: float = 0.035 #3.5% purchase tax

gross_price: float = net_price * (1 + purchase_tax) #price after tax in Euros

print(f'This land costs {gross_price}€')

'''
here I was not sure what would be the type of the variables after multiplication,
so I checked the type with type function, apparently it remains an int if you multiply
an int with an int, but it will be converted to float type if an int is multiplied by
a float type object like in case of gross_price.
'''

#print(type(rect_area), type(net_price), type(gross_price))