# store the data about shares held by a user as tuples
# containing the following information about shares

# share name
# date of purchase
# cost price
# number of shares
# selling price

# write a program to determine

# - total cost of the portfolio
# - total amount gained or lost
# - percentage profit gained or incurred

ShrOne = ('TATA', '04/08/19', 40, 3, 51)
ShrTwo = ('Tesla', '09/11/19', 45, 4, 55)
ShrThr = ('SpaceX', '17/05/20', 35, 2, 30)
ShrFou = ('Amazon', '26/05/21', 51, 7, 62)
ShrFiv = ('BlueOrigin', '07/07/20', 42, 5, 45)

TotShares = (ShrOne, ShrTwo, ShrThr, ShrFou, ShrFiv)


# total cost of the portfolio
# -----------------------------------------------------------------

TotCostShrs = 0
for i in TotShares:
    CostIndShr = i[4] * i[3]
    TotCostShrs = TotCostShrs + CostIndShr
print(TotCostShrs)


# total amount gained or lost
# -----------------------------------------------------------------

TotShrsGainedLost = 0
for i in TotShares:
    ShrsPurchased = i[2] * i[3]
    ShrsPresent = i[4] * i[3]
    IndShrGainedLost = ShrsPresent - ShrsPurchased
    TotShrsGainedLost = TotShrsGainedLost + IndShrGainedLost
print(TotShrsGainedLost)


# percentage profit gained or incurred
# -----------------------------------------------------------------

ShrsPurchased = 0
ShrsPresent = 0
for i in TotShares:
    ShrsPurchased = ShrsPurchased + (i[2] * i[3])
    ShrsPresent = ShrsPresent + (i[4] * i[3])
print(ShrsPurchased)
print(ShrsPresent)

# profit = selling price - buying price
# profit percentage = (profit / buying price) * 100

Profit = ShrsPresent - ShrsPurchased
ProfitPer = (Profit / ShrsPurchased) * 100
print(ProfitPer)
