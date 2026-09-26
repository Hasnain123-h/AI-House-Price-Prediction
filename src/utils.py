def format_price(price):
    print("PRICE:", price)
    print("TYPE:", type(price))
    price=float(price)
    return f"${price:.2f}"
  
   
    
    


if __name__=="__main__":
    test_price=250000
    
    formated_price=format_price(test_price)
    print(formated_price)