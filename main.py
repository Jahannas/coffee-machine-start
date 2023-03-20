MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


quarter = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


resources_espresso_water = MENU["espresso"]["ingredients"]["water"]
resources_espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
resources_espresso_cost = MENU["espresso"]["cost"]

resources_latte_water = MENU["latte"]["ingredients"]["water"]
resources_latte_milk = MENU["latte"]["ingredients"]["milk"]
resources_latte_coffee = MENU["latte"]["ingredients"]["coffee"]

resources_cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
resources_cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
resources_cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]

resources_water = resources["water"]
resources_milk = resources["milk"]
resources_coffee = resources["coffee"]

def users_choice ():
  choice = input ("What would you like? espresso/latte/cappucino : ")
  report = input("Enter 'report' to view the current resource values:")
  
  #while close != "off":
  if report == "report":   
      print(resources)

  if choice == "espresso":
  
    if resources_water - resources_espresso_water >= 0 and resources_coffee - resources_espresso_coffee >= 0:
       output =  print ("You have enough resources for espresso") 
       coins = float(input("Please insert coins."))
          
    elif resources_water - resources_espresso_water < 0:
        if resources_coffee - resources_espresso_coffee >= 0:
             print("Sorry you don't have enough water")
    elif resources_water - resources_espresso_water >= 0:
        if resources_coffee - resources_espresso_coffee < 0:
             print("Sorry you don't have enough coffe")  
    else:
        print("Sorry you don't have enough resources")
      
    if coins == resources_espresso_cost:
      print("Here is your espresso")
      #You have left water, milk, coffee
           
      print (resources)
    elif coins > resources_espresso_cost:
      print(f"Here is your change of ${coins - resources_espresso_cost}")
    else: 
      print("You don't have enough money")
        
  #close = input ("Turn off the Coffee Machine by entering 'off'.")
   
    resources["cost"] = coins
    resources["water"]= resources_water - resources_espresso_water
    resources["coffee"]= resources_coffee - resources_espresso_coffee
  
users_choice()
  
