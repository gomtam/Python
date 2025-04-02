nums =[1,2,5,5,9,8,4,2,6,3,5,8,4,7,1,22.3,4.21,1.5,8.5,6.1,4.9]

"""
myList = []
for num in nums:
    if num < 5 :
        myList.append(num)
"""

myList = [num for num in nums if num < 5]
print(myList)

