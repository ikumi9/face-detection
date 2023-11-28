import pymongo
from pymongo.database import Database
from pymongo.collection import Collection

class MongoDBConnection:
    def __init__(self, host: str, port: int, database_name: str):
        self.client: pymongo.MongoClient = pymongo.MongoClient(host, port)
        self.database: Database = self.client[database_name]

    def get_collection(self, collection_name: str) -> Collection:
        return self.database[collection_name]
    

    def close_connection(self):
        self.client.close()

if __name__ == "__main__":
    # Usage example
    connection = MongoDBConnection("localhost", 27017, "image_tracking_db")
    image_collection = connection.get_collection("images")

    # Perform MongoDB operations
    image_data = {"timestamp": "20230912093000", "file_path": "/path/to/image.jpg"}
    image_collection.insert_one(image_data)

    # Close the MongoDB connection
    connection.close_connection()
