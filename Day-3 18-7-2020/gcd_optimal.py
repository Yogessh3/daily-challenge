#O(N log n) Time Complexity min(a,b)=>n / O(1) Space Complexity
def find_gcd(a,b):
    if(a==0):
        return b
    else:
        return find_gcd(b%a,a)
a=13
b=60
print(find_gcd(a,b))
