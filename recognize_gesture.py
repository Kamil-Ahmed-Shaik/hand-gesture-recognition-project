import pandas as pd
import cv2
import numpy as np
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
from sklearn.linear_model import LogisticRegression
import joblib
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load dataset
print("reached before path")
path = "Data_source.xlsx"
df = pd.read_excel(path, sheet_name='Sheet', header=None)
tt = 24
print("Reached after tt")
labels = [i for i in df.iloc[:, tt].unique()]
lab = {j: labels[j] for j in range(len(labels))}
lab1 = {labels[j]: j for j in range(len(labels))}
y = np.array([lab1[i] for i in df.iloc[:, tt].values])
x = df.iloc[:, :tt].values

# Distance and feature extraction
def dist(x, y):
    return ((x[1] - y[1])**2 + (x[2] - y[2])**2)**0.5 / 1000

def fun(a):
    ini = a[0]
    dis = a[1:]
    result = []
    for i in dis:
        if i[0] not in [1, 2, 5, 9, 13, 17]:
            dip = dist(i, ini)
            result.append(dip)
    lst = [4, 8, 12, 16, 20]
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            result.append(dist(a[lst[i]], a[lst[j]]))
    return result

# UI Assets
back_ground = cv2.resize(cv2.imread("Back_5.png"), (1100, 650))
repeat_ing = cv2.imread("Back_6.png")
repeat_ing2 = cv2.imread("Back_7.png")
detector = HandDetector(maxHands=1)

# Model setup
model = LogisticRegression(multi_class='multinomial')
model.fit(x, y)
joblib.dump(model, 'model_filename.pkl')
model = joblib.load('model_filename.pkl')

# Camera and MediaPipe
cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils

print("Press 'e' to exit")

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    hand_s, img_s = detector.findHands(img)

    # Top bar update
    back_ground[395:480, 640:1040] = cv2.resize(repeat_ing, (400, 85))

    if hand_s:
        hand_s = hand_s[0]
        x_box, y_box, w_box, h_box = hand_s['bbox']
        h_img, w_img, _ = img_s.shape
        x1 = max(x_box - 20, 0)
        y1 = max(y_box - 10, 0)
        x2 = min(x_box + w_box + 20, w_img)
        y2 = min(y_box + h_box + 10, h_img)
        try:
            cropped_hand = img_s[y1:y2, x1:x2]
            back_ground[135:350, 635:1040] = cv2.resize(cropped_hand, (1040 - 635, 350 - 135))
        except:
            pass
    else:
        back_ground[135:350, 630:1050] = cv2.resize(repeat_ing2, (1050 - 630, 350 - 135))

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            temp = [[id, int(lm.x * img.shape[1]), int(lm.y * img.shape[0])] for id, lm in enumerate(handLms.landmark)]
            try:
                input_data = [fun(temp)]
                pred_index = model.predict(input_data)[0]
                prediction = lab[pred_index]
                cv2.putText(back_ground, prediction, (660, 450), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 0, 0), 2)
            except Exception as e:
                print("Prediction error:", e)
            mpdraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)

    # Insert main cam view
    back_ground[135:520, 35:565] = cv2.resize(img, (530, 385))
    cv2.imshow("IMG2:", back_ground)

    if cv2.waitKey(1) == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
