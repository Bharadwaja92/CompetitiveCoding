"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is
equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.

"""


def digitsProduct(product):
    # Get factors of product
    if product == 0:
        return 10
    if product == 1:
        return 1
    factorsOfProduct = [i for i in range(2, int(product/2)+1) if product%i == 0 and len(str(i)) == 1]
    # i = 2
    # while i <= int(product/2):
    #     factorsOfProduct.append(i) if product%i == 0 and len(str(i)) == 1 else None
    #     i += 1
    print('\n\nfactorsOfProduct are', factorsOfProduct)
    if len(factorsOfProduct) == 0:
        return -1
    p1 = product
    nums = []
    while p1 > 1:
        flag = False
        f = len(factorsOfProduct)-1
        while f >= 0 and not flag:
            if p1 % factorsOfProduct[f] == 0:
                nums.append(factorsOfProduct[f])
                p1 /= factorsOfProduct[f]
                flag = True
            f -= 1
    # print('nums is', nums)
    return int(''.join(map(str, sorted(nums))))





product = 450   # 2559
print(product, digitsProduct(product))
product = 12
print(product, digitsProduct(product))
product = 127
print(product, digitsProduct(product))
product = 0     # 10
print(product, digitsProduct(product))
product = 13     # -1
print(product, digitsProduct(product))
product = 1     # 1
print(product, digitsProduct(product))
product = 243     # 399
print(product, digitsProduct(product))
product = 576     # 889
print(product, digitsProduct(product))
product = 360     # 589
print(product, digitsProduct(product))


"""
    for i in range(len(factorsOfProduct)):
        for j in range(len(factorsOfProduct)):
            if factorsOfProduct[i]*factorsOfProduct[j] == product:
                nums.append(int((str(factorsOfProduct[i])+str(factorsOfProduct[j]))))

"""