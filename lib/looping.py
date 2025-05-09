#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        print("Happy New Year!")
        i -= 1

def square_integers(int_list):
    # code goes here!
    return list(x ** 2 for x in int_list)

def fizzbuzz(num = 100):
    # code goes here!
  for i in range(1, num + 1):
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)
