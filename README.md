# hand-gesture-recognition-project
Real-time hand gesture recognition with OpenCV, MediaPipe, and scikit-learn

This is a real-time hand gesture recognition system using OpenCV, MediaPipe, scikit-learn, and CVZone. It allows you to **add new gestures** and then **recognize them** using a trained logistic regression model.

---

## 📁 Features

- Live gesture capture using webcam
- Feature extraction based on hand landmark distances
- Custom gesture labeling and storage in Excel
- Gesture classification using scikit-learn's Logistic Regression
- User interface with overlay images

---

## 🛠 Requirements

- Python 3.9 (recommended)
- Webcam
---

## 📦 Installation

```bash
git clone https://github.com/Kamil-Ahmed-Shaik/hand-gesture-recognition-project.git
cd hand-gesture-recognition-project
pip install -r requirements.txt
python add_gesture.py  ##To add gesture(Creates the Data_source.xlsx file and model_filename.pkl at the beginning)
python recognise_gesture.py
```

---

## 🧠 How It Works

### ➕ Gesture Capture (`add_gesture.py`)
- Press `t` to capture the gesture.
- Press `f` to save it in `Data_source.xlsx`.
- Press `q` to quit without saving.

### 🔍 Gesture Recognition (`recognise_gesture.py`)
- Runs real-time recognition.
- Displays prediction on screen.
- Press `e` to exit.

---

## 📂 Folder Structure

```
hand-gesture-recognition-project/
├── recognise_gesture.py
├── Data_source.xlsx
├── Back_5.png
├── Back_6.png
├── Back_7.png
├── add_gesture.py
├── model_filename.pkl
├── requirements.txt
└── README.md
```

---

## 📋 Dependencies with Versions

```text
cvzone==1.6.1
opencv-python==4.11.0
mediapipe==0.10.9
openpyxl==3.1.5
pandas==2.2.3
numpy==1.23.3
scikit-learn==1.1.2
joblib==1.4.2
```

---

## 🚀 Future Improvements

- Multi-hand gesture recognition
- Enhanced accuracy using deep learning
- Export to ONNX or TFLite for mobile inference

---

## 📬 Process flow

-Install all the Dependencies using the command "pip install -r requirements.txt"
-It is required to add the hand gestures(execution of add_gesture.py) before performing the recognition task(execution of recognise_gesture.py)
-The Repository does not contain Data_source.xlsx and model_filename.pkl files  at beginning,But the are generated during the execution of add_gesture.py



