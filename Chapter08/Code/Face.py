import face_recognition as fr
import os

class Face:
    def __init__(self, faces_dir):
        self.faces = {}
        for root, dirs, filenames in os.walk(faces_dir):
            for filename in filenames:
                image = fr.load_image_file(faces_dir + "/" + filename)
                face_encodings = fr.face_encodings(image) 
                if len(face_encodings)==1:
                    self.faces[filename.split(".")[0]] = face_encodings
                        
    def get_name(self, source, source_type="file"):
        
        if source_type=="file":
            image = fr.load_image_file(source)
            unknown_face = fr.face_encodings(image)
        else:
            unknown_face = fr.face_encodings(source)
            
        if len(unknown_face) != 1:
            return None
        
        for face_name, face in self.faces.items():
            match = fr.compare_faces([face][0], unknown_face[0], 0.5)
            if match[0]:
                return face_name      
        return "Unknown Person"

