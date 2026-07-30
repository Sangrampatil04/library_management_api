from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    published_date = models.DateField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()



class BorrowRecord(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="borrow_records"
    )

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="borrow_records"
    )

    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"    


    def __str__(self):
        return self.title