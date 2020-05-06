def romano(input):
    ints = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
    nums = ('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input/ ints[i])
        result.append(nums[i]*count)
        input -= ints[i]*count
    return ''.join(result)

num = int(input('Entre com um número de 1 a 1000:'))
print(romano(num))