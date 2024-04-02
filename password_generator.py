import random
import time
import sys

alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = alphabet_lower.upper()
numbers = "1234567890"
famous_characters = "`~!@#$%^&*()_-=+\/{[}]?.<,>;:,"

print("""
              :::::::              
            :::::::::::            
          :::::     :::::          
          :::         :::          
         ::::         ::::         
         ::::         ::::         
         ::::         ::::         
         ::::         ::::         
        :::::::::::::::::::        
      :::::::::::::::::::::::.     
     :::::::::::::::::::::::::     
     :::::::::::::::::::::::::     
     ::::::::::     ::::::::::     
     ::::::::::     ::::::::::     
     :::::::::::   :::::::::::     
     :::::::::::   :::::::::::     
     :::::::::::   :::::::::::     
     :::::::::::::::::::::::::     
       :::::::::::::::::::::       
""")
number_of_characters = int(input("Enter the number of characters in the password:"))

password = ""

for i in range(number_of_characters//4):
    strings = [alphabet_lower, alphabet_lower.upper(), numbers, famous_characters]
    random_characters = [random.choice(s) for s in strings]
    random.shuffle(random_characters)
    for i in range(len(random_characters)):
        password += random_characters[i]
        time.sleep(.08)
        print(random_characters[i], end='')
        sys.stdout.flush()




