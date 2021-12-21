# Session Saver

This is the first programming project I did outside of university. I made it
back in 2019 when I first started learning python.

&nbsp;

When I needed to learn for exams I had two options: Either leave my notebook on
overnight or close all files and websites just to open them all again in the
morning. Back in the time I just completed an online python course so I figured:
why not write a program for that? So I did.

&nbsp;

The program has a button to select files you want to use next time. It opens a
filedialog in which files can be chosen. The filenames are then written into the
left box. Urls have to be copied into the right box by hand. I have used a
chrome-extension for that purpose.

&nbsp;

By clicking the first button on the bottom, the filepaths to selected files are
written into a txt-file named "sessionfiles.txt", each on separate lines. URLs
are written into a txt-file called "session_urls.txt" in the same manner. The
second button is used to open all saved files and URLs again.

Then there are buttons to delete files in the left box or urls in the right box.

&nbsp;

The frontend was made using the Qt designer. With it, you can simply drag
UI-Elements into a window (WYSIWYG-Editor). The code is written automatically
using the qt-framework.

&nbsp;

I had a lot of fun finding a solution to my problem. To learn python I have used
[this](https://www.udemy.com/course/python-bootcamp/) german python course on
udemy.
