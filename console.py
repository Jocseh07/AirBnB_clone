#!/usr/bin/python3
"""Entry point of command interpreter."""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def arguments(arg):
    curly = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Define command interpreter."""

    prompt = "(hbnb) "
    __cls = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Execute nothing with empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        dos = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            args = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])
            if match is not None:
                command = [args[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in dos.keys():
                    call = "{} {}".format(args[0], command[1])
                    return dos[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Creates a new class instance and prints its id.
        """
        args = arguments(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__cls:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class name>.show(<id>)
        Display the string representation of a name or id.
        """
        args = arguments(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__cls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class name>.destroy(<id>)
        Delete a class instance given an id.
        """
        args = arguments(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__cls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """all or all class or <class>.all().
        Display string representation of all instances based or not on class.
        """
        args = arguments(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__cls:
            print("** class doesn't exist **")
        else:
            list = []
            for obj in storage.all().values():
                if len(args) > 0:
                    if args[0] == obj.__class__.__name__:
                        list.append(obj.__str__())
                else:
                    list.append(obj.__str__())
            print(list)

    def do_update(self, arg):
        """update <class name> <id> <attribute name> <attribute value>
        or <class name>.update(<id>, <attribute name>, <attribute value>)
        or <class name>.update(<id>, <dictionary representation>).
        Update instance based on class and id and save the change
        """
        args = arguments(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__cls:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            print("** value missing **")
            return False

        if len(args) == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            obj.__dict__[args[2]] = args[3]
            storage.save()

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a class.
        """
        args = arguments(arg)
        count = 0
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__cls:
            print("** class doesn't exist **")
            return False
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
