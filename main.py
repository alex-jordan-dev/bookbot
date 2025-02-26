import sys
from stats import word_count

def main():

    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open (sys.argv[1]) as f:
        file_contents = f.read()
        
    count = word_count (file_contents)
    lower_case = letter_count (file_contents) 
    print ("Start of Report for Frankenstein") 
    print (f"{count} words found in the document")  
    for item in lower_case:
        print (f"{item['char']}: {item["num"]}")
    print ("-----end of report-----")



def letter_count (file_content):
    letter_dict = {}
    letters = file_content.lower()
    
    for letter in letters:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1 

    list_of_dicts = [{"char": key, "num": value} for key, value in letter_dict.items()]  

    list_of_dicts.sort (key=sort_key, reverse = True)
    return list_of_dicts

def sort_key(item):
    return item["num"]    
    


    
main() 
