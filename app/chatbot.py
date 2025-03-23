from app.size_recommendation import recommend_size

def get_usual_size():
    # List of available UK clothing sizes from 4 to 16
    size_options = {
        "UK 4": 4,
        "UK 6": 6,
        "UK 8": 8,
        "UK 10": 10,
        "UK 12": 12,
        "UK 14": 14,
        "UK 16": 16
    }

    # Print available size options
    print("Select your usual UK clothing size from the following options:")
    for size in size_options.keys():
        print(size)

    # Get user input
    choice = input("Enter your UK size (e.g., UK 8): ").strip()
    
    if choice in size_options:
        return size_options[choice]
    else:
        print("Invalid selection. Please try again.")
        return get_usual_size()  # Recursively prompt for a valid input

def start_chat():
    print("Hi! I can help you find your perfect clothing size.")
    
    # Collect user inputs
    usual_size = get_usual_size()  # Get the user's usual UK clothing size
    height = float(input("What is your height in cm? "))
    fit_preference = input("Do you like a tight or looser fit? ").lower()
    
    # Process recommendation
    recommended_size = recommend_size(usual_size, height, fit_preference)
    print(f"Based on your input, we recommend size: {recommended_size}")
    
if __name__ == "__main__":
    start_chat()
