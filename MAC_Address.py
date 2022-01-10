def new_mac(keys, address):
    # Iterating over list of keys
    for i in keys:
        # To make changes in MAC Address as per dictionary
        address = address.replace(i, str(mapper.get(i)))

    return address


# user input for MAC Address
# mac = str(input("Please enter the MAC Address: "))
mac = "EC:BO:8T:E4"
# Initializing the dictionary
mapper = {"E": 0, "T": 0}
# Storing keys in list
key_list = mapper.keys()

# printing the result
print(new_mac(key_list, mac))
