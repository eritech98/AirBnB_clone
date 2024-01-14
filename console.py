#!/usr/bin/python3

"""
Contains the CMD pROGRAMram.
"""
import cmd
import re
import ast
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Contains entry point of the command interpreter.
    """
    prompt = '(hbnb)'

    def do_create(self, class_name_1):
        """
        Creates a new instae of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not class_name_1:
            print("** class name missing **")
        elif shlex.split(class_name_1)[0] in \
            ["BaseModel", "User", "State", "City", "Amenity",
             "Place", "Review"]:
            class_Name_1 = shlex.split(class_name_1)[0]
            new_obj_1 = eval(class_Name_1)()
            new_obj_1.save()
            print(new_obj_1.id_1)
        else:
            print("** class does not exist **")

    def do_show(self, class_plus_id):
        """
        Prints the string Representation of an instance
        based on the classs name and id_1.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        if not class_plus_id:
            print("** class name missing **")
        elif shlex.split(class_plus_id)[0] not in \
            ["BaseModel", "User", "State", "City", "Amenity",
             "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(shlex.split(class_plus_id)) > 1:
            class_name_1 = shlex.split(class_plus_id)[0]
            obj_id_1 = shlex.split(class_plus_id)[1]
            all_objs = storage.all()
            if f"{class_name_1}.{obj_id_1}" in all_objs.keys():
                print(all_objs[f"{class_name_1}.{obj_id_1}"])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, class_plus_id):
        """
        Deletes an instance based on THW class name and id.
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if not class_plus_id:
            print("** class name missing **")
        elif shlex.split(class_plus_id)[0] not in \
            ["BaseModel", "User", "State", "City", "Amenity",
             "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(shlex.split(class_plus_id)) > 1:
            class_name_1 = shlex.split(class_plus_id)[0]
            obj_id_1 = shlex.split(class_plus_id)[1]
            all_objs = storage.all()
            if f"{class_name_1}.{obj_id_1}" in all_objs.keys():
                del all_objs[f"{class_name_1}.{obj_id_1}"]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, class_name_1):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        all_objs = storage.all()
        if not class_name_1:
            for v in all_objs.values():
                print(v)
        elif shlex.split(class_name_1)[0] in \
            ["BaseModel", "User", "State", "City", "Amenity",
             "Place", "Review"]:
            class_Name_1 = shlex.split(class_name_1)[0]
            for v in all_objs.values():
                if v.__class__.__name__ == class_Name_1:
                    print(v)
        else:
            print("** class doesn't exist **")

    @staticmethod
    def count(class_name_1):
        """
        Counts the number of instances of a class.
        """
        all_objs = storage.all()
        count = 0
        for v in all_objs.values():
            if v.__class__.__name__ == class_name_1:
                count += 1

        print(count)

    @staticmethod
    def find_dict(text):
        """
        Finds a dictionary within a text and returns the dictionary.
        """
        pattern = r"(\{.+\})"
        check_match = re.findall(pattern, text)
        if len(check_match):
            return ast.literal_eval(check_match[0])

    def do_update(self, class_plus_att):
        """
         Updates an instance based on the class name and id
         by adding or updating attribute (save the change into the JSON file).
         Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        if not class_plus_att:
            print("** class name missing **")
        elif shlex.split(class_plus_att)[0] not in \
            ["BaseModel", "User", "State", "City", "Amenity",
             "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(shlex.split(class_plus_att)) > 1:
            class_name_1 = shlex.split(class_plus_att)[0]
            obj_id_1 = shlex.split(class_plus_att)[1]
            all_objs = storage.all()
            if f"{class_name_1}.{obj_id_1}" in all_objs.keys():
                if len(shlex.split(class_plus_att)) > 2:
                    if len(shlex.split(class_plus_att)) > 3:
                        obj_attribute_1 = shlex.split(class_plus_att)[2]
                        obj_att_value_1 = shlex.split(class_plus_att)[3]
                        obj = all_objs[f"{class_name_1}.{obj_id_1}"]
                        obj.__dict__[obj_attribute_1] = obj_att_value_1
                        obj.save()
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_EOF(self, line):
        """
        EOF command to exit the program.
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def emptyline(self):
        pass

    def default(self, line):
        class_name_1 = line.split('.')[0]
        dict_repr = HBNBCommand.find_dict(line)

        if class_name_1 in ["BaseModel", "User", "State", "City",
                          "Amenity", "Place", "Review"]:
            try:
                obj_att = line.split('(')[1].strip(')').split(',')
                obj_id_1 = ""
                obj_att_name = ""
                obj_att_value_1 = ""
                check_dict_1 = 0
                command_update_1 = f"{class_name_1}.update()"
                if len(obj_att) == 1:
                    obj_id_1 = obj_att[0]
                    command_update_1 = f"{class_name_1}.update({obj_id_1})"
                elif len(obj_att) == 2:
                    obj_id_1 = obj_att[0]
                    obj_att_name = obj_att[1]
                    command_update_1 = f"{class_name_1}.update({obj_id_1},{obj_att_name})"
                elif len(obj_att) > 2:
                    obj_id_1 = obj_att[0]
                    obj_att_name = obj_att[1]
                    obj_att_value_1 = obj_att[2]
                    command_update_1 = f"{class_name_1}.update({obj_id_1},{obj_att_name},{obj_att_value_1})"
                if len(obj_att) and dict_repr:
                    check_dict_1 = 1
            except IndexError:
                return cmd.Cmd.default(self, line)
            command_all_1 = f"{class_name_1}.all()"
            command_count_1 = f"{class_name_1}.count()"
            command_show_1 = f"{class_name_1}.show({obj_id_1})"
            command_destroy_1 = f"{class_name_1}.destroy({obj_id_1})"
            if line == command_all_1:
                line = f'all {class_name_1}'
                cmd.Cmd.onecmd(self, line)
            elif line == command_count_1:
                HBNBCommand.count(class_name_1)
            elif line == command_show_1:
                line = f'show {class_name_1} {obj_id_1}'
                cmd.Cmd.onecmd(self, line)
            elif line == command_destroy_1:
                line = f'destroy {class_name_1} {obj_id_1}'
                cmd.Cmd.onecmd(self, line)
            elif line == command_update_1 or check_dict_1:
                if check_dict_1:
                    for key_Erick, v in dict_repr.items():
                        line = f'update {class_name_1} {obj_id_1} {key_Erick} {v}'
                        cmd.Cmd.onecmd(self, line)
                else:
                    line = f'update {class_name} {obj_id_1} {obj_att_name} {obj_att_value_1}'
                    cmd.Cmd.onecmd(self, line)
            else:
                return cmd.Cmd.default(self, line)
        else:
            return cmd.Cmd.default(self, line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
