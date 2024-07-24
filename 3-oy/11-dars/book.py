from validator import ValidateBook


class Book(ValidateBook):
    def __init__(self, title, author, year, genre, page_count):
        self.validate_year(year)
        self.validate_genre(genre)
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.page_count = page_count

    @property
    def title(self):
        return self.__dict__["title"]

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and new_title != "":
            self.__dict__["title"] = new_title
        else:
            raise ValueError("Title must be a non-empty string")

    @title.deleter
    def title(self):
        raise PermissionError("Ruxsat etilmagan operatsiya")
        # del self.__dict["title"]

    def add_bookmark(self, page):
        if isinstance(page, int) and page > 0 and page <= self.page_count:
            try:
                f = open(f"{self.title}_bookmarks.txt", "r")
            except:
                f = open(f"{self.title}_bookmarks.txt", "w")
                f.write(f"{self.title} ---> {page} sahifasi")
                f.close()
            else:
                f = f = open(f"{self.title}_bookmarks.txt", "w")
                f.write(f"{self.title} ---> {page} sahifasi")
            finally:
                f.close()

book = Book("Python", "Ilon Mask", 2010, "Ilmiy1", 250)
book.add_bookmark(15)
