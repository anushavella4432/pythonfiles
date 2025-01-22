def count_vowels(input_string):
    vowels='aeiouAEIOU'
    count=0
    for char in input_string:
        if char in vowels:
            count+=1
    return count
input_string=input('enter the word')
vowel_count=count_vowels(input_string)
print('the number of vowels in the word is: '+str(vowel_count))