Welcome to a Python Programming Project!
========================================

This is an instructional project on using Python to build a video game based on the 
popular Frogger (tm) game of the 1980's and 90's distributed by Sega and Sega-Gremlin. 
This instructional project and series of videos in no way attempts to replace or 
compete with the Frogger video game. The project is intended to teach computer programming
in a fun and interesting way. 

There is a [playlist for all these videos on Youtube](https://www.youtube.com/playlist?list=PL8tLy_7ToXL9-Z_5GoWI_01-op8SeyN2E).

Prerequisites
---------------

Please see the [setting up video](http://youtube.com/CSProfessor/) for instructions on 
installing the required software on your computer. You can follow along on this video to get all the software installed. 

If you choose, you may follow the steps below instead of watching the set up video. 
To begin, you must have Git, Python 3, and Wing IDE 101 installed on your computer. First check and see if a system administrator or teacher has installed this software for you. If no one has installed this software, then you can download these packages from these locations. Be sure to get the Windows version if you are running Microsoft Windows or the Mac version if you are running Mac OS X. 

* Git
	+ [Git For Windows](https://git-scm.com/download/win)
	+ [Git for Mac](https://git-scm.com/download/mac)
* [Python 3](https://www.python.org/downloads/)
	+ Be sure to click on the Download link for Python 3.x.y on the page. Using Python 2.x.y will not work for this instructional project. 
* [Wing IDE 101 from Wingware.com](http://wingware.com/downloads/wingide-101/)
	+ This is a free program from Wingware. The program is free for educational use.


Configuring Wing 101
---------------------

After downloading and installing the programs above, you must configure Wing IDE 101 to run Python 3. Find the Wing IDE 101 application under the Start Menu on Windows or under Applications on a Mac. Open Wing and consent to the free license. Then go to the Edit menu. Select *Configure Python...*, click the *Custom* radio buttonn next to the **Python Executable* part of the dialog box, and in the text box below the radio button type *python3* as the executable. Make sure you type *python3* in all lower case letters with no spaces. Wing IDE 101 will ask if you want to restart the shell which you want to do that this time. 

The Lessons
-------------
Once you have completed the steps under the prerequisites and configured Wing 101 you are ready to begin the lessons. You do the lessons by watching the video for a lesson, following the steps contained in each. [You can access the lesson videos on YouTube by clicking here](https://www.youtube.com/playlist?list=PL8tLy_7ToXL9-Z_5GoWI_01-op8SeyN2E).

At the beginning of each video you are prompted to execute a *git* command from a terminal window. If you don't have access to a terminal window, you may be able to run a script instead to set up each lesson. If you don't have access to a terminal window, download the zip file of the master branch of this project. Put Frogger-master.zip where you want it on your system (i.e. your Documents folder). Unzip or uncompress the zip file. Navigate to the Frogger-master folder. Then double-click on the *setup* file. This will create a new folder called *Frogger* which will be set up correcty to do each of the lessons. If you don't have access to a terminal window then before doing a lesson, double-click on the *setuplessonX* file where *X* is the number of the lesson. So, you would double-click *setuplesson1* to setup the project before watching the video for lesson 1. If the directions in this paragraph don't work for you it is because you don't have a computer that can run *bash* programs. In that case you would need to get access to a terminal window for your system.

You will be asked to pause videos at certain points. You should pause them and then try the indicated excercises. When you restart the video you will be shown the correct answer to give you immediate feedback. 

Don't worry if something gets messed up in your code at some point in a lesson. You can always restart a lesson by watching the video again. **Just be aware that any changes you make to the project will be lost when you reset the lesson or switch to the next lesson.** These lessons are intended for instruction and practice. So, if you want to save your work, save your program to a different location, other than the location indicated in each video. 

To get the most from these lessons, watch them in order and do the indicated exercises until you feel comfortable you understand all the concepts that are taught. If you feel you need additional information, you may find online resources for learning Python programming or you can buy the text [Python Programming Fundamentals](http://www.amazon.com/Programming-Fundamentals-Undergraduate-Computer-Science/dp/1849965366/ref=sr_1_1?ie=UTF8&qid=1457286492&sr=8-1&keywords=python+programming+fundamentals) by me. It contains additional information and useful exercises with solutions provided to practice problems in the text.

To begin you must open a terminal window (a command shell in Windows) and issue the command:
	
	git clone https://github.com/kentdlee/Frogger

Each of the lessons goes through the steps that you must executed to get the code for that lesson. The first four lessons provide some backgound on Python. The last eight lessons build the application. An outline of the lessons is provided below. 

* Lesson One - Getting Started. You can find additional documentation on what you can do with [turtle graphics here](https://docs.python.org/3.5/library/turtle.html). 
* Lesson Two - Defining Functions
* Lesson Three - Drawing Circles
* Lesson Four - Defining Classes
* Lesson Five - The FroggerApplication; Drawing a river and a road. [Additional Frogger images can be found here](http://strategywiki.org/wiki/Frogger/Getting_Started). Additional images are not required for any of the lessons presented here. 
* Lesson Six - A Frog Class
* Lesson Seven - A Racecar Class
* Lesson Eight - A Log Class
* Lesson Nine - Avoiding Cars
* Lesson Ten - Jumping on Logs
* Lesson Eleven - Alligators or Crocodiles
* Lesson Twelve - Keeping Score

Have fun and enjoy the lectures and building an arcade game in Python! 
