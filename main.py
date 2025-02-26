from stats import word_count

def main():


    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    count = word_count (file_contents)
    lower_case = letter_count (file_contents) 
    print ("Start of Report for Frankenstein") 
    print (f"{count} words found in the document")  
    for item in lower_case:
        print (f"The '{item['char']}' character was found {item["num"]} times")
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
