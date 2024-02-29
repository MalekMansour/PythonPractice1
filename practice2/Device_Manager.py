class System:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"{device} added to the system.")

    def remove_device(self, device):
        if device in self.devices:
            self.devices.remove(device)
            print(f"{device} removed from the system.")
        else:
            print(f"{device} not found in the system.")

    def display_devices(self):
        print("Devices in the system:")
        for device in self.devices:
            print("-", device)


def main():
    system = System()
    
    while True:
        print("\n1. Add device")
        print("2. Remove device")
        print("3. Display devices")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            device = input("Enter the name of the device to add: ")
            system.add_device(device)
        elif choice == '2':
            device = input("Enter the name of the device to remove: ")
            system.remove_device(device)
        elif choice == '3':
            system.display_devices()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
