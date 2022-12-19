class Publisher:

    def _init_(self,Pubname):
        self.Pubname = Pubname

    def display(self):
        print("Publisher:",self.Pubname)

class book(Publisher):

    def _init_(self,Pubname,title,author):

        Publisher._init_(self,Pubname)
        self.title = title
        self.author = author

    def display(self):

        print("Title:",self.title)
        print("Author:",self.author)

class python(book):

    def _init_(self,Pubname,title,author,price,no_of_pages):

        book._init_(self.Pubname,title,author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):

        print("Title:", self.title)
        print("Author:", self.author)
        print("Publisher:", self.Pubname)
        print("Price:", self.price)
        print("No of pages:", self.no_of_pages)

b1 = python("Penguin Random House","Ann Frank's Diary","Ann Frank","300","215")
b1.display()