
#Shopping Cart 
class ShoppingCart:
    def __init__(self, request):
        
        #in this session
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")

        #if cart is not created, create an empty cart
        if not cart:
            cart = self.session["cart"] = {}

        #else just get the same cart
        self.cart = cart
        
    #add a product in the cart
    def add (self, product):

        #if the product is not in the cart dicctionary, it is added using the id as key
        if (str(product.id) not in self.cart.keys()):
            self.cart[product.id] = {
                "id" : product.id,
                "name": product.name,
                "price": str(product.price),
                "quantity": 1,
                "pic": product.pic.url,
            }

        #if the product is in the car, just modify quantity+1
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"]+1
                    break 

        #save the cart modifications
        self.saveCart()

    #saving the cart modifications
    def saveCart(self):

        #apply modifications
        self.session["cart"] = self.cart
        self.session.modified = True

    #Delete product in the cart
    def deleteProduct(self, product):
        product.id = str(product.id)

        #if product id is in the cart, it will removed from the dictionary
        if product.id in self.cart:
            del self.cart[product.id]
            self.saveCart()

    #substract 1 product in the cart
    def substractProduct(self, product):
        
        #iterate over the dictionary
        for key, value in self.cart.items():

                #if the product id is found, quantity = 1 on de product dictionary
                if key == str(product.id):
                    value["quantity"] = value["quantity"]-1

                    #if there are no more products, delete product dictionary
                    if value["quantity"]<1:
                        self.deleteProduct(product) 

                    #when the product is found and the quantity is changed stop looking
                    break 
        #save changes        
        self.saveCart()
    
    #restart the cart
    def cleanCart(self):
        self.session["cart"] = {}
        self.session.modified = True
