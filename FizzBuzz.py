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
        

