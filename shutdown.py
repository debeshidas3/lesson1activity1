def shutdown():
    """
    Simulate a shutdown command with validation.
    Dhriti uses this function to confirm before shutting down.
    """
    # Ask user for confirmation
    answer = input("Do you really want to shut down the system? (yes / no): ").strip().lower()

    # Check conditions
     if answer == "yes":
        print("Shutting down...")
     # (Here you could insert real shutdown commands, e.g. os.system or subprocess, if desired)
    elif answer == "no":
        print("About shutdown. System will remain on.")
    else:
        print("Sorry, I didn't understand your response. Please enter yes or no.")

if __name__ == "__main__":
    # Simulate Dhriti’s situation
    print("Dhriti: I’m finding it hard to switch off the system.")
    shutdown()
