import grpc
from concurrent import futures
import time

import university_pb2
import university_pb2_grpc


# Mock veriler
books = [
    university_pb2.Book(id="1", title="Yapay Zeka 101", author="Mehmet Yilmaz", isbn="", publisher="", pageCount=0, stock=1),
    university_pb2.Book(id="2", title="Derin Ogrenme", author="Ayse Demir", isbn="", publisher="", pageCount=0, stock=1),
    university_pb2.Book(id="3", title="Veri Bilimine Giris", author="Fatma Celik", isbn="", publisher="", pageCount=0, stock=1),
    university_pb2.Book(id="4", title="Programlama Dilleri", author="Ali Vural", isbn="", publisher="", pageCount=0, stock=1),
    university_pb2.Book(id="5", title="Bilgisayar Aglari", author="Zeynep Kaya", isbn="", publisher="", pageCount=0, stock=1),
]

students = [
    university_pb2.Student(id="1", name="Ahmet Kaya", studentNumber="1001", email="ahmet@example.com", isActive=True),
    university_pb2.Student(id="2", name="Elif Yilmaz", studentNumber="1002", email="elif@example.com", isActive=True),
    university_pb2.Student(id="3", name="Mehmet Demir", studentNumber="1003", email="mehmet@example.com", isActive=False),
    university_pb2.Student(id="4", name="Ayse Celik", studentNumber="1004", email="ayse@example.com", isActive=True),
    university_pb2.Student(id="5", name="Fatma Vural", studentNumber="1005", email="fatma@example.com", isActive=True),
]

loans = [
    university_pb2.Loan(id="1", bookId="1", studentId="1", loanDate="2025-06-10", returnDate="", status=university_pb2.ONGOING),
    university_pb2.Loan(id="2", bookId="3", studentId="2", loanDate="2025-06-05", returnDate="2025-06-12", status=university_pb2.RETURNED),
    university_pb2.Loan(id="3", bookId="4", studentId="3", loanDate="2025-06-11", returnDate="", status=university_pb2.ONGOING),
    university_pb2.Loan(id="4", bookId="2", studentId="4", loanDate="2025-06-09", returnDate="", status=university_pb2.ONGOING),
    university_pb2.Loan(id="5", bookId="5", studentId="5", loanDate="2025-06-01", returnDate="2025-06-08", status=university_pb2.RETURNED),
]



class BookService(university_pb2_grpc.BookServiceServicer):
    def ListBooks(self, request, context):
        for book in books:
            yield book

    def GetBook(self, request, context):
        for book in books:
            if book.id == request.id:
                return book
        return university_pb2.Book()

    def AddBook(self, request, context):
        books.append(request)
        return request

    def UpdateBook(self, request, context):
        for i, book in enumerate(books):
            if book.id == request.id:
                books[i] = request
                return request
        return university_pb2.Book()

    def DeleteBook(self, request, context):
        global books
        books = [book for book in books if book.id != request.id]
        return university_pb2.Empty()

class StudentService(university_pb2_grpc.StudentServiceServicer):
    def ListStudents(self, request, context):
        for student in students:
            yield student

    def GetStudent(self, request, context):
        for student in students:
            if student.id == request.id:
                return student
        return university_pb2.Student()

    def AddStudent(self, request, context):
        students.append(request)
        return request

    def UpdateStudent(self, request, context):
        for i, student in enumerate(students):
            if student.id == request.id:
                students[i] = request
                return request
        return university_pb2.Student()

    def DeleteStudent(self, request, context):
        global students
        students = [student for student in students if student.id != request.id]
        return university_pb2.Empty()

class LoanService(university_pb2_grpc.LoanServiceServicer):
    def ListLoans(self, request, context):
        for loan in loans:
            yield loan

    def GetLoan(self, request, context):
        for loan in loans:
            if loan.id == request.id:
                return loan
        return university_pb2.Loan()

    def AddLoan(self, request, context):
        loans.append(request)
        return request

    def ReturnLoan(self, request, context):
        for loan in loans:
            if loan.id == request.id:
                loan.status = university_pb2.RETURNED
                return loan
        return university_pb2.Loan()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    university_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    university_pb2_grpc.add_StudentServiceServicer_to_server(StudentService(), server)
    university_pb2_grpc.add_LoanServiceServicer_to_server(LoanService(), server)

    server.add_insecure_port('[::]:50051')
    print("Sunucu başlatıldı...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
