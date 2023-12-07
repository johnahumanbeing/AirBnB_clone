#!/usr/bin/python3
"""
Console front end of hbnb project
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "hbnb"

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



if __name__ == '__main__':
    HBNBCommand().cmdloop()