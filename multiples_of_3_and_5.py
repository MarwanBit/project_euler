'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
def sum_of_multiples_of_3_and_5_below_n(n):
    multiples_of_5_set = set()
    multiples_of_3_set = set()
    for i in range(1,n):
        if i%3 == 0:
            multiples_of_3_set.add(i)
        if i%5 == 0:
            multiples_of_5_set.add(i)
    format_string = "Multiples of 3: {},\n\n\n Multiples of 5: {},\n\n\n Union: {},\n\n\n Sum of All Multiples {}"
    sum_of_multiples = 0
    for i in multiples_of_3_set.union(multiples_of_5_set):
        sum_of_multiples += int(i)
    formatted_prompt = format_string.format(str(multiples_of_3_set),str(multiples_of_5_set),
    str(multiples_of_3_set.union(multiples_of_5_set)),sum_of_multiples)
    return formatted_prompt


print(sum_of_multiples_of_3_and_5_below_n(1000))