import random
def num():
    list= [n for n in range(0, 9) ]
    data="706534"
    for _ in range(0,4):
        choice=random.choice(list)
        data +=str(choice)
    return data


nums = input("enter the country code: ")
def add(nums):
    nums += num()
    return nums


def list_num(data):
    for n in data:
        print(n)

def proce():
    valid = []
    if len(nums) < 3:
        print("wrong entry")
    else:
        
        total_num=int(input("how many number do you want: "))
        for n in range(0, total_num):
            join = add(nums)
            if join not in valid:
                valid.append(join) 
    #print(valid)
    return valid

#proce()
list_num(proce())

def test(*argv):
    #data = argv[0]
    if isinstance(argv[0], str):
        print("success")
    else:
        print("fail")

#test(45)