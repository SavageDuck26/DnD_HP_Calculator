import random
from tkinter import Tk, ttk

def parse_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def calculate_hp(hit_dice, die, add_con):
    hit_dice = parse_int(hit_dice)
    die = parse_int(die)
    add_con = parse_int(add_con)

    hp = 0
    for i in range(hit_dice):
        hp += random.randint(1, die)
    hp += add_con
    return hp


def mass_roll_hp(hit_dice, die, add_con):
    hit_dice = parse_int(hit_dice)
    die = parse_int(die)
    add_con = parse_int(add_con)

    median_roll = (die + 1) / 2
    non_mod_hp = hit_dice * median_roll
    hp = non_mod_hp + add_con
    return round(hp)

def build_main_window():
    root = Tk()
    root.title("D&D Monster HP Calculator")
    width = 700
    height = 160

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")

    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text = "Created by SavageDuck26").grid(column = 0, row = 0)
    ttk.Button(frm, text = "Quit", command = root.destroy).grid(column = 0, row = 1)
    # ========================================================================
    ttk.Label(frm, text = "Hit Dice:").grid(column = 1, row = 0)
    hit_dice = ttk.Entry(frm)
    hit_dice.grid(column = 1, row = 1)
    
    ttk.Label(frm, text = "Dice Sides:").grid(column = 2, row = 0)
    die = ttk.Entry(frm)
    die.grid(column = 2, row = 1)
    
    ttk.Label(frm, text = "Constitution Addition:").grid(column = 3, row = 0)
    add_con = ttk.Entry(frm)
    add_con.grid(column = 3, row = 1)
    
    result_label = ttk.Label(frm, text="", font = ("Arial", 14))
    result_label.grid(column=1, row=3, columnspan=3)

    def on_calculate():
        result = calculate_hp(hit_dice.get(), die.get(), add_con.get())
        result_label.config(text=f"HP = {result}", font = ("Arial", 14))
        
        avg_result = mass_roll_hp(hit_dice.get(), die.get(), add_con.get())
        result_label.config(text=f"HP = {result}\nAverage HP = {avg_result}", font = ("Arial", 14))


    ttk.Button(
        frm,
        text="Calculate HP",
        command=on_calculate
    ).grid(column=0, row=2)

    return root

    

def main():
    root = build_main_window()
    root.mainloop()

if __name__ == "__main__":
    main()