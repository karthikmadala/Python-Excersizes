
def is_prime_bw(start,end):
    for num in range(start,end+1):
        if num>1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:
                print(is_prime(num))
                print(int(num))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


is_prime_bw(2,10)