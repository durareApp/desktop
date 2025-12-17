<p align="center">
  <img src="https://raw.githubusercontent.com/durareApp/.github/main/assets/durare-logo.png" width="80" alt="Durare Logo"/>
</p>

<h1 align="center">Durare – AI Pull-Up / Chin-Up Counter 🧗</h1>

<p align="center">
  <b>Real-time pull-up and chin-up counter using computer vision</b><br/>
  Powered by Python, OpenCV & MediaPipe
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Workout-Pull--Up%20%2F%20Chin--Up-orange"/>
  <img src="https://img.shields.io/badge/Platform-Windows%2010%2F11-blue"/>
  <img src="https://img.shields.io/badge/Python-3.10-success"/>
  <img src="https://img.shields.io/badge/MediaPipe-Pose-green"/>
</p>

---

## 🔥 Overview

This module is part of the **Durare Desktop** project and provides an **AI-based pull-up / chin-up counter** that works in real time using a webcam.

The system uses **pose estimation** to track body landmarks and counts repetitions automatically—no wearables, no manual input.

This folder contains **only the logic for pull-ups**, making it modular and easy to extend or integrate into a unified workout system.

---

## 🧠 How It Works

1. Webcam captures live video
2. MediaPipe Pose detects body landmarks
3. A virtual horizontal reference line is calculated using wrist positions
4. The nose landmark is tracked relative to this line
5. A rep is counted when:
   - Nose moves above the bar → `UP`
   - Returns below the bar → `DOWN`
6. State-based logic prevents false counts

---

## ✨ Features

- Real-time pose detection using **MediaPipe Pose**
- Automatic pull-up & chin-up counting
- Smart `UP` / `DOWN` state machine
- Wrist-based virtual bar reference
- Offset tolerance to reduce noise
- Live OpenCV visual overlay
- Minimal false positives
- Runs fully offline

---

## 📂 Files in This Folder

    pull-up/
    ├── pull-up.py      # Pull-up / chin-up detection logic
    └── README.md       # This documentation

---

## ▶️ Run From Source
### Requirements

 - Windows 10 / 11 (64-bit)

 - Python 3.10

 - Webcam

### Setup & Run

    cd pull-up
    python -m venv venv
    venv\Scripts\activate
    pip install opencv-python mediapipe numpy
    python pull-up.py

---

## 📥 Download (EXE)

A standalone Windows executable is available in the Releases section of the main repository.

💡 Python is not required to run the EXE.

<p align="center"> <a href="https://github.com/durareApp/desktop/releases"> <img src="https://img.shields.io/badge/Download-EXE-black?style=for-the-badge&logo=windows"/> </a> </p>

---

## ⚠️ Notes

 - First EXE launch may take a few seconds

 - Camera permission must be enabled

 - Antivirus warnings may appear (unsigned EXE)

 - Lighting conditions can affect accuracy

---

## 📜 License

This module is licensed under the GPL-3.0 License

<p align="center"> <b>Durare — Precision training powered by AI.</b> </p>

