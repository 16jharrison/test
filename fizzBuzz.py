def fizzBuzz(first , second , UpperLimit):   

    for num in range(1,UpperLimit):
        result = ""
        if num % first == 0 : result += "fizz"
        if num % second == 0 : result += "Buzz"
        print( result or num)

fizzBuzz(3,5,100)

#advanced Fizz lets you pass a dictonary with custom words as keys with respective numbers for more flexiblity 
#Advanced Fizz also lets you set a custom upper and lower limit number range , ex 50 and 290 instead of the base 1 - 100
def advancedFizzBuzz(dic , lowerLimit , upperLimit):
    
    for num in range(lowerLimit,upperLimit+1):
        advResult = ""
        for key in dic:
            if num % dic[key] == 0 : advResult += key
        print(advResult or num)



advancedFizzBuzz({'Fizz':3 , 'Buzz':5} , 1 , 100)