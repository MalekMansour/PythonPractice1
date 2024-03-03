class Property:
    def __init__(self, property_id, address, asking_price, comments, legal_description, quadrant, zoning):
        self.property_id = property_id
        self.address = address
        self.asking_price = asking_price
        self.comments = comments
        self.legal_description = legal_description
        self.quadrant = quadrant
        self.zoning = zoning

    def __str__(self):
        return f"Property ID: {self.property_id}, Address: {self.address}, Asking Price: {self.asking_price}, Legal Description: {self.legal_description}"

class Client:
    def __init__(self, client_id, first_name, last_name, address, phone_number, client_type):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.client_type = client_type

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.first_name} {self.last_name}, Type: {self.client_type}"

class SAITMLS:
    def __init__(self):
        self.properties = []
        self.clients = []

    def add_property(self, property):
        self.properties.append(property)
        print("Property added successfully.")

    def modify_property(self, property_id, new_details):
        for prop in self.properties:
            if prop.property_id == property_id:
                # Modify the property details
                if 'address' in new_details:
                    prop.address = new_details['address']
                if 'asking_price' in new_details:
                    prop.asking_price = new_details['asking_price']
                if 'comments' in new_details:
                    prop.comments = new_details['comments']
                if 'legal_description' in new_details:
                    prop.legal_description = new_details['legal_description']
                if 'quadrant' in new_details:
                    prop.quadrant = new_details['quadrant']
                if 'zoning' in new_details:
                    prop.zoning = new_details['zoning']
                print("Property modified successfully.")
                return
        print("Property not found.")

    def remove_property(self, property_id):
        for prop in self.properties:
            if prop.property_id == property_id:
                self.properties.remove(prop)
                print("Property removed successfully.")
                return
        print("Property not found.")

    def search_property(self, search_criteria):
        results = []
        for prop in self.properties:
            if search_criteria.lower() in prop.address.lower() or \
               search_criteria.lower() in prop.legal_description.lower() or \
               search_criteria.lower() in prop.quadrant.lower():
                results.append(prop)
        return results

    def add_client(self, client):
        self.clients.append(client)
        print("Client added successfully.")

    def modify_client(self, client_id, new_details):
        for client in self.clients:
            if client.client_id == client_id:
                # Modify the client details
                if 'first_name' in new_details:
                    client.first_name = new_details['first_name']
                if 'last_name' in new_details:
                    client.last_name = new_details['last_name']
                if 'address' in new_details:
                    client.address = new_details['address']
                if 'phone_number' in new_details:
                    client.phone_number = new_details['phone_number']
                if 'client_type' in new_details:
                    client.client_type = new_details['client_type']
                print("Client modified successfully.")
                return
        print("Client not found.")

    def remove_client(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                self.clients.remove(client)
                print("Client removed successfully.")
                return
        print("Client not found.")

    def search_client(self, search_criteria):
        results = []
        for client in self.clients:
            if search_criteria.lower() in client.first_name.lower() or \
               search_criteria.lower() in client.last_name.lower() or \
               search_criteria.lower() in client.client_type.lower():
                results.append(client)
        return results

def main():
    saitmls = SAITMLS()

    while True:
        print("\n1. Add Property")
        print("2. Modify Property")
        print("3. Remove Property")
        print("4. Search Property")
        print("5. Add Client")
        print("6. Modify Client")
        print("7. Remove Client")
        print("8. Search Client")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            property_id = int(input("Enter Property ID: "))
            address = input("Enter Address: ")
            asking_price = float(input("Enter Asking Price: "))
            comments = input("Enter Comments: ")
            legal_description = input("Enter Legal Description: ")
            quadrant = input("Enter Quadrant: ")
            zoning = input("Enter Zoning: ")

            prop = Property(property_id, address, asking_price, comments, legal_description, quadrant, zoning)
            saitmls.add_property(prop)

        elif choice == '2':
            property_id = int(input("Enter Property ID to modify: "))
            # Provide options for modification
            new_details = {}
            address = input("Enter new address (leave blank if not changing): ")
            if address:
                new_details['address'] = address
            saitmls.modify_property(property_id, new_details)

        elif choice == '3':
            property_id = int(input("Enter Property ID to remove: "))
            saitmls.remove_property(property_id)

        elif choice == '4':
            search_criteria = input("Enter search criteria: ")
            results = saitmls.search_property(search_criteria)
            print("\nSearch Results for Properties:")
            for prop in results:
                print(prop)

        elif choice == '5':
            client_id = int(input("Enter Client ID: "))
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            address = input("Enter Address: ")
            phone_number = input("Enter Phone Number: ")
            client_type = input("Enter Client Type: ")

            client = Client(client_id, first_name, last_name, address, phone_number, client_type)
            saitmls.add_client(client)

        elif choice == '6':
            client_id = int(input("Enter Client ID to modify: "))
            new_details = {}
            first_name = input("Enter new first name (leave blank if not changing): ")
            if first_name:
                new_details['first_name'] = first_name
            saitmls.modify_client(client_id, new_details)

        elif choice == '7':
            client_id = int(input("Enter Client ID to remove: "))
            saitmls.remove_client(client_id)

        elif choice == '8':
            search_criteria = input("Enter search criteria: ")
            results = saitmls.search_client(search_criteria)
            print("\nSearch Results for Clients:")
            for client in results:
                print(client)

        elif choice == '9':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
