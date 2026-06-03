from pathlib import Path


class FaceDatabase:
    def __init__(self):
        self.faces_dir = Path(
            "data/known_faces"
        )

        self.faces_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def get_known_faces(self):
        return list(
            self.faces_dir.glob("*")
        )