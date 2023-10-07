from typing import List

from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self) -> None:
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []
        
    def add_category(self, category:Category) -> None:
        if category not in self.categories:
            self.categories.append(category)
            
    def add_topic(self, topic:Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)
            
    def add_document(self, document:Document) -> None:
        if document not in self.documents:
            self.documents.append(document)
            
    def edit_category(self, category_id: int, new_name:str) -> None:
        try:
            category = [c for c in self.categories if c.id == category_id][0]
        except IndexError:
            pass
        
        if category.name != new_name:
            category.name = new_name
            
    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        try:
            topic = [t for t in self.topics if t.id == topic_id][0]
        except IndexError:
            pass
        
        if topic.topic != new_topic:
            topic.topic = new_topic
            
        if topic.storage_folder != new_storage_folder:
            topic.storage_folder = new_storage_folder
            
    def edit_document(self, document_id: int, new_file_name: str) -> None:
        try:
            document = [d for d in self.documents if d.id == document_id][0]
        except IndexError:
            pass
        
        if document.file_name != new_file_name:
            document.file_name = new_file_name
            
    def delete_category(self, category_id: int) -> None:
        try:
            category = [c for c in self.categories if c.id == category_id][0]
        except IndexError:
            pass
        
        self.categories.remove(category)
        
    def delete_topic(self, topic_id: int) -> None:
        try:
            topic = [t for t in self.topics if t.id == topic_id][0]
        except IndexError:
            pass
        
        self.topics.remove(topic)
        
    def delete_document(self, document_id: int) -> None:
        try:
            document = [d for d in self.documents if d.id == document_id][0]
        except IndexError:
            pass
        
        self.documents.remove(document)
        
    def get_document(self, document_id: int) -> Document:
        try:
            return [d for d in self.documents if d.id == document_id][0]
        except IndexError:
            pass
        
    def __repr__(self) -> str:
        documents = [str(d) for d in self.documents]
        
        return "\n".join(documents)