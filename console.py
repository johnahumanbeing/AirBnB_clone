#!/usr/bin/python3
"""
Console front end of hbnb project
"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """
        Exit the program on EOF
        """

        print("Exiting the HBNB console...")
        return True
    
    def do_quit(self, arg):
        """
        Exit the program
        """

        print("Exiting the HBNB console...")
        return True
    
    def emptyline(self):

        """
        Do nothing on an empty line
        """
        pass


    def do_create(self, args):
        """
        Creates a new instance of BadeModel
        Uusage: create BaseModel
        """

        if not args:
            print("** class name missing **")
            return
        
        class_name = args.split()[0]

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        new_intstance = BaseModel()

        storage.new(new_intstance)
        storage.save()

        print(new_intstance.id)

    def do_show(self, args):

        """
        print string representation of an instance base on
        class and id
        Usage: show BaseModel 1234-1234-1234
        """

        if not args:
            print("** class name missing **")
            return
        
        args = args.split()
        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return
        
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        obj_dict = storage.all()

        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    
    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        Usage: destroy BaseModel 1234-1234-1234
        """

        if not args:
            print("** class name missing **")
            return
        
        args = args.split()
        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return
        
        obj_id  = args[1]
        key = "{}.{}".format(class_name, obj_id)

        obj_dict = storage.all()

        if key in obj_dict:
            del obj_dict[key]
            storage.save()

        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()