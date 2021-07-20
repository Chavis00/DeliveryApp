#Global Variable to Show cart total amount in all pages 
def cartTotalAmount(request):
    total = 0
    if 'cart' in request.session:
        for key, value in request.session["cart"].items():
            total = total + (float(value["price"])*value["quantity"])
    return {"cartTotalAmount":total}


