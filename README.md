# 🎹 KeyPaw Piano

A piano that lives in your keyboard. Press keys to play notes. No extra hardware needed - just your typing fingers.

## 📝 Description

`KeyPaw` turns your keyboard into a musical instrument. Now with 12 notes, sharps, and two octaves!

### Features:
- 🎵 12 notes (including sharps)
- ⌨️ Uses your keyboard as input
- 🔊 No `.wav` files - sound generated with musicpy
- 🐱 Zero musical talent required

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd KeyPaw
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

```bash
python keypaw.py
```

### Controls

#### Main octave:

| Key | Note |
| --- | --- |
| 1   | Do  |
| 2   | Re  |
| 3   | Mi  |
| 4   | Fa  |
| 5   | Sol |
| 6   | Lja |
| 7   | Si  |

#### Higher octave:

| Key | Note |
| --- | --- |
| q   | Do  |
| w   | Re  |
| e   | Mi  |
| r   | Fa  |
| t   | Sol |
| y   | Lja |
| u   | Si  |

#### Sharps (black keys):

| Key | Note |
| --- | --- |
| Shift+1 | Do# |
| Shift+2 | Re# |
| Shift+4 | Fa# |
| Shift+5 | Sol# |
| Shift+6 | Lja# |

## 🎵 Play something

Try these simple tabs! 
* **Spaces** mean short pauses.
* **Dashes (`-`)** mean holding the note a bit longer.

```text
1 1 5 5 6 6 5  (Twinkle Twinkle Little Star)
```

Or this:

### 🎂 Happy Birthday
```text
1 1 2 1 4 3 - 1 1 2 1 5 4 - 1 1 7 5 4 3 2 - 6 6 5 4 5 4
```

## ⚠️ Known Issues

Arrows and special keys may also trigger sounds. This is not a bug, it's a feature. Your keyboard is just very musical.

## 👤 Author
- **FelineFantasy**
- **License**: MIT
