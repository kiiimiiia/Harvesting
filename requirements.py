import mysql.connector

db = mysql.connector.connect(user='root', password='maSliD@1372',
                              host='127.0.0.1',
                              database='test')
# cnx.close()
mycursor = db.cursor()
sql = "CREATE TABLE forum (id int(11) NOT NULL AUTO_INCREMENT,  name varchar(50), PRIMARY KEY (id))"
mycursor.execute(sql)
db.commit()

sql = "CREATE TABLE user (id int(11) NOT NULL AUTO_INCREMENT ,name varchar(45) ,fname varchar(45) ,username varchar(45)" \
      ", registry_date date , , PRIMARY KEY (id)) "
mycursor.execute(sql)
db.commit()

sql="CREATE TABLE forum_user (user_forum_id int(11) NOT NULL AUTO_INCREMENT ,title varchar(45) , post mediumtext " \
    ",username varchar(50), forumname int(45) , PRIMARY  KEY (user_forum_id) , FOREIGN KEY (username) REFERENCES user(name)" \
    ",FOREIGN KEY (forumname) REFERENCES forum (name))"
mycursor.execute(sql)
db.commit()