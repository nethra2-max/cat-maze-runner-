import tkinter as tk
from PIL import Image, ImageTk

TILE = 40
ROWS = 20
COLS = 40
WIDTH = COLS * TILE
HEIGHT = ROWS * TILE
UNLOCKED_LEVELS = 1

LEVELS = [
    {
        "maze": [
            "1111111111111111111111111111111111111111",
            "1000000000000000000111100001110000000011",
            "1011111110111111110111101111110111111011",
            "1001000010100000110110000000000111111011",
            "1111011010101110110110111111100000011011",
            "1000011010100010110110100000001111011011",
            "1011011010111010110110101011111111011011",
            "1010010010000010110110101000000000011011",
            "1011111011111010110110001111111111011011",
            "1000001000001010000111111111100000011011",
            "1011101011101011110111110000001111111011",
            "1010000010001010000111110111111000000011",
            "1011111110111010111111100111111011011111",
            "1000000000000010000000001111111011011111",
            "1111101111111111101111110000000011011111",
            "1111101001111111101000000111101111011111",
            "1000001101000000000011111111000000000011",
            "1011111101011111111000000011011111111111",
            "1000000000011111111111111000000000000000",
            "1111111111111111111111111111111111111111",
        ],
        "time": 60,
        "speed": 200,
        "obstacles": [
            [3, 5, 1], [7, 10, -1], [9, 3, 1],
            [3, 14, -1], [7, 35, 1], [15, 18, 1],
            [3, 20, -1], [15, 20, -1],
            [16, 35, -1], [13, 4, -1],
            [16, 15, -1], [9, 13, -1], [11, 30, 1]
        ]
    },
    {
        "maze": [
            "1111111111111111111111111111111111111111",
            "1000001000000100000100000100000100000011",
            "1011101011110101110101110101110101111011",
            "1010001000010100010100010100010100011011",
            "1010111010111101010111010111010111011011",
            "1010001000100001010001010001010001011011",
            "1010111010111101010111010111010111011011",
            "1010100010000101010001010001010001011011",
            "1010101110111101010111010111010111011011",
            "1010101000100001010001010001010001011011",
            "1010101010111101010111010111010111011011",
            "1010101010000101010001010001010001011011",
            "1010101010111101010111010111010111011011",
            "1010001010000101000001010001010000011011",
            "1010111010111101011111010111010111111011",
            "1010001000100001010000010100010110000011",
            "1011111010111111011111010111010110111011",
            "1000000010000000000000010000010000111011",
            "1111111111111111111111111111111111111000",  
            "1111111111111111111111111111111111111111",
        ] + ["1"*40]*11,
        "time": 60,
        "speed": 120,
        "obstacles": [
            [3, 8, 1],       
            [4, 12, "v1"],   
            [5, 20, -1],     
            [5, 25, 1],[9, 25, 1],[13 , 25, 1],  
            [8, 14, "v1"],
            [10, 30, "v1"],
            [13, 16, "v-1"],[5,4,1],
            [15,7,"v1"],
            [15, 22, 1]
        ]
    },
    {
        "maze": [
           
            "1111111111111111111111111111111111111111",
            "1000000000000000011111000001110000000011",
            "1011111110111111011111011111110111111011",
            "1001000010100000011110000000000111111011",
            "1111011010101111011110111111100000011011",
            "1000011010100010011110100000001111011011",
            "1011011010111011010000101011111111011011",
            "1010010010000010010111101000000000011011",
            "1011111011111011010000001111111111011011",
            "1000001000001010011111011111100000011011",
            "1011101011101011011111010000001111111011",
            "1010000010001010011100000111111000000011",
            "1011111110111011011101111111111011011111",
            "1000000000000010000001111111111011011111",
            "1111101111111111101111110000000011011111",
            "1111101001111111101000000111101111011111",
            "1000001101000000000011111111000000000011",
            "1011111101011111111000000011011111111111",
            "1000000000011111111111111000000000000000",
            "1111111111111111111111111111111111111111"
        ],
        "time": 60,
        "speed": 120,
        "obstacles": [
            [3, 15, -1], [6, 22, 1],
            [13, 10, 1], [10, 30, 1],[17, 25, "v1"],[11, 4, -1],[16,30,1],[16,19,"v1"],[4,28,1],[15,34,"v1"],
           
                ]
    },
  
    {
        "maze": [
           
            "1111111111111111111111111111111111111111", 
            "1000100000001000000100000011100011111001", 
            "1110101111101011101111100111110110011001", 
            "1000000010001010000111100100110011101111", 
            "1011111011111011110000000110110000111101", 
            "1010001000000000000111110010000010010001", 
            "1010111111111111101111111010111000011101", 
            "1000000010001000100000111010111111001101", 
            "1111111010101010101110000011100001001111", 
            "1000001010101010100111111011111011000011", 
            "1011101010101010111101111000010010110111",
            "1000100010000000100000101110000010101011", 
            "1110111111111111101110000110111010000101", 
            "1000000000100000100111111110111011100101", 
            "1011111110101110111111100010111000110001", 
            "1000100010101000000101000000000011111101", 
            "1110101110101011110101011111111000000011", 
            "1000001000001000000001011001000010111011", 
            "1111000001111000111000001101011010001000", 
            "1111111111111111111111111111111111111111", 
            ],
        "time": 60,
        "speed": 120,
        "obstacles": [
            [3, 5, "v1"], [4, 13, "v1"], [11,28,1],[5,32,1],[9,20,1],[12,20,1],[17,15,1],[11,10,1],[7,3,"v1"],
            [13, 6, 1],
            [16, 25, "v1"]
        ]
    }
]


class HomeScreen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Cat Maze Runner 🐾")
        self.window.geometry("1500x2050")
        self.window.config(bg="#ffb3ec")
        self.window.resizable(False, False)

        self.chosen_color = "black"

        tk.Label(
            self.window, text="🐾 Cat Maze Runner 🐾",
            font=("Comic Sans MS", 60, "bold"),
            fg="#5a0099", bg="#ffb3ec"
        ).pack(pady=20)

        tk.Label(
            self.window,
            text=(
        "🐾 HOW TO PLAY 🐾\n\n"
        "• Use the ARROW KEYS to move the cat through the maze\n"
        "• Avoid the moving red obstacles – touching them costs a life\n"
        "• You have 3 lives and a limited time per level\n"
        "• Reach the GREEN exit tile to complete the level\n"
        "• Each level gets harder with faster obstacles\n\n"
        "Good luck and have fun! 😺"
        ),
            font=("Comic Sans MS", 28),
            fg="#5a0099",
            bg="#ffb3ec",
            justify="center",
            wraplength=1200
            ).pack(pady=20)

        tk.Button(
            self.window, text="Start Game",
            font=("Comic Sans MS", 35, "bold"),
            bg="palevioletred", width=12,
            command=self.start_game
        ).pack(pady=40)

        tk.Button(
            self.window, text="Exit",
            font=("Comic Sans MS", 25),
            bg="#ff6666", fg="white",
            width=10,
            command=self.window.quit
        ).pack()

        self.window.mainloop()

    def set_color(self, color):
        self.chosen_color = color

    def start_game(self):
        self.window.destroy()
        LevelSelectScreen(self.chosen_color)


class LevelSelectScreen:
    def __init__(self, player_color):
        self.player_color = player_color
        self.window = tk.Tk()
        self.window.title("Select Level ⭐")
        self.window.geometry("1500x2050")
        self.window.config(bg="#ffb3ec")
        self.window.resizable(False, False)

        tk.Label(
            self.window,
            text="⭐ Select a Level ⭐",
            font=("Comic Sans MS", 55, "bold"),
            fg="#5a0099",
            bg="#ffb3ec"
        ).pack(pady=20)

        for i in range(len(LEVELS)):
            if i < UNLOCKED_LEVELS:
                tk.Button(
                    self.window,
                    text=f"Level {i+1}",
                    font=("Comic Sans MS", 25),
                    width=25,
                    bg="yellow",
                    command=lambda lvl=i: self.start_level(lvl)
                ).pack(pady=20)
            else:
                tk.Button(
                    self.window,
                    text=f"🔒 Level {i+1}",
                    font=("Comic Sans MS", 25),
                    width=25,
                    bg="lightgray",
                    state="disabled"
                ).pack(pady=20)

        tk.Button(
            self.window,
            text="⬅ Back",
            font=("Comic Sans MS", 25),
            bg="lightgray",
            command=self.back
        ).pack(pady=15)

        self.window.mainloop()
           

    def start_level(self, level):
        self.window.destroy()
        root = tk.Tk()
        MazeGame(root, self.player_color, level)
        root.mainloop()

    def back(self):
        self.window.destroy()
        HomeScreen()


class NextLevelScreen:
    def __init__(self, player_color, next_level):
        global UNLOCKED_LEVELS
        if next_level > UNLOCKED_LEVELS:
            UNLOCKED_LEVELS = next_level

        self.player_color = player_color
        self.next_level = next_level

        self.window = tk.Tk()
        self.window.title("Level Complete ⭐")
        self.window.geometry("1500x2050")
        self.window.config(bg="#c8facc")
        self.window.resizable(False, False)

        tk.Label(
            self.window,
            text="🎉 Level Complete! 🎉",
            font=("Comic Sans MS", 45, "bold"),
            bg="#c8facc",
            fg="#006400"
        ).pack(pady=30)

        if next_level < len(LEVELS):
            tk.Button(
                self.window,
                text="➡ Next Level",
                font=("Comic Sans MS", 35),
                bg="yellow",
                width=30,
                command=self.next_level_game
            ).pack(pady=15)

        tk.Button(
            self.window,
            text="❌ Exit Game",
            font=("Comic Sans MS", 35),
            bg="#ff9999",
            width=30,
            command=self.window.destroy
        ).pack()

        self.window.mainloop()


    def next_level_game(self):
        self.window.destroy()
        root = tk.Tk()
        MazeGame(root, self.player_color, self.next_level)
        root.mainloop()


class MazeGame:
    def __init__(self, root, player_color, level):
        self.root = root
        self.level = level
        self.player_color = player_color

        self.maze = LEVELS[level]["maze"]
        self.time_left = LEVELS[level]["time"]
        self.obstacle_speed = LEVELS[level]["speed"]

        self.root.title(f"Cat Maze Runner - Level {level+1}")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="pink")
        self.canvas.pack()

        self.cat_row, self.cat_col = 1, 1
        self.exit_row, self.exit_col = 18, 39
        self.lives = 3
        self.game_over = False

        self.draw_maze()
        self.draw_exit()
        self.draw_ui()
        self.create_obstacles()

        
        self.cat_frames = []
        self.frame_index = 0
        self.cat_frames = {
            "Right": [],
            "Left": [],
            "Up": [],
            "Down": []
        }

        self.direction = "Right"
        self.frame_index = 0
 
        self.load_frames() 
        self.is_moving = 0
        self.draw_player() 
        self.animate_player() 
       

        self.root.bind("<KeyPress>", self.move_cat)
        self.update_timer()
        self.update_obstacles()

   

    def create_default_image(self):
        
        default_img = Image.new('RGB', (TILE, TILE), self.player_color)
        return ImageTk.PhotoImage(default_img)


    def load_frames(self):
        SPRITE_SIZE = 120  
        base_frames = ["cat1.png", "cat2.png", "cat3.png"]

        for file in base_frames:
            try:
                img = Image.open(file).resize((SPRITE_SIZE, SPRITE_SIZE), Image.NEAREST)
                self.cat_frames["Right"].append(ImageTk.PhotoImage(img))
                self.cat_frames["Left"].append(
                    ImageTk.PhotoImage(img.transpose(Image.FLIP_LEFT_RIGHT))
                    )
                self.cat_frames["Down"].append(
                    ImageTk.PhotoImage(img.rotate(-90, expand=True))
                    )
                self.cat_frames["Up"].append(
                    ImageTk.PhotoImage(img.rotate(90, expand=True))
                    )
            except FileNotFoundError:
                print(f"Missing {file}, using default")
                default = self.create_default_image()
                for d in self.cat_frames:
                    self.cat_frames[d].append(default)


    def animate_player(self):
        if self.game_over:
            return

        frames = self.cat_frames[self.direction]

        if self.is_moving > 0:
            self.frame_index = (self.frame_index + 1) % len(frames)
            self.is_moving -= 1
        else:
            self.frame_index = 0  

        frame = frames[self.frame_index]
        self.canvas.itemconfig(self.cat, image=frame)
        self.root.image = frame
        self.root.after(120, self.animate_player)

    def draw_exit(self):
        self.canvas.create_rectangle(
            self.exit_col * TILE,
            self.exit_row * TILE,
            (self.exit_col + 1) * TILE,
            (self.exit_row + 1) * TILE,
            fill="green",
            outline="darkgreen",
            width=3,
            tag="exit"
        )
        self.canvas.create_text(
            (self.exit_col + 0.5) * TILE,
            (self.exit_row + 0.5) * TILE,
            text="🏁",
            font=("Arial", 22)
        )



   
   
    def draw_player(self):
        start_frame = self.cat_frames["Right"][0]
        self.cat = self.canvas.create_image(
            (self.cat_col + 0.5) * TILE,
            (self.cat_row + 0.5) * TILE,
        image=start_frame,
        tag="player"
        )
        self.root.image = start_frame


    def draw_maze(self):
        for r in range(ROWS):
            for c in range(COLS):
                if self.maze[r][c] == "1":
                    self.canvas.create_rectangle(
                        c*TILE, r*TILE,
                        (c+1)*TILE, (r+1)*TILE,
                        fill="white", outline="pink"
                    )

    


    def draw_ui(self):
        self.timer_text = self.canvas.create_text(
            80, 25, text=f"Time: {self.time_left}",
            font=("Arial", 24, "bold")
        )

        self.hearts = []
        for i in range(self.lives):
            self.hearts.append(
                self.canvas.create_text(
                    WIDTH - 80 - i*55, 25,
                    text="♥", fill="red",
                    font=("Arial", 30, "bold")
                )
            )

    def can_move(self, r, c):
        return 0 <= r < ROWS and 0 <= c < COLS and self.maze[r][c] == "0"

    def move_cat(self, event):
        if self.game_over:
            return

        dr = dc = 0
        if event.keysym == "Up":
             dr = -1
             self.direction = "Up"
        elif event.keysym == "Down":
            dr = 1
            self.direction = "Down"
        elif event.keysym == "Left":
            dc = -1
            self.direction = "Left"
        elif event.keysym == "Right":
            dc = 1
            self.direction = "Right"


        nr, nc = self.cat_row + dr, self.cat_col + dc
        if self.can_move(nr, nc):
            self.cat_row, self.cat_col = nr, nc

            self.is_moving = 6
           
          
            self.canvas.coords(
                self.cat,
                (nc + 0.5) * TILE, 
                (nr + 0.5) * TILE  
            )

        if (nr, nc) == (self.exit_row, self.exit_col):
            self.win_game()

    def update_timer(self):
        if self.game_over:
            return
        if self.time_left <= 0:
            self.lose_game("TIME'S UP!")
            return

        self.canvas.itemconfig(self.timer_text, text=f"Time: {self.time_left}")
        self.time_left -= 1
        self.root.after(1000, self.update_timer)

    def create_obstacles(self):
       
        self.obstacles = LEVELS[self.level].get("obstacles", [])
        self.obstacle_items = []
        for r, c, _ in self.obstacles:
            self.obstacle_items.append(
                self.canvas.create_rectangle(
                    c*TILE, r*TILE,
                    (c+1)*TILE, (r+1)*TILE,
                    outline="", fill="red"
                )
            )

    def update_obstacles(self):
        if self.game_over:
            return

        for i, (r, c, d) in enumerate(self.obstacles):
            if d == 1 or d == -1: 
                nc = c + d
                if self.maze[r][nc] == "1":
                    d *= -1
                    self.obstacles[i][2] = d
                    nc = c + d
                self.obstacles[i][1] = nc
                self.canvas.coords(
                    self.obstacle_items[i],
                    nc*TILE, r*TILE,
                    (nc+1)*TILE, (r+1)*TILE
                )
                if (self.cat_row, self.cat_col) == (r, nc):
                    self.hit_obstacle()
            else:  
                dr = int(d.replace("v",""))
                nr = r + dr
                if self.maze[nr][c] == "1":
                    dr *= -1
                    self.obstacles[i][2] = f"v{dr}"
                    nr = r + dr
                self.obstacles[i][0] = nr
                self.canvas.coords(
                    self.obstacle_items[i],
                    c*TILE, nr*TILE,
                    (c+1)*TILE, (nr+1)*TILE
                )
                if (self.cat_row, self.cat_col) == (nr, c):
                    self.hit_obstacle()

        self.root.after(self.obstacle_speed, self.update_obstacles)

    def hit_obstacle(self):
        self.lives -= 1
        self.canvas.delete(self.hearts.pop())
        if self.lives == 0:
            self.lose_game("No lives left!")
        else:
            self.cat_row, self.cat_col = 1, 1
            self.direction = "Right"
            self.frame_index = 0
           
            self.canvas.coords(self.cat, 1.5*TILE, 1.5*TILE)
            self.canvas.itemconfig(
                self.cat,
                image=self.cat_frames["Right"][0]
            )
            self.root.image = self.cat_frames["Right"][0]
           
    def win_game(self):
        self.game_over = True
        self.root.destroy()

        if self.level + 1 < len(LEVELS):
            NextLevelScreen(self.player_color, self.level + 1)
        else:
            root = tk.Tk()
            self.end_screen(root)

    def end_screen(self, root):
        canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="light green")
        canvas.pack()
        canvas.create_text(
            WIDTH//2, HEIGHT//2,
            text="🏆 YOU BEAT ALL LEVELS! 🏆",
            font=("Comic Sans MS", 40, "bold"),
            fill="#5a0099"
        )

    def lose_game(self, msg):
        self.game_over = True
        self.root.destroy()
        root = tk.Tk()
        canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="orange")
        canvas.pack()
        canvas.create_text(
            WIDTH//2, HEIGHT//2,
            text=f"💥 GAME OVER 💥\n{msg}",
            font=("Comic Sans MS", 36, "bold"),
            fill="#5a0099",
            justify="center"
        )


HomeScreen()


