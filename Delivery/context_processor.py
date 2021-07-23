#Global Variable to Show cart total amount in all pages 
def cartTotalAmount(request):
    total = 0
    if 'cart' in request.session:
        for key, value in request.session["cart"].items():
            total = total + (float(value["price"])*value["quantity"])
    total = "{:.2f}".format(total)
    return {"cartTotalAmount":total}
    
def total(request):

    total = 0
    if 'cart' in request.session:
        for key, value in request.session["cart"].items():
            total = total + (float(value["price"])*value["quantity"])
    total += 4
    total = "{:.2f}".format(total)   
    
    return {"total":total}

