x = int(input( "What's your x :"))
y = int(input( "What's your y :"))

if x % 2 == 0:
    print ("x is pair")
elif x < y:
    print("x is less than y")
elif x > y: 
    print("x is greater than y")
else:
    print("x is equal than y")