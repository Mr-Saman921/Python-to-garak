from datetime import date

current_year = date.today().year


class ValidateBook:

    @staticmethod
    def validate_year(year: int):
        if isinstance(year, int) and year > 1850 and year < current_year:
            return True
        else:
            raise ValueError("Invalid publication year")

    @staticmethod
    def validate_genre(genre: str):
        if isinstance(genre, str) and len(genre) > 5 and len (genre) < 20:
            return True
        else:
            raise ValueError("Invalid genre")
