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
if len(nums) < 3:
   print("wrong entry")
else:
    total_num=int(input("how any number do you want: "))
    for n in range(0, total_num):
        join = add(nums)
        if join=="7065345904":
            print(f"your number is {join} you win")
        print(join)