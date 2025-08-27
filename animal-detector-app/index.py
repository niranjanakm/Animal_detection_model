import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import os
from ultralytics import YOLO

# === CONFIGURATION ===
MODEL_PATH = "weights/best.pt"
CARNIVORES = ['cat', 'dog', 'bear']
CLASSES = ['cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe']

# Load model
model = YOLO(MODEL_PATH)

# === GUI SETUP ===
window = tk.Tk()
window.title("Animal Detection Model")
window.geometry("800x600")

panel = tk.Label(window)
panel.pack()

def detect_image(image_path):
    results = model(image_path)
    im = results[0].plot()
    img_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb).resize((700, 500))
    img_tk = ImageTk.PhotoImage(img_pil)

    panel.configure(image=img_tk)
    panel.image = img_tk

    # Carnivore counting
    labels = results[0].boxes.cls.tolist()
    names = results[0].names
    count = sum(1 for label in labels if names[int(label)] in CARNIVORES)

    if count > 0:
        messagebox.showinfo("Carnivores Detected", f"{count} carnivorous animals detected!")

def detect_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        im = results[0].plot()

        im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(im_rgb).resize((700, 500))
        img_tk = ImageTk.PhotoImage(img_pil)

        panel.configure(image=img_tk)
        panel.image = img_tk
        window.update()

        labels = results[0].boxes.cls.tolist()
        names = results[0].names
        count = sum(1 for label in labels if names[int(label)] in CARNIVORES)

        if count > 0:
            messagebox.showinfo("Carnivores Detected", f"{count} carnivorous animals detected!")

    cap.release()

def open_file():
    path = filedialog.askopenfilename()
    if not path:
        return
    ext = os.path.splitext(path)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png']:
        detect_image(path)
    elif ext in ['.mp4', '.avi', '.mov']:
        detect_video(path)
    else:
        messagebox.showerror("Error", "Unsupported file format.")

btn = tk.Button(window, text="Select Image or Video", command=open_file)
btn.pack()

window.mainloop()
