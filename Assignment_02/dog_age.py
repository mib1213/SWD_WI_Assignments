dog_age: int = int(input("How old is your dog (in years)? "))


if dog_age == 1: #if dog is 1 year old
    human_age: int = 14 #human age should be 14
elif dog_age == 2: #if dog is 2 years old
    human_age: int = 22 #human age should be 22
else: #if dog is more than 2 years old
    extra_years: int = dog_age - 2 #number of years come after 2
    human_age: int = 22 + (extra_years * 5) #22 is the age at 2 years old, after that for each year
                                            #it should be 5 times for each extra year
print(human_age)
