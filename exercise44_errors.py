def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

grades = []

print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}.")
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")


students = [
    {"name": "Bob", "grades": [75,90]},
    {"name": "Rolf", "grades": [3,40]},
    {"name": "Jen", "grades": [100,90]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")

class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count:int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return(
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages:int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
            )
        self.pages_read += pages
        print (f"You have now read {self.pages_read} pages out of {self.page_count}")

python101 = Book("Python 101", 50)
python101.read(35)
python101.read(50)