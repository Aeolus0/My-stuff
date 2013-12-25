"""Sum of all even fibonacci numbers from 2 to x [4 million]"""

fib = [1, 1, 2]

def next_fib():
    global fib
    fib.append(fib[1] + fib[2])
    del fib[0]

def add_fib(final_number):
    total_fib = 0
    global fib
    for iterator in xrange(0,final_number + 1):
        if final_number <= fib[len(fib) - 1]:
            break
        if fib[len(fib) - 1] % 2 == 0:
            total_fib += fib[len(fib) - 1]
        next_fib()
    return total_fib

inp = long(raw_input("enter final number here: "))
print add_fib(inp)