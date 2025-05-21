import functions
import logging

def show_menu():
    print("\n=== Veterinary Clinic - Main Menu ===")
    print("1. Register pet")
    print("2. Register consultation")
    print("3. List pets")
    print("4. View consultation history of a pet")
    print("5. Exit")

def main():
    logging.info("Application started.")
    try:
        while True:
            show_menu()
            option = input("Select an option: ").strip()
            if option == "1":
                functions.register_pet()
            elif option == "2":
                functions.register_consultation()
            elif option == "3":
                functions.list_pets()
            elif option == "4":
                functions.view_pet_history()
            elif option == "5":
                print("Goodbye!")
                logging.info("Application closed by user.")
                break
            else:
                print("Invalid option. Please try again.")
                logging.warning(f"Invalid menu option selected: {option}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"Unexpected error in main loop: {e}")

if __name__ == "__main__":
    main()