#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.


def collectStrings(obj):
    temp_list=[]
    for j,i in obj.items():
        print(j,i)
        if type(i) is str:
            temp_list.append(i)
        if type(i) is dict:
            return temp_list+collectStrings(i)
    return temp_list



# def collectStrings1(obj):
#     resultArr = []
#     for key in obj:
#         if type(obj[key]) is str:
#             resultArr.append(obj[key])
#         if type(obj[key]) is dict:
#             resultArr = resultArr + collectStrings1(obj[key])
#     return resultArr





obj2 = {
    'employee':{
        'name': 'John Doe',
        'age': '30',
        'position': 'Software Engineer',
        'contact': {
            'email': 'john.doe@example.com',
            'phone': '555-1234'
        },
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'CA',
            'zip': '12345'
        }
    }
}





print(collectStrings(obj2))
