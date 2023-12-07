#!/usr/bin/python3
import cmd
import models
import re
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    __classNames = ["BaseModel"]

    def do_EOF(self, arg):
        print()
        return True
    
    def do_quit(self, arg):
        return True
    
    def default(self, arg):
        cmds = {
            "show": self.do_show,
            "all": self.do_all,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_couunt
        }
    
    def do_show(self, arg):
        args = self.split(arg)

        if len(args) == 1 and args[0] == "":
            print("** class name missing **")
        elif args[0] not in self.__classNames:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = models.storage.all()

            if key in objects.keys():
                print(objects[key].__str__())
            else:
                print("** no instance found **")

    def do_all(self, arg):
        args = self.split(arg)
        obbjects = models.storage.all()

        if len(args) == 1 and args[0] == "":
            print([obj.__str__() for obj in object.values()])
        elif args[0] not in self.__classNames:
            print("** class doesn't exist **")
        else:
            print([obj.__str__() for obj in object.vaalues()
                   if obj.__class__.__name__== args[0]])

if __name__ == '__main__':
    HBNBCommand().cmdloop()