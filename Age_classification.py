print("\nHI! Here you can know your actual age and if you are an adult or not\n--------------------------------------------------------------------- ")
year_1= int(input("\nType the actual year: "))
year_2= int(input("Type your birth year: "))
age = year_1 - year_2
if age >= 18:
    print (f"\n\t***Your actual age is: {age}***\n\n=> You are an ADULT")
elif 0 < age < 18:
    print(f"\n\t***Your actual age is: {age}***\n\n=> You are UNDERAGE")
else:
    print("\n........... Value error :( , start again ..............")
