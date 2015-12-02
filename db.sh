#!/bin/bash

if [ -f "test_db" ];
then
   echo "Removing old DB"
   rm test_db
fi

echo "Creating test_db"
sqlite3 test_db << EOF
.mode csv
.import people.txt people 
EOF
echo "Db Created - table people inserted"
echo "Test query"

sqlite3 test_db << EOF
.separator \t
select * from people;
EOF
