/*

##### SQL INTRO

1. CREATE TABLE is a clause that tells SQL you want to create a new table.
2. celebs is the name of the table.
3. (id INTEGER, name TEXT, age INTEGER) is a list of parameters defining each column, or attribute in the table and its data type:

id is the first column in the table. It stores values of data type INTEGER
name is the second column in the table. It stores values of data type TEXT
age is the third column in the table. It stores values of data type INTEGER

*/

CREATE TABLE celebs (
    id INTEGER,
    name TEXT,
    age INTEGER
);

/*

1. INSERT INTO is a clause that adds the specified row or rows.
2. celebs is the name of the table the row is added to.
3. (id, name, age) is a parameter identifying the columns that data will be inserted into.
4. VALUES is a clause that indicates the data being inserted.
(1, 'Justin Bieber', 22) is a parameter identifying the values being inserted.

1 is an integer that will be inserted into the id column
'Justin Bieber' is text that will be inserted into the name column
22 is an integer that will be inserted into the age column

*/

INSERT INTO celebs (id, name, age) VALUES (1, 'Justin Bieber', 22);

INSERT INTO celebs (id, name, age) VALUES (2, 'Beyonce Knowles', 33);

INSERT INTO celebs (id, name, age) VALUES (3, 'Jeremy Lin', 26);

INSERT INTO celebs (id, name, age) VALUES (4, 'Taylor Swift', 26);

SELECT * FROM celebs;

/*

1. SELECT is a clause that indicates that the statement is a query. You will use SELECT every time you query data from a database.
2. name specifies the column to query data from.
3. FROM celebs specifies the name of the table to query data from. In this statement, data is queried from the celebs table.

You can also query data from all columns in a table with SELECT.

SELECT * FROM celebs;

SELECT statements always return a new table called the result set.

*/

SELECT name from celebs;

/*

1. ALTER TABLE is a clause that lets you make the specified changes.
2. celebs is the name of the table that is being changed.
3. ADD COLUMN is a clause that lets you add a new column to a table:

twitter_handle is the name of the new column being added
TEXT is the data type for the new column
4. NULL is a special value in SQL that represents missing or unknown data. Here, the rows that existed before the column was added have NULL values for twitter_handle.

*/

ALTER TABLE celebs ADD COLUMN twitter_handle TEXT;

SELECT * FROM celebs;

/*

1. UPDATE is a clause that edits a row in the table.
2. celebs is the name of the table.
3. SET is a clause that indicates the column to edit.

twitter_handle is the name of the column that is going to be updated
@taylorswift13 is the new value that is going to be inserted into the twitter_handle column.
4. WHERE is a clause that indicates which row(s) to update with the new column value. Here the row with a 4 in the id column is the row that will have the twitter_handle updated to @taylorswift13.

*/

UPDATE celebs SET twitter_handle = '@taylorswift13' WHERE id = 4;

SELECT * from celebs;

/*

DELETE FROM is a clause that lets you delete rows from a table.
celebs is the name of the table we want to delete rows from.
WHERE is a clause that lets you select which rows you want to delete. Here we want to delete all of the rows where the twitter_handle column IS NULL.
IS NULL is a condition in SQL that returns true when the value is NULL and false otherwise.

*/

DELETE FROM celebs WHERE twitter_handle IS NULL;

SELECT * from celebs;

/*

Constraints that add information about how a column can be used are invoked after specifying the data type for a column.

They can be used to tell the database to reject inserted data that does not adhere to a certain restriction.

The statement below sets constraints on the celebs table.

CREATE TABLE celebs (
   id INTEGER PRIMARY KEY,
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable'
);

1. PRIMARY KEY columns can be used to uniquely identify the row. Attempts to insert a row with an identical value to a row already in the table will result in a constraint violation which will not allow you to insert the new row.

2. UNIQUE columns have a different value for every row. This is similar to PRIMARY KEY except a table can have many different UNIQUE columns.

3. NOT NULL columns must have a value. Attempts to insert a row without a value for a NOT NULL column will result in a constraint violation and the new row will not be inserted.

4. DEFAULT columns take an additional argument that will be the assumed value for an inserted row if the new row does not specify a value for that column.

*/

CREATE TABLE awards (
id INTEGER PRIMARY KEY,
recipient TEXT NOT NULL,
award_name TEXT DEFAULT 'Grammy'
);


/*

Generalizations
Congratulations! You’ve learned six commands commonly used to manage data stored in a relational database and how to set constraints on such data. What can we generalize so far?

SQL is a programming language designed to manipulate and manage data stored in relational databases.

A relational database is a database that organizes information into one or more tables.
A table is a collection of data organized into rows and columns.
A statement is a string of characters that the database recognizes as a valid command.

CREATE TABLE creates a new table.
INSERT INTO adds a new row to a table.
SELECT queries data from a table.
ALTER TABLE changes an existing table.
UPDATE edits a row in a table.
DELETE FROM deletes rows from a table.
Constraints add information about how a column can be used.

*/
