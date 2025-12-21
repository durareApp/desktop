<p align="center">
  <img src="https://github.com/user-attachments/assets/13284f01-93cf-4524-a9f1-76cc79afab3e" width="90" alt="Durare Logo"/>
</p>

<h1 align="center">Durare – AI Workout Counter (Desktop)</h1>

<p align="center">
  <b>AI-powered desktop fitness assistant using real-time computer vision</b><br/>
  Built with Python, OpenCV & MediaPipe
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows%2010%2F11-blue"/>
  <img src="https://img.shields.io/badge/Python-3.10-success"/>
  <img src="https://img.shields.io/badge/MediaPipe-Pose-orange"/>
  <img src="https://img.shields.io/badge/Status-Active-green"/>
  <img src="https://img.shields.io/github/license/durareApp/desktop"/>
</p>

---

## 🔥 About Durare (Desktop)

**Durare Desktop** is an AI-based workout tracking system that uses your **webcam** to automatically detect and count exercises in real time.

Instead of wearables or manual input, Durare leverages **pose estimation** and **motion logic** to track reps accurately.

This repository serves as the **central desktop hub**, where:
- Each workout has its **own dedicated folder**
- Users can run workouts individually
- A future `main.py` will act as a **central workout controller**

---

## 🏋️ Supported Workouts

### 🧗 Chin-Up / Pull-Up Counter
📁 `pull-up/`

- Real-time chin-up & pull-up detection
- Uses MediaPipe Pose landmarks
- Smart `UP` / `DOWN` state tracking
- Wrist-based virtual bar reference
- Accurate rep counting with offset tolerance
- Live OpenCV overlay

More workouts coming soon 👇

---

## 📂 Repository Structure

    desktop/
    │
    ├── pull-up/
    │   ├── pull-up.py        # Chin-up / Pull-up workout logic
    │   ├── README.md         # Workout-specific documentation
    │
    ├── push-up/              # (Planned)
    │   ├── push-up.py
    │
    ├── squat/                # (Planned)
    │   ├── squat.py
    │
    ├── main.py               # (Planned) Central workout selector
    │
    └── README.md             # This file

---

## 📥 Download (EXE)

You can download standalone Windows executables from the Releases section.

💡 Python is NOT required to run the EXE files. <p align="right"> <a href="https://github.com/durareApp/desktop/releases"> <img src="https://img.shields.io/badge/Download-EXE-black?style=for-the-badge&logo=windows"/> </a> </p>

---

## ⚙️ How It Works

 - Webcam captures live video feed

 - MediaPipe extracts body landmarks

 - Exercise-specific logic analyzes movement

 - Valid rep cycles are detected

 - Counter updates in real time

 - Each workout module defines its own rules, thresholds, and states.

---

## 🧠 Tech Stack

| Component	| Technology |
|-----------|------------|
| Language |	Python 3.10|
Computer Vision	| OpenCV
Pose Estimation	| MediaPipe
Packaging	| PyInstaller
Platform	| Windows Desktop

---

## 🖥️ Running From Source (Developers)

    git clone https://github.com/durareApp/desktop.git
    cd desktop
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python pull-up/pull-up.py

---

## ⚠️ Important Notes

 - Windows 10 / 11 (64-bit) only

 - First EXE launch may take 5–15 seconds

 - Camera permission must be enabled

 - Antivirus warnings may appear (unsigned EXE)

---

## 📜 License

This project is licensed under the GPL-3.0 License.

---

## 🤝 Contributions

Durare is an evolving AI fitness project.
Ideas, issues, and contributions are welcome.

If you find this useful, consider ⭐ starring the repo.

<p align="center"> <b>Durare — Build strength with intelligence.</b> </p>

