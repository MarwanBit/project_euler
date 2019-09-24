#WIP

def get_factors_list_of_n(n):
    factors_list = []
    for i in range(1,n+1):
        if n%i == 0:
            factors_list.append(i)
    return factors_list 

def find_primes_in_a_list(input_list):
    primes_list = []
    for i in input_list:
        prime_factors_list = []
        for k in range(1,i+1):
            if i%k == 0:
                prime_factors_list.append(i)
        if len(prime_factors_list) > 2:
            pass 
        else:
            primes_list.append(i)
    return primes_list


