n=int(input("print till ", ))

def print_till_zero(n):
    if n == 0:
        return ("нечего писать Т_Т")
    else:
        while n>0:
            print(n)
            n=n-1
            return(print_till_zero(n))
        
print(print_till_zero(n))
