import sqlite3

conn = sqlite3.connect('gesture_db.db')
print ("Opened database successfully");

'''conn.execute("update gesture set g_name='Hi' where g_id=42")'''
cursor = conn.execute("SELECT g_id, g_name from gesture")

for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])

print ("Operation done successfully");
conn.close()
