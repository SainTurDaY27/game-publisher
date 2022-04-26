class PublisherDao(object):
    def __init__(self, db):
        self.db = db
        self.cursor = self.db.cursor()

    def get_all_publishers(self):
        self.cursor.execute("SELECT * FROM publisher_data")
        return self.cursor.fetchall()

    def get_publisher_by_id(self, publisher_id):
        self.cursor.execute("SELECT * FROM publisher_data WHERE publisher_id = %s", (publisher_id,))
        return self.cursor.fetchone()

    def get_publisher_by_name(self, publisher_name):
        self.cursor.execute("SELECT * FROM publisher_data WHERE publisher_name = %s", (publisher_name,))
        return self.cursor.fetchone()











