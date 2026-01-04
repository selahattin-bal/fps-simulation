# 🎯 FPS Simulation V2

> **Laser-based FPS Simulation using OpenCV & Unreal Engine**
<img width="2306" height="1345" alt="image" src="https://github.com/user-attachments/assets/58ac947d-826c-4a34-94ff-524a9819cbb0" />
<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/bb126606-9229-4ee9-9038-8c2b33196bd4" />

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
│
├── unreal/
│   └── Unreal_Project_Files (External - Google Drive)
│
├── README.md
└── requirements.txt

🎮 Unreal Engine Project Files (Google Drive)

Due to GitHub file size limitations, the Unreal Engine project files are hosted externally.

📁 Unreal Engine Project Folder:
🔗 https://drive.google.com/drive/folders/1oSWNEdQfQLGQxveZTbZg2Ur2jUxgT_uU

⚠️ Download the entire folder and open it using a compatible Unreal Engine version.

🎥 Demo Video

▶️ Watch Project Demo on YouTube:
🔗 https://youtu.be/rLjKV4MCWVc
