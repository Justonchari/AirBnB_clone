#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the AirBNB console."""

=======
"""
This module defines the entry point of the hbnb command interpreter used
to interact with hbnb framework
"""
import cmd
import json
import shlex
import textwrap
from models import storage
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
<<<<<<< HEAD
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import cmd
import re
from shlex import split
from models import storage

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = parse(arg)
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
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
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
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()
=======
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def strip(s):
    return s.strip("'").strip('"')


class HBNBCommand(cmd.Cmd):
    """Simple command processor for the hbnb project"""

    prompt = "(hbnb) "
    hbnb_classes = ["BaseModel", "User", "State",
                    "City", "Amenity", "Place", "Review"]

    def do_EOF(self, arg):
        """Exit"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def postloop(self):
        print()

    def emptyline(self):
        """Action if empty line (don't do anything)"""
        pass

    def precmd(self, arg):
        """Capture help commands and parse method docstring using textwrap"""

        command, args, line = cmd.Cmd.parseline(self, arg)
        if command == "help" and args != "":
            eval_str = line.replace("help", "do").replace(" ", "_")
            eval_str = f"self.{eval_str}.__doc__"
            try:
                ret = textwrap.dedent(eval(eval_str)).lstrip("\n")
                print(ret)
            except AttributeError:
                print("No such command")
            finally:
                return ""

        return line

    def do_create(self, arg):
        """
        Create new instance of Class, save to json file and print id
            Ex:
            >> create BaseModel
            >> Create User
        """
        if not arg:
            print("** class name missing **")

        elif arg not in self.hbnb_classes:
            print("** class doesn't exist **")

        else:
            eval_string = f"{arg}()"
            new_base = eval(eval_string)
            new_base.save()
            print(new_base.id)

    def do_show(self, arg):
        """
        Print string representation of instance if it exists
            Ex:
            >> show Basemodel <id>
            >> BaseModel.show(<id>)
        """
        if not arg:
            print("** class name missing **")

        else:
            argv = shlex.split(arg)
            argc = len(argv)

            if argv[0] not in self.hbnb_classes:
                print("** class doesn't exist **")

            else:
                if argc == 1:
                    print("** instance id missing **")

                else:
                    storage.reload()
                    instance_key = f"{argv[0]}.{strip(argv[1])}"
                    instance = storage.all().get(instance_key, None)

                    if instance is None:
                        print("** no instance found **")
                    else:
                        print(instance)

    def do_destroy(self, arg):
        """
        Delete instance base on class name and id, save to json file
            Ex:
            >> destroy BaseModel <id>
            >> BaseModel.destroy(<id>)
        """
        if not arg:
            print("** class name missing **")

        else:
            argv = shlex.split(arg)
            argc = len(argv)

            if argv[0] not in self.hbnb_classes:
                print("** class doesn't exist **")

            else:
                if argc == 1:
                    print("** instance id missing **")

                else:
                    storage.reload()
                    instance_key = f"{argv[0]}.{strip(argv[1])}"
                    instance = storage.all().get(instance_key, None)

                    if instance is None:
                        print("** no instance found **")
                    else:
                        storage.all().pop(instance_key)
                        storage.save()

    def do_all(self, arg):
        """
        Print string representation of all instances
            Ex:
            >> all BaseModel
            >> BaseModel.all()
        """

        def eval_str(string):
            return string.split(".")[0]

        storage.reload()

        if arg == "":
            print(json.dumps([str(v) for k, v in storage.all().items()]))

        else:
            if arg not in self.hbnb_classes:
                print("** class doesn't exist **")
            else:
                print(
                    json.dumps(
                        [
                            str(v)
                            for k, v in storage.all().items()
                            if arg == v.__class__.__name__
                        ]
                    )
                )

    def do_update(self, arg):
        """
        Update/Add instance attribute based on class, name and id
            Ex:
            >> update BaseModel <id> <attr> <attr_value>
            >> BaseModel.update(<id> <attr> <attr_value>
            >> BaseModel.update(<id> {"first_name": "BaseModel1", "Age": 10})
        """

        if not arg:
            print("** class name missing **")

        else:
            # argv = shlex.split(arg)
            argv = arg.split()
            argc = len(argv)

            if argv[0] not in self.hbnb_classes:
                print("** class doesn't exist **")
                return

            if argc < 2:
                print("** instance id missing **")
                return

            else:
                storage.reload()
                instance_key = f"{argv[0]}.{strip(argv[1])}"
                instance = storage.all().get(instance_key, None)

                if instance is None:
                    print("** no instance found **")
                else:
                    if argc < 3:
                        print("** attribute name missing **")
                        return
                    try:
                        if argv[2].startswith("{") and argv[2].endswith("}"):
                            instance.__dict__.update(json.loads(argv[2]))
                            storage.save()
                            return
                    except (ValueError, json.decoder.JSONDecodeError):
                        pass

                    if argc < 4:
                        print("** value missing **")
                        return
                    else:
                        dont_update = ["id", "created_at", "updated_at"]
                        attribute = strip(argv[2])
                        if attribute not in dont_update:
                            instance.__dict__[strip(argv[2])] = strip(argv[3])
                            storage.save()

    def do_count(self, arg):
        """
        Count number of instances of a class
            Ex:
            >> count BaseModel
            >> BaseModel.count()
        """

        if not arg:
            print("** class name missing **")

        else:
            argv = shlex.split(arg)
            argc = len(argv)

            if argv[0] not in self.hbnb_classes:
                print("** class doesn't exist **")
            else:
                storage.reload()
                count = [v for v in storage.all().values()
                         if arg == v.__class__.__name__
                         ]
                print(len(count))

    def default(self, arg):
        """Parse unrecognized command prefixes"""

        # parseline returns tuple (command, args, line)
        command, args, line = cmd.Cmd.parseline(self, arg)
        # ex. arg = User.all()
        # command, args, line = ("User", ".all()",  "User.all()")

        # if command in self.hbnb_classes:
        do_cmd, _, add_args = args.strip(".)").partition("(")

        if do_cmd == "":
            print("No command found, use help")
            return

        if add_args == "":
            new_arg = f"{do_cmd} {command}"

        else:
            # Convert args to a list and join with spaces
            add_args = add_args.split(",", 1)
            for idx, add_arg in enumerate(add_args):
                if add_arg.strip().startswith("{"):
                    add_args[idx] = add_arg.replace(
                            " ", "").replace("'", '"')
                else:
                    add_args[idx] = add_arg.replace(",", "")

            add_args = " ".join(add_args)
            new_arg = f"{do_cmd} {command} {add_args}"

        cmd.Cmd.onecmd(self, new_arg)
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c


if __name__ == "__main__":
    HBNBCommand().cmdloop()
<<<<<<< HEAD

=======
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c
