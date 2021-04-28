# daily_mail_for_newly_published_Physics_articles
This is a program that mails you the details of newly published articles on Physics from the "Nature" website.

To run this program you need to install smtplib, requests, bs4 mudules. You can install these modules by simply writing, pip install module_name , in the command prompt.

In order to get the update regularly, you have to schedule the program to run everyday at a certain time. In windows you can do that by using the task schedular tool, steps are given below.
- Create a batch file, given by the paths of the python.exe file and the python script.
- - You can create a batch file by opening the notepad and write the paths of those files in "", separated by a "space", and save the file as "file name you want.bat". 
- Copy the path of the batch file.
- Open the task schedular tool, select on "create a Basic Task", give a name to the task, select next.
- Now as you want to run the program daily, select on daily, then select next.
- Select the start date and the time when you want the program to be run, select next, and now select "start a program" and select next.
- Now enter the path of the batch file that you create previously and select next.
- Select finish!

Now you are done!
Note that, you should enter a time when you usually use your computer, every day. Because the task will only execute when your computer is on.
