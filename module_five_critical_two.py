def main():
    num_books = int(input("Enter the number of books: "))
    if num_books in range(0,2):
        print("No points awarded.")
    elif num_books in range(2,4):
        print("5 points awarded.")
    elif num_books in range(4,6):
        print("15 points awarded.")
    elif num_books in range(6,8):
        print("30 points awarded.")
    elif num_books >= 8:
        print("60 points awarded.")
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()