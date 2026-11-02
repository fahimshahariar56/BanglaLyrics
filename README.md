# 🎧 Python Lyrics Player

A simple Python-based lyrics player that plays music and displays synchronized lyrics in the terminal with a dynamic typing effect.

## ✨ Features

* 🎵 Play audio files using Pygame.
* 📝 Display lyrics synchronized with music.
* ⌨️ Character-by-character typing effect.
* ⏱️ Timestamp-based lyric synchronization.
* 💻 Lightweight terminal-based application.
* 🚀 Simple and beginner-friendly Python project.

## 🛠️ Technologies Used

* **Python** – Core programming language.
* **Pygame CE** – Audio playback.
* **Time** – Playback timing and animation.
* **OS** – Operating system utilities.

## 📁 Project Structure

```text
Lyrics/
│
├── main.py
├── song.mp3
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/USERNAME/Lyrics.git
```

### 2. Navigate to the Project

```bash
cd Lyrics
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Add Your Audio File

Place your audio file inside the project directory and name it:

```text
song.mp3
```

### 5. Run the Application

```bash
python main.py
```

## 📦 Requirements

The project uses Pygame CE.

Install manually:

```bash
python -m pip install pygame-ce
```

`requirements.txt`:

```text
pygame-ce
```

## 🧠 How It Works

1. Pygame loads and plays the audio file.
2. Each lyric line has a specific start and end timestamp.
3. The program tracks the current playback time.
4. Lyrics are progressively displayed according to the playback progress.
5. The next lyric appears when its scheduled time arrives.

## 🎯 Learning Objectives

This project demonstrates practical use of:

* Python functions
* Lists and loops
* Conditional statements
* String slicing
* Time-based programming
* External Python libraries
* Audio playback and synchronization

## 🔮 Future Improvements

* GUI-based lyrics player.
* Support for multiple songs.
* Automatic lyrics synchronization.
* Customizable typing speed.
* Background and text customization.
* Better audio format support.

## 👨‍💻 Author

**Shahariar Ahammad Fahim**

CSE Student | Python Learner | Frontend Developer

---

⭐ If you like this project, consider giving it a star!
