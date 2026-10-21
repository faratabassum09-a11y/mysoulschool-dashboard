MySoulSchool Sales Dashboard
- index.html : the finished dashboard (open in any browser; needs internet for Chart.js + fonts)
- build.py   : reads Students_Records.xlsx (Dashboard tab), cleans it, writes the dashboard
- t.html     : dashboard template used by build.py
To refresh: put a new Students_Records.xlsx at the path in build.py, run: python3 build.py
(build.py needs pandas + openpyxl; edit the file paths at the top/bottom to your own folders)
