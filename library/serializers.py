from rest_framework import serializers
from .models import Author, Book, Member, BorrowRecord


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"        

class BorrowRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = BorrowRecord
        fields = "__all__"

    def validate(self, data):
        book = data["book"]

        already_borrowed = BorrowRecord.objects.filter(
            book=book,
            is_returned=False
        ).exists()

        if already_borrowed:
            raise serializers.ValidationError(
                "This book is already borrowed."
            )

        return data      