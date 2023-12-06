import sqlite3

class DeviceDatabase:
    def __init__(self, db_file='device_records.db'):
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")

    def create_table(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS devices (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Serial TEXT NOT NULL,
                    Mac TEXT NOT NULL,
                    Tag_Num INTEGER NOT NULL,
                    Make TEXT NOT NULL,
                    Model TEXT NOT NULL,
                    Factory_Reset TEXT
                );
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def create_device_record(self):
        try:
            device_data = self.get_user_input()
            self.cursor.execute('''
                INSERT INTO devices (Serial, Mac, Tag_Num, Make, Model, Factory_Reset)
                VALUES (?, ?, ?, ?, ?, ?);
            ''', tuple(device_data.values()))
            self.conn.commit()
            print("\nDevice record created successfully!")
        except sqlite3.Error as e:
            print(f"Error creating device record: {e}")

    def read_device_record(self, search_choice=None, search_value=None):
        try:
            if search_choice is None:
                print("\nSearch Menu:")
                print("1. Search by ID")
                print("2. Search by Serial")
                print("3. Search by MAC")
                print("4. Search by Tag_Num")
                print("5. View All Records")  # Added option to view all records
                search_choice = input("Enter your search choice (1-5): ")

            if search_choice == '5':
                self.view_all_records()
                return

            if search_value is None:
                search_value = input("Enter the value to search for: ")

            column_name = ["ID", "Serial", "MAC", "Tag_Num"][int(search_choice) - 1]
            self.cursor.execute(f'SELECT * FROM devices WHERE {column_name} = ?;', (search_value,))
            result = self.cursor.fetchone()

            if result:
                self.display_device_record(result)
            else:
                print("\nERROR: Device record not found.")

            # Allow recursive search
            self.read_device_record(search_choice, None)
        except sqlite3.Error as e:
            print(f"Error reading device record: {e}")

    def update_device_record(self):
        try:
            device_id = input("Enter ID of the device record to update: ")
            device_data = self.get_user_input(update=True)
            self.cursor.execute('''
                UPDATE devices
                SET Serial = ?, Mac = ?, Tag_Num = ?, Make = ?, Model = ?, Factory_Reset = ?
                WHERE ID = ?;
            ''', tuple(device_data.values()) + (device_id,))
            self.conn.commit()
            print("\nDevice record updated successfully!")
        except sqlite3.Error as e:
            print(f"Error updating device record: {e}")

    def delete_device_record(self, delete_choice=None, delete_value=None):
        try:
            if delete_choice is None:
                print("\nDelete Menu:")
                print("1. Delete by ID")
                print("2. Delete by Serial")
                print("3. Delete by MAC")
                print("4. Delete by Tag_Num")
                print("5. Delete All Records")  # Added option to delete all records
                delete_choice = input("Enter your delete choice (1-5): ")

            if delete_choice == '5':
                self.delete_all_records()
                return

            if delete_value is None:
                delete_value = input("Enter the value to delete: ")

            column_name = ["ID", "Serial", "MAC", "Tag_Num"][int(delete_choice) - 1]
            self.cursor.execute(f'SELECT * FROM devices WHERE {column_name} = ?;', (delete_value,))
            existing_record = self.cursor.fetchone()

            if existing_record:
                self.display_device_record(existing_record)
                confirm_delete = input("\nDo you really want to delete this record? (yes/no): ").lower()
                if confirm_delete == 'yes' or confirm_delete == 'y':
                    self.cursor.execute(f'DELETE FROM devices WHERE ID = ?;', (delete_value,))
                    self.conn.commit()
                    print("\nDevice record ID", delete_value, "deleted successfully!")
                else:
                    print("\nDeletion canceled.")
            else:
                print("\nERROR: Device record not found.")

            # Allow recursive delete
            self.delete_device_record(delete_choice, None)
        except sqlite3.Error as e:
            print(f"Error deleting device record: {e}")

    def view_all_records(self):
        try:
            self.cursor.execute('SELECT * FROM devices;')
            results = self.cursor.fetchall()
            if results:
                print("\nAll Device Records:")
                for result in results:
                    self.display_device_record(result)
            else:
                print("\nERROR: No device records found.")
        except sqlite3.Error as e:
            print(f"Error viewing all device records: {e}")

    def delete_all_records(self):
        try:
            confirm_delete_all = input("\nDo you really want to delete all records? (yes/no): ").lower()
            if confirm_delete_all == 'yes' or confirm_delete_all == 'y':
                self.cursor.execute('DELETE FROM devices;')
                self.conn.commit()
                print("\nAll device records deleted successfully!")
            else:
                print("\nDeletion canceled.")
        except sqlite3.Error as e:
            print(f"Error deleting all device records: {e}")

    def display_device_record(self, record):
        print("\nDevice record found:")
        print("ID:", record[0])
        print("Serial:", record[1])
        print("MAC:", record[2])
        print("Tag_Num:", record[3])
        print("Make:", record[4])
        print("Model:", record[5])
        print("Factory_Reset:", record[6])

    def get_user_input(self, update=False):
        serial = input("Enter Serial: ")
        mac = input("Enter MAC: ")
        tag_num = input("Enter Tag_Num: ")
        make = input("Enter Make: ")
        model = input("Enter Model: ")
        factory_reset = input("Enter Factory_Reset (True/False): ").lower() == 'true'

        if update:
            return {'Serial': serial, 'Mac': mac, 'Tag_Num': tag_num, 'Make': make, 'Model': model, 'Factory_Reset': factory_reset}
        else:
            return {'Serial': serial, 'Mac': mac, 'Tag_Num': tag_num, 'Make': make, 'Model': model, 'Factory_Reset': factory_reset}

    def close_connection(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing the database connection: {e}")

# Main Program
try:
    db = DeviceDatabase()

    while True:
        print("\nMain Menu:")
        print("1. Create a new device record")
        print("2. Read or search a device record")
        print("3. Update a device record")
        print("4. Delete a device record")
        print("5. View All Records")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            db.create_device_record()
        elif choice == '2':
            db.read_device_record()
        elif choice == '3':
            db.update_device_record()
        elif choice == '4':
            db.delete_device_record()
        elif choice == '5':
            db.view_all_records()
        elif choice == '6':
            db.close_connection()
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
