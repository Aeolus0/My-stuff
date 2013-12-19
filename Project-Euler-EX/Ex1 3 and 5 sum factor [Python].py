"""Ex 1 Euler, find the sum of all factors of the number divisible by 3 or 5"""
sum_array = [3]

def what_inc(term_num):
    if term_num == 0 or term_num == 4:
        return 2
    if term_num == 1 or term_num == 3:
        return 1
    if term_num == 2 or term_num == 5:
        return 3

def sum_num(final_num):
    global temp
    count = -1
    for incr in range(1,final_num + 1):
        count = count + 1
        if count <= 5:
            temp = sum_array[len(sum_array) - 1]
            if (temp + what_inc(count)) >= final_num:
                break
            sum_array.append(temp + what_inc(count))

        else:
            count = 0

    return sum_array


temp = 0
inp = long(raw_input("Enter last number: "))
print sum(sum_num(inp))