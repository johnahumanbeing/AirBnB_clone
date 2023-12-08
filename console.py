#!/usr/bin/python3
"""
Console front end of hbnb project
"""

import cmd
from models.base_model import BaseModel
from models import storage
#from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    __ClassNames = ["BaseModel",
                    "User"]

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
        Usage: create BaseModel
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
            obj_to_delete = obj_dict[key]
            storage.delete(obj_to_delete)  # Utilize the delete method
            storage.save()

        else:
            print("** no instance found **")


    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name
        Usage: all BaseModel or all
        """
        obj_dict = storage.all()

        if not args:
            # If no class name is provided, print all instances
            print([str(obj_dict[key]) for key in obj_dict])
            return

        class_name = args.split()[0]

        # Check if the class name exists in your project
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        print([str(obj_dict[key]) for key in obj_dict if key.startswith(class_name + ".")])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id adding
        or updateing the attributes
        Usage: update <class_name> <id> <attribute name> "attribute name"
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
        
        if key not in obj_dict:
            print("** no instance found **")
            return
        
        if len(args) < 4:
            print("** attribute name missing **")
            return
        
        attr_name = args[2]
        attr_value = args[3]

        instance = obj_dict[key]
        attr_type = type(getattr(instance, attr_name, None))

        if attr_type is None:
            print("** value missing **")
            return
        
        try:
            casted_value = attr_type(attr_value)
        
        except (ValueError, TypeError):
            print(f"Invalid value for {attr_name}")
            return
        
        setattr(instance, attr_name, casted_value)
        storage.save()
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()