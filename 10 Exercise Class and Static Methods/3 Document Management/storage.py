class Storage:
    def __init__(self):
        self.category = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.category:
            self.category.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [el for el in self.category if el.id == category_id]
        category = category[0]
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [el for el in self.topics if el.id == topic_id]
        topic = topic[0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = [el for el in self.documents if document_id == el.id]
        document = document[0]
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = [el for el in self.category if el.id == category_id]
        category = category[0]
        self.category.remove(category)

    def delete_topic(self, topic_id):
        topic = [el for el in self.topics if el.id == topic_id]
        topic = topic[0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [el for el in self.documents if document_id == el.id]
        document = document[0]
        self.documents.remove(document)

    def get_document(self, document_id):
        document = [el for el in self.documents if document_id == el.id]
        document = document[0]
        result = document.__repr__()
        print(result)
        return result

    def __repr__(self):
        documents = '\n'.join([c.__repr__() for c in self.documents])
        return documents


