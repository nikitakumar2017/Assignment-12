#Q.1- Print the current day using Datetime module
import datetime as dt
ans=dt.date.today()
print(ans.day)

#Q.2- Open your browser and play a video using webbrowser module in python.
import webbrowser
search=input("Enter your video search ")
webbrowser.open_new_tab('https://www.youtube.com/results?search_query=%s' % search)


#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.
import os
for filename in os.listdir("folder1"):
    dst =filename + ".jpg"
    src ='folder1'+ filename
    dst ='folder1'+ dst

