# AirBnB clone-The console
<html>
<h3>Welcome to the AirBnB clone project!</h3>
<h4>AUTHORS:</h4>
<ul>
<li> Yasin Alhadi </li>
<li> Afolabi Adepena </li>
</ul>
<h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>
<p>
"This is the first step towards building first full web application: the" <strong>AirBnB</strong> "clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…"
</p>
<p>Each task is linked and will help you to:</p>
<ul>
<li>put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file</li>
<li>create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
</li>
<li>create the first abstracted storage engine of the project: File storage.
</li>
<li>create all unittests to validate all our classes and storage engine
</li>
</ul>
<h3>Execution</h3>
<p>shell should work like this in interactive mode:</p>
<pre>
<code>
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code>
</pre>
<p>also in non-interactive mode:</p>
<pre>
<code>
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
$
</code>
</pre>
</html>

