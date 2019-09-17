

def main():
    nums = list(map(int, input().split(' ')))
    a, b = nums[0], nums[1]
    small = a if a < b else b
    print([i for i in range(1, small+1) if a % i == 0 and b % i == 0][-1])

 # Write code here

main()

