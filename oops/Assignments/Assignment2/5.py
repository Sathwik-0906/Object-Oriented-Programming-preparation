# Problem Statement
# A post office wants to automate the process of allocation of letters to different postmen based on their allocated area.
# Write a python program to implement the class diagram given below.



# Class description
# Letter class:

# Initialize static variable counter to 1
# Auto-generate attribute, letter_id starting from 1 in the constructor
# PostMan class:

# Initialize static variable counter to 100
# Auto-generate attribute, postman_id starting from 101 prefixed by “P” in the constructor
# post_list_to_deliver: List of letter objects to be delivered by the postman
# PostOffice class:

# area_list: List of names of areas under the post office
# postmen_list: List of postman objects working in the post office. There is one to one correspondence between the two lists – which means postman at index position 0 delivers letters in the area at index position 0 of area_list
# validate_letter(letter): Accept the letter and validate its receiver area. If letter.receiver_area is present in area_list, return the index position of that area in area_list. Else return -1
# allocate_posts(letter_list): Allocate letters in the letter_list to the appropraie postman
# For every letter in letter_list
# Validate letter.receiver_area
# If valid, append the letter to the corresponding postman's post_list_to_deliver
# Else, add it to an invalid letter list
# Return invalid letter list
# Perform case sensitive comparison.
# Create objects of Letter class, PostMan class and PostOffice class, invoke appropriate methods and test your program.

class Letter:
    counter = 1

    def __init__(self, receiver_name, receiver_area):
        self.letter_id = Letter.counter
        Letter.counter += 1
        self.receiver_name = receiver_name
        self.receiver_area = receiver_area


class PostMan:
    counter = 100

    def __init__(self, name):
        PostMan.counter += 1
        self.postman_id = "P" + str(PostMan.counter)
        self.name = name
        self.post_list_to_deliver = []


class PostOffice:
    def __init__(self, area_list, postmen_list):
        self.area_list = area_list
        self.postmen_list = postmen_list

    def validate_letter(self, letter):
        try:
            return self.area_list.index(letter.receiver_area)
        except ValueError:
            return -1

    def allocate_posts(self, letter_list):
        invalid_letters = []
        for letter in letter_list:
            index = self.validate_letter(letter)
            if index != -1:
                self.postmen_list[index].post_list_to_deliver.append(letter)
            else:
                invalid_letters.append(letter)
        return invalid_letters

postman1 = PostMan("Arun")
postman2 = PostMan("Ravi")
postman3 = PostMan("John")

area_list = ["MG Road", "Brigade Road", "Church Street"]
postmen_list = [postman1, postman2, postman3]

post_office = PostOffice(area_list, postmen_list)

letter1 = Letter("Rahul", "MG Road")
letter2 = Letter("Anjali", "Brigade Road")
letter3 = Letter("David", "Church Street")
letter4 = Letter("Sneha", "Indira Nagar")

letters = [letter1, letter2, letter3, letter4]
invalid_letters = post_office.allocate_posts(letters)

print("Postman Deliveries:")
for postman in postmen_list:
    print(f"{postman.name} ({postman.postman_id}): {[letter.receiver_name for letter in postman.post_list_to_deliver]}")

print("Invalid Letters:")
for letter in invalid_letters:
    print(f"{letter.letter_id}: {letter.receiver_name} - {letter.receiver_area}")


