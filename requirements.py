import mysql.connector

db = mysql.connector.connect(user='root', password='maSliD@1372',
                              host='127.0.0.1',
                              database='test')
# cnx.close()
mycursor = db.cursor()
sql = "CREATE TABLE forum (id int(11) NOT NULL AUTO_INCREMENT,  forum_name varchar(45), PRIMARY KEY (id))"
mycursor.execute(sql)
db.commit()

sql = "CREATE TABLE user (id int(11) NOT NULL AUTO_INCREMENT ,user_name varchar(45) UNIQUE " \
      ", registry_date varchar (30), birth_date varchar (30), PRIMARY KEY (id)) "
mycursor.execute(sql)
db.commit()

sql="CREATE TABLE forum_user (user_forum_id int(11) NOT NULL AUTO_INCREMENT ,title varchar(45) , post mediumtext " \
    ",username varchar(45), " \
    "forumname varchar(45) , " \
    "PRIMARY  KEY (user_forum_id) )"
mycursor.execute(sql)
db.commit()