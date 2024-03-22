"""Practice with dictionaries"""

ice_cream: dict[str, int] = {"chocolate":12, "vanilla":8, "strawberry":5}

#Adding
ice_cream["mint"] = 3
print("After adding mint")
print(ice_cream)

#Removing 
ice_cream.pop("mint")
print("After removing mint")
print(ice_cream)

#Accessing
print(ice_cream["vanilla"])
# or print(f"{ice_cream['vanila']}") -> note the single quote in vanila' f string doesn't understand another "" for vanilla if used 
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#Updating a value
ice_cream["vanilla"] += 1
print("After adding 1 vanilla")
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#Checking if in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)


for key in ice_cream:
    print(ice_cream[key])

print(len(ice_cream))