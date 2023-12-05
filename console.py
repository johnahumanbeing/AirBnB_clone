#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    __classNames = ["BaseModel"]

    def do_EOF(self, line):
        print()
        return True
    
    def do_quit(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()