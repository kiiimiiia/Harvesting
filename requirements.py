import mysql.connector

db = mysql.connector.connect(user='root', password='maSliD@1372',
                              host='127.0.0.1',
                              database='test')
# cnx.close()
mycursor = db.cursor()
sql = "CREATE TABLE forum (id int(11) NOT NULL AUTO_INCREMENT,  name varchar(50), PRIMARY KEY (id))"
mycursor.execute(sql)
db.commit()

sql = "CREATE TABLE user (id int(11) NOT NULL AUTO_INCREMENT ,name varchar(45) ,fname varchar(45) ,username varchar(45) , PRIMARY KEY (id)) "
mycursor.execute(sql)
db.commit()

sql="CREATE TABLE forum_user (user_forum_id int(11) NOT NULL AUTO_INCREMENT ,title varchar(45) , post mediumtext " \
    ",user_id int(11), forum_id int(11) , PRIMARY  KEY (user_forum_id) , FOREIGN KEY (user_id) REFERENCES user(id)" \
    ",FOREIGN KEY (forum_id) REFERENCES forum (id))"
mycursor.execute(sql)
db.commit()