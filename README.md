# Python Programming II (Final Project)

This is the readme.md file for Python Programming II (Final Project).  Our final project is a device management system, and is going to contain two layers, cli and gui.  

# Team

Tyson and Blake

## Device Management System

The Device Management System is written in python programming language.  The python program primarily contains two layers, cli and gui.  The cli is for the admin to create, read, update, and delete device records.  The gui is for the user to read device records.

## CLI (command line interface)

Upon running the python program through the command line interface, the admin user will be presented with a main menu.   The main menu will give the admin user options to create a device record, read or search a device record, update a device record, and delete a record.

## GUI (tkinter)

Upon running the python program to launch the tkinter gui, the user will have options to view device records in a read only mode.

## Database backend (SQLite)

The database backend for this project will be SQLite.  When the admin user creates a record, the record will be stored, processed, and edited using the SQLite database. 

## SQLite Fields, data types, and contraints for the records

The **unique id** for the record is **id** the datatype is **integer**, we also include the following records and corresponding SQLite **datatypes**:

1. ID = INTEGER PRIMARY KEY AUTOINCREMENT
2. Serial = TEXT NOT NULL
3. Mac = TEXT NOT NULL
4. Tag_Num = INTEGER NOT NULL
5. Make = TEXT NOT NULL
6. Model = TEXT NOT NULL
7. Factory_Reset = TEXT


# Communication

This area is for communication between Tyson and Blake.  We will keep a **team member**, a **date**, a **time**, and a **comment** for each log entry.  To uptain formatting standards, we will also show our **newest** log entries at the **top**, and **oldest** entries at the **bottom**.
<br />
<br />

**Team Member:** Blake <br />
**Date:** 12/01/23 <br />
**Time:**  11:01 am <br />
**Comment:** Updated the CLI python Code version 1.0 txt file, also updated the README.MD file with a table example, and compatible data types for SQLite <br />
<br />

**Team Member:** Tyson <br />
**Date:** 11/28/23 <br />
**Time:**  11:13 pm <br />
**Comment:** Created the CLI python Code version 1.0. txt file <br />
<br />

**Team Member:** Blake <br />
**Date:** 11/27/23 <br />
**Time:**  11:42 am <br />
**Comment:** Created the readme.md file <br />
<br />


## Table file format example

|ID              |SERIAL                         |MAC                          |TAG_NUM                      |MAKE                         |MODEL                        |FACTORY_RESET                |
|----------------|-------------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
|1               |112233445566                   |C3:E1:34:D7:CE:D2            |54321                        |CISCO                        |CATALYST 1000                |TRUE                         | 
|2               |223344556677                   |C4:E1:34:D7:CE:D4            |55555                        |DELL                         |N3048P                       |TRUE                         |
|3               |334455667788                   |C7:E1:34:D7:CE:D7            |77777                        |EXTREME                      |X440-G2                      |TRUE                         |

|                   |           +---------------------+
|                   |
+-------------------+

