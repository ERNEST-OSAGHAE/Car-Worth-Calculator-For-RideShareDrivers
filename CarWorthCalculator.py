
import calendar

#Ask purchase price here and ask once
m = int(input("What month did you purchase this car? "))
year = int(input("What year did you buy the car? "))
Purchase = input("What is the puchase price of the car? $")
#print("Make sure your earning from this car brings you the "Asset Value"")

def carWorth():
        return int(Purchase) * 3
print("The purchase price of this car = " + "$" + Purchase)
print("The \"Asset Value\" of this car = " + "$" + str(carWorth()) + " (This value is calculated by multiply the purchase price by 3)")
print("")

for month in calendar.month_name[m:]:
    print(month, year)




#funtion for value of car = Previous function - How much car has made(InputVariable)
    MoneyMade = input("How much has this car made? $")
    def valueOfCar():
        return int(MoneyMade) - int(carWorth())
    print("The car has made " + "$" + str(MoneyMade))
    print("The \"Asset Value\" - \"Money Made\" = " + "$" + str(valueOfCar()))
    if int(carWorth()) > int(MoneyMade):
        print("You have to work until this car value becomes positive.")
    elif int(carWorth()) == int(MoneyMade):
        print("You have broken even with price of car.")
    elif int(carWorth()) < int(MoneyMade):
        print("You have successfully worked the value of the car. Its in the positive.")
 #ifelse statement. if car runs into negative, place positive in front. if runs into negative value, place + in front
    print("")


#Function for remaining cost of car = CostofCar - Payment Made
    CarPayments = input("How much payments have been made? $")
    def remainingCostofCar():
        return int(Purchase) - int(CarPayments)
    print("The remaining payment for this car = " + "$" + str(remainingCostofCar()))
    print("")



