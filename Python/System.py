import cv2
from fer import FER
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

"Leer imagenes de video en vivo"

vid = cv2.VideoCapture(1)
# Setting up the blob detector
params = cv2.SimpleBlobDetector_Params()

params.filterByInertia
params.minInertiaRatio = 0.6

detector = cv2.SimpleBlobDetector_create(params)

def GetImage():
    while(True):

        grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow("grayFrame",grayFrame)
        res = cv2.waitKey(1)
        # Stop if the user presses "q"
        if res & 0xFF == ord('q'):
            break
    return grayFrame

def TurnOff():
    # When everything is done, release the capture
    vid.release()
    cv2.destroyAllWindows()

def GetEmotion():
    while(True):

        "Obtener el frame de la camara"

        ret, frame = vid.read()
        emotion_detector = FER()
        emotion = emotion_detector.detect_emotions(frame)
        print(emotion)

        if(emotion != []):

            "Poner el rectangulo alrededor de la cara"

            bounding_box = emotion[0]["box"]
            emotions = emotion[0]["emotions"]
            cv2.rectangle(frame, (bounding_box[0], bounding_box[1]), (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),(0, 155, 255), 2, )

            "Escribir la emocion en la imagen"

            emotion_name, score = emotion_detector.top_emotion(frame)

            for index, (emotion_name, score) in enumerate(emotions.items()):
                color = (211, 211, 211) if score < 0.01 else (255, 0, 0)
                emotion_score = "{}: {}".format(emotion_name, "{:.2f}".format(score))

                cv2.putText(frame, emotion_score,
                            (bounding_box[0], bounding_box[1] + bounding_box[3] + 30 + index * 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA, )
        cv2.imshow("Frame", frame)
        res = cv2.waitKey(1)
        # Stop if the user presses "q"
        if res & 0xFF == ord('q'):
            break;

    TurnOff()

GetEmotion()
