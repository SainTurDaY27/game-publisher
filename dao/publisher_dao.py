from model import Publisher


class PublisherDao(object):
    def __init__(self, session):
        self.session = session

    def get_all_publishers(self):
        return self.session.query(Publisher).all()

    def get_publisher_by_id(self, publisher_id):
        return self.session.query(Publisher).filter_by(publisher_id=publisher_id).first()

    def get_publisher_by_name(self, publisher_name):
        return self.session.query(Publisher).filter_by(publisher_name=publisher_name).first()

    def update_publisher_data(self, publisher_id, publisher_name):
        publisher = self.session.query(Publisher).filter_by(publisher_id=publisher_id).first()
        publisher.publisher_name = publisher_name
        self.session.commit()

    def add_publisher_data(self, publisher_name):
        publisher = Publisher(publisher_name)
        self.session.add(publisher)
        self.session.commit()

    def remove_publisher_by_id(self, publisher_id):
        publisher = self.session.query(Publisher).filter_by(publisher_id=publisher_id).first()
        self.session.delete(publisher)
        self.session.commit()

    def remove_publisher_by_name(self, publisher_name):
        publisher = self.session.query(Publisher).filter_by(publisher_name=publisher_name).first()
        self.session.delete(publisher)
        self.session.commit()


