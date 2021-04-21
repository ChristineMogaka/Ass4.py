#Enter the price of the House you wish to Buy
price = float (input("Enter the house price: "))
print(price)

#Enter the credit score
CreditScore = int (input("Enter the credit score: "))
print(CreditScore)

#Enter the first name
first_name = input("Enter the first name: ")
print(first_name)

#Enter the last name
last_name = input("Enter the last name: ")
print(last_name)

fullnames = first_name + " "+ last_name

#Enter the email

email = input("Enter the email address: ")
print(email)

#Enter the phone number
phone = input("Enter the phone number: ")
print(phone)

#Enter the mailing
mailingAddress= input("Enter the mailing address: ")
print(mailingAddress)

#Enter the city
city = input("Enter the city: ")
print(city)

#Enter the zipcode
zipcode = input("Enter the zipcode: ")
print(zipcode)
#qualifying the loans with best interest rates
if 780 <=850:
    downPayment = 0.0 * price
    print("Excellent Credit")
    print("Downpayment = " + str(downPayment))


#Usually qualify for loans with the best interest rates
elif 740 <= CreditScore <=779:
    downPayment = 0.2 * price
    print("Very Good Credit")
    print("downPayment = " + str(downPayment))
    price = downPayment + price

#May face slightly higher loan Interest rates
elif CreditScore >= 720 and CreditScore <=739:
    downPayment = 0.3 * price
    print("Above Average")
    print("downPayment = " + str(downPayment))
    price = downPayment + price

#May qualify for most loans of higher interest rates
elif CreditScore >= 680 and CreditScore <= 719:
    downPayment = 0.6 * price
    print("Average")
    print("DownPayment = " + str(downPayment))
    price = downPayment + price

#May qualify for most loans at significant higher Interest rates
elif creditscore >= 620 and creditscore <= 679:
    downPayment = 0.18 * price
    print("Below Average")
    print("DownPayment = " + str(downPayment))
    price = downPayment + price

#Usually has some credit issues; will probably not qualify for most loans
elif creditscore >= 580 and creditscore <= 619:
    downPayment = 0.20 * price
    print("Poor Credit Score")
    print("DownPayment = " + str(downPayment))
    price = downPayment + price
#Facing extreme credit issue
else: 
    creditscore < 520
    downPayment = 0.25 * price
    print("Poor Credit Score")
    print("DownPayment = " + str(downPayment))
    price = downPayment + price