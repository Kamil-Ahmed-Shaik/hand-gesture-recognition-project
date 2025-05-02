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
- `Data_source.xlsx` for gesture storage
- Background images: `Back_5.png`, `Back_6.png`, `Back_7.png`

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/gesture-recognition.git
cd gesture-recognition
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🧠 How It Works

### ➕ Gesture Capture (`gesture_capture.py`)
- Press `t` to capture the gesture.
- Press `f` to save it in `Data_source.xlsx`.
- Press `q` to quit without saving.

### 🔍 Gesture Recognition (`gesture_predictor.py`)
- Runs real-time recognition.
- Displays prediction on screen.
- Press `e` to exit.

---

## 📂 Folder Structure

```
gesture-recognition/
├── gesture_capture.py
├── gesture_predictor.py
├── Data_source.xlsx
├── Back_5.png
├── Back_6.png
├── Back_7.png
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

## 📬 Contact

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

