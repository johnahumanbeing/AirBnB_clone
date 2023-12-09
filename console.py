#!/usr/bin/python3
"""
Console front end of hbnb project
"""

import cmd
from models import storage
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console class."""

    prompt = "(hbnb) "
    __classes = {"BaseModel",
                 "User",
                 "State",
                 "City",
                 "Place",
                 "Amenity",
                 "Review"}

    def default(self, arg):
        """Handle invalid input."""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[: match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][: match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown command: {}".format(arg))
        return False

    def do_count(self, arg):
        """Return the number of count.

        Usage: <class name>.count().
        Example: User.count().
        """
        argl = parsing(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_EOF(self, line):
        """EOF command to end/close the program."""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Emptyline method."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it (to the JSON file).

        Usage: create <class_name>
        Example: create Basemodel
        """
        argv = parsing(arg)
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argv[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Print the string representation of an instance based on the class name.

        Usage: show <class_name> <id>
        Example: show BaseModel 1234-1234-1234
        """
        argl = parsing(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.

        Usage: destroy <class_name> <id>
        Example: destroy BaseModel 1234-1234-1234
        """
        argl = parsing(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.__objects = objdict
            storage.save()

    def do_all(self, arg):
        """
        Print string representation of all instances.

        If a class name is provided, will print only instances of that class.
        Usage: all
        or   : all <class_name>
        """
        argl = parsing(arg)
        objdict = storage.all()
        if len(argl) == 0:
            res = []
            for key in objdict:
                res.append(str(objdict[key]))
            print(res)
        elif argl[0] and argl[0] in HBNBCommand.__classes:
            res = []
            for key in objdict:
                classLen = len(argl[0]) + 2
                if str(objdict[key])[:classLen] == "[{}]".format(argl[0]):
                    res.append(str(objdict[key]))
            print(res)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update an instance based on its class name and id.

        Usage: update <class name> <id> <attribute name> '<attribute value>'
        """
        argl = parsing(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if k in obj.__class__.__dict__.keys() and type(
                    obj.__class__.__dict__[k]
                ) in {str, int, float}:
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


def parsing(arg):
    """Parse argument."""
    brace = re.search(r"\{(.*?)\}", arg)
    bracket = re.search(r"\[(.*?)\]", arg)
    if brace is None:
        if bracket is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lxr = split(arg[: bracket.span()[0]])
            ret = [i.strip(",") for i in lxr]
            ret.append(bracket.group())
            return ret
    else:
        lxr = split(arg[: brace.span()[0]])
        ret = [i.strip(",") for i in lxr]
        ret.append(brace.group())
        return ret


if __name__ == "__main__":
    HBNBCommand().cmdloop()
