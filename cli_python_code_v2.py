import sqlite3

# Connection to Database
conn = sqlite3.connect('device_records.db')
cursor = conn.cursor()

# Create the device table if not exists
cursor.execute('''
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

conn.commit()

# Function to create a device record
def create_device_record():
    serial = input("Enter Serial: ")
    mac = input("Enter MAC: ")
    tag_num = input("Enter Tag_Num: ")
    make = input("Enter Make: ")
    model = input("Enter Model: ")
    factory_reset = input("Enter Factory_Reset (True/False): ").lower() == 'true'

    cursor.execute('''
        INSERT INTO devices (Serial, Mac, Tag_Num, Make, Model, Factory_Reset)
        VALUES (?, ?, ?, ?, ?, ?);
    ''', (serial, mac, tag_num, make, model, factory_reset))
    conn.commit()
    print("\nDevice record created successfully!")

# Function to read or search a device record
def read_device_record():
    print("\nSearch Menu:")
    print("1. Search by ID")
    print("2. Search by Serial")
    print("3. Search by MAC")
    print("4. Search by Tag_Num")
    print("5. View All Records")  # Added option to view all records

    search_choice = input("Enter your search choice (1-5): ")

    if search_choice == '5':
        cursor.execute('SELECT * FROM devices;')
        results = cursor.fetchall()
        if results:
            print("\nAll Device Records:")
            for result in results:
                print("ID:", result[0])
                print("Serial:", result[1])
                print("MAC:", result[2])
                print("Tag_Num:", result[3])
                print("Make:", result[4])
                print("Model:", result[5])
                print("Factory_Reset:", result[6])
                print("-----------------------")
        else:
            print("\nERROR: No device records found.")
        return

    search_value = input("Enter the value to search for: ")

    if search_choice == '1':
        cursor.execute('SELECT * FROM devices WHERE ID = ?;', (search_value,))
    elif search_choice == '2':
        cursor.execute('SELECT * FROM devices WHERE Serial = ?;', (search_value,))
    elif search_choice == '3':
        cursor.execute('SELECT * FROM devices WHERE MAC = ?;', (search_value,))
    elif search_choice == '4':
        cursor.execute('SELECT * FROM devices WHERE Tag_Num = ?;', (search_value,))
    else:
        print("\nERROR: Invalid search choice. Please enter a number between 1 and 5.")
        return

    result = cursor.fetchone()

    if result:
        print("\nDevice record found:")
        print("ID:", result[0])
        print("Serial:", result[1])
        print("MAC:", result[2])
        print("Tag_Num:", result[3])
        print("Make:", result[4])
        print("Model:", result[5])
        print("Factory_Reset:", result[6])
    else:
        print("\nERROR: Device record not found.")
# Function to update a device record
def update_device_record():
    device_id = input("Enter ID of the device record to update: ")
    serial = input("Enter new Serial: ")
    mac = input("Enter new MAC: ")
    tag_num = input("Enter new Tag_Num: ")
    make = input("Enter new Make: ")
    model = input("Enter new Model: ")
    factory_reset = input("Enter new Factory_Reset (True/False): ").lower() == 'true'

    cursor.execute('''
        UPDATE devices
        SET Serial = ?, Mac = ?, Tag_Num = ?, Make = ?, Model = ?, Factory_Reset = ?
        WHERE ID = ?;
    ''', (serial, mac, tag_num, make, model, factory_reset, device_id))
    conn.commit()
    print("\nDevice record updated successfully!")

# Function to delete a device record
# Function to delete a device record
def delete_device_record():
    print("\nDelete Menu:")
    print("1. Delete by ID")
    print("2. Delete by Serial")
    print("3. Delete by MAC")
    print("4. Delete by Tag_Num")
    print("5. Delete All Records")  # Added option to delete all records

    delete_choice = input("Enter your delete choice (1-5): ")

    if delete_choice == '5':
        confirm_delete_all = input("\nDo you really want to delete all records? (yes/no): ").lower()
        if confirm_delete_all == 'yes' or confirm_delete_all == 'y':
            cursor.execute('DELETE FROM devices;')
            conn.commit()
            print("\nAll device records deleted successfully!")
        else:
            print("\nDeletion canceled.")
        return

    delete_value = input("Enter the value to delete: ")

    if delete_choice == '1':
        cursor.execute('SELECT * FROM devices WHERE ID = ?;', (delete_value,))
    elif delete_choice == '2':
        cursor.execute('SELECT * FROM devices WHERE Serial = ?;', (delete_value,))
    elif delete_choice == '3':
        cursor.execute('SELECT * FROM devices WHERE MAC = ?;', (delete_value,))
    elif delete_choice == '4':
        cursor.execute('SELECT * FROM devices WHERE Tag_Num = ?;', (delete_value,))
    else:
        print("\nERROR: Invalid delete choice. Please enter a number between 1 and 5.")
        return

    existing_record = cursor.fetchone()

    if existing_record:
        print("\nDevice record found:")
        print("ID:", existing_record[0])
        print("Serial:", existing_record[1])
        print("MAC:", existing_record[2])
        print("Tag_Num:", existing_record[3])
        print("Make:", existing_record[4])
        print("Model:", existing_record[5])
        print("Factory_Reset:", existing_record[6])

        confirm_delete = input("\nDo you really want to delete this record? (yes/no): ").lower()
        if confirm_delete == 'yes' or confirm_delete == 'y':
            cursor.execute(f'DELETE FROM devices WHERE ID = ?;', (delete_value,))
            conn.commit()
            print("\nDevice record ID", delete_value, "deleted successfully!")
        else:
            print("\nDeletion canceled.")
    else:
        print("\nERROR: Device record not found.")

# Loop to list all devices
while True:
    print("\nMain Menu:")
    print("1. Create a new device record")
    print("2. Read or search a device record")
    print("3. Update a device record")
    print("4. Delete a device record")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        create_device_record()
    elif choice == '2':
        read_device_record()
    elif choice == '3':
        update_device_record()
    elif choice == '4':
        delete_device_record()
    elif choice == '5':
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 5.")

conn.close()
