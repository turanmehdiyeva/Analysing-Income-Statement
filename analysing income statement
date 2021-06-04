Sale = float(input('Sales:'))
COGS = float(input('Cost of Goods Sold:'))
GP = Sale - COGS
print('Gross Profit:',GP)
mup = (GP/COGS)*100
print('Markup on cost:',str(mup)+'%')
gm = (GP/Sale)*100
print('Gross marign:', str(gm)+'%')
while True:
    i = input('Expenses (0 to exit):\n')
    i = float(i)
    if i == 0:
        break
    Total = []
    Total.append(i)
    Totalex = sum(Total)
NP = GP-Totalex
print('Net Profit',NP)
npm = (NP/Sale)*100
print('Net Profit Margin:', str(npm)+'%')
pp = (NP/COGS)*100
print('Profit Percentage:', str(pp)+'%')
