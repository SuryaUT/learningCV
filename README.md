# LearningCV — Messing Around with Computer Vision (OpenCV + MediaPipe)

This repository contains a collection of computer vision projects built using **Python**, **OpenCV**, and **MediaPipe**.  
The goal of this repo is to learn and implement core CV techniques through hands-on scripts, working step-by-step from the basics to modern, real-time AI-driven models.

# 📚 Project Overview

This repository covers multiple computer vision concepts:

### ✔ Basic Image Processing  
- Loading & saving images  
- Resizing  
- Grayscale, blur, edge detection  
- Drawing shapes/text  
- Image rotation, flipping, and transformations  

### ✔ Webcam + Video I/O  
- Capturing webcam frames  
- Displaying frames  
- Saving processed video to `.mp4`  
- Adjusting FPS, frame size  
- Working with `cv2.VideoWriter`  

### ✔ Hand Tracking (MediaPipe Hands)  
- Real-time hand + finger tracking  
- Landmark extraction (21 keypoints)  
- Finger joint visualization  
- Foundation for gesture recognition

### ✔ Face Detection (Haar Cascades)  
- Detecting faces using Haar cascade XML models  
- Drawing facial bounding boxes  
- Detecting smiles and eyes  
- ROI extraction & processing

### ✔ Face Detection + Face Mesh (MediaPipe)  
- Modern neural-based face detection  
- 468-point facial landmark mesh  
- Real-time detection + tracking  
- Keypoint/mesh visualization  
- Mode switching between detection & mesh  
- Saving mesh videos to the `assets/` folder

---

## 🙌 Credits

A large portion of the conceptual learning roadmap for this repository was inspired by  
**Sam Westby's OpenCV Python Tutorial Series**:  
🔗 https://github.com/samwestby/OpenCV-Python-Tutorial  

Special thanks to **Sam Westby** (GitHub: [samwestby](https://github.com/samwestby))  
for the structured guidance and foundational material that informed the overall progression  
of this computer vision learning project.
