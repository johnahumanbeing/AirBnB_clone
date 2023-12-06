#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    __classNames = ["BaseModel"]

    def do_EOF(self, arg):
        print()
        return True
    
    def do_quit(self, arg):
        return True
    
    def do_show(self, arg):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()