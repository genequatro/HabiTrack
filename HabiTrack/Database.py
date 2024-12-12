import pymysql
from tkinter import messagebox

def connect_database():
  global mycursor, con
  try:
    con = pymysql.connect(host="localhost", user="root", password="Jinqtro25.")
    mycursor = con.cursor()
  except:
    messagebox.showerror("Error", "Something went wrong, Please open the mysql server.")
    return
  
  mycursor.execute("CREATE DATABASE IF NOT EXISTS HabiTrack")
  mycursor.execute("USE HabiTrack")
  mycursor.execute("""CREATE TABLE IF NOT EXISTS Tracks (
                  trackingID INT PRIMARY KEY,
                  name VARCHAR(50) NOT NULL,
                  address VARCHAR(50) NOT NULL,
                  type VARCHAR(50) NOT NULL,
                  species VARCHAR(50) NOT NULL,
                  numofspecies INT
                  ); """)

def get_species_count():
    query = "SELECT type, SUM(numofspecies) FROM Tracks GROUP BY type"
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

def search(option, value):
  column_map = {
    "Tracking ID": "trackingID",
    "Species Type": "type",
    "Species": "species",
    "No. of Species": "numofspecies",
    "Name": "name",
    "Address": "address"
  }

  actual_column = column_map.get(option, option)

  if actual_column in ["trackingID", "numofspecies"]:
    value = int(value)
  query = f"SELECT * FROM tracks WHERE {actual_column}=%s"
  mycursor.execute(query, (value,))
  result = mycursor.fetchall()
  return result



def delete(trackingID):
  mycursor.execute('DELETE FROM tracks WHERE trackingID=%s', trackingID)
  con.commit()

def update(new_name, new_address, new_type, new_species, new_numofspecies, trackingID):
  mycursor.execute("UPDATE tracks SET name=%s, address=%s, type=%s, species=%s, numofspecies=%s WHERE trackingID=%s", 
                  (new_name, new_address, new_type, new_species, new_numofspecies, trackingID))
  con.commit()


def insert(trackingID, name, address, type, species, numofspecies):
  mycursor.execute('INSERT INTO Tracks (trackingID, name, address, type, species, numofspecies) VALUES (%s, %s, %s, %s, %s, %s)',
                  (trackingID, name, address, type, species, numofspecies))
  con.commit()

def id_exists(trackingID):
  mycursor.execute('SELECT COUNT(*) FROM Tracks WHERE trackingID=%s', trackingID)
  result = mycursor.fetchone()
  return result[0]>0


def fetch_tracks():
  mycursor.execute('SELECT * from tracks')
  result = mycursor.fetchall()
  return result


connect_database()