"""
Create a Book class that has two attributes:
    .title
    .author
and two methods:
    A method named .get_title() that returns: "Title: " + the instance title.
    A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:
    Pride and Prejudice - Jane Austen (PP)
    Hamlet - William Shakespeare (H)
    War and Peace - Leo Tolstoy (WP)
The name of the new instances should be PP, H, and WP, respectively.
For instance, if I instantiated the following book using this Book class:
    Harry Potter - J.K. Rowling (HP)
I would get the following attributes and methods:
Examples
HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Title: Harry Potter"
HP.get_author() ➞ "Author: J.K. Rowling"
Notes
    Read more about Python classes in Resources.
    Remember, after you've finished writing the class and its methods, you must instantiate it through 
    the creation of new objects.
"""


class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
    def get_title(self):
        print(f"Title: {self.title}")
    def get_author(self):
        print(f"Author: {self.author}")
    

HP = Book("Harry Potter", "J.K. Rowling")
PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamlet", "William Shakespeare")
WP = Book("War and Peace", "Leo Tolstoy")

print(HP.title)
print(HP.author)
HP.get_title()
HP.get_author()

print(PP.title)
print(PP.author)
PP.get_title()
PP.get_author()

print(H.title)
print(H.author)
H.get_title()
H.get_author()

print(WP.title)
print(WP.author)
WP.get_title()
WP.get_author()
