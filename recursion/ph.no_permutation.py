def phone_number(processed,unprocessed):
    if unprocessed=="":
        print(processed)
        return
    phone_number(processed+chr(97+(int(unprocessed[0])-1)*3),unprocessed[1:])
    phone_number(processed+chr(98+(int(unprocessed[0])-1)*3),unprocessed[1:])
    phone_number(processed+chr(99+(int(unprocessed[0])-1)*3),unprocessed[1:])
phone_number("","123")


# using for loop insead of 3 recurion calls #---------------------------------------

def phone_number(processed,unprocessed):
    if unprocessed=="":
        print (processed)
        return
    for i in range(97,100):
        phone_number(processed+chr(i+(int(unprocessed[0])-1)*3),unprocessed[1:])
        
phone_number("","11")


# Returning List #-----------------------------------------------------------

def phone_number(processed,unprocessed):
    if unprocessed=="":
        return [processed]
    a=phone_number(processed+chr(97+(int(unprocessed[0])-1)*3),unprocessed[1:])
    b=phone_number(processed+chr(98+(int(unprocessed[0])-1)*3),unprocessed[1:])
    c=phone_number(processed+chr(99+(int(unprocessed[0])-1)*3),unprocessed[1:])
    return a+b+c
print(phone_number("","123"))

#Returning List For loop#--------------------------------------------------

def phone_number(processed,unprocessed):
    list1=[]
    if unprocessed=="":
        return [processed]
    for i in range(97,100):
        
        list1+=phone_number(processed+chr(i+(int(unprocessed[0])-1)*3),unprocessed[1:])
    return list1
        
print(phone_number("","123"))

#Using Global list #-----------------------------------------------------------------

list1 = []  # Declare list1 outside of the function

def phone_number(processed, unprocessed):
    global list1  # Use the global keyword to modify the global list1

    if unprocessed == "":
        list1.append(processed)  # Append the result to the global list1
        return

    for i in range(97, 100):
        phone_number(processed + chr(i + (int(unprocessed[0]) - 1) * 3), unprocessed[1:])

phone_number("", "123")
print(list1)  # The global list1 will contain all the phone number combinations

