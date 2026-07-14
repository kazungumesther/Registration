import sqlite3
from contextlib import contextmanager

DATABASE_NAME = "school.db"

@contextmanager
def get_connection():
   connection = sqlite3.connect(DATABASE_NAME)
   connection.row_factory = sqlite3.Row 
   try:
       yield connection
       connection.commit()
   except Exception as e:
       connection.rollback()
       raise e
   finally:
       connection.close()











