import os
from datetime import datetime
from werkzeug.utils import secure_filename



def imagePathCoder(image):
    if image:

        ext = os.path.splitext(image.filename)[1]
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = secure_filename(f"{timestamp}{ext}")

        image_path = os.path.join("static", "image", filename)
        return image_path
