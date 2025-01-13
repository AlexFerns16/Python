# store the data about shares held by a user as tuples
# containing the following information about shares

# share name
# date of purchase
# cost price
# number of shares
# selling price

# write a program to determine

# total cost of the portfolio
# total amount gained or lost
# percentage profit gained or incurred
    
    # profit = selling price - buying price
    # profit percentage = (profit / buying price) * 100

ShrOne = ('TATA', '04/08/19', 40, 3, 51)
ShrTwo = ('Tesla', '09/11/19', 45, 4, 55)
ShrThr = ('SpaceX', '17/05/20', 35, 2, 30)

TotShares = (ShrOne, ShrTwo, ShrThr)

TotCostShares = 0

for i in TotShares:
    IndCostShare = i[4] * i[3]
    TotCostShares = TotCostShares + IndCostShare
    #     153             0               153
    #     373            153              220
    #     433            373              60
print(TotCostShares)
