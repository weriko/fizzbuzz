#Easy way

empt = []
for x in range(1,101):
    
    if x %5 == 0:
        if x %3 ==0:
            empt.append("fizzbuzz")
        else:
            empt.append("buzz")
    elif x %3 == 0:
        empt.append("fizz")

    else:
        empt.append(str(x))
print(empt)

#Easy way but a bit less dumb
empt2 = []
for x in range(1,101):
    temp =""
    if x%3 ==0: temp+="fizz"
    if x%5 == 0: temp+="buzz"
    
    if not temp: temp = str(x)
    
    empt2.append(temp)
    
print(empt2)
#Dumb ternary way
print([   ("fizzbuzz" if (x%3==0 and x%5==0) else ("buzz" if x%5==0 else "fizz"))  if (x%3==0 or x %5 == 0) else str(x) for x in range(1,101)])

#Dumb lambda hype way
print(list ( map( lambda x: f"{'fizz'*(x%3==0)}{'buzz'*(x%5==0)}" or str(x), range(1,101) ) ) )


#Dumb over engineered dictionary way
dictionary = {
    "3" : "fizz",
    "5" : "buzz",
    "35" : "fizzbuzz",
    
    }

empty = []

for x in range(1,101):
    try:
        empty.append( dictionary[(x%3==0)*str(3) + (x%5==0)*str(5)] )
        
    except:
        
        empty.append(str(x))


print(empty)

#The Dumb over engineered dictionary way but with an extra touch of dumb over engineered list comprehensions
print([ dictionary.get((x%3==0)*str(3) + (x%5==0)*str(5), str(x) ) for x in range (1,101)])
        

#FizzBuzz but for more numbers? with epic list comprehensions that I won't comprehend in two weeks!

def fizzbuzz(dictionary, rang):
    return(["".join(  [dictionary.get((x % int(k) == 0)*str(k), ""  ) for k in dictionary.keys()  ]) or str(x) for x in range (rang[0],rang[1]) ])

dictionary2 = {
    
    "3" : "fizz",
    "5" : "buzz",
    "7" : "something",
    "9" : "im",
    "11" : "not",
    "13" : "creative"
    
    }

print(fizzbuzz(dictionary2 , (1,101) ))


dictionary3 = {
    "3": "at",
    "5": "this",
    "7": "point",
    "9": "there",
    "11": "isnt",
    "13": "even",
    "17" : "fizz",
    "19" : "or",
    "23" : "buzz",
    "29" : "random",
    "31" : "primes",
    }

#print(fizzbuzz(dictionary3 , (1,1001) ))


#why








