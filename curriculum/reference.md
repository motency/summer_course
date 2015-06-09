Reference
=========

I'll keep things here that you may need to refer to from time to time.


Using Git
---------

Making Commits
++++++++++++++

Commits are a way of saving changes to your work. It's good to commit 
frequently. There are two main ways to use git: using the GitHub program,
or using git directly from Terminal.

From the GitHub program:

1. Work on your files using TextWrangler.
2. When you're ready to commit, open GitHub. It will detect the changes you've 
  made since the last commit. You can choose which to include in the commit. 
3. Add a commit message explaining the changes you made. 
4. Press "Commit"
5. Press the Sync button to upload your changes to GitHub. Now everyone can 
   see them. 

From Terminal:

1. `cd` into the directory holding your work.
2. type `git status` to see which files have been changed. 
3. (optional) type `git diff` to see all the changes that have been made to files.
4. type `git add ________` to add a file to the commit you're about to make. If you 
   type `git status` again, you'll see this file is now staged for the commit.
5. Once you're ready to commit, type `git commit -m "A message explaining what's new..."`
6. type `git push` to upload your changes to GitHub. Now everyone can see them.

Updating your fork
++++++++++++++++++++++++

The easiest way to update your fork with changes I made is to use the GitHub website, as 
described [here](http://www.hpique.com/2013/09/updating-a-fork-directly-from-github/).

If you want to use Terminal, there are two steps:

1. [Add an upstream remote](https://help.github.com/articles/configuring-a-remote-for-a-fork/), pointing to 
   my original repository
2. [Sync your fork](https://help.github.com/articles/syncing-a-fork/) with the original repo.

(Hello, everyone! This is Annie/motency. I asked Chris some questions about the code we learned recently, and he asked me to post the questions and answers, so here they are:)

1. Could you explain "magic methods" to me a little more? I think they are magic if there is a set of underscores around the method. What does the magic part do? Does it make it unaccessible for the user?

Magic methods are called "magic" because, unlike normal methods, they are called indirectly. For example, __init__() is called when a new object is created, __str__() is called when a string representation of an object is needed, and __len__() is called when you ask for the "length" of your teakettle.  These are really useful for controlling how your object will act, and for making your object act more "naturally" in Python. We will play with some examples of magic methods on Tuesday. This page (http://rafekettler.com/magicmethods.html) has good documentation of all the magic methods; it's most useful if you already know what you're looking for though. The double underscores are meant to suggest that the methods aren't for using directly, but in Python you can't actually make methods inaccessible to the user. (This is a difference between Python and Java.)

2. Why can I not enter the names of a method and have them work? I have tried entering "Animal()" and "Kettle()," and that makes the program say something. However, if I try to enter the name of a method like I did in "hangman()," the program states something like "__init__ is not defined." This also happens if I enter the name of something that is not a magic method. Why is this?

Let's clarify some terminology: functions exist on their own; methods are functions attached to objects. But to give a good answer, I need to introduce a new idea, which we'll talk about on Tuesday: scope. A variable's scope is its territory, its universe, the areas where it is defined. If you write two Python modules (files), you're probably not surprised that a variable you define in one doesn't magically appear in the other file. This is because a variable's scope is the module in which it lives. Objects have their own inner worlds; the scope of variables inside an object is the object. So this shouldn't be surprising: 
>>> kettle.mood = "Tired of being boiled"
>>> kettle.mood
'Tired of being boiled'
>>> mood
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mood' is not defined
The variable mood only exists inside the kettle. The same is true for methods:
>>> kettle.pour(4)
You poured out 4 cold water!
>>> pour(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pour' is not defined

3. I am a little fuzzy on the "self" variable. I see that you typed something like "self.name = name." Why did you not have to define 'name?' I think that if you put 'self' in the parenthesis next to the method and type self.(something), you don't need to define self.

You don't have to define name because you can add new attributes to objects whenever you want. So if you have a Kettle called kettle, you can do this:
>>> kettle.mood = "Tired of being boiled"
>>> kettle.mood
'Tired of being boiled'
The effect of "self.name = name" is to store the name variable (which will go away at the end of the function) as an attribute of the object, so that it won't be lost. 

4. Why did you put these symbols (< and >) in your print statements? The program seemed to work without them, so do they serve a purpose?

I added these to the representations of our objects so that they look like the representations of other Python objects such as modules and functions: 
>>> random
<module 'random' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.pyc'>
>>> random.randint
<bound method Random.randint of <random.Random object at 0x7fa85c833820>>
>>> kettle
<Kettle with 10 cold water>
>>> kettle.pour
<bound method Kettle.pour of <Kettle with 10 cold water>>
>>> import random

5. How do you use the curly brackets to say something in a print statement? How do the curly brackets know which variable to use?

We'll go over this on Tuesday as well. There are lots of fancy things you can do with the curly braces, but the simplest way to use them is by position. When you format a string, the first argument goes into the first placeholder, and so forth:
"I would like to eat {} cups of {} for {}.".format("six", "porridge", "breakfast")
'I would like to eat six cups of porridge for breakfast.'

6. Did you import one program into another by typing "from animal import Animal"? If so, how can I do this?

Instead of "program", let's say "module". In Python, each file is a module. Each module is its own universe, and can contain variables, functions, objects, and other things. As you said, you use import to bring one module into another module. There are two ways of doing this: You can either import the module and then access its attributes:
>>> random.randint(0, 5)
5
Or you can directly import objects:
>>> from random import randint
>>> randint(0, 5)
2
 
Of course, imports will only succeed if Python can find the module you're looking for. When Python looks for a module, it starts by looking in the current folder. So if you keep all your code for a project in the same folder, you'll be able to successfully import. Then Python goes looking in other folders, technically defined by an environmental variable called PYTHONPATH. There are a couple of standard places "installed" modules get stored, and they can be loaded from these locations. 
A few students had interesting problems with their hangman programs when they made a file called random.py and saved them in the same folder as their hangman programs. Then when they tried to import random, this file got loaded instead of the built-in random library. 
