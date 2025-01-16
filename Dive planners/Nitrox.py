import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Dekompresní tabulky pro různé směsi
DECO_TABLE = {
    12: {
        125: [(3, 1)], 
        140: [(3, 5)], 
        150: [(3, 8)],
    },
    15: {
        75: [(3, 1)],
        80: [(3, 3)],
        90: [(3, 7)],
        100: [(3, 12)],
        110: [(3, 17)],
        120: [(3, 20)],
    },
    18: {
        51: [(3, 1)],
        60: [(3, 5)],
        70: [(3, 11)],
        80: [(3, 18)],
        90: [(3, 24)],
    },
    21: {
        35: [(3, 1)],
        40: [(3, 2)],
        50: [(3, 8)],
        60: [(3, 16)],
        70: [(3, 25)],
        80: [(6, 3), (3, 29)],
    },
    24: {
        25: [(3, 1)],
        30: [(3, 2)],
        35: [(3, 4)],
        40: [(3, 8)],
        50: [(3, 17)],
        60: [(6, 4), (3, 24)],
        70: [(6, 10), (3, 30)],
    },
    27: {
        20: [(3, 1)],
        30: [(3, 5)],
        35: [(3, 10)],
        40: [(6, 2), (3, 13)],
        45: [(6, 3), (3, 18)],
        50: [(6, 6), (3, 22)],
        55: [(6, 8), (3, 27)],
        60: [(6, 10), (3, 30)],
    },
    30: {
        17: [(3, 1)],
        20: [(3, 2)],
        25: [(3, 5)],
        30: [(6, 2), (3, 7)],
        35: [(6, 3), (3, 14)],
        40: [(6, 5), (3, 17)],
        45: [(6, 9), (3, 23)],
        50: [(9, 2), (6, 10), (3, 28)],
    },
    33: {
        14: [(3, 1)],
        20: [(3, 4)],
        25: [(6, 2), (3, 7)],
        30: [(6, 4), (3, 11)],
        35: [(6, 6), (3, 17)],
        40: [(9, 2), (6, 8), (3, 23)],
        45: [(9, 4), (6, 11), (3, 28)],
        50: [(9, 5), (6, 15), (3, 31)]
    },
    36: {
        12: [(3, 1)],
        15: [(3, 3)],
        20: [(6, 2), (3, 5)],
        25: [(6, 4), (3, 9)],
        30: [(9, 2), (6, 5), (3, 15)],
        35: [(9, 2), (6, 8), (3, 23)],
        40: [(9, 5), (6, 10), (3, 28)],
        45: [(9, 7), (6, 15), (3, 31)],
    },
    39: {
        10: [(3, 1)],
        15: [(3, 4)],
        20: [(6, 3), (3, 7)],
        25: [(9, 2), (6, 4), (3, 12)],
        30: [(9, 3), (6, 7), (3, 18)],
        35: [(9, 5), (6, 9), (3, 28)],
        40: [(12, 2), (9, 6), (6, 15), (3, 29)],
    },
    42: {
        9: [(3, 1)],
        12: [(3, 4)],
        15: [(6, 1), (3, 5)],
        18: [(6, 4), (3, 6)],
        21: [(9, 2), (6, 4), (3, 10)],
        24: [(9, 3), (6, 6), (3, 16)],
        27: [(9, 4), (6, 7), (3, 19)],
        30: [(12, 2), (9, 4), (6, 9), (3, 25)],
        33: [(12, 2), (9, 6), (6, 12), (3, 29)],
        36: [(12, 2), (9, 7), (6, 15), (3, 32)],
    },
    45: {
        9: [(3, 2)],
        12: [(3, 5)],
        15: [(6, 3), (3, 5)],
        18: [(9, 2), (6, 4), (3, 9)],
        21: [(9, 3), (6, 5), (3, 13)],
        24: [(9, 4), (6, 6), (3, 18)],
        27: [(12, 2), (9, 4), (6, 9), (3, 22)],
        30: [(12, 3), (9, 6), (6, 10), (3, 27)],
    },
    48: {
        9: [(3, 3)],
        12: [(6, 2), (3, 5)],
        15: [(6, 4), (3, 6)],
        18: [(9, 3), (6, 4), (3, 10)],
        21: [(9, 4), (6, 6), (3, 16)],
        24: [(12, 2), (9, 4), (6, 7), (3, 22)],
        27: [(12, 4), (9, 5), (6, 10), (3, 26)],
        30: [(15, 1), (12, 4), (9, 6), (6, 13), (3, 30)],
    },
    51: {
        9: [(3, 4)],
        12: [(6, 3), (3, 6)],
        15: [(9, 2), (6, 4), (3, 8)],
        18: [(9, 4), (6, 5), (3, 13)],
        21: [(12, 3), (9, 4), (6, 7), (3, 18)],
        24: [(12, 4), (9, 5), (6, 9), (3, 24)],
        27: [(12, 5), (9, 6), (6, 13), (3, 28)],
        30: [(15, 3), (12, 4), (9, 8), (6, 16), (3, 32)],
    },
    54: {
        9: [(6, 1), (3, 5)],
        12: [(9, 1), (6, 4), (3, 6)],
        15: [(9, 3), (6, 4), (3, 10)],
        18: [(12, 1), (9, 3), (6, 6), (3, 17)],
        21: [(12, 4), (9, 4), (6, 9), (3, 21)],
        24: [(15, 2), (12, 4), (9, 5), (6, 12), (3, 27)],
        27: [(15, 3), (12, 5), (9, 7), (6, 15), (3, 31)],
    },
    57: {
        9: [(6, 2), (3, 5)],
        12: [(9, 2), (6, 4), (3, 8)],
        15: [(12, 1), (9, 4), (6, 5), (3, 11)],
        18: [(12, 3), (9, 4), (6, 7), (3, 18)],
        21: [(15, 2), (12, 3), (9, 6), (6, 10), (3, 24)],
        24: [(15, 3), (12, 4), (9, 9), (6, 12), (3, 29)],
    },
    60: {
        9: [(6, 4), (3, 5)],
        12: [(9, 3), (6, 5), (3, 9)],
        15: [(12, 2), (9, 4), (6, 5), (3, 14)],
        18: [(12, 4), (9, 5), (6, 6), (3, 22)],
        21: [(15, 3), (12, 4), (9, 5), (6, 11), (3, 27)],
    },
}
DECO_TABLE_21 = {
        12: {
        125: [(3, 1)], 
        140: [(3, 5)], 
        150: [(3, 8)],
    },
    15: {
        75: [(3, 1)],
        80: [(3, 3)],
        90: [(3, 7)],
        100: [(3, 12)],
        110: [(3, 17)],
        120: [(3, 20)],
    },
    18: {
        51: [(3, 1)],
        60: [(3, 5)],
        70: [(3, 11)],
        80: [(3, 18)],
        90: [(3, 24)],
    },
    21: {
        35: [(3, 1)],
        40: [(3, 2)],
        50: [(3, 8)],
        60: [(3, 16)],
        70: [(3, 25)],
        80: [(6, 3), (3, 29)],
    },
    24: {
        25: [(3, 1)],
        30: [(3, 2)],
        35: [(3, 4)],
        40: [(3, 8)],
        50: [(3, 17)],
        60: [(6, 4), (3, 24)],
        70: [(6, 10), (3, 30)],
    },
    27: {
        20: [(3, 1)],
        30: [(3, 5)],
        35: [(3, 10)],
        40: [(6, 2), (3, 13)],
        45: [(6, 3), (3, 18)],
        50: [(6, 6), (3, 22)],
        55: [(6, 8), (3, 27)],
        60: [(6, 10), (3, 30)],
    },
    30: {
        17: [(3, 1)],
        20: [(3, 2)],
        25: [(3, 5)],
        30: [(6, 2), (3, 7)],
        35: [(6, 3), (3, 14)],
        40: [(6, 5), (3, 17)],
        45: [(6, 9), (3, 23)],
        50: [(9, 2), (6, 10), (3, 28)],
    },
    33: {
        14: [(3, 1)],
        20: [(3, 4)],
        25: [(6, 2), (3, 7)],
        30: [(6, 4), (3, 11)],
        35: [(6, 6), (3, 17)],
        40: [(9, 2), (6, 8), (3, 23)],
        45: [(9, 4), (6, 11), (3, 28)],
        50: [(9, 5), (6, 15), (3, 31)]
    },
    36: {
        12: [(3, 1)],
        15: [(3, 3)],
        20: [(6, 2), (3, 5)],
        25: [(6, 4), (3, 9)],
        30: [(9, 2), (6, 5), (3, 15)],
        35: [(9, 2), (6, 8), (3, 23)],
        40: [(9, 5), (6, 10), (3, 28)],
        45: [(9, 7), (6, 15), (3, 31)],
    },
    39: {
        10: [(3, 1)],
        15: [(3, 4)],
        20: [(6, 3), (3, 7)],
        25: [(9, 2), (6, 4), (3, 12)],
        30: [(9, 3), (6, 7), (3, 18)],
        35: [(9, 5), (6, 9), (3, 28)],
        40: [(12, 2), (9, 6), (6, 15), (3, 29)],
    },
    42: {
        9: [(3, 1)],
        12: [(3, 4)],
        15: [(6, 1), (3, 5)],
        18: [(6, 4), (3, 6)],
        21: [(9, 2), (6, 4), (3, 10)],
        24: [(9, 3), (6, 6), (3, 16)],
        27: [(9, 4), (6, 7), (3, 19)],
        30: [(12, 2), (9, 4), (6, 9), (3, 25)],
        33: [(12, 2), (9, 6), (6, 12), (3, 29)],
        36: [(12, 2), (9, 7), (6, 15), (3, 32)],
    },
    45: {
        9: [(3, 2)],
        12: [(3, 5)],
        15: [(6, 3), (3, 5)],
        18: [(9, 2), (6, 4), (3, 9)],
        21: [(9, 3), (6, 5), (3, 13)],
        24: [(9, 4), (6, 6), (3, 18)],
        27: [(12, 2), (9, 4), (6, 9), (3, 22)],
        30: [(12, 3), (9, 6), (6, 10), (3, 27)],
    },
    48: {
        9: [(3, 3)],
        12: [(6, 2), (3, 5)],
        15: [(6, 4), (3, 6)],
        18: [(9, 3), (6, 4), (3, 10)],
        21: [(9, 4), (6, 6), (3, 16)],
        24: [(12, 2), (9, 4), (6, 7), (3, 22)],
        27: [(12, 4), (9, 5), (6, 10), (3, 26)],
        30: [(15, 1), (12, 4), (9, 6), (6, 13), (3, 30)],
    },
    51: {
        9: [(3, 4)],
        12: [(6, 3), (3, 6)],
        15: [(9, 2), (6, 4), (3, 8)],
        18: [(9, 4), (6, 5), (3, 13)],
        21: [(12, 3), (9, 4), (6, 7), (3, 18)],
        24: [(12, 4), (9, 5), (6, 9), (3, 24)],
        27: [(12, 5), (9, 6), (6, 13), (3, 28)],
        30: [(15, 3), (12, 4), (9, 8), (6, 16), (3, 32)],
    },
    54: {
        9: [(6, 1), (3, 5)],
        12: [(9, 1), (6, 4), (3, 6)],
        15: [(9, 3), (6, 4), (3, 10)],
        18: [(12, 1), (9, 3), (6, 6), (3, 17)],
        21: [(12, 4), (9, 4), (6, 9), (3, 21)],
        24: [(15, 2), (12, 4), (9, 5), (6, 12), (3, 27)],
        27: [(15, 3), (12, 5), (9, 7), (6, 15), (3, 31)],
    },
    57: {
        9: [(6, 2), (3, 5)],
        12: [(9, 2), (6, 4), (3, 8)],
        15: [(12, 1), (9, 4), (6, 5), (3, 11)],
        18: [(12, 3), (9, 4), (6, 7), (3, 18)],
        21: [(15, 2), (12, 3), (9, 6), (6, 10), (3, 24)],
        24: [(15, 3), (12, 4), (9, 9), (6, 12), (3, 29)],
    },
    60: {
        9: [(6, 4), (3, 5)],
        12: [(9, 3), (6, 5), (3, 9)],
        15: [(12, 2), (9, 4), (6, 5), (3, 14)],
        18: [(12, 4), (9, 5), (6, 6), (3, 22)],
        21: [(15, 3), (12, 4), (9, 5), (6, 11), (3, 27)],
    },
}
DECO_TABLE_32 = {
    15: {
        150: [(4.5, 4)],
    },
    18: {
        80: [(4.5, 2)],
        100: [(4.5, 7)],
    },
    21: {
        60: [(4.5, 5)],
        70: [(4.5, 8)],
        80: [(4.5, 13)],
        90: [(4.5, 18)],
        100: [(4.5, 24)],
        110: [(4.5, 29)],
        120: [(4.5, 33)],
    },
    24: {
        40: [(4.5, 3)],
        50: [(4.5, 7)],
        60: [(4.5, 12)],
        70: [(4.5, 18)],
        80: [(4.5, 25)],
        90: [(4.5, 32)],
        100: [(4.5, 38)],
        110: [(6, 1), (4.5, 47)],
        120: [(6, 2), (4.5, 47)],
    },
    27: {
        30: [(4.5, 3)],
        40: [(4.5, 8)],
        50: [(4.5, 13)],
        60: [(4.5, 21)],
        70: [(6, 1), (4.5, 29)],
        80: [(6, 3), (4.5, 35)],
        90: [(6, 4), (4.5, 41)],
        100: [(6, 7), (4.5, 55)],
        110: [(9, 2), (6, 8), (4.5, 68)],
        120: [(9, 4), (6, 8), (4.5, 80)],
        130: [(9, 5), (6, 11), (4.5, 89)],
    },
    30: {
        20: [(4.5, 1)],
        25: [(4.5, 3)],
        30: [(4.5, 6)],
        40: [(4.5, 13)],
        50: [(6, 1), (4.5, 20)],
        60: [(6, 3), (4.5, 28)],
        70: [(9, 1), (6, 5), (4.5, 36)],
        80: [(9, 3), (6, 6), (4.5, 42)],
        90: [(9, 5), (6, 8), (4.5, 59)],
        100: [(9, 8), (6, 8), (4.5, 74)],
        110: [(9, 10), (6, 11), (4.5, 85)],
        120: [(9, 13), (6, 12), (4.5, 96)],
    },
    33: {
        20: [(4.5, 3)],
        30: [(4.5, 10)],
        40: [(6, 2), (4.5, 16)],
        50: [(9, 1), (6, 4), (4.5, 23)],
        60: [(9, 4), (6, 4), (4.5, 34)],
        70: [(9, 6), (6, 6), (4.5, 41)],
        80: [(9, 9), (6, 8), (4.5, 58)],
        90: [(9, 13), (6, 8), (4.5, 76)],
        100: [(12, 2), (9, 14), (6, 11), (4.5, 88)],
        110: [(12, 3), (9, 17), (6, 13), (4.5, 102)],
    },
    36: {
        20: [(4.5, 5)],
        30: [(6, 1), (4.5, 12)],
        40: [(9, 2), (6, 3), (4.5, 20)],
        50: [(9, 5), (6, 4), (4.5, 30)],
        60: [(9, 8), (6, 5), (4.5, 40)],
        70: [(12, 2), (9, 10), (6, 7), (4.5, 55)],
        80: [(12, 4), (9, 12), (6, 8), (4.5, 75)],
        90: [(12, 6), (9, 15), (6, 11), (4.5, 88)],
        100: [(12, 8), (9, 18), (6, 13), (4.5, 105)],
    },
    39: {
        15: [(4.5, 3)],
        20: [(4.5, 7)],
        30: [(9, 1), (6, 2), (4.5, 15)],
        40: [(9, 5), (6, 3), (4.5, 23)],
    },
}
DECO_TABLE_34 = {
    15: {
        170: [(4.5, 4)],
        },
    18: {
        100: [(4.5, 5)],
        110: [(4.5, 7)],
        120: [(4.5, 11)],
    },
    21: {
        60: [(4.5, 3)],
        70: [(4.5, 6)],
        80: [(4.5, 10)],
        90: [(4.5, 14)],
        100: [(4.5, 19)],
        110: [(4.5, 24)],
        120: [(4.5, 28)],
    },
    24: {
        40: [(4.5, 2)],
        50: [(4.5, 6)],
        60: [(4.5, 10)],
        70: [(4.5, 15)], 
        80: [(4.5, 21)],
        90: [(4.5, 28)],
        100: [(4.5, 34)],
        110: [(4.5, 39)],
        120: [(4.5, 52)],
    },
    27: {
        40: [(4.5, 6)],
        50: [(4.5, 12)],
        60: [(4.5, 18)],
        70: [(4.5, 26)],
        80: [(6, 1), (4.5, 33)],
        90: [(6, 3), (4.5, 38)],
        100: [(6, 4), (4.5, 48)],
        110: [(6, 7), (4.5, 60)],
        120: [(9, 1), (6, 8), (4.5, 72)],
    },
    30: {
        30: [(4.5, 5)],
        40: [(4.5, 11)],
        50: [(4.5, 18)],
        60: [(6, 2), (4.5, 25)],
        70: [(6, 4), (4.5, 33)],
        80: [(9, 2), (6, 5), (4.5, 39)],
        90: [(9, 3), (6, 7), (4.5, 51)],
        100: [(9, 5), (6, 8), (4.5, 66)],
        110: [(9, 8), (6, 9), (4.5, 77)],
        120: [(9, 10), (6, 11), (4.5, 87)],
    },
    33: {
        30: [(4.5, 8)],
        40: [(6, 1), (4.5, 15)],
        50: [(6, 4), (4.5, 21)],
        60: [(9, 2), (6, 5), (4.5, 31)],
        70: [(9, 5), (6, 5), (4.5, 38)],
        80: [(9, 7), (6, 7), (4.5, 51)],
        90: [(9, 10), (6, 8), (4.5, 67)],
        100: [(9, 13), (6, 10), (4.5, 80)],
    },
}
DECO_TABLE_36 = {
    15: {
        180: [(4.5, 1)],
        200: [(4.5, 4)],
        220: [(4.5, 9)],
    },
    18: {
        100: [(4.5, 2)],
        110: [(4.5, 4)],
        120: [(4.5, 7)],
        130: [(4.5, 10)],
    },
    21:{
        80: [(4.5, 7)],
        90: [(4.5, 11)],
        100: [(4.5, 15)],
        110: [(4.5, 20)],
        120: [(4.5, 24)],
        130: [(4.5, 27)],
    },
    24: {
        60: [(4.5, 8)],
        70: [(4.5, 13)],
        80: [(4.5, 17)],
        90: [(4.5, 24)],
        100: [(4.5, 29)],
        110: [(4.5, 34)],
        120: [(4.5, 43)],
        130: [(4.5, 54)],
    },
    27: {
        40: [(4.5, 5)],
        50: [(4.5, 10)],
        60: [(4.5, 15)],
        70: [(4.5, 22)],
        80: [(4.5, 30)],
        90: [(6, 1), (4.5, 35)],
        100: [(6, 2), (4.5, 40)],
        110: [(6, 4), (4.5, 53)],
        120: [(6, 6), (4.5, 64)],
    },
    30: {
        30: [(4.5, 4)],
        40: [(4.5, 9)],
        50: [(4.5, 16)],
        60: [(6, 1), (4.5, 22)],
        70: [(6, 3), (4.5, 30)],
        80: [(6, 5), (4.5, 36)],
        90: [(9, 2), (6, 5), (4.5, 44)],
        100: [(9, 3), (6, 7), (4.5, 58)],
    },
}
DECO_TABLE_40 = {
    18: {
        140: [(4.5, 5)],
        170: [(4.5, 11)],
    },
    21: {
        80: [(4.5, 3)],
        90: [(4.5, 5)],
        100: [(4.5, 8)],
        110: [(4.5, 12)],
        120: [(4.5, 15)],
        130: [(4.5, 19)],
        140: [(4.5, 21)],
        150: [(4.5, 25)],
        160: [(4.5, 33)],
        170: [(4.5, 40)],
    },
    24: {
        60: [(4.5, 4)],
        70: [(4.5, 7)],
        80: [(4.5, 11)],
        90: [(4.5, 16)],
        100: [(4.5, 21)],
        110: [(4.5, 26)],
        120: [(4.5, 29)],
        130: [(4.5, 36)],
    },
    27: {
        60: [(4.5, 10)],
        70: [(4.5, 16)],
        80: [(4.5, 22)],
        90: [(4.5, 28)],
        100: [(4.5, 33)],
        110: [(4.5, 39)],
    },
}

# Funkce pro přidání dalších polí pro hloubku a čas
def add_depth_time_fields():
    depth_label = tk.Label(depth_time_frame, text="Maximální hloubka (m):")
    depth_label.pack(anchor="w", pady=2)
    depth_entry = tk.Entry(depth_time_frame)
    depth_entry.pack(anchor="w", pady=2)

    time_label = tk.Label(depth_time_frame, text="Čas pod vodou (min):")
    time_label.pack(anchor="w", pady=2)
    time_entry = tk.Entry(depth_time_frame)
    time_entry.pack(anchor="w", pady=2)

    depth_labels.append(depth_label)
    time_labels.append(time_label)
    depth_entries.append(depth_entry)
    time_entries.append(time_entry)

# Funkce pro odebrání posledních polí pro hloubku a čas
def remove_depth_time_fields():
    if depth_entries and time_entries and depth_labels and time_labels:
        depth_entry = depth_entries.pop()
        time_entry = time_entries.pop()
        depth_label = depth_labels.pop()
        time_label = time_labels.pop()

        depth_entry.destroy()
        time_entry.destroy()
        depth_label.destroy()
        time_label.destroy()

# Funkce pro výpočet spotřebovaného vzduchu
def calculate_consumption(deco_stops, table):
    try:
        consumption = float(consumption_entry.get())
        bottle_volume = float(bottle_volume_entry.get())
        total_bars_used = 0

        for depth_entry, time_entry in zip(depth_entries, time_entries):
            depth = float(depth_entry.get())
            time_at_depth = float(time_entry.get())
            adjusted_consumption = consumption * (1 + depth / 10)
            bars_used = (adjusted_consumption * time_at_depth) / bottle_volume
            total_bars_used += bars_used

        for stop_depth, stop_time in deco_stops:
            adjusted_consumption = consumption * (1 + stop_depth / 10)
            bars_used = (adjusted_consumption * stop_time) / bottle_volume
            total_bars_used += bars_used

        consumption_label.config(text=f"Spotřebované bary: {total_bars_used:.2f}")

    except ValueError:
        messagebox.showerror("Chyba", "Zadejte platné hodnoty pro výpočet spotřeby.")

# Funkce pro validaci vstupů a vykreslení grafu
def plot_dive_plan():
    try:
        # Validace minutové spotřeby
        consumption = float(consumption_entry.get())
        if consumption <= 0:
            raise ValueError("Minutová spotřeba musí být kladné číslo.")

        profile_times = [0]
        profile_depths = [0]
        ascent_descent_rate = 10  # Rychlost klesání/stoupání v m/min

        # Vyber správnou dekompresní tabulku podle směsi
        if nitrox_var.get():
            ean = nitrox_selection.get()  
            if ean == "EAN 21%":
                deco_table = DECO_TABLE_21
                max_depth = (1.5 / (21 / 100) - 1) * 10
            elif ean == "EAN 32%":
                deco_table = DECO_TABLE_32
                max_depth = (1.5 / (32 / 100) - 1) * 10
            elif ean == "EAN 34%":
                deco_table = DECO_TABLE_34
                max_depth = (1.5 / (34 / 100) - 1) * 10
            elif ean == "EAN 36%":
                deco_table = DECO_TABLE_36
                max_depth = (1.5 / (36 / 100) - 1) * 10
            elif ean == "EAN 40%":
                deco_table = DECO_TABLE_40
                max_depth = (1.5 / (40 / 100) - 1) * 10
            
            else:
                raise ValueError("Vyberte platný EAN.")
        else:
            deco_table = DECO_TABLE
            max_depth = None

        deco_stops = []
        for depth_entry, time_entry in zip(depth_entries, time_entries):
            depth = float(depth_entry.get())
            time_at_depth = float(time_entry.get())

            # Přidání klesání
            descent_time = depth / ascent_descent_rate
            profile_times.append(profile_times[-1] + descent_time)
            profile_depths.append(depth)

            # Přidání pobytu v hloubce
            profile_times.append(profile_times[-1] + time_at_depth)
            profile_depths.append(depth)

            # Přidání dekompresních zastávek pro tuto hloubku a čas
            depth_key = min([d for d in deco_table if d >= depth], default=None)
            if depth_key is None:
                raise ValueError(f"Pro hloubku {depth} m neexistuje dekompresní tabulka.")

            time_key = min([t for t in deco_table[depth_key] if t >= time_at_depth], default=None)
            if time_key is None:
                raise ValueError(f"Pro čas {time_at_depth} min na hloubce {depth_key} m neexistuje dekompresní tabulka.")

            deco_stops.extend(deco_table[depth_key][time_key])

        # Přidání stoupání a dekompresních zastávek
        for stop_depth, stop_time in deco_stops:
            # Přidání stoupání k zastávce
            if profile_depths[-1] > stop_depth:
                ascent_time = (profile_depths[-1] - stop_depth) / ascent_descent_rate
                profile_times.append(profile_times[-1] + ascent_time)
                profile_depths.append(stop_depth)

            # Pobyt na zastávce
            profile_times.append(profile_times[-1] + stop_time)
            profile_depths.append(stop_depth)

        # Přidání závěrečného stoupání na povrch
        if profile_depths[-1] > 0:
            final_ascent_time = profile_depths[-1] / ascent_descent_rate
            profile_times.append(profile_times[-1] + final_ascent_time)
            profile_depths.append(0)

        # Vymazání starého grafu
        ax.clear()

        # Vykreslení nového grafu
        ax.plot(profile_times, profile_depths, marker='o', label="Ponor")

        if nitrox_var.get() and max_depth:
            ax.axhline(y=max_depth, color="red", linestyle="--", label="Maximální hloubka Nitrox")

        ax.set_xlabel("Čas (minuty)")
        ax.set_ylabel("Hloubka (metry)")
        ax.invert_yaxis()
        ax.legend()

        canvas.draw()

        # Aktualizace tabulky dekompresních zastávek
        for widget in table_frame.winfo_children():
            if widget != consumption_label:
                widget.destroy()  # Odstranění existujících widgetů kromě Spotřebované bary

        consumption_label.grid(row=0, column=0, columnspan=2, pady=10)  # Přesun Spotřebované bary nad tabulku
        
        tk.Label(table_frame, text="Dekompresní zastávky", font=("Arial", 10, "bold")).grid(row=1, column=0, columnspan=2)
        tk.Label(table_frame, text="Hloubka (m)").grid(row=2, column=0)
        tk.Label(table_frame, text="Čas (min)").grid(row=2, column=1)

        for i, (stop_depth, stop_time) in enumerate(deco_stops, start=3):
            tk.Label(table_frame, text=f"{stop_depth:.1f}").grid(row=i, column=0)
            tk.Label(table_frame, text=f"{stop_time:.1f}").grid(row=i, column=1)

        # Vypočítání spotřebovaného vzduchu
        calculate_consumption(deco_stops, deco_table)

    except ValueError as e:
        messagebox.showerror("Chyba", str(e))

# Funkce pro ukončení aplikace
def quit_application():
    root.quit()
    root.destroy()

# Hlavní okno aplikace
root = tk.Tk()
root.title("Plánovač ponorů")
root.geometry("1200x800")

# Rámec pro vstupní hodnoty
input_frame = tk.Frame(root, width=300)
input_frame.pack(side="left", fill="y", padx=10, pady=10)
input_frame.pack_propagate(False)

# Sekce pro výběr směsi
tk.Label(input_frame, text="Směs s kterou se potápíme:").pack(anchor="w")

nitrox_var = tk.BooleanVar()
nitrox_check = tk.Checkbutton(input_frame, text="Nitrox", variable=nitrox_var)
nitrox_check.pack(anchor="w")

nitrox_selection = ttk.Combobox(input_frame, values=["EAN 21%", "EAN 32%", "EAN 34%", "EAN 36%", "EAN 40%"], state="readonly")
nitrox_selection.pack(anchor="w", pady=5)

# Sekce pro minutovou spotřebu
tk.Label(input_frame, text="Minutová spotřeba (litry/min):").pack(anchor="w", pady=5)
consumption_entry = tk.Entry(input_frame)
consumption_entry.pack(anchor="w")

# Sekce pro objem lahve
tk.Label(input_frame, text="Objem lahve v litrech:").pack(anchor="w", pady=5)
bottle_volume_entry = tk.Entry(input_frame)
bottle_volume_entry.pack(anchor="w")

# Sekce pro hloubku a čas pod vodou
tk.Label(input_frame, text="Maximální hloubka a čas pod vodou:").pack(anchor="w", pady=5)

depth_time_frame = tk.Frame(input_frame)
depth_time_frame.pack(anchor="w")

depth_labels = []
time_labels = []
depth_entries = []
time_entries = []

add_depth_time_fields()

add_button = tk.Button(input_frame, text="Přidat další", command=add_depth_time_fields)
add_button.pack(pady=5)

remove_button = tk.Button(input_frame, text="Odebrat poslední", command=remove_depth_time_fields)
remove_button.pack(pady=5)

# Tlačítko pro vykreslení grafu
plot_button = tk.Button(input_frame, text="Vykreslit plán ponoru", command=plot_dive_plan)
plot_button.pack(pady=10)

# Tlačítko pro ukončení aplikace
quit_button = tk.Button(input_frame, text="Ukončit aplikaci", command=quit_application)
quit_button.pack(pady=10)

# Sekce pro grafy a tabulky
graph_table_frame = tk.Frame(root)
graph_table_frame.pack(side="right", fill="both", expand=True)

figure_frame = tk.Frame(graph_table_frame)
figure_frame.pack(side="left", fill="both", expand=True)

table_frame = tk.Frame(graph_table_frame)
table_frame.pack(side="right", padx=10, fill="y")

consumption_label = tk.Label(table_frame, text="Spotřebované bary: --")
consumption_label.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(table_frame, text="Dekompresní zastávky", font=("Arial", 10, "bold")).grid(row=1, column=0, columnspan=2)
tk.Label(table_frame, text="Hloubka (m)").grid(row=2, column=0)
tk.Label(table_frame, text="Čas (min)").grid(row=2, column=1)

fig, ax = plt.subplots()
ax.set_xlabel("Čas (minuty)")
ax.set_ylabel("Hloubka (metry)")
ax.invert_yaxis()
canvas = FigureCanvasTkAgg(fig, master=figure_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill="both", expand=True)

# Spuštění hlavní smyčky
root.mainloop()     #new pull
