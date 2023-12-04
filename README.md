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

# Authors :
- **JOHN BARAKA NGALA** <[johnahumanbeing](https://github.com/johnahumanbeing)>
- **IAN MBAI NJUGUNA** <[programmer-88](https://github.com/programmer-88)>