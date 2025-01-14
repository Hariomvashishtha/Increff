import _mysql_connector
my_db= _mysql_connector.connect(
    host ="localhost",
    user="root",
    passwd="HariomJyoti@2004",
)

my_cursor = my_db.cursor()