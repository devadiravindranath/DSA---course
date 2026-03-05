"""def count_char(text):
    count = 0
    for char in text:
        count+=1
    return count

def main():
    text = input("enter name: ")
    print("character count : ",count_char(text))

main()"""


"""def count_vowels(text):
    count = 0
    vowels='aeiouAEIOU'
    for char in text:
        if char in vowels:
            count+=1
    return count

def main():
    text = input("enter name: ")
    print("character count : ",count_vowels(text))

main()"""

def reverse_str(text):
    #reversed_text = ""
    #for char in text:
        #reversed_text = char + reversed_text
        #return reversed_text
    
    return text[::-1]

def main():
    text = input("enter name: ")
    print("reversed text : ",reverse_str(text))

main()
    



