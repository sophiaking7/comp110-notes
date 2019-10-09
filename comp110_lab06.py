"""
Module: comp110_lab06

Exercises from lab 06, dealing with string accumualators.
"""


def create_edited_string(text_with_edit_marks):
    """ Function that returns a sting with editing applied. """

    final_str = ""

    for ch in text_with_edit_marks:
        final_str = final_str + ch

    return final_str



def test_create_edited_string():
    """ Function that tests the create_edited_string function. """

    if create_edited_string("This was !qwicked awesome") != "This was wicked awesome":
        print("Test 1 failed")
    if create_edited_string("Please do not ^make me yell") != "Please do not MAKE ME YELL":
        print("Test 2 failed")
    if create_edited_string("This is my ^roar!s") != "This is my ROAR":
        print("Test 3 failed")
    if create_edited_string("You need to \_CALM DOWN") != "You need to calm down":
        print("Test 4 failed")
    if create_edited_string("You need to \_CALM ^down") != "You need to calm DOWN":
        print("Test 5 failed")

# Do not modify anything after this point.
if __name__ == "__main__":
    test_create_edited_string()
