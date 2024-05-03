import json

class Zone:
    def _init_(self, zone_id, speed_limit):
        self.zone_id = zone_id
        self.speed_limit = speed_limit

class Vehicle:
    def _init_(self, vehicle_id):
        self.vehicle_id = vehicle_id

class SpeedMonitoringSystem:
    def _init_(self):
        self.zones = {}
        self.speeding_data = []

    def add_zone(self, zone_id, speed_limit):
        zone = Zone(zone_id, speed_limit)
        self.zones[zone_id] = zone
        print(f"Zone {zone_id} added with speed limit {speed_limit}.")
        self.save_data("speeding_data.json")

    def get_zone(self, zone_id):
        return self.zones.get(zone_id)

    def update_zone_speed_limit(self, zone_id, new_speed_limit):
        if zone_id in self.zones:
            self.zones[zone_id].speed_limit = new_speed_limit
            self.save_data("speeding_data.json")
            print(f"Speed limit for zone {zone_id} updated successfully.")
        else:
            print(f"Zone {zone_id} not found. Unable to update speed limit.")

    def delete_zone(self, zone_id):
        if zone_id in self.zones:
            del self.zones[zone_id]
            print(f"Zone {zone_id} deleted.")
            self.save_data("speeding_data.json")
        else:
            print(f"Zone {zone_id} not found. Unable to delete.")

    def monitor_vehicle_speeds(self, vehicle_id, zone_id, speed):
        zone = self.get_zone(zone_id)
        if zone:
            self.speeding_data.append({
                "vehicle_id": vehicle_id,
                "zone_id": zone_id,
                "speed": speed,
                "is_speeding": speed > zone.speed_limit
            })
            self.save_data("speeding_data.json")
        else:
            print(f"Zone {zone_id} not found. Unable to monitor vehicle speed.")

    def issue_speeding_tickets(self):
        for data in self.speeding_data:
            zone = self.get_zone(data["zone_id"])
            if zone:
                if data["is_speeding"]:
                    print(f"Issuing speeding ticket for vehicle {data['vehicle_id']} in zone {data['zone_id']} (speed: {data['speed']}, limit: {zone.speed_limit})")
            else:
                print(f"Zone {data['zone_id']} associated with speeding data not found.")

    def perform_operation(self, operation):
        if operation == 'create':
            zone_id = input("Enter zone ID: ")
            speed_limit = int(input("Enter speed limit: "))
            self.add_zone(zone_id, speed_limit)
            print("Recorded successfully")
        elif operation == 'read':
            zone_id = input("Enter zone ID to retrieve: ")
            zone = self.get_zone(zone_id)
            if zone:
                print(f"Zone {zone_id} - Speed Limit: {zone.speed_limit}")
            else:
                print(f"Zone {zone_id} not found.")
        elif operation == 'update':
            zone_id = input("Enter zone ID to update: ")
            new_speed_limit = int(input("Enter new speed limit: "))
            self.update_zone_speed_limit(zone_id, new_speed_limit)
        elif operation == 'delete':
            zone_id = input("Enter zone ID to delete: ")
            self.delete_zone(zone_id)
        elif operation == 'monitor':
            vehicle_id = input("Enter vehicle ID: ")
            zone_id = input("Enter zone ID: ")
            speed = int(input("Enter vehicle speed: "))
            self.monitor_vehicle_speeds(vehicle_id, zone_id, speed)
        elif operation == 'issue':
            self.issue_speeding_tickets()
        elif operation == 'save and exit':
            self.save_data("speeding_data.json")
            print("Data saved successfully. Exiting...")
            exit()
        else:
            print("Invalid operation.")

    def save_data(self, file_name):
        with open(file_name, 'w') as file:
            json.dump({"zones": [(zone.zone_id, zone.speed_limit) for zone in self.zones.values()],
                       "speeding_data": self.speeding_data}, file, indent=4)

    def load_data(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                for zone_id, speed_limit in data["zones"]:
                    self.add_zone(zone_id, speed_limit)
                self.speeding_data = data["speeding_data"]
        except FileNotFoundError:
            print("No existing data found.")

# Example usage
system = SpeedMonitoringSystem()
system.load_data("speeding_data.json")

while True:
    print("Select operation:")
    print("1. Create a zone")
    print("2. Read a zone")
    print("3. Update a zone")
    print("4. Delete a zone")
    print("5. Monitor vehicle speeds")
    print("6. Issue speeding tickets")
    print("7. Save and Exit")

    choice = input("Enter choice (1-7): ")

    if choice.isdigit() and int(choice) in range(1, 8):
        operations = ['create', 'read', 'update', 'delete', 'monitor', 'issue', 'save and exit']
        system.perform_operation(operations[int(choice) - 1])
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
