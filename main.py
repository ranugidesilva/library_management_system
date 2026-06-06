#Data structures to store information

books = [["001", "Harry Potter", "J.K.Rowling","Fiction", 7, 5],
        ["002", "Wonder", "R.J. Palacio","Fiction", 3,2],
        ["003", "Cosmos", "Carl Sagan","Science", 5, 3],
        ["004", "The Body", "Bill Bryson","Science", 0, 3],
        ["005", "Cleopatra", "Stacy Schiff","History", 8, 5],
        ["006", "Gandhi", "Louis Fischer","History", 7,4]]

members = [["M001","Riyana", "18", "0701775683", "18-04-2023"],
          ["M002","Shevon","22","0743446791","20-09-2024"],
          ["M003","Shenon"," 19"," 0707746591"," 22-04-2024"]]
           
issues = [["I001", "M001", "001", "20-04-2023", "10-05-2023", "First-time borrower"],
         ["I002", "M002", "002", "25-09-2024", "15-10-2024", "Traveling, may return late"],
         ["I003", "M003", "003", "18-05-2024", "15-06-2024", "Approved by librarian"]]

# Making the Main Menu 
exit_program = 0

while exit_program == 0:
    print("")
    print("========================================")
    print("InfoVault Library Management System")
    print("Main Menu")
    print("========================================")
    print("1. Add new book details")
    print("2. Register a member")
    print("3. Search for available books")
    print("4. Issue a book")
    print("5. Update book details")
    print("6. Exit")
    print("========================================")
    
    choice = int(input("Your Choice: "))

# If the user selects 1
    if choice == 1:
        # Adding new book details
        print("")
        print("InfoVault Library Management System")
        print("Add New Book Details")
        print("")
        
        ISBN = input("ISBN(3 digits) - ISBN")
        title = input("Title - ")
        category = input("Category (Fiction/Science/History) - ")
        author = input("Author - ")
        total_copies = int(input("Total Copies - "))
        available_copies = int(input("Available Copies - "))
        
        print("")
        confirm = input("Do you want to add (Yes/No)? ")
        
        if confirm == "Yes":
            # Validate book number format 
            if len(ISBN) == 3:
                # Checking if all 3 characters are digits
                number_valid = 1
                count = 0
                while count < 3:
                    if ISBN[count] < "0" or ISBN[count] > "9":
                        number_valid = 0
                    count = count + 1
                
                if number_valid == 1:
                    # Validating the category
                    if category == "Fiction" or category == "Science" or category == "History":
                        # Validating that total copies and available copies are positive
                        if total_copies > 0 and available_copies > 0:
                            # Checking if book number already exists 
                            found = 0
                            count = 0
                            while count < len(books):
                                if books[count][0] == ISBN:
                                    found = 1
                                count = count + 1
                            
                            if found == 0:
                                # Adding to books to the list
                                books.append([ISBN, title, author, category, total_copies, available_copies])
                                print("Book added successfully!")
                            else:
                                print("Error: Book number already exists!")
                        else:
                            print("Error: Total copies and available copies must be positive numbers!")
                    else:
                        print("Error: Invalid category! Must be Fiction, Science, or History")
                else:
                    print("Error: ISBN must contain only digits!")
            else:
                print("Error: ISBN must be 3 digits (e.g., 001, 002)")
        else:
            print("Book not added")

    #If the user selects 2
    elif choice == 2:
        # Registering a member
        print("")
        print("InfoVault Library Management System")
        print("Register a member")
        print("")
        
        membership_id = input("Membership ID - ")
        name = input("Name - ")
        
        # Validate age is an integer
        age_input = input("Age - ")
        age_valid = 1
        count = 0
        while count < len(age_input):
            if age_input[count] < "0" or age_input[count] > "9":
                age_valid = 0
            count = count + 1
        
        if age_valid == 0:
            print("Error: Age should be an integer!")
        else:
            age = int(age_input)
            
            # Validating whether the contact number contains only integers
            contact = input("Contact Number - ")
            contact_valid = 1
            count = 0
            while count < len(contact):
                if contact[count] < "0" or contact[count] > "9":
                    contact_valid = 0
                count = count + 1
            
            if contact_valid == 0:
                print("Error: Contact number should consist only of integers!")
            else:
                print("Note: Please enter membership date in format DD/MM/YYYY (e.g., 15-01-2025)")
                membership_date = input("Membership Date - ")
                
                print("")
                confirm = input("Do you want to register (Yes/No)? ")
                
                if confirm == "Yes":
                    # Validate Membership ID format
                    if len(membership_id) == 4 and membership_id[0] == "M":
                        # Checking if the remaining 3 characters are digits
                        id_valid = 1
                        count = 1
                        while count < 4:
                            if membership_id[count] < "0" or membership_id[count] > "9":
                                id_valid = 0
                            count = count + 1
                        
                        if id_valid == 1:
                            # Checking if the Membership ID already exists
                            found = 0
                            count = 0
                            while count < len(members):
                                if members[count][0] == membership_id:
                                    found = 1
                                count = count + 1
                            
                            if found == 0:
                                members.append([membership_id, name, age, contact, membership_date])
                                print("Member registered successfully!")
                            else:
                                print("Error: Membership ID already exists!")
                        else:
                            print("Error: ID is not according to the format (M followed by 3 digits, e.g., M001)")
                    else:
                        print("Error: ID is not according to the format (M followed by 3 digits, e.g., M001)")
                else:
                    print("Member not registered")

    #If the user selects 3
    elif choice == 3:
        # Searching for available books
        print("")
        print("InfoVault Library Management System")
        print("Search for available books")
        print("")
        
        # Searching Multiple Searches
        continue_search = 1
        while continue_search == 1:
            category = input("Category - ")
            
            # Validate category
            if category == "Fiction" or category == "Science" or category == "History":
                print("")
                print("Category -", category)
                print("ISBN       Title         Total Copies       Available Copies")
                print("-----------------------------------------------------------------------")
                
                #Displaying matching category
                count = 0
                found = 0
                while count < len(books):
                    if books[count][3] == category:
                        print(books[count][0], '   ', books[count][1], '         ', books[count][4], '             ', books[count][5])
                        found = 1
                    count = count + 1
                
                if found == 0:
                    print("No books found in this category")
            else:
                print("Error: Invalid category!")
            
            print("")
            search_again = input("Do you want to search another category (Yes/No)? ")
            if search_again == "No":
                continue_search = 0

    #If the user selects 4 
    elif choice == 4:
        # Issuing a book
        print("")
        print("InfoVault Library Management System")
        print("Issue a Book")
        print("")
        
        issue_id = input("Issue ID - ")
        membership_id = input("Membership ID - ")
        ISBN = input("ISBN - ISBN")
        print("Note: Please enter Issue date in format DD-MM-YYYY (e.g., 15-01-2025)")
        issue_date = input("Issue Date - ")
        return_date = input("Return Date - ")
        remarks = input("Remarks - ")
        
        print("")
        confirm = input("Do you want to issue (Yes/No)? ")
        
        if confirm == "Yes":
            # Validate Issue ID format 
            if len(issue_id) == 4 and issue_id[0] == "I":
                # Check if remaining 3 characters are digits
                id_valid = 1
                count = 1
                while count < 4:
                    if issue_id[count] < "0" or issue_id[count] > "9":
                        id_valid = 0
                    count = count + 1
                
                if id_valid == 1:
                    # Check if member exists
                    member_found = 0
                    count = 0
                    while count < len(members):
                        if members[count][0] == membership_id:
                            member_found = 1
                        count = count + 1
                    
                    # Checking if the book exists and is available
                    book_found = 0
                    book_index = 0
                    count = 0
                    while count < len(books):
                        if books[count][0] == ISBN:
                            book_found = 1
                            book_index = count
                        count = count + 1
                    
                    if member_found == 1 and book_found == 1:
                        # Checking if the copies are available
                        if books[book_index][5] > 0:
                            # Checking if Issue ID already exists
                            issue_found = 0
                            count = 0
                            while count < len(issues):
                                if issues[count][0] == issue_id:
                                    issue_found = 1
                                count = count + 1
                            
                            if issue_found == 0:
                                issues.append([issue_id, membership_id,ISBN, issue_date, return_date, remarks])
                                # Reducing available copies
                                books[book_index][5] = books[book_index][5] - 1
                                print("Book issued successfully!")
                                print("Remaining copies:", books[book_index][5])
                            else:
                                print("Error: Issue ID already exists!")
                        else:
                            print("Error: No copies available!")
                    else:
                        if member_found == 0:
                            print("Error: Member not found!")
                        if book_found == 0:
                            print("Error: Book not found!")
                else:
                    print("Error: Issue ID is not according to the correct format (I followed by 3 digits, e.g., I001)")
            else:
                print("Error: Issue ID is not according to the correct format (I followed by 3 digits, e.g., I001)")
        else:
            print("Book not issued")

    #If the user selects 5
    elif choice == 5:
        # Update book details
        print("")
        print("InfoVault Library Management System")
        print("Update Book Details")
        print(""    )
        
        isbn = input("ISBN - ISBN")
        
        # Search for the book
        book_found = 0
        book_index = 0
        count = 0
        while count < len(books):
            if books[count][0] == isbn:
                book_found = 1
                book_index = count
            count = count + 1
        
        if book_found == 1:
            print("")
            # Display current details and get new values
            print("Current Title:", books[book_index][1])
            title = input("Title - ")
            
            print("Current Author:", books[book_index][2])
            author = input("Author - ")
            
            print("Current Category:", books[book_index][3])
            category = input("Category - ")
            
            print("Current Total Copies:", books[book_index][4])
            total_copies = int(input("Total Copies - "))
            
            print("Current Available Copies:", books[book_index][5])
            available_copies = int(input("Available Copies - "))
            
            print("")
            confirm = input("Do you want to update (Yes/No)? ")
            
            if confirm == "Yes":
                if category == "Fiction" or category == "Science" or category == "History":
                    books[book_index][1] = title
                    books[book_index][2] = author
                    books[book_index][3] = category
                    books[book_index][4] = total_copies
                    books[book_index][5] = available_copies
                    print("Book updated successfully!")
                else:
                    print("Error: Invalid category!")
            else:
                print("Book not updated")
        else:
            print("Error: Book not found!")
    #If the user selects 6
    elif choice == 6:
        # Exit
        print("")
        print("Thank you for using InfoVault Library Management System")
        print("Goodbye!")
        exit_program = 1
    
    else:
        print("")
        print("Invalid choice! Please enter a Valid number")
