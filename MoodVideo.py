from keras.preprocessing.image import img_to_array
import importlib
import imutils
import cv2
from keras.models import load_model
import numpy as np
from DataWriting import *

# Chemin du model de détection facial
detection_model_path = 'model/haarcascade_frontalface_default.xml'
# Chemin du model de prédiction d'humeur
emotion_model_path = 'model/_mini_XCEPTION.66-0.64.hdf5'

# Appel du model haar cascade de détection du visage
face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)
#Listes des émotions existantes dans le dataset
EMOTIONS = ["angry", "disgust", "scared", "happy", "sad", "surprised",
            "neutral"]

EMOTIONS = ["Pas content", "Pas content", "Pas content", "Content", "Pas content", "Pas content",
            "Couci-couca"]


"""
for emotion in EMOTIONS:
    if emotion == "angry" or emotion == "disgust" or emotion == "scared" or emotion == "surprised" or emotion == "sad":
        emotion = "Pas content"
"""

#df = frameReset()

# Lancement de la capture webcam
cv2.namedWindow('Capture du mood')
camera = cv2.VideoCapture(0)
while True:
    frame = camera.read()[1]
    # Lecture de la capture
    frame = imutils.resize(frame, width=400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(90, 90),
                                            flags=cv2.CASCADE_SCALE_IMAGE)

    #canvas = np.zeros((250, 300, 3,), dtype="uint8")
    frameClone = frame.copy()
    if len(faces) > 0:
        faces = sorted(faces, reverse=True,
                       key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = faces
        #Détermination et découpage de la ROI (Region Of Interest)
        #prétraitement de la ROI et soumission à la ROI
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        preds = emotion_classifier.predict(roi)[0]
        emotion_probability = np.max(preds)
        label = EMOTIONS[preds.argmax()]
    else:
        continue

    # Affichage des labels + pourcentages
    for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
        text = "{}: {:.2f}%".format(emotion, prob * 100)
        #text = "{:.2f}%".format(prob * 100)
        w = int(prob * 300)
        #cv2.rectangle(canvas, (7, (i * 35) + 5),
        #     (w, (i * 35) + 35), (0, 255, 0), -1)
        #cv2.putText(canvas, text, (10, (i * 35) + 23),
        #           cv2.FONT_HERSHEY_SIMPLEX, 0.45,
        #            (255, 255, 255), 2)
        #finalText = label + " = " + text
        if label.lower() == "happy":
            label = "Content"
        elif label.lower() == "neutral":
            label = "Couci-Couca"
        elif label.lower() == "angry":
            label = "Pas content"

        cv2.putText(frameClone, label, (fX, fY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
        cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                      (0, 255, 0), 2)

    cv2.imshow('Capture du mood', frameClone)
    #cv2.imshow("Probabilités", canvas)
    #Appuie sur la barre d'espace
    k = cv2.waitKey(1) & 0xFF
    if k == 32:
        realMood = label
        print("Veuillez appuyer la touche 'Y' pour confirmer l'humeur: "+realMood)
    if k == ord('y'):
        frameUpdate(day, realMood)
        #frameUpdate(day, label)
        print("Humeur'"+realMood+"'confirmée pour votre "+day)
    if k == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()