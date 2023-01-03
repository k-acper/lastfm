---- PREPARING THE DATA ----
Use this website to export your lastfm to csv:
https://benjaminbenben.com/lastfm-to-csv/
2. Download and install python 3.9.2
3. Make sure to install arrow via pip using this command (in terminal or cmd):
'pip install arrow' or 'pip3 install arrow'
4. Add the following line as the first line of your csv:
artist,album,track,date
[no spaces]
You can do this by editing your csv file in a text editor.
MAKE SURE YOUR DATE FORMAT IS DD MMM YYYY HH:mm
(ex. 01 Jan 2021 16:16) otherwise it won't work.
If the format is different change it using excel.
5. Put the exported csv in the same folder as the lastfm.py file
6. Name your csv file “lastfm.csv”
---- RUNNING THE SCRIPT ----
7. Run the lastfm.py script in terminal or cmd:
[MacOs] (e.g. If the files (lastfm.csv and lastfm.py) are on your desktop type in "cd desktop" and then "python3 lastfm.py")
---- VISUALISATION ----
8. Enter this link and click "Duplicate and edit":
https://public.flourish.studio/visualisation/5640566/
9. Upload your processed data.
---- DOWNLOAD LINK----
use this link to download the python script: https://github.com/k-acper/lastfm

idea inspired by u/lfshammu
the script is an extended and modified version of u/plissk3n's code

If you're stuck or keep getting some kind of traceback, upload your csv to dropbox or googledrive and send it to me via private chat and I'll process it for you.

-----DISCLAIMER-----
If there's any sort of traceback it's a formatting problem 99% of the time.
example of a good formatting:
lur,The Magic Whip,New World Towers,22 Mar 2021 16:55
Two Door Cinema Club,Tourist History,What You Know,22 Mar 2021 16:51

if anything looks a bit different, that's the thing causing the problem.
