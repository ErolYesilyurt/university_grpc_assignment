import grpc
import university_pb2
import university_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')

    # Kitap servisi stub'u
    book_stub = university_pb2_grpc.BookServiceStub(channel)
    print("Tum kitaplari listeleme...")
    for book in book_stub.ListBooks(university_pb2.Empty()):
        print(book)
    print("-" * 40)

    # Ogrenci servisi stub'u
    student_stub = university_pb2_grpc.StudentServiceStub(channel)
    print("Tum ogrencileri listeleme...")
    for student in student_stub.ListStudents(university_pb2.Empty()):
        print(student)
    print("-" * 40)

    # Odunc alma servisi stub'u
    loan_stub = university_pb2_grpc.LoanServiceStub(channel)
    print("Tum odunc kayitlarini listeleme...")
    for loan in loan_stub.ListLoans(university_pb2.Empty()):
        print(loan)

if __name__ == '__main__':
    run()
