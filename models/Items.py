#Class use for Item Creation

class Item:
     def __init__(self,name,description,price):
         self.name =  name
         self.description  = description
         self.price   =   price

     def getName(self):
         return self.name
    
     def getDescription(self):
        return self.description
    
     def getPrice(self):
         return self.price
    
     def getInfo(self):
        str = 'Name: ' + self.name + ' Description: ' + self.description + '  Price: ' + self.price