def fizzBuzz(first , second , UpperLimit):   

    for num in range(1,UpperLimit):
        result = ""
        if num % first == 0 : result += "fizz"
        if num % second == 0 : result += "Buzz"
        print( result or num)



def advancedFizzBuzz(dic , lowerLimit , upperLimit):
    
    for num in range(lowerLimit,upperLimit+1):
        advResult = ""
        for key in dic:
            if num % dic[key] == 0 : advResult += key
        print(advResult or num)


        
advancedFizzBuzz({'Fizz':3 , 'Buzz':5} , 1 , 100)