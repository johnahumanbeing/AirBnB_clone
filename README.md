<p align="center">
   <img src="/images/hbnb_logo.png" alt="AirBnb Clone logo"
	width="720" height="300"/>
</p>

# Team Project AirBnb Clone
Hbnb: HolbertonBnb is AirBnb Clone, a complete web application that composed by :
 - A Command interpreter to manipulate data without a visual interface.
 - A website (the Front-end) that shows the final product to everybody: static and dynamic.
 - A database or files that store data.
 - An API that provides a communication interface between the front-end and data (retrieve, create, delete, update them).

In this project, we will implement the first part: The console.

# Models (Classes)
This project composes of the following classes:

| class Name | Public Instance Attributes | Public Instance Methods | Public Class Attributes | Private Class Attributes |
| ---------- | ------------------- | ---------------- | ---------------- | ------------- |
| BaseModel | * id: string <br> * created_at: datetime <br> * updated_at: datetime | * save <br> * to_dict |  |  |
| FileStorage | | * all <br> * new <br> * save <br> * reload | | * file_path: string <br> * objects: dictionary |
| User | | | * email: string <br> * password: string <br> * first_name: string <br> last_name: string | |
| State | | | * name: string | |
| City | | | * state_id: string <br> * name: string | |
| Amenity | | | * name: string | |
| Place | | | * city_id: string <br> * user_id: string <br> * name: string <br> * description: string <br> * number_rooms: integer <br> * number_bathrooms: integer <br> * max_guest: integer <br> * price_by_night: integer <br> * latitude: float <br> * longitude: float <br> * amenity_ids: list of string | |
| Review | | | * place_id: string <br> * user_id: string <br> * text: string | |

# Storage
All models are handled by a storage engine defined in the FileStorage model.


# Console : Command line Interpreter
The Console is command line interpreter, it manage the backend part of the HolbertonBnb application
by managing objects and storing/persisting the objects from/to JSON file.

## How to start the Console

The console is executed in interactive mode by running `./console.py`, and a prompt when be displaying and waiting for input:

```
$ ./console.py
(hbnb) help
```

Also in non-interactive mode by piping command to the executable console file:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb) 
$
```

```
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb) 
$
```
```
## How to use the console

To show command help, we enter the command help:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
```
To quit the Console, press CTRL+D (to input EOF signal) or enter quit command:

```
$ ./console.py
(hbnb) EOF
$
```

```
$ ./console.py
(hbnb) quit
$
```


# Commands

Holberton console handles the followings commands:

* create: 
	* Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
	* Usage: create <class name>

Example of creating a User:

```
$ ./console.py
(hbnb) create User
82a6f205-779b-4292-8678-fb53c90fb64e
(hbnb)
```

* show:
	* Prints the string representation of an instance based on the class name and id.
	* Usage: show <class name> <id>

Example of showing the User instance:

```
$ ./console.py
(hbnb) show User 83880763-f364-4e70-8bc5-1ad5218378fe
(hbnb) show User 83880763-f364-4e70-8bc5-1ad5218378fe
[User] (83880763-f364-4e70-8bc5-1ad5218378fe) {'id': '83880763-f364-4e70-8bc5-1ad5218378fe', 'created_at': datetime.datetime(2023, 8, 10, 13, 29, 20, 460431), 'updated_at': datetime.datetime(2023, 8, 10, 13, 29, 20, 460436)}
(hbnb)
```

* destroy:
	* Deletes an instance based on the class name and id (save the change into the JSON file).
	* Usage: destroy <class name> <id>

Example of destroying an instance of User that is already stored in the JSON file:

```
$ ./console.py
(hbnb) destroy User 83880763-f364-4e70-8bc5-1ad5218378fe
(hbnb)
```

* all:
	* Prints all string representation of all instances based or not on the class name.
	* Usage: all <class name> or all

Example of printing instances of all classes:
```
$ ./console.py
(hbnb) all
["[BaseModel] (c07899a9-85f0-439b-851e-624bbb74b996) {'id': 'c07899a9-85f0-439b-851e-624bbb74b996', 'created_at': datetime.datetime(2023, 8, 10, 13, 42, 47, 772518), 'updated_at': datetime.datetime(2023, 8, 10, 13, 42, 47, 772525)}", "[BaseModel] (12f855f0-0b0e-44ab-baee-1d0e29d3a51f) {'id': '12f855f0-0b0e-44ab-baee-1d0e29d3a51f', 'created_at': datetime.datetime(2023, 8, 10, 13, 42, 49, 896756), 'updated_at': datetime.datetime(2023, 8, 10, 13, 42, 49, 896759)}", "[Place] (268500c2-ce81-428a-be70-e71b2ca61704) {'id': '268500c2-ce81-428a-be70-e71b2ca61704', 'created_at': datetime.datetime(2023, 8, 10, 13, 42, 55, 799743), 'updated_at': datetime.datetime(2023, 8, 10, 13, 42, 55, 799748)}", "[Place] (707a4dc3-e294-4d09-a6e6-24f0302125c4) {'id': '707a4dc3-e294-4d09-a6e6-24f0302125c4', 'created_at': datetime.datetime(2023, 8, 10, 13, 42, 57, 317565), 'updated_at': datetime.datetime(2023, 8, 10, 13, 42, 57, 317569)}", "[Amenity] (5ccd437b-7ee0-4919-b652-c96ea48ef3e2) {'id': '5ccd437b-7ee0-4919-b652-c96ea48ef3e2', 'created_at': datetime.datetime(2023, 8, 10, 13, 43, 3, 162054), 'updated_at': datetime.datetime(2023, 8, 10, 13, 43, 3, 162058)}"]
(hbnb)
```

Example of printing instance of a specific class (for example : Place)
```
$ ./console.py
(hbnb) all Place
["[Place] (268500c2-ce81-428a-be70-e71b2ca61704) {'id': '268500c2-ce81-428a-be70-e71b2ca61704', 'created_at': datetime.datetime(2023, 8, 10, 13, 42, 55, 799743), 'updated_at': datetime.datetime(2023, 8, 10, 13, 42, 55, 799748)}", "[Place] (707a4dc3-e294-4d09-a6e6-24f0302125c4) {'id': '707a4dc3-e294-4d09-a6e6-24f0302125c4', 'created_at': datetime.datetime(2023, 8, 10, 13, 42, 57, 317565), 'updated_at': datetime.datetime(2023, 8, 10, 13, 42, 57, 317569)}"]
(hbnb)
```

* update:
	* Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
	* Usage: update <class name> <id> <attribute name> "<attribute value>"

```
$ ./console.py
(hbnb) update Place 268500c2-ce81-428a-be70-e71b2ca61704 number_rooms 35
(hbnb) 
```

# Tests

Launch tests:
```
python3 -m unittest discover tests
```

All tests should also pass in non-interactive mode: 

```
$ echo "python3 -m unittest discover tests" | bash
```

# Authors :

- **JOHN BARAKA NGALA** <[johnahumanbeing](https://github.com/johnahumanbeing)>
- **IAN MBAI NJUGUNA** <[programmer-88](https://github.com/programmer-88)>