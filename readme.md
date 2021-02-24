# SWING TRADES USING ARK INVEST

I have created a python script that can track tickers across all ARK ETFs 
to flag for any new buys.

I have created a database of historical ark transactions using sqlite3 and is checked into codebase.

The database is upto date as of 02-23-2021.

My strategy to swing trade is based on using this script to find any new stocks that ARK invests in across its ETFs.
The idea is to buy it before others and sell it for a 5% profit.
I have explained my strategy in this  [video](https://youtu.be/52p1feIkRLw).
To use the repo this is what you need to do.

1. register your email ID for daily ARK transactions at https://ark-funds.com/trade-notifications
2. clone this project locally.
3. Install python 3+. I have tested this script against 3.9 version.
4. Switch to the project root directory and install the dependencies for this project as follows.
    - python -m venv my_env ( this will create a folder with name my_env)
    - activate the virtual env by running activate.bat or activate.sh ( find it under my_env\Scripts\activate*)
    - install the required dependendies by running `pip install -r requirements.txt`
5. there is a glitch in using xlrd library with the format of excel files ARK publishes. Follow these steps to over come the limitation.
    - go to folder `my_env\Lib\site-packages\xlrd`.
    - edit file compdoc.py and comment out the lines from 426 to 429.
        - ```# if self.seen[s]:
                # if not self.ignore_workbook_corruption:
                    # print("_locate_stream(%s): seen" % qname, file=self.logfile); dump_list(self.seen, 20, self.logfile)
                    # raise CompDocError("%s corruption: seen[%d] == %d" % (qname, s, self.seen[s]))```
        details of this change can be found [here](https://stackoverflow.com/questions/12705527/reading-excel-files-with-xlrd)
6. Now we are ready to process the daily files. Download the daily transactions file and move it under `analyze_ark_invest\src\resources\input\daily`.
7. Run the application using command `python main.py` from the project root folder 'analyze_ark_invest'.
8. choose option 1 and console output will flag if there are new buys on a given day.


Don't take the position on new stocks if others have already run up the stock 10% before you can take a position. They almost always pull back for an entry.

Good luck!
    
 