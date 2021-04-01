"Basic Flask Blueprint for Databases with SQL-Alchemy" 

NB! https://stackoverflow.com/questions/66647787/attributeerror-cant-set-attribute-when-connecting-to-sqlite-database-with-flas

Currently there's a 'bug' in SQLAlchemy 1.4+ that creates an inability to set the sa_url attribute. revert to last --v 1.2.23
