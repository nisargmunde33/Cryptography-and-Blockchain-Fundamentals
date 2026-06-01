import hashlib

vehicles = {}

saved_message = ""
saved_signature = ""

while True:
    print("\n===== Cryptography and Blockchain Fundamentals =====")
    print("1. Generate SHA-256 Hash")
    print("2. Create Digital Signature")
    print("3. Verify Digital Signature")
    print("4. Register Vehicle")
    print("5. Retrieve Vehicle")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter a message: ")

        hash_value = hashlib.sha256(message.encode()).hexdigest()

        print("SHA-256 Hash:")
        print(hash_value)

    elif choice == "2":
        saved_message = input("Enter message to sign: ")

        saved_signature = hashlib.sha256(saved_message.encode()).hexdigest()

        print("Digital Signature Created Successfully")
        print("Signature:")
        print(saved_signature)

    elif choice == "3":
        if saved_message == "":
            print("No signed message found.")
        else:
            verify_signature = hashlib.sha256(saved_message.encode()).hexdigest()

            if verify_signature == saved_signature:
                print("Signature is VALID")
            else:
                print("Signature is INVALID")

    elif choice == "4":
        plate = input("Enter Number Plate: ")

        if plate in vehicles:
            print("Vehicle already registered.")
        else:
            owner = input("Enter Owner Name: ")
            model = input("Enter Vehicle Model: ")

            vehicles[plate] = {
                "owner": owner,
                "model": model
            }

            print("Vehicle Registered Successfully")

    elif choice == "5":
        plate = input("Enter Number Plate: ")

        if plate in vehicles:
            print("Vehicle Details")
            print("Owner:", vehicles[plate]["owner"])
            print("Model:", vehicles[plate]["model"])
        else:
            print("Vehicle Not Found")

    elif choice == "6":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
