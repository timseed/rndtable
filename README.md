#Background

As part of several computer projects we often need to trial systems -  But in order to conduct a realistic trial we need to use representative data. The problem now becomes with privacy. In the past we have hand developed data, which is tiresome and relies on the developer taking the time to think of allthe test cases.

These 2 classes are an attempt to speed up this process at the same time keeping the data obfuscated as well as realistic.


#Required Modules

There should be no special modules required for this code.

##People_sql

This requires

    sqlite3

To install this (assuming pyenv being used)

    pip install sqlite3 

#Python Version

It was developed using Python 3.4, I have run it with no issues using

      - 2.7
      - 3.4
      - 3.5
      
#Example

## Create the Database

There is a supplied db.sh script - which will load a data file called **people.txt** 

To install

    bash db.sh
     
You should then see
     
    Removing old DB
    Creating test_db
    Db Created - table people inserted
    Test query
    1	bill	1-jan-1981	m
    2	bob	2-Feb-2002	f
    3	john	3-mar-2003	m

At this point the Db is sorted.

##Python code
The "real" data was listed in the SQL create database command compare how the data looks after this


    import sqlite3
    import pprint
    import tab
    sqlite_file='test_db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('SELECT * FROM people ')
    all_rows = c.fetchall()
    #sqlite returns an array of tuples...
    #Convert into a nested array
    
    data=[[col for col in r] for r in all_rows]
    
    """
    Now use the rndtab class -
    """
    
    rt=tab.rndtab()
    rt.setdata(data)
    rt.random_row()
    rt.dump()


#Future Development

##Fuzzing
I already have some **fuzzing** - a blurring of the data.... which could be bolted on should I feel the need.

##Specific Fields
Should your dataset have a specific field that needs obfuscating - then this will not do this. The data stays the same.
This could be troubling should you start dealing with Credit Card type data.