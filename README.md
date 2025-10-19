# 👁️ Real-Time Face Detection with OpenCV

A Python project that detects faces from your **webcam** in real time using **OpenCV** and **Haar Cascade Classifiers**.  
This project demonstrates basic computer vision and live webcam processing using Python.

---

## 🚀 Features

- Real-time face detection using your webcam  
- Highlights detected faces with green rectangles  
- Lightweight and easy to run  
- Works completely offline using Haar Cascade model

---

## 🧰 Requirements

- Python 3.x  
- OpenCV library (`opencv-python`)  

Install OpenCV via pip:

```bash
pip install opencv-python
```

---

## ⚙️ Setup (Virtual Environment Recommended)

1. Open **PowerShell** or **Command Prompt** in your project folder.
2. Create a virtual environment named `myenv`:

```powershell
python -m venv myenv
```

3. Activate the virtual environment:

**PowerShell:**
```powershell
.\myenv\Scripts\activate
```

**Command Prompt:**
```cmd
myenv\Scripts\activate.bat
```

4. Upgrade pip and install dependencies:

```bash
pip install --upgrade pip
pip install opencv-python
```

---

## 💻 Usage

1. Make sure your webcam is connected.  
2. Run the face detection script:

```bash
python face_detect.py
```

3. The webcam window will open. Faces will be detected and highlighted in green rectangles.  
4. Press **q** to exit the program.

---

## 🧠 How It Works

1. OpenCV accesses the webcam and reads frames continuously.  
2. Each frame is converted to **grayscale**.  
3. Haar Cascade classifier (`haarcascade_frontalface_default.xml`) detects faces.  
4. Rectangles are drawn around detected faces.  
5. The live video feed with face detection is displayed.

---

## 📄 Example Code Snippet

```python
import cv2

# Load Haar Cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Access webcam
webcam = cv2.VideoCapture(0)

while True:
    success, frame = webcam.read()
    if not success:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
print("Code Completed!")
```

---

## 📁 Project Structure

```
face-detection/
│
├── face_detect.py                       # Main Python script
├── haarcascade_frontalface_default.xml  # Haar cascade model
├── myenv/                               # Virtual environment
└── README.md                            # Project documentation
```

---

## 📸 Demo

*(Add screenshots or a short GIF here showing face detection in action)*

---

## 🧑‍💻 Author

**PoPolo**  
GitHub: [https://github.com/<your-username>](https://github.com/<your-username>)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and share.

