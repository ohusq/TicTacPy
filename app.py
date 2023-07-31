if "__main__" != __name__:
    exit()

import subprocess
import tkinter
from   tkinter import messagebox

class App():
    """
    Create a window with Tic Tac Toe game
    """
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x300")

        self.buttons = []
        self.turn = "X"
        self.winner = None

    def play(self) -> None:
        """
        Start the game
        """
        self.create_buttons()
        self.root.mainloop()

    def create_buttons(self) -> None:
        """
        Create buttons for the game
        """
        for i in range(3):
            row = []
            for j in range(3):
                button = tkinter.Button(self.root, width=10, height=5, command=lambda i=i, j=j: self.click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, i: int, j: int) -> None:
        """
        Handle the click event
        """
        if self.buttons[i][j]["text"] == "" and not self.winner:
            self.buttons[i][j]["text"] = self.turn
            self.check_winner()
            self.change_turn()

    def change_turn(self) -> None:
        """
        Change the turn
        """
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def check_winner(self) -> None:
        """
        Check if there is a winner
        """
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                self.winner = self.buttons[i][0]["text"]
                self.buttons[i][0].config(bg="green")
                self.buttons[i][1].config(bg="green")
                self.buttons[i][2].config(bg="green")
                self.show_winner()
                return

            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                self.winner = self.buttons[0][i]["text"]
                self.buttons[0][i].config(bg="green")
                self.buttons[1][i].config(bg="green")
                self.buttons[2][i].config(bg="green")
                self.show_winner()
                return

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            self.winner = self.buttons[0][0]["text"]
            self.buttons[0][0].config(bg="green")
            self.buttons[1][1].config(bg="green")
            self.buttons[2][2].config(bg="green")
            self.show_winner()
            return

        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            self.winner = self.buttons[0][2]["text"]
            self.buttons[0][2].config(bg="green")
            self.buttons[1][1].config(bg="green")
            self.buttons[2][0].config(bg="green")
            self.show_winner()
            return
        
        if self.check_draw():
            self.show_winner()
            return
        
    def check_draw(self) -> bool:
        """
        Check if there is a draw
        """
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == "":
                    return False
        return True
    
    def show_winner(self) -> None:
        """
        Show the winner
        """
        if self.winner:
            tkinter.Message(self.root, text=f"{self.winner} won!", width=100).grid(row=3, column=0, columnspan=3)
        else:
            tkinter.Message(self.root, text="Draw!", width=100).grid(row=3, column=0, columnspan=3)


    def reset(self) -> None:
        """
        Reset the game
        """
        self.buttons = []
        self.turn = "X"
        self.winner = None
        self.create_buttons()

if "__main__" == __name__:
    app = App()
    app.play()

    # Restart the game
    while True:
        if app.winner:
            if messagebox.askyesno("Restart", "Do you want to restart the game?"):
                app.reset()
            else:
                break