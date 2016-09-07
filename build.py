from model import *

def table_magic():
    ConnectDatabase.db.connect()
    # ConnectDatabase.db.drop_tables([UserStory], safe=True)
    ConnectDatabase.db.create_tables([UserStory], safe=True)