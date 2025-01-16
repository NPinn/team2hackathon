import chromadb


class ChromaDB:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="database/chroma.db",
        )
        self.medical_clerking = self.client.get_or_create_collection(
            name="medical_clerking",
        )
        self.discharge_note = self.client.get_or_create_collection(
            name="discharge_note",
        )
