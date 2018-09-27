# Anthony & Will

def fizzBuzz(max_value):
    i = 1
    while (i <= max_value):
        output = ""
        if i % 3 == 0:
            output+="Fizz"
        if i % 5 == 0:
            output+="Buzz"
        if output:
            print(output)
        else:
            print(i)
        i+=1
    return int(max_value / 15)

fizzBuzz(100