# my first project 😌 Gemini challenged me 🫣 but didn't help to solve 😑 just helped me to found bugs 🥹 and i fixed all of them alone :)

import sys # or exit() or quit() — no need to import anything for those functions

# function1
def selectmovie(select_movie):
        if select_movie == "1":
                movie_name = "Rajkumar"
                return movie_name
        elif select_movie == "2":
                movie_name = "Bonolota Express"
                return movie_name
        elif select_movie == "3":
                movie_name = "Surongo"
                return movie_name

# function2
def membership_condition(membership_status):
    if membership_status == "yes":
        free = "৳100"
        membership = "yes"
        return free, membership 
    elif membership_status == "no":
        free = "৳0"
        membership = "no"
        return free, membership 
    else:
        free ="৳0"
        membership = "no"
        return free, membership 


# function3 
def age_validation():
    while True:
        try:
            age = input("Age: ")
            age = int(age)        
            if age>=110 and age<=120:
                print("Please, video call to this Whatsapp number to verify and buy special ticket for VIP seat: +8801982-483176. Thank you!")
                sys.exit()        
            elif age<0 or age>120:
                print("Please provide a valid age to continue.")
            else:
                return age

        except ValueError:
            print("Invalid Input.")       

# function4     
def promocode_check(promocode, ticket_price):
    if promocode == "yes":
        promo_code = input("Submit your promocode: ")
        if promo_code in ["GEMINIFRND", "JHS2026", "BDCYCLE", "KIAJHS1234"]:
                promo_code = promo_code
                discount = ticket_price*0.05
                total_price = ticket_price-discount
                return promo_code, discount, total_price

        else:
                promo_code = "None"
                discount = ticket_price*0
                total_price = ticket_price
                return promo_code, discount, total_price
    elif promocode == "no":
        promo_code = "N/A"
        discount = ticket_price*0
        total_price = ticket_price
        return promo_code, discount, total_price
    else: # no chance to correct 
        promo_code = "Invalid Input!"
        discount = ticket_price*0
        total_price = ticket_price
        return promo_code, discount, total_price
# intro
print("Welcome to JHS Movie Theater!\nYou can start buying tickets from here with providing some information.\nLet's start with your Full Name or Username...")

username = input("Full Name or Username: ").strip()
while True: # giving chance/pressure users to input valid thing
    if username:
        age = age_validation()
        break
    else:
        print("Please, provide your name/username.")
        username = input("Full Name or Username: ").strip()



while True: # giving chance/pressure users to input valid thing
    if age:
        membership_status = input("Do you have any membership?[Yes/No]").lower().strip()

        free, membership = membership_condition(membership_status)

        break

    else:
        print("Please, provide your age.")
        age = int(input("Age: ")) 

print("What movie do you want to enjoy?")
print("1. Rajkumar")
print("2. Bonolota Express")
print("3. Surongo")

select_movie = input("Select [1/2/3]: ")

while True: # giving chance/pressure users to input valid thing
    if select_movie in ["1", "2", "3"]:
        moviename = selectmovie(select_movie)
        break
    else:
        print("You pushed invalid input.")
        select_movie = input("Select [1/2/3]: ")

print("We're informing you... Generally ticket price is ৳500/person")
continue_0 = input("To continue, type '0', otherwise type anything to quit: ").strip()

if continue_0 == "0":
    if age<=5:
        ticket_price = 0
    elif age<18 and membership == "yes":
        ticket_price = 350
    #elif age<18 or membership == "yes": # this is wrong here
    elif age>=18 and membership == "yes":
       ticket_price = 375
    #elif age>=18 and membership == "yes": # and this is wrong here too. just do vice-versa 
    elif age<18 and membership == "no":
        ticket_price = 400

    elif age>=18 and membership == "no":
        ticket_price = 500
else:
    print("Ticket preparing cancelled!")
    sys.exit() #or can exit() or quit() 


promocode = input("Do you have any promocode?[Yes/No]").lower().strip()

promo_code, discount, total_price = promocode_check(promocode, ticket_price)

# ticket & money receipt 
print("Just wait.\nYour ticket is being processed...")

print(f"Audience: {username} ({age} y/o)")

print(f"Movie Name: {moviename}")

print(f"JHS Member: {membership} (You got discount {free}.)")

print(f"Sub-total: ৳{ticket_price}")

print(f"Promocode: {promo_code} (You got discount ৳{discount}.)")

print(f"Total Price: ৳{total_price}")

print(f"Thank you {username} for staying with us and using our service!")
