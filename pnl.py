def income_statement():
  sales = float(input('Enter Sales: '))
  cogs = float(input('Enter cost of sales: '))
  while True:
    expenses = float(input('Enter expenses (enter 0 to exit):\n'))
    if expenses==0:
      break
    Total = []
    Total.append(expenses)
  Totalex = sum(Total)
  gp = sales-cogs
  np = gp-Totalex
  mup = str(round((gp/cogs)*100,2))+'%'
  gm = str(round((gp/sales)*100,2))+'%'
  npm = str(round((np/sales)*100,2))+'%'
  pp = str(round((np/cogs)*100,2))+'%'
  print(f' Gross profit for the year is: {gp}\n Mark up on cost is: {mup}\n Gross marign is: {gm}\n Net Profit for the year is: {np}\n Net Profit Margin is: {npm}\n Profit Percentage: {pp}')
