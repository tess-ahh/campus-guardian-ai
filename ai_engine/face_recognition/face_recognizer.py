from ai_engine.face_recognition.face_database import FaceDatabase


class FaceRecognizer:
    def __init__(self):
        self.database = FaceDatabase()

    def load_known_faces(self):
        return self.database.get_known_faces()

    def recognize(self, frame):
        """
        Placeholder for future face recognition.

        Returns:
            List of recognized persons.
        """

        return []