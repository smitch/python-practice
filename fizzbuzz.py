import sys

def fizzbuzz(n):
    ret="1"
    for i in range(2, n+1):
        if (i%15)==0:
            ret+=" FizzBuzz"
        elif (i%3)==0:
            ret+=" Fizz"
        elif (i%5)==0:
            ret+=" Buzz"
        else:
            ret+=(" "+str(i))
    print(ret)

if __name__ == "__main__":
    args = sys.argv;

    if len(args)<2:
        print("error: python fizzbuzz.py <positive number>")
    elif not (args[1].isdigit()):
        print("error: python fizzbuzz.py <positive number>")
    elif int(args[1])<1:
        print("error: python fizzbuzz.py <positive number>")
    else:
        fizzbuzz(int(args[1]))
