class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.shoe_type = shoe_type
        self.price = price
        #availability
        self.in_stock=True
    
    def on_sale_by_percent(self,percent):
        self.price = (1 - percent) * self.price

    #Add tax to the Item
    def total_with_tax(self,tax_rate):
        self.price = (1 + tax_rate) * self.price
        return self.price
    
    #Discount Item by x amount
    def fixed_discount(self,disc_amount):
        self.price = self.price -disc_amount
        return self.price
    
    def __str__(self):
        return f'{self.brand} {self.shoe_type} {self.price} In Stock: {self.in_stock}'
    
    


skater_shoe = Shoe('Vans','Low-top Trainers',59.99)
dress_shoe = Shoe('Nike','Basketball',29.99)
print(skater_shoe)
print(dress_shoe)

print(skater_shoe.brand)
print(dress_shoe.brand)

akala=Shoe('Mike','Sandal',35.99)
print(akala)
akala.in_stock=False
print(akala)
print(akala.price)

print(akala)
akala.on_sale_by_percent(0.2)
print(akala)
akala.total_with_tax(.16)
print(akala)
akala.fixed_discount(20)
print(akala)


'''
#skater shoe 20%  sale
skater_shoe.price = (1 - .2) * skater_shoe.price
#dress hoe down 10%
dress_shoe.price = dress_shoe.price * (1 - .1 )
print(skater_shoe.price)
#another 10% resuction for skater
skater_shoe.price = (1 - .1) * skater_shoe.price

#what changed? the percentage amount!
Everything is referancable by self.attribute


#Change this into a function
'''