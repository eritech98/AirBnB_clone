**AirBnB clone - The console project**
---
**Description:**The objective of this project is to deploy a simple Airbnb website - check it out! [Airnb] (https://www.airbnb.com/)It involves creating a command intepreter/something like simple shell to manage the airbnb Objects
---

**usage:**
Here is a simple demonstration of how it all works
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
----
**The shell should work like this in interactive mode:**
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
---
**The shell should also work in non-interactive mode**
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
----
