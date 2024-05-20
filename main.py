sale_product = ["sale", "resale"]

products = ["shirt", "shoes"]

sale_shirt = input("please enter numbers of sale from shirt : ")

sale_shoes = input("please enter numbers of sale from shoes : ")

resale_shirt = input("please enter numbers of resale from shirt : ")

resale_shoes = input("please enter numbers of resale from shoes : ")

print("This month we have : ", sale_product[0], sale_shirt + " product from", products[0],
	  " and we have : ", sale_product[0], sale_shoes + " product from", products[1]
	)

print("This month we have : ", sale_product[1], resale_shirt + " product from ", products[0], 
	  " and we have : ", sale_product[1], resale_shoes + " product from ", products[1]
	)

print("Thanks for visiting our store.")