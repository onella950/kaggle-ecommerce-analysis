import math

#1. Required inputs
teammates = (int(input("Enter number of team members: ")))
rank = (int(input("Enter competition rank (1 = first): ")))
teams = (int(input("Enter total number of teams: ")))

print("Inputs are:", teammates, rank, teams)  #have the inputs displayed in the order prompted above

#2. Iterate over the number of days since the competition (monthly increments)
    #Broke down formula into (A,B,C) components for clarity
A = 100000 / math.sqrt(teammates)
B = rank ** (-0.75)
C = math.log10(1 + math.log10(teams))

print("Awarded competition points over time:")
print("Days   Points")

#3. Over each number of days t = 0, 30, 60, …, 360
for t in range(0, 361, 30):        #loop in increments of 30 days (t= days)
    D = math.exp(-t / 500.0)        # As t increases, the exponent (-t/500) becomes more negative,
                                    # so as D gets smaller (closer to 0). This simulates exponential decay over time.
    points = A * B * C * D
    print(f"{t:3d}   {points:,.2f}")  # 3d- "d" stands for integers and 3 is so that there is at least 3 spaces wide
                                      #"2f" requesting that it shows as a floating-point number with 2 decimal places
