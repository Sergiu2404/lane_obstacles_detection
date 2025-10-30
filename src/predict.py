from PIL import Image
from numpy.f2py.crackfortran import verbose
from ultralytics import YOLO
import cv2

model = YOLO("D:\\Programming\\projects\\computer_vision\\object_detection\\training\\runs\\detect\\train\\weights\\best.pt")

results = model.predict(
    source="D:\\Programming\\projects\\computer_vision\\test_pothole_detection\\drum-groapa.jpg",
    show=True, # display frames live
    save=True,
    conf=0.3, # min confidence threshold
    verbose=True
)

# only for image
for r in results:
    im_array = r.plot()  # get BGR numpy array with boxes
    im = Image.fromarray(im_array[..., ::-1])  # convert BGR to RGB for PIL
    im.show()  # opens a window; stays open until you close manually