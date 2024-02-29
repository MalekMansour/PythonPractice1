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
        if self.devices:
            for idx, device in enumerate(self.devices, start=1):
                print(f"{idx}. {device}")
        else:
            print("No devices found in the system.")


def main():
    system = System()
    
    while True:
        print("\nChoose an option:")
        print("1. Add a device")
        print("2. Remove a device")
        print("3. Display all devices")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            device = input("Enter the name of the device to add: ")
            system.add_device(device)
        elif choice == '2':
            system.display_devices()
            if system.devices:
                device_idx = int(input("Enter the index of the device to remove: "))
                if 1 <= device_idx <= len(system.devices):
                    device = system.devices[device_idx - 1]
                    system.remove_device(device)
                else:
                    print("Invalid device index.")
        elif choice == '3':
            system.display_devices()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
