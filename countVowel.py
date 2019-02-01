m = input("Enter a word: ")

def countVowel(m):
    vowels = 'aeiou'
    found_vowels = ""
    no_of_duplicates = 0
    for x in m.lower():
        if x in vowels:
            if x in found_vowels:
                no_of_duplicates += 1
            else:
                found_vowels += str(x)

    
    return (found_vowels, no_of_duplicates)

       
  
       
print(countVowel(m))




 





