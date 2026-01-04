# 🎯 FPS Simulation V2

> **Laser-based FPS Simulation using OpenCV & Unreal Engine**

A real-time FPS simulation project where **laser gun hits are detected via camera input** and translated into **mouse click events**, enabling interaction with a projected or on-screen Unreal Engine simulation.

---

## 🚀 Project Overview

This project combines **computer vision** and **game engine integration** to create a **realistic laser-based FPS simulation**.

🔹 A camera detects **laser points** in real time using **OpenCV**  
🔹 Detected laser coordinates are converted into **mouse click events**  
🔹 These clicks interact with the **Unreal Engine FPS simulation**  
🔹 The shot is registered exactly at the projected / displayed hit point  

This setup allows physical laser shots to control a digital FPS environment.

---

## 🛠️ Technologies Used

- 🧠 **OpenCV** – Laser point detection & image processing  
- 🎮 **Unreal Engine** – FPS simulation environment  
- 🐍 **Python** – Vision processing & mouse event handling  
- 🖱️ **Mouse Event Triggering** – Real-time interaction bridge  
- 📷 **Camera Input** – Laser tracking source  

---

## 📂 Project Structure

```text
fps-simulation/
│
├── vision/
│   ├── laser_detection.py
│
├── unreal/
│   └── FPS_Project_Files (https://drive.google.com/drive/folders/1oSWNEdQfQLGQxveZTbZg2Ur2jUxgT_uU)
│
├── README.md
└── requirements.txt
