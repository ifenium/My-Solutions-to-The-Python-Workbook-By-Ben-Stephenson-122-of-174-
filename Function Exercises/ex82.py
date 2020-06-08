'''
Exercise 82: Taxi Fare
In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
for every 140 meters traveled. Write a function that takes the distance traveled (in
kilometers) as its only parameter and returns the total fare as its only result. Write a
main program that demonstrates the function.
'''

def taxifare(distance):
    base = 4.00
    extra = distance * 1000 % 140
    total = base + extra * 0.25
    return total

def main():
    distance = float(input('Enter total distance traveled(in kilometers): '))
    print('Your Taxi Fare for {} Kilometer(s) is ${}'. format(distance, taxifare(distance)))

main()