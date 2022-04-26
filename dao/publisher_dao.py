class PublisherDao(object):
    def __init__(self, session):
        self.session = session

    def get_all_publishers(self):
        self.session.execute("SELECT * FROM publisher_data")
        return self.session.fetchall()

    def get_publisher_by_id(self, publisher_id):
        self.session.execute("SELECT * FROM publisher_data WHERE publisher_id = %s", (publisher_id,))
        return self.session.fetchone()

    def get_publisher_by_name(self, publisher_name):
        self.session.execute("SELECT * FROM publisher_data WHERE publisher_name = %s", (publisher_name,))
        return self.session.fetchone()

    def update_publisher_data(self, publisher_id, publisher_name):
        self.session.execute("UPDATE publisher_data SET publisher_name = %s WHERE publisher_id = %s", (publisher_name, publisher_id))
        self.session.commit()













