#!/usr/bin/python3
"""
    HBNBCommand
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    prompt = '(hbnb) '

    def emptyline(self):
        """an empty line + ENTER no command executed"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
