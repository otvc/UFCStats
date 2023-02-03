# Description 
This reposetory contain classes for parse sites:
- www.ufcstats.com.
- www.consultant.ru
- www.yurist-online.net

# Requirements
You should have ```chromedriver.exe``` in folder with ```Stroller.py```

# Usage
If you want use parser and to save data in same foldaer in csv format then just write in console:
```
python run_parser.py
```
Another configurations of using is shown in block ```Configuration```

# Configuration
## Flags
When you use running `run_parser.py`, the following flags are available:

    - `-c`, `--connection` contain connection string if you want save data in mongodb
    - `-d`, `--dbname`, contain name of database in mongo
    - `-s`, `--saved`, checked if you used parser and want start from the saved results
    - `-fp`, `--first_page`, contained first page, from which you want start (on this moment work only for ufcstats)
    - `-m`, checked if you want use mongo db
    - `-p`,  `--parsers`, use for choose cite which you want parse and chose from ['ufcstats', 'consult']

By default:
```
connection = 'mongodb://localhost:27017',
dbname = StatsUFC,
saved = False,
first_page = 'http://www.ufcstats.com/statistics/events/completed'
m = False
parsers = ufcstats
```