# ⚽ Pitch-Vision

## 📌 Introduction

**Pitch-Vision** is a computer vision-based football analysis tool that uses state-of-the-art deep learning techniques to detect and track players, referees, and the ball from match footage. It also classifies players into teams using KMeans clustering based on jersey color and measures player movement using optical flow and perspective transformation. The final output includes the player's speed, distance covered, and team ball possession statistics.

This project integrates concepts from object detection, clustering, optical flow, and geometric transformations, making it ideal for both beginners and experienced ML engineers looking to explore sports analytics.

---

## 📸 Output Screenshot

![Output Screenshot](screenshot.png)

---

## 🧠 Modules Used

- **YOLO (You Only Look Once)** – Object detection for players, ball, and referee.
- **KMeans Clustering** – For classifying players into teams based on jersey colors.
- **Optical Flow** – To estimate camera movement and isolate actual player motion.
- **Perspective Transformation** – Converts image coordinates to real-world coordinates to calculate distances accurately.
- **Speed & Distance Calculation** – Computes each player’s speed (m/s) and distance covered (meters).

---

## 🏋️ Trained Models

- ✅ YOLOv5/YOLOv8 custom trained weights (`best.pt`, `last.pt`)
- 🎞️ Sample input/output videos available in the repository

---

## Requirements

Make sure you have the following installed:

- Python 3.x
- [ultralytics](https://pypi.org/project/ultralytics/) – for YOLOv8
- [supervision](https://pypi.org/project/supervision/) – for video annotation
- [OpenCV](https://pypi.org/project/opencv-python/) – for image processing
- [NumPy](https://pypi.org/project/numpy/) – for numerical computation
- [Matplotlib](https://pypi.org/project/matplotlib/) – for data visualization
- [Pandas](https://pypi.org/project/pandas/) – for data analysis

You can install them using:

```bash
pip install ultralytics supervision opencv-python numpy matplotlib pandas
```

## How to Run
1. Clone the repository:

```bash
git clone https://github.com/AbhiKunkal/Pitch-Vision.git
cd Pitch-Vision
```
2. Place your input video in the project directory.

3. Run the main script:

```bash
python main.py
```

4. View the output video and stats.

## ✨ Features
✅ Real-time player, referee, and ball detection

🎯 Automatic team classification via color clustering

📈 Ball possession analysis

🏃 Speed and distance metrics for each player

🖼️ Annotated visualizations on the match video

## 📊 Future Scope
⏱️ Live match analysis integration

📊 Interactive analytics dashboards

🌡️ Heatmaps and player movement zones

🧠 Integration with match scoreboard APIs

## 🙌 Contributing

Feel free to fork this repo, make improvements, and raise PRs. Let's build something awesome for the campus community!

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

## 👤 Author

**Abhishek Kumar**  
[GitHub: AbhiKunkal](https://github.com/AbhiKunkal)



