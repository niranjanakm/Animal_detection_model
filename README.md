# 🐾 Animal Detection Model

A Python application that detects animals in images and videos using a custom-trained YOLOv8 model. The application intelligently identifies and highlights carnivorous animals with real-time alerts and counting features.

## ✨ Features

- 🎯 **Multi-animal Detection**: Detect and classify multiple animals per frame
- 🔴 **Carnivore Highlighting**: Automatically highlights detected carnivores (cat, dog, bear)
- 📊 **Animal Counter**: Real-time counting of detected carnivorous animals
- 🚨 **Pop-up Alerts**: Get notified when carnivores are detected
- 🖼️ **Image & Video Support**: Process both static images and video files
- 🎨 **User-Friendly GUI**: Built with Tkinter for easy interaction
- 🚀 **High Performance**: Powered by YOLOv8 for accurate and fast detection

## 🛠️ Tech Stack

- **Python 3.x**: Core programming language
- **YOLOv8**: Custom-trained object detection model
- **OpenCV**: Image and video processing
- **Tkinter**: GUI framework
- **Pillow**: Image manipulation

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- A system with at least 4GB RAM (8GB recommended for video processing)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/niranjanakm/Animal_detection_model.git
cd Animal_detection_model
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
cd animal-detector-app
pip install -r requirements.txt
```

### Dependencies

- `ultralytics>=8.0.0` - YOLOv8 model framework
- `opencv-python` - Image and video processing
- `Pillow` - Image manipulation
- `tk` - GUI framework (usually pre-installed with Python)

## 📖 Usage

### Running the Application

```bash
# From the animal-detector-app directory
python app.py
```

### Using the GUI

1. **Launch the Application**: Run the app using the command above
2. **Load Media**: 
   - Click "Select Image" to analyze a single image
   - Click "Select Video" to analyze a video file
3. **View Results**: The application will display:
   - Detected animals with bounding boxes
   - Highlighted carnivores in red/distinctive color
   - Count of detected carnivores
   - Pop-up alerts for carnivore detections
4. **Save Results**: Option to save detected images/videos with annotations

## 🎓 How It Works

1. **Input Processing**: User selects an image or video file via the GUI
2. **Object Detection**: YOLOv8 model processes the input and identifies animals
3. **Carnivore Classification**: Detected animals are classified; carnivores (cat, dog, bear) are flagged
4. **Highlighting & Alerting**: Carnivores are highlighted with distinctive colors and pop-up alerts trigger
5. **Counting**: Real-time counter tracks the number of carnivores detected
6. **Output**: Annotated results are displayed or saved

## 📁 Project Structure

```
Animal_detection_model/
├── README.md
├── animal-detector-app/
│   ├── app.py                 # Main application file
│   ├── requirements.txt        # Python dependencies
│   ├── models/                # YOLOv8 model files
│   ├── sample_data/           # Sample images/videos for testing
│   └── output/                # Processed results (generated)
```

## 🔧 Configuration

### Modifying Carnivore Detection

Edit the list of carnivorous animals in the application:

```python
CARNIVORES = ['cat', 'dog', 'bear']  # Modify as needed
```

### Adjusting Detection Confidence

```python
confidence_threshold = 0.5  # Adjust between 0-1 (higher = stricter)
```

## 🎯 Example Workflow

```python
# Pseudo-code example
1. Load image/video
2. Run YOLOv8 inference
3. For each detected object:
   - If animal is in CARNIVORES list → Highlight it
   - Increment carnivore counter
   - Trigger alert if threshold exceeded
4. Display/save annotated output
```

## ⚠️ Limitations & Considerations

- Detection accuracy depends on image/video quality
- Performance may vary based on system specifications
- Real-time processing of high-resolution videos requires adequate hardware
- Model trained on specific animal dataset; may not detect all animal species
- Large video files may require significant processing time

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Model not loading | Ensure YOLOv8 is properly installed: `pip install --upgrade ultralytics` |
| GUI not responding | Check system resources; close other applications |
| Low detection accuracy | Ensure good lighting and clear visibility of animals |
| Memory issues with large videos | Process shorter segments or reduce video resolution |

## 📝 License

This project is provided as-is. Please refer to the repository for any specific licensing information.

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs or issues
- Suggest new features
- Submit pull requests with improvements

## 📧 Contact & Support

For questions or support, please open an issue on the [GitHub repository](https://github.com/niranjanakm/Animal_detection_model/issues).

## 🙏 Acknowledgments

- **YOLOv8** by Ultralytics for the powerful object detection framework
- **OpenCV** for comprehensive computer vision tools
- **Tkinter** for the lightweight GUI framework

---

**Happy Detecting! 🐾**

*Last Updated: May 2026*
