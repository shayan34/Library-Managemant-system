
class library :
    def __init__(self) -> None:      #constractor banaya 2 instand banaye jo program ma kaha gaaya ha
        self.noBooks = 0          # abi books 0 hein
        self.books= []              # books jitni add hunge unki list hoge is main

    def addBook(self , book):               #add book ka ak function banaya ha
        self.books.append(book)             # book add krnay k lia append use hota python main.
        self.noBooks = len(self.books)

    def showinfo(self):
        print(f"The library has {self.noBooks} books..")
        for book in self.books :     # jitni bi book add ki hen unko self.books ma parhi hen peint krco bs
            print(book)
    

l1 = library()
l1.addBook("Harry Potter")  #self.book.append ma add krdy.
l1.addBook("Harry Potter") 
l1.addBook("Harry Potter")     
l1.showinfo()                  #showinfo ma result dikhy ga.
    



