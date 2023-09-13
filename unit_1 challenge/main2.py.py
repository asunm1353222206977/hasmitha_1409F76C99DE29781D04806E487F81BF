year=int(input("Enter your year:"))
if year%4==0:
  print("%d given year is leap year"%year)
elif(year%100==0):
  print("%d given year is not leap year" %year)
elif(year%400==0):
  print("%d give year is leap year" %year)
else:
  print("%d given year is not leap year.")
  