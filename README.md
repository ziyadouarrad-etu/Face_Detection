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
- haarcascade_frontalface_default.xml in the same folder as your script (detection.py).

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

## 📁 Project Structure

```
face-detection/
│
├── detection.py                         # Main Python script
├── haarcascade_frontalface_default.xml  # Haar cascade model
├── myenv/                               # Virtual environment
└── README.md                            # Project documentation
```

---

## 📸 Demo

<img width="800" height="449" alt="Me and my friend with green rectangles around our faces." src="https://github.com/user-attachments/assets/efda927d-ee78-4377-b2e0-f8a73a29a4f8" />

---

## 🧑‍💻 Author

**Ziyad Ouarrad**  
GitHub: [https://github.com/Ziyadouarrad-etu](https://github.com/Ziyadouarrad-etu)

---

