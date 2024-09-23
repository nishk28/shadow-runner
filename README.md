# Shadow Runner Game

Shadow Runner is a horizontal scrolling game where the player navigates through various obstacles and challenges in a dark-themed environment. The goal is to reach the finish line without hitting any obstacles, while collecting the best score based on time.

## Project Structure
The project is made using PyQt5 for GUI in Python, HTML/CSS/JavaScript for the game interface, and Bootstrap for styling. It consists of the following key files:

- **`app.py`**: Main Python script to launch the game using PyQt5.
- **`index.html`**: Contains the HTML structure of the game, including the layout and game screens.
- **`style.css`**: Defines the game's visual design, animations, and responsive elements.
- **`script.js`**: Handles game mechanics, including obstacle movement, player interaction, and scoring.

### app.py
The `app.py` file initializes a PyQt5 window to display the local HTML game using the `QWebEngineView` widget. It loads the `index.html` file and sets the window title.

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'index.html'))

        if not os.path.exists(file_path):
            print(f"Error: {file_path} does not exist.")
            sys.exit()

        self.browser.setUrl(QUrl.fromLocalFile(file_path))
        self.setCentralWidget(self.browser)
        self.setWindowTitle('Shadow Runner')
        self.showMaximized()
```

### index.html
The `index.html` file contains the core structure for the game UI. It has different screens such as "Start Screen," "Game Over," and "Win" screens. The game uses various elements like images, text, and buttons to create the gaming experience.

```html
<body>
    <div class="start screen">
        <div class="main-title row d-flex justify-content-center align-items-center">
            <h1>Scroll Game: Dark Run</h1>
            <p>Scroll to Start</p>
        </div>
    </div>
    <div id="gameContainer">
        <div id="left-wall"></div>
        <div id="hero"></div>
        <div class="obstacles"></div>
        <div class="finish-line"></div>
    </div>
    <div class="game-over screen">Game Over</div>
</body>
```

### style.css
The `style.css` file provides the styling for the game. It controls the animations, obstacle design, and overall game aesthetics, such as a scrolling background and character animations.

Key elements include:
- **Hero**: Controls player animation, movement, and idle states.
- **Obstacles**: Defines obstacle animation like hammers and saws moving up and down.
- **Background**: Implements the game’s background, which scrolls as the player progresses.

```css
#hero {
    position: fixed;
    width: 32px;
    height: 44px;
    top: calc(50% + 200px);
    left: 10%;
}
@keyframes runRight {
    from { background-position: 0 0; }
    to { background-position: -192px 0; }
}
```

### script.js
This JavaScript file manages the game logic, including player movements, scrolling interaction, timer, and game state transitions. It also handles collisions and winning conditions.

Key Features:
- **Hero State Management**: The hero character changes states (e.g., idle, running, jumping) based on player input.
- **Collision Detection**: Checks for collisions between the player and obstacles.
- **Timer**: Tracks the time it takes for the player to complete the level.
  
```javascript
$(document).ready(function () {
    function handleScroll(scrollDirection) {
        $(".obstacle, .bush, .floor, .object").each(function () {
            const left = parseInt($(this).css("left"));
            $(this).css("left", left - scrollDirection * scrollSpeed + "px");
        });
        checkCollision();
    }
});
```

## How to Run

### Prerequisites
- Python 3.x
- PyQt5 library: Install using `pip install PyQt5`.
- WebEngine for PyQt5: Install using `pip install PyQtWebEngine`.

### Commands to Run the Game
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/shadow-runner-game.git
   cd shadow-runner-game
   ```

2. Install the dependencies:
   ```bash
   pip install PyQt5 PyQtWebEngine
   ```

3. Run the game:
   ```bash
   python app.py
   ```
