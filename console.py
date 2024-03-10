#!/usr/bin/python3
"""Console module serving as entry point"""

import cmd
import re
import sys

from models.__init__ import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def precmd(self, line):
        if "." in line:
            parse = re.findall(r"[a-zA-Z]+", line)
            if len(parse) >= 2:
                parse = parse[1] + " " + parse[0]

            return cmd.Cmd.precmd(self, parse)
        else:
            return cmd.Cmd.precmd(self, line)

    __classes = {
        "BaseModel": BaseModel
    }

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """End program with ctrl D"""
        return True

    def do_quit(self, line):
        """quit to end program"""
        return True

    def default(self, line):
        print("Unkown command {}".format(line))

    def do_create(self, line):
        """Creates an Instance."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        name = args[0]
        new_instance = HBNBCommand.__classes[name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Lists all the created and saved instances"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the ID"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objs:
            del objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instance"""
        args = line.split()
        objs = []

        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                if len(args) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = "{}.{}".format(class_name, args[1])
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objs[key], args[2], eval(args[3]))
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

