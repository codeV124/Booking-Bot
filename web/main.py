from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from datetime import datetime
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QStyledItemDelegate, QApplication, QMainWindow, QGroupBox, QComboBox, QPushButton, QMessageBox, QLabel, QTextEdit
import sys
from threading import Thread
from PIL import Image


bowling_pins_107 = {"1": [{"x": 54, "y": 15, "pixel": (193, 39, 45, 255)}], "2": [{"x": 28, "y": 15, "pixel": (193, 39, 45, 255)}, {"x": 78, "y": 15, "pixel": (193, 39, 45, 255)}], "3": [{"x": 28, "y": 16, "pixel": (193, 39, 45, 255)}, {"x": 78, "y": 16, "pixel": (193, 39, 45, 255)}, {"x": 53, "y": 36, "pixel": (193, 39, 45, 255)}], "4": [{"x": 26, "y": 13, "pixel": (193, 39, 45, 255)}, {"x": 78, "y": 13, "pixel": (193, 39, 45, 255)}, {"x": 44, "y": 33, "pixel": (193, 39, 45, 255)}, {"x": 62, "y": 33, "pixel": (193, 39, 45, 255)}], "5": [{"x": 36, "y": 16, "pixel": (193, 39, 45, 255)}, {"x": 54, "y": 16, "pixel": (193, 39, 45, 255)}, {"x": 71, "y": 16, "pixel": (193, 39, 45, 255)}, {"x": 46, "y": 24, "pixel": (193, 39, 45, 255)}, {"x": 62, "y": 24, "pixel": (193, 39, 45, 255)}], "6": [{"x": 35, "y": 16, "pixel": (193, 39, 45, 255)}, {"x": 52, "y": 16, "pixel": (193, 39, 45, 255)}, {"x": 70, "y": 16, "pixel": (193, 39, 45, 255)}, {"x": 61, "y": 24, "pixel": (193, 39, 45, 255)}, {"x": 45, "y": 24, "pixel": (193, 39, 45, 255)}, {"x": 53, "y": 34, "pixel": (193, 39, 45, 255)}], "7": [{"x": 26, "y": 12, "pixel": (193, 39, 45, 255)}, {"x": 43, "y": 12, "pixel": (193, 39, 45, 255)}, {"x": 60, "y": 12, "pixel": (193, 39, 45, 255)}, {"x": 78, "y": 12, "pixel": (193, 39, 45, 255)}, {"x": 52, "y": 25, "pixel": (193, 39, 45, 255)}, {"x": 69, "y": 25, "pixel": (193, 39, 45, 255)}, {"x": 35, "y": 25, "pixel": (193, 39, 45, 255)}], "8": [{"x": 26, "y": 14, "pixel": (181, 65, 95, 255)}, {"x": 43, "y": 14, "pixel": (181, 65, 95, 255)}, {"x": 35, "y": 25, "pixel": (193, 39, 45, 255)}, {"x": 52, "y": 25, "pixel": (193, 39, 45, 255)}, {"x": 70, "y": 25, "pixel": (193, 39, 45, 255)}, {"x": 62, "y": 33, "pixel": (193, 39, 45, 255)}, {"x": 44, "y": 33, "pixel": (193, 39, 45, 255)}, {"x": 53, "y": 43, "pixel": (193, 39, 45, 255)}], "9": [{"x": 26, "y": 15, "pixel": (193, 39, 45, 255)}, {"x": 44, "y": 15, "pixel": (193, 39, 45, 255)}, {"x": 61, "y": 15, "pixel": (193, 39, 45, 255)}, {"x": 35, "y": 25, "pixel": (193, 39, 45, 255)}, {"x": 52, "y": 25, "pixel": (193, 39, 45, 255)}, {"x": 69, "y": 25, "pixel": (193, 39, 45, 255)}, {"x": 61, "y": 33, "pixel": (193, 39, 45, 255)}, {"x": 44, "y": 33, "pixel": (193, 39, 45, 255)}, {"x": 53, "y": 43, "pixel": (193, 39, 45, 255)}]}
cake_candles_107 = {"1": [{"x": 54, "y": 37, "pixel": (204, 79, 39, 255)}], "2": [{"x": 43, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 63, "y": 37, "pixel": (204, 79, 39, 255)}], "3": [{"x": 36, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 56, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 74, "y": 37, "pixel": (204, 79, 39, 255)}], "4": [{"x": 28, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 47, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 66, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 83, "y": 37, "pixel": (204, 79, 39, 255)}], "5": [{"x": 28, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 42, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 55, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 68, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 82, "y": 37, "pixel": (204, 79, 39, 255)}], "6": [{"x": 26, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 37, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 48, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 60, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 72, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 83, "y": 37, "pixel": (204, 79, 39, 255)}], "7": [{"x": 20, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 31, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 43, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 55, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 66, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 78, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 89, "y": 37, "pixel": (204, 79, 39, 255)}], "8": [{"x": 19, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 28, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 38, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 49, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 59, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 69, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 79, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 89, "y": 37, "pixel": (204, 79, 39, 255)}], "9": [{"x": 19, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 28, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 37, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 46, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 56, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 65, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 74, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 83, "y": 37, "pixel": (204, 79, 39, 255)}, {"x": 91, "y": 37, "pixel": (204, 79, 39, 255)}]}
flag_poles_107 =   {"1": [{"x": 80, "y": 25, "pixel": (196, 66, 36, 255)}], "2": [{"x": 80, "y": 25, "pixel": (196, 66, 36, 255)}, {"x": 24, "y": 26, "pixel": (196, 66, 36, 255)}], "3": [{"x": 79, "y": 26, "pixel": (196, 66, 36, 255)}, {"x": 45, "y": 21, "pixel": (196, 66, 36, 255)}, {"x": 17, "y": 28, "pixel": (196, 66, 36, 255)}], "4": [{"x": 80, "y": 26, "pixel": (196, 66, 36, 255)}, {"x": 39, "y": 24, "pixel": (196, 66, 36, 255)}, {"x": 23, "y": 39, "pixel": (196, 66, 36, 255)}, {"x": 62, "y": 39, "pixel": (196, 66, 36, 255)}], "5": [{"x": 80, "y": 26, "pixel": (196, 66, 36, 255)}, {"x": 49, "y": 27, "pixel": (196, 66, 36, 255)}, {"x": 17, "y": 27, "pixel": (196, 66, 36, 255)}, {"x": 33, "y": 40, "pixel": (196, 66, 36, 255)}, {"x": 64, "y": 39, "pixel": (196, 66, 36, 255)}], "6": [{"x": 27, "y": 26, "pixel": (196, 66, 36, 255)}, {"x": 53, "y": 26, "pixel": (196, 66, 36, 255)}, {"x": 80, "y": 26, "pixel": (196, 66, 36, 255)}, {"x": 69, "y": 40, "pixel": (196, 66, 36, 255)}, {"x": 42, "y": 40, "pixel": (196, 66, 36, 255)}, {"x": 16, "y": 40, "pixel": (196, 66, 36, 255)}], "7": [{"x": 13, "y": 28, "pixel": (196, 66, 36, 255)}, {"x": 38, "y": 28, "pixel": (196, 66, 36, 255)}, {"x": 63, "y": 28, "pixel": (196, 66, 36, 255)}, {"x": 88, "y": 28, "pixel": (196, 66, 36, 255)}, {"x": 76, "y": 40, "pixel": (196, 66, 36, 255)}, {"x": 51, "y": 40, "pixel": (196, 66, 36, 255)}, {"x": 25, "y": 40, "pixel": (196, 66, 36, 255)}], "8": [{"x": 10, "y": 27, "pixel": (196, 66, 36, 255)}, {"x": 33, "y": 27, "pixel": (196, 66, 36, 255)}, {"x": 58, "y": 27, "pixel": (196, 66, 36, 255)}, {"x": 81, "y": 27, "pixel": (196, 66, 36, 255)}, {"x": 93, "y": 42, "pixel": (196, 66, 36, 255)}, {"x": 70, "y": 42, "pixel": (196, 66, 36, 255)}, {"x": 45, "y": 42, "pixel": (196, 66, 36, 255)}, {"x": 20, "y": 42, "pixel": (196, 66, 36, 255)}], "9": [{"x": 14, "y": 25, "pixel": (196, 66, 36, 255)}, {"x": 34, "y": 25, "pixel": (196, 66, 36, 255)}, {"x": 53, "y": 25, "pixel": (196, 66, 36, 255)}, {"x": 72, "y": 25, "pixel": (196, 66, 36, 255)}, {"x": 90, "y": 25, "pixel": (196, 66, 36, 255)}, {"x": 82, "y": 39, "pixel": (196, 66, 36, 255)}, {"x": 63, "y": 39, "pixel": (196, 66, 36, 255)}, {"x": 44, "y": 39, "pixel": (196, 66, 36, 255)}, {"x": 26, "y": 39, "pixel": (196, 66, 36, 255)}]}
piggy_coins_107 =  {"1": [{"x": 52, "y": 38, "pixel": (253, 219, 67, 255)}], "2": [{"x": 52, "y": 28, "pixel": (254, 224, 89, 255)}, {"x": 52, "y": 42, "pixel": (254, 224, 87, 255)}], "3": [{"x": 52, "y": 14, "pixel": (254, 223, 82, 255)}, {"x": 52, "y": 28, "pixel": (254, 221, 76, 255)}, {"x": 52, "y": 41, "pixel": (254, 224, 89, 255)}], "4": [{"x": 47, "y": 28, "pixel": (254, 224, 87, 255)}, {"x": 61, "y": 28, "pixel": (253, 219, 67, 255)}, {"x": 61, "y": 41, "pixel": (254, 224, 87, 255)}, {"x": 47, "y": 41, "pixel": (254, 224, 89, 255)}], "5": [{"x": 45, "y": 14, "pixel": (254, 224, 89, 255)}, {"x": 45, "y": 28, "pixel": (254, 224, 89, 255)}, {"x": 45, "y": 42, "pixel": (254, 224, 89, 255)}, {"x": 58, "y": 28, "pixel": (254, 224, 89, 255)}, {"x": 58, "y": 42, "pixel": (254, 224, 87, 255)}], "6": [{"x": 42, "y": 15, "pixel": (254, 224, 89, 255)}, {"x": 56, "y": 15, "pixel": (254, 224, 89, 255)}, {"x": 42, "y": 29, "pixel": (254, 224, 89, 255)}, {"x": 56, "y": 29, "pixel": (254, 224, 89, 255)}, {"x": 42, "y": 43, "pixel": (254, 224, 89, 255)}, {"x": 56, "y": 43, "pixel": (254, 224, 87, 255)}], "7": [{"x": 38, "y": 13, "pixel": (254, 221, 76, 255)}, {"x": 52, "y": 13, "pixel": (254, 224, 87, 255)}, {"x": 38, "y": 27, "pixel": (254, 223, 82, 255)}, {"x": 52, "y": 27, "pixel": (254, 224, 89, 255)}, {"x": 52, "y": 41, "pixel": (254, 224, 89, 255)}, {"x": 66, "y": 41, "pixel": (254, 224, 89, 255)}], "8": [{"x": 38, "y": 13, "pixel": (254, 224, 89, 255)}, {"x": 52, "y": 13, "pixel": (254, 224, 89, 255)}, {"x": 38, "y": 27, "pixel": (254, 224, 89, 255)}, {"x": 52, "y": 27, "pixel": (254, 224, 89, 255)}, {"x": 66, "y": 27, "pixel": (254, 223, 82, 255)}, {"x": 38, "y": 40, "pixel": (254, 223, 82, 255)}, {"x": 52, "y": 40, "pixel": (254, 224, 89, 255)}, {"x": 65, "y": 40, "pixel": (254, 224, 89, 255)}], "9": [{"x": 38, "y": 14, "pixel": (254, 224, 89, 255)}, {"x": 52, "y": 14, "pixel": (254, 224, 89, 255)}, {"x": 65, "y": 14, "pixel": (254, 224, 89, 255)}, {"x": 38, "y": 28, "pixel": (254, 224, 89, 255)}, {"x": 52, "y": 28, "pixel": (254, 224, 87, 255)}, {"x": 65, "y": 28, "pixel": (254, 224, 87, 255)}, {"x": 38, "y": 42, "pixel": (254, 224, 89, 255)}, {"x": 52, "y": 42, "pixel": (254, 223, 82, 255)}, {"x": 65, "y": 42, "pixel": (254, 223, 82, 255)}]}
dogs_107 =         {"1": [{"x": 52, "y": 40, "pixel": (153, 20, 20, 255)}], "2": [{"x": 43, "y": 41, "pixel": (153, 20, 20, 255)}, {"x": 61, "y": 41, "pixel": (154, 21, 21, 255)}], "3": [{"x": 39, "y": 43, "pixel": (153, 20, 20, 255)}, {"x": 54, "y": 43, "pixel": (153, 20, 20, 255)}, {"x": 68, "y": 43, "pixel": (153, 20, 20, 255)}], "4": [{"x": 36, "y": 43, "pixel": (154, 21, 21, 255)}, {"x": 49, "y": 43, "pixel": (153, 20, 20, 255)}, {"x": 62, "y": 43, "pixel": (153, 20, 20, 255)}, {"x": 73, "y": 43, "pixel": (153, 20, 20, 255)}], "5": [{"x": 34, "y": 28, "pixel": (153, 20, 20, 255)}, {"x": 54, "y": 28, "pixel": (154, 21, 21, 255)}, {"x": 72, "y": 27, "pixel": (153, 20, 20, 255)}, {"x": 64, "y": 56, "pixel": (153, 20, 20, 255)}, {"x": 43, "y": 57, "pixel": (153, 20, 20, 255)}], "6": [{"x": 38, "y": 26, "pixel": (153, 20, 20, 255)}, {"x": 52, "y": 26, "pixel": (157, 23, 23, 255)}, {"x": 67, "y": 26, "pixel": (155, 22, 22, 255)}, {"x": 68, "y": 58, "pixel": (157, 23, 23, 255)}, {"x": 54, "y": 58, "pixel": (157, 23, 23, 255)}, {"x": 39, "y": 58, "pixel": (153, 20, 20, 255)}], "7": [{"x": 34, "y": 26, "pixel": (153, 20, 20, 255)}, {"x": 47, "y": 26, "pixel": (153, 20, 20, 255)}, {"x": 59, "y": 26, "pixel": (153, 20, 20, 255)}, {"x": 72, "y": 26, "pixel": (153, 20, 20, 255)}, {"x": 41, "y": 57, "pixel": (155, 22, 22, 255)}, {"x": 54, "y": 57, "pixel": (153, 20, 20, 255)}, {"x": 66, "y": 57, "pixel": (154, 21, 21, 255)}], "8": [{"x": 32, "y": 26, "pixel": (155, 22, 22, 255)}, {"x": 47, "y": 26, "pixel": (153, 20, 20, 255)}, {"x": 59, "y": 26, "pixel": (153, 20, 20, 255)}, {"x": 70, "y": 26, "pixel": (156, 22, 22, 255)}, {"x": 70, "y": 59, "pixel": (153, 20, 20, 255)}, {"x": 58, "y": 59, "pixel": (153, 20, 20, 255)}, {"x": 46, "y": 59, "pixel": (155, 22, 22, 255)}, {"x": 33, "y": 59, "pixel": (153, 20, 20, 255)}], "9": [{"x": 34, "y": 26, "pixel": (154, 21, 21, 255)}, {"x": 48, "y": 26, "pixel": (153, 20, 20, 255)}, {"x": 59, "y": 26, "pixel": (155, 22, 22, 255)}, {"x": 71, "y": 26, "pixel": (156, 22, 22, 255)}, {"x": 79, "y": 57, "pixel": (157, 23, 23, 255)}, {"x": 65, "y": 57, "pixel": (161, 26, 26, 255)}, {"x": 53, "y": 57, "pixel": (160, 25, 25, 255)}, {"x": 41, "y": 57, "pixel": (157, 23, 23, 255)}, {"x": 29, "y": 57, "pixel": (154, 21, 21, 255)}]}

bowling_pins_150 = {"1": [{"x": 75, "y": 21, "pixel": (192, 31, 35, 255)}], "2": [{"x": 39, "y": 21, "pixel": (192, 39, 46, 255)}, {"x": 109, "y": 21, "pixel": (199, 64, 69, 255)}], "3": [{"x": 39, "y": 22, "pixel": (189, 19, 24, 255)}, {"x": 109, "y": 22, "pixel": (189, 19, 24, 255)}, {"x": 74, "y": 50, "pixel": (185, 39, 56, 255)}], "4": [{"x": 36, "y": 18, "pixel": (192, 26, 29, 255)}, {"x": 109, "y": 18, "pixel": (192, 25, 29, 255)}, {"x": 61, "y": 46, "pixel": (194, 68, 81, 255)}, {"x": 86, "y": 46, "pixel": (195, 74, 87, 255)}], "5": [{"x": 50, "y": 22, "pixel": (186, 46, 65, 255)}, {"x": 75, "y": 22, "pixel": (188, 62, 82, 255)}, {"x": 99, "y": 22, "pixel": (187, 58, 78, 255)}, {"x": 64, "y": 33, "pixel": (184, 72, 100, 255)}, {"x": 86, "y": 33, "pixel": (181, 53, 82, 255)}], "6": [{"x": 49, "y": 22, "pixel": (197, 91, 108, 255)}, {"x": 72, "y": 22, "pixel": (197, 91, 108, 255)}, {"x": 98, "y": 22, "pixel": (197, 91, 108, 255)}, {"x": 85, "y": 33, "pixel": (199, 113, 133, 255)}, {"x": 63, "y": 33, "pixel": (199, 114, 135, 255)}, {"x": 74, "y": 47, "pixel": (199, 116, 137, 255)}], "7": [{"x": 36, "y": 16, "pixel": (200, 133, 157, 255)}, {"x": 60, "y": 16, "pixel": (200, 133, 157, 255)}, {"x": 84, "y": 16, "pixel": (200, 133, 157, 255)}, {"x": 109, "y": 16, "pixel": (200, 133, 157, 255)}, {"x": 72, "y": 35, "pixel": (194, 53, 63, 255)}, {"x": 96, "y": 35, "pixel": (192, 46, 56, 255)}, {"x": 49, "y": 35, "pixel": (194, 54, 63, 255)}], "8": [{"x": 36, "y": 19, "pixel": (217, 175, 189, 255)}, {"x": 60, "y": 19, "pixel": (218, 175, 188, 255)}, {"x": 49, "y": 35, "pixel": (194, 54, 63, 255)}, {"x": 72, "y": 35, "pixel": (194, 53, 63, 255)}, {"x": 98, "y": 35, "pixel": (194, 55, 64, 255)}, {"x": 86, "y": 46, "pixel": (195, 74, 87, 255)}, {"x": 61, "y": 46, "pixel": (195, 67, 79, 255)}, {"x": 74, "y": 60, "pixel": (196, 76, 89, 255)}], "9": [{"x": 36, "y": 21, "pixel": (198, 61, 67, 255)}, {"x": 61, "y": 21, "pixel": (196, 53, 60, 255)}, {"x": 85, "y": 21, "pixel": (198, 62, 68, 255)}, {"x": 49, "y": 35, "pixel": (194, 54, 63, 255)}, {"x": 72, "y": 35, "pixel": (194, 53, 63, 255)}, {"x": 96, "y": 35, "pixel": (192, 46, 56, 255)}, {"x": 85, "y": 46, "pixel": (197, 73, 85, 255)}, {"x": 61, "y": 46, "pixel": (195, 67, 79, 255)}, {"x": 74, "y": 60, "pixel": (196, 76, 89, 255)}]}
cake_candles_150 = {"1": [{"x": 75, "y": 51, "pixel": (206, 74, 32, 255)}], "2": [{"x": 60, "y": 51, "pixel": (214, 80, 37, 255)}, {"x": 88, "y": 51, "pixel": (210, 88, 49, 255)}], "3": [{"x": 50, "y": 51, "pixel": (209, 76, 34, 255)}, {"x": 78, "y": 51, "pixel": (216, 82, 39, 255)}, {"x": 103, "y": 51, "pixel": (206, 73, 31, 255)}], "4": [{"x": 39, "y": 51, "pixel": (211, 79, 37, 255)}, {"x": 65, "y": 51, "pixel": (210, 99, 63, 255)}, {"x": 92, "y": 51, "pixel": (212, 79, 36, 255)}, {"x": 116, "y": 51, "pixel": (208, 89, 51, 255)}], "5": [{"x": 39, "y": 51, "pixel": (215, 81, 39, 255)}, {"x": 58, "y": 51, "pixel": (207, 77, 35, 255)}, {"x": 77, "y": 51, "pixel": (207, 79, 38, 255)}, {"x": 95, "y": 51, "pixel": (218, 82, 39, 255)}, {"x": 114, "y": 51, "pixel": (206, 78, 37, 255)}], "6": [{"x": 36, "y": 51, "pixel": (209, 77, 34, 255)}, {"x": 51, "y": 51, "pixel": (206, 74, 32, 255)}, {"x": 67, "y": 51, "pixel": (214, 80, 37, 255)}, {"x": 84, "y": 51, "pixel": (214, 81, 39, 255)}, {"x": 100, "y": 51, "pixel": (206, 78, 37, 255)}, {"x": 116, "y": 51, "pixel": (214, 81, 38, 255)}], "7": [{"x": 28, "y": 51, "pixel": (208, 83, 43, 255)}, {"x": 43, "y": 51, "pixel": (209, 75, 32, 255)}, {"x": 60, "y": 51, "pixel": (211, 79, 36, 255)}, {"x": 77, "y": 51, "pixel": (217, 83, 40, 255)}, {"x": 92, "y": 51, "pixel": (208, 74, 31, 255)}, {"x": 109, "y": 51, "pixel": (218, 82, 39, 255)}, {"x": 124, "y": 51, "pixel": (205, 72, 29, 255)}], "8": [{"x": 26, "y": 51, "pixel": (213, 81, 38, 255)}, {"x": 39, "y": 51, "pixel": (209, 87, 47, 255)}, {"x": 53, "y": 51, "pixel": (210, 88, 49, 255)}, {"x": 68, "y": 51, "pixel": (209, 75, 32, 255)}, {"x": 82, "y": 51, "pixel": (211, 78, 35, 255)}, {"x": 96, "y": 51, "pixel": (208, 77, 35, 255)}, {"x": 110, "y": 51, "pixel": (210, 96, 59, 255)}, {"x": 124, "y": 51, "pixel": (230, 149, 123, 255)}], "9": [{"x": 26, "y": 51, "pixel": (211, 96, 59, 255)}, {"x": 39, "y": 51, "pixel": (210, 88, 48, 255)}, {"x": 51, "y": 51, "pixel": (208, 79, 37, 255)}, {"x": 64, "y": 51, "pixel": (210, 92, 53, 255)}, {"x": 78, "y": 51, "pixel": (209, 76, 34, 255)}, {"x": 91, "y": 51, "pixel": (210, 79, 37, 255)}, {"x": 103, "y": 51, "pixel": (206, 74, 32, 255)}, {"x": 116, "y": 51, "pixel": (210, 78, 35, 255)}, {"x": 127, "y": 51, "pixel": (208, 75, 33, 255)}]}
flag_poles_150 =   {"1": [{"x": 112, "y": 35, "pixel": (196, 65, 35, 255)}], "2": [{"x": 112, "y": 35, "pixel": (196, 65, 35, 255)}, {"x": 33, "y": 36, "pixel": (199, 62, 29, 255)}], "3": [{"x": 110, "y": 36, "pixel": (197, 63, 32, 255)}, {"x": 63, "y": 29, "pixel": (196, 65, 35, 255)}, {"x": 23, "y": 39, "pixel": (197, 64, 33, 255)}], "4": [{"x": 112, "y": 36, "pixel": (196, 66, 36, 255)}, {"x": 54, "y": 33, "pixel": (201, 59, 26, 255)}, {"x": 32, "y": 54, "pixel": (196, 66, 36, 255)}, {"x": 86, "y": 54, "pixel": (200, 59, 25, 255)}], "5": [{"x": 112, "y": 36, "pixel": (196, 66, 36, 255)}, {"x": 68, "y": 37, "pixel": (196, 66, 36, 255)}, {"x": 23, "y": 37, "pixel": (198, 62, 30, 255)}, {"x": 46, "y": 56, "pixel": (196, 66, 36, 255)}, {"x": 89, "y": 54, "pixel": (196, 66, 36, 255)}], "6": [{"x": 37, "y": 36, "pixel": (196, 66, 36, 255)}, {"x": 74, "y": 36, "pixel": (196, 66, 36, 255)}, {"x": 112, "y": 36, "pixel": (196, 66, 36, 255)}, {"x": 96, "y": 56, "pixel": (196, 66, 36, 255)}, {"x": 58, "y": 56, "pixel": (196, 66, 36, 255)}, {"x": 22, "y": 56, "pixel": (196, 66, 36, 255)}], "7": [{"x": 18, "y": 39, "pixel": (196, 66, 36, 255)}, {"x": 53, "y": 39, "pixel": (196, 66, 36, 255)}, {"x": 88, "y": 39, "pixel": (196, 66, 36, 255)}, {"x": 123, "y": 39, "pixel": (196, 66, 36, 255)}, {"x": 106, "y": 56, "pixel": (196, 66, 36, 255)}, {"x": 71, "y": 56, "pixel": (196, 66, 36, 255)}, {"x": 35, "y": 56, "pixel": (196, 66, 36, 255)}], "8": [{"x": 14, "y": 37, "pixel": (196, 66, 36, 255)}, {"x": 46, "y": 37, "pixel": (196, 66, 36, 255)}, {"x": 81, "y": 37, "pixel": (196, 66, 36, 255)}, {"x": 113, "y": 37, "pixel": (196, 66, 36, 255)}, {"x": 130, "y": 58, "pixel": (196, 66, 36, 255)}, {"x": 98, "y": 58, "pixel": (196, 66, 36, 255)}, {"x": 63, "y": 58, "pixel": (196, 66, 36, 255)}, {"x": 28, "y": 58, "pixel": (196, 66, 36, 255)}], "9": [{"x": 19, "y": 35, "pixel": (196, 65, 35, 255)}, {"x": 47, "y": 35, "pixel": (196, 66, 36, 255)}, {"x": 74, "y": 35, "pixel": (196, 66, 36, 255)}, {"x": 100, "y": 35, "pixel": (196, 66, 36, 255)}, {"x": 126, "y": 35, "pixel": (196, 66, 36, 255)}, {"x": 114, "y": 54, "pixel": (196, 66, 36, 255)}, {"x": 88, "y": 54, "pixel": (196, 66, 36, 255)}, {"x": 61, "y": 54, "pixel": (196, 66, 36, 255)}, {"x": 36, "y": 54, "pixel": (197, 64, 34, 255)}]}
piggy_coins_150 =  {"1": [{"x": 72, "y": 53, "pixel": (254, 224, 88, 255)}], "2": [{"x": 72, "y": 39, "pixel": (254, 224, 89, 255)}, {"x": 72, "y": 58, "pixel": (254, 224, 90, 255)}], "3": [{"x": 72, "y": 19, "pixel": (254, 224, 90, 255)}, {"x": 72, "y": 39, "pixel": (254, 224, 90, 255)}, {"x": 72, "y": 57, "pixel": (254, 224, 89, 255)}], "4": [{"x": 65, "y": 39, "pixel": (254, 224, 90, 255)}, {"x": 85, "y": 39, "pixel": (253, 222, 83, 255)}, {"x": 85, "y": 57, "pixel": (254, 225, 92, 255)}, {"x": 65, "y": 57, "pixel": (254, 222, 79, 255)}], "5": [{"x": 63, "y": 19, "pixel": (254, 224, 89, 255)}, {"x": 63, "y": 39, "pixel": (254, 224, 91, 255)}, {"x": 63, "y": 58, "pixel": (254, 224, 91, 255)}, {"x": 81, "y": 39, "pixel": (254, 224, 91, 255)}, {"x": 81, "y": 58, "pixel": (254, 224, 90, 255)}], "6": [{"x": 58, "y": 21, "pixel": (254, 223, 82, 255)}, {"x": 78, "y": 21, "pixel": (254, 225, 92, 255)}, {"x": 58, "y": 40, "pixel": (253, 221, 77, 255)}, {"x": 78, "y": 40, "pixel": (254, 224, 90, 255)}, {"x": 58, "y": 60, "pixel": (254, 223, 87, 255)}, {"x": 78, "y": 60, "pixel": (254, 224, 92, 255)}], "7": [{"x": 53, "y": 18, "pixel": (254, 217, 62, 255)}, {"x": 72, "y": 18, "pixel": (253, 217, 60, 255)}, {"x": 53, "y": 37, "pixel": (253, 219, 56, 255)}, {"x": 72, "y": 37, "pixel": (253, 218, 59, 255)}, {"x": 72, "y": 57, "pixel": (254, 221, 69, 255)}, {"x": 92, "y": 57, "pixel": (254, 225, 90, 255)}], "8": [{"x": 53, "y": 18, "pixel": (254, 222, 77, 255)}, {"x": 72, "y": 18, "pixel": (254, 223, 78, 255)}, {"x": 53, "y": 37, "pixel": (254, 220, 73, 255)}, {"x": 72, "y": 37, "pixel": (253, 220, 71, 255)}, {"x": 92, "y": 37, "pixel": (254, 225, 91, 255)}, {"x": 53, "y": 56, "pixel": (254, 220, 69, 255)}, {"x": 72, "y": 56, "pixel": (253, 220, 68, 255)}, {"x": 91, "y": 56, "pixel": (254, 223, 83, 255)}], "9": [{"x": 53, "y": 19, "pixel": (254, 223, 85, 255)}, {"x": 72, "y": 19, "pixel": (254, 223, 86, 255)}, {"x": 91, "y": 19, "pixel": (254, 224, 91, 255)}, {"x": 53, "y": 39, "pixel": (254, 224, 90, 255)}, {"x": 72, "y": 39, "pixel": (254, 224, 90, 255)}, {"x": 91, "y": 39, "pixel": (254, 224, 91, 255)}, {"x": 53, "y": 58, "pixel": (254, 224, 89, 255)}, {"x": 72, "y": 58, "pixel": (254, 224, 91, 255)}, {"x": 91, "y": 58, "pixel": (254, 224, 90, 255)}]}
dogs_150 =         {"1": [{"x": 72, "y": 56, "pixel": (152, 19, 19, 255)}], "2": [{"x": 60, "y": 57, "pixel": (152, 19, 19, 255)}, {"x": 85, "y": 57, "pixel": (154, 21, 21, 255)}], "3": [{"x": 54, "y": 60, "pixel": (153, 19, 19, 255)}, {"x": 75, "y": 60, "pixel": (154, 21, 21, 255)}, {"x": 95, "y": 60, "pixel": (153, 20, 20, 255)}], "4": [{"x": 50, "y": 60, "pixel": (155, 21, 21, 255)}, {"x": 68, "y": 60, "pixel": (153, 20, 20, 255)}, {"x": 86, "y": 60, "pixel": (153, 20, 20, 255)}, {"x": 102, "y": 60, "pixel": (153, 20, 20, 255)}], "5": [{"x": 47, "y": 39, "pixel": (155, 21, 21, 255)}, {"x": 75, "y": 39, "pixel": (157, 22, 22, 255)}, {"x": 100, "y": 37, "pixel": (153, 20, 20, 255)}, {"x": 89, "y": 78, "pixel": (154, 20, 20, 255)}, {"x": 60, "y": 79, "pixel": (153, 20, 20, 255)}], "6": [{"x": 53, "y": 36, "pixel": (153, 19, 19, 255)}, {"x": 72, "y": 36, "pixel": (157, 22, 22, 255)}, {"x": 93, "y": 36, "pixel": (155, 21, 21, 255)}, {"x": 95, "y": 81, "pixel": (157, 22, 22, 255)}, {"x": 75, "y": 81, "pixel": (159, 24, 24, 255)}, {"x": 54, "y": 81, "pixel": (155, 21, 21, 255)}], "7": [{"x": 47, "y": 36, "pixel": (153, 20, 20, 255)}, {"x": 65, "y": 36, "pixel": (154, 21, 21, 255)}, {"x": 82, "y": 36, "pixel": (154, 21, 21, 255)}, {"x": 100, "y": 36, "pixel": (153, 20, 20, 255)}, {"x": 57, "y": 79, "pixel": (154, 20, 20, 255)}, {"x": 75, "y": 79, "pixel": (154, 20, 20, 255)}, {"x": 92, "y": 79, "pixel": (154, 20, 20, 255)}], "8": [{"x": 44, "y": 36, "pixel": (151, 17, 17, 255)}, {"x": 65, "y": 36, "pixel": (153, 19, 19, 255)}, {"x": 82, "y": 36, "pixel": (153, 20, 20, 255)}, {"x": 98, "y": 36, "pixel": (154, 21, 21, 255)}, {"x": 98, "y": 82, "pixel": (153, 20, 20, 255)}, {"x": 81, "y": 82, "pixel": (154, 20, 20, 255)}, {"x": 64, "y": 82, "pixel": (154, 21, 21, 255)}, {"x": 46, "y": 82, "pixel": (154, 20, 20, 255)}], "9": [{"x": 47, "y": 36, "pixel": (154, 21, 21, 255)}, {"x": 67, "y": 36, "pixel": (154, 20, 20, 255)}, {"x": 82, "y": 36, "pixel": (155, 22, 22, 255)}, {"x": 99, "y": 36, "pixel": (156, 22, 22, 255)}, {"x": 110, "y": 79, "pixel": (154, 21, 21, 255)}, {"x": 91, "y": 79, "pixel": (154, 21, 21, 255)}, {"x": 74, "y": 79, "pixel": (154, 21, 21, 255)}, {"x": 57, "y": 79, "pixel": (154, 21, 21, 255)}, {"x": 40, "y": 79, "pixel": (154, 20, 20, 255)}]}

others = {"107" : [bowling_pins_107, cake_candles_107, flag_poles_107, piggy_coins_107, dogs_107], "150" : [bowling_pins_150, cake_candles_150, flag_poles_150, piggy_coins_150, dogs_150]}
finger = {"1": [78, 108], "2": [74, 107], "3": [76, 105], "4": [76, 104], "5": [77, 103], "6": [104, 102], "7": [105, 99], "8": [105, 103], "9": [103, 102]}

green_r, green_g, green_b = [144, 238, 144]
pink_r, pink_g, pink_b = [255, 116, 185]
yellow_r, yellow_g, yellow_b = [255, 218, 18]
blue_r, blue_g, blue_b = [18, 255, 255]
grey_r, grey_g, grey_b = [106, 165, 167]

def checking_captcha(driver: webdriver.Chrome) -> int:
    with open('save.png', 'wb') as file:
        img_element = driver.find_element(By.TAG_NAME, 'img')
        file.write(img_element.screenshot_as_png)

    image = Image.open('save.png')
    [width, height] = image.size

    content = driver.find_element(By.TAG_NAME, 'h3').text.lower()

    if 'finger' in content:
        for j in range(1, 10):
            if finger[f"{j}"] == [width, height]:
                return j
    if width != 150 or width != 107:
        image = image.resize((150, 150))
        width = 150
    for index, type in enumerate(['bowling', 'candle', 'flag', 'coin', 'dog']):
        if type in content:
            data = others[f'{width}'][index]
    limit = 100
    if 'dogs' in content:
        limit = 30
    for i in range(9, 0, -1):
        locations = data[f'{i}']
        same = True
        for location in locations:
            x = int(location['x'])
            y = int(location['y'])
            r1, g1, b1, a1 = image.getpixel((x, y))
            r2, g2, b2, a2 = location['pixel']

            if abs(r1 - r2) > limit or abs(g1 - g2) > limit or abs(b1 - b2) > limit or abs(a1 - a2) > limit:
                same = False
                break
        if same:
            return i

Ui_MainWindow, QtBaseClass = uic.loadUiType('dialog.ui')

class CenterDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = Qt.AlignmentFlag.AlignCenter
        super().paint(painter, option, index)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.month = self.findChild(QComboBox, 'month')
        self.day = self.findChild(QComboBox, 'day')
        self.hour = self.findChild(QComboBox, 'hour')
        self.minute = self.findChild(QComboBox, 'minute')
        self.meridium = self.findChild(QComboBox, 'meridium')
        self.trans = self.findChild(QComboBox, 'trans')
        self.start_button = self.findChild(QPushButton, 'start')
        self.restart_button = self.findChild(QPushButton, 'restart')
        self.group = self.findChild(QGroupBox, 'groupbox')
        self.current_server_time = self.findChild(QLabel, 'current_server_time')
        self.current_server_time.setText('12 : 00 : 00  AM')
        self.message = self.findChild(QTextEdit, 'message')
        self.alone = self.findChild(QComboBox, 'alone')
        self.today_event = self.findChild(QComboBox, 'today_event')

        # events
        self.month.currentIndexChanged.connect(self.on_month_changed)
        self.day.currentIndexChanged.connect(self.on_day_changed)
        self.hour.currentIndexChanged.connect(self.on_hour_changed)
        self.minute.currentIndexChanged.connect(self.on_minute_changed)
        self.meridium.currentIndexChanged.connect(self.on_meridium_changed)
        self.trans.currentIndexChanged.connect(self.on_trans_changed)
        self.start_button.clicked.connect(self.on_start_button_clicked)
        self.restart_button.clicked.connect(self.on_restart_button_clicked)
        self.alone.currentIndexChanged.connect(self.on_alone_changed)
        self.today_event.currentIndexChanged.connect(self.on_today_event_changed)

        # parameters
        self.desired_month = datetime.now().month
        self.desired_day = 1
        self.desired_hour = datetime.now().hour % 12
        self.desired_minute = 0
        self.desired_meridium = 'AM'
        self.desired_trans = 'CRT'
        self.how_many = 'with Wife'
        self.has_event = 'No Event'

        self.server_time = ''
        self.is_running = False

        # element init
        self.month.setCurrentIndex(self.desired_month - 1)
        self.setup_day()
        self.hour.setCurrentIndex(self.desired_hour)
        self.setup_minute()
        self.alone.setCurrentText(self.how_many)
        self.today_event.setCurrentText(self.has_event)

        self.process = Thread(target=self.reservation)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://web.foretees.com/v5/servlet/LoginPrompt?cn=clearwaterbaygolf')
        form = find_element(self.driver, By.ID, 'login')
        username = form.find_element(By.ID, 'user_name')
        sleep(5)
        action = ActionChains(self.driver)
        action.click(username).perform()
        user_text = 'S419-04-01'
        for char in user_text:
            action.send_keys(char)
            action.pause(0.5)
        action.perform()
        password = form.find_element(By.ID, 'password')
        action.click(password).perform()
        password_text = 'Golfbook99'
        for char2 in password_text:
            action.send_keys(char2)
            action.pause(0.5)
        action.perform()  
        form.find_element(By.CLASS_NAME, "button-primary").click()      
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="rwdNav"]/ul/li[1]/a').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="rwdNav"]/ul/li[1]/ul/li[1]/a').click()
        sleep(3)
        

    def setup_day(self):
        self.day.addItems([str(i) for i in range(1, 32)])

    def setup_minute(self):
        self.minute.addItems([str(i) for i in range(0, 60)])

    def on_month_changed(self):
        self.desired_month = int(self.month.currentText())

    def on_day_changed(self):
        self.desired_day = int(self.day.currentText())

    def on_hour_changed(self):
        self.desired_hour = int(self.hour.currentText())
        if self.desired_hour >= 7 and self.desired_hour <= 11:
            self.meridium.setCurrentText('AM')
        else:
            self.meridium.setCurrentText('PM')

    def on_minute_changed(self):
        self.desired_minute = int(self.minute.currentText())

    def on_meridium_changed(self):
        self.desired_meridium = self.meridium.currentText()

    def on_trans_changed(self):
        self.desired_trans = self.trans.currentText()

    def on_alone_changed(self):
        self.how_many = self.alone.currentText()

    def on_today_event_changed(self):
        self.has_event = self.today_event.currentText()

    def on_start_button_clicked(self):
        if self.is_running:
            self.is_running =False
        
        self.message.clear()
        self.server_time = "9:30:00 AM"
        self.process = Thread(target=self.reservation)
        self.process.start()

    def on_restart_button_clicked(self):
        if self.is_running:
            self.is_running =False

        self.message.clear()
        self.driver.get('https://web.foretees.com/v5/clearwaterbaygolf_golf_m24/Member_select')
        sleep(3)
        # Getting current server time
        curr_time = find_element(self.driver, By.CLASS_NAME, 'jquery_server_clock').text       
        
        curr_meridium = curr_time.split(' ')[1]
        curr_time = curr_time.split(' ')[0]
        curr_hour = int(curr_time.split(':')[0])
        curr_minute = int(curr_time.split(':')[1])
        curr_second = int(curr_time.split(':')[2])

        temp = int((curr_second + 5) / 60)
        curr_second = (curr_second + 5) % 60

        # temp_hour = (curr_minute + temp) / 60
        curr_minute = (curr_minute + temp) % 60

        self.server_time = "{}:{:02d}:{:02d} {}".format(curr_hour, curr_minute, curr_second, curr_meridium)

        self.process = Thread(target=self.reservation)
        self.process.start()

    def reservation(self):
        self.is_running = True
        month = self.desired_month
        day = self.desired_day
        hour = self.desired_hour
        minute= self.desired_minute
        meridium = self.desired_meridium
        trans = self.desired_trans
        server_time = self.server_time

        self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], waiting for "{server_time}"...')

        if meridium == 'PM' and hour != 12:
            hour += 12
        desired_minutes = hour * 60 + minute
        is_allowed_to_refresh = False

        refreshing_time = 0
        while True:
            try:
                curr_time = self.driver.find_element(By.CLASS_NAME, 'jquery_server_clock').text
                curr_meridium = curr_time.split(' ')[1]
                temp = curr_time.split(' ')[0]
                curr_hour = int(temp.split(':')[0])
                curr_hour = '{:02d}'.format(curr_hour)
                curr_minute = temp.split(':')[1]
                curr_second = temp.split(':')[2]
                self.current_server_time.setText(f'{curr_hour} : {curr_minute} : {curr_second}  {curr_meridium}')

                if curr_time == server_time:
                    is_allowed_to_refresh = True
                    start_time = datetime.now()
                    self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], started reservation')
                else:
                    refreshing_time += 1
                    if refreshing_time == 100:
                        refreshing_time = 0
                        self.driver.find_element(By.ID, "refresh").click()

                if is_allowed_to_refresh:
                    self.driver.find_element(By.ID, "refresh").click()
                    self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], refresh button was clicked')
                    break
            except:
                pass
            if not self.is_running:
                break
            sleep(0.1)

        if not self.is_running:
            return
        
        # Select desired day
        available_days = self.driver.find_elements(By.CSS_SELECTOR, 'td[data-handler="selectDay"]')
        is_found_available_day = False
        for item_day in available_days:
            curr_day = int(item_day.text)
            if curr_day == day:
                sleep(1)
                self.driver.execute_script("arguments[0].click();", item_day)
                self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], {curr_day} day in calender was clicked')
                is_found_available_day = True
                break
        if not is_found_available_day:
            self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], {day} day is not available. ')
            return

        has_captcha = False
        while True:
            try:
                self.driver.find_element( By.CLASS_NAME, "mem_notice").text
                has_captcha = False
                break
            except:
                pass
            try:
                if 'captcha prompt' == self.driver.find_element(By.ID, "title").text.lower():
                    has_captcha = True
                    break
            except:
                pass
            sleep(0.1)

        if has_captcha:
            # Passing CAPTCHA
            self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], passing captcha...')
            number = checking_captcha(self.driver)
            while True:
                number_buttons = find_element(self.driver, By.ID, 'main_login').find_elements(By.TAG_NAME, 'a')
                if len(number_buttons) > 0:
                    break
                sleep(0.1)
            number_buttons[int(number) - 1].click()
            self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], button"{number}" was clicked')
            
        # Select desired time in table
        if self.how_many == 'with Wife':
            available_times = find_elements(self.driver, By.CLASS_NAME, "noRowColor")
            available_count = 2
        else:
            available_times = find_elements(self.driver, By.CLASS_NAME, "hasRowColor")
            if self.how_many == 'Alone':
                available_count = 3
            else:
                available_count = 0


        if not self.is_running:
            return
        
        for available_time in available_times:
            try:
                button = available_time.find_element(By.TAG_NAME, 'a')
                if self.how_many == 'with Guests':
                    try:
                        color = available_time.get_attribute('style').split(');')[0].split('rgb(')[1].split(',')
                        r = int(color[0])
                        g = int(color[1])
                        b = int(color[2])
                        if (abs(r - pink_r) > 20 or abs(g - pink_g) > 20 or abs(b - pink_b) > 20):
                            continue
                    except:
                        continue
                row_type = available_time.get_attribute('data-ftrowtype')
                if self.how_many == 'with Wife' and 'B' not in row_type:
                    continue
                content = available_time.text
                text = content.split('\n')[0]
                reserve_time = text.split(' ')[0]
                reserve_hour = int(reserve_time.split(':')[0])
                if reserve_hour != 12 and 'PM' in text:
                    reserve_hour += 12
                reserve_minute = int(reserve_time.split(':')[1])
                reserve_minutes = reserve_hour * 60 + reserve_minute

                count = content.count('CLK') + content.count('WLK')

                if reserve_minutes >= desired_minutes and count <= available_count:
                    sleep(1)                   
                    self.driver.execute_script("arguments[0].click();", button)
                    self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], "{text}" button was clicked')
                    if self.has_event == "Today's Event":
                        sleep(1) 
                        find_element(self.driver, By.CLASS_NAME, 'ui-dialog-buttonset').find_elements(By.TAG_NAME, 'button')[1].click()
                        self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], Continue button was clicked')
                    
                    if self.how_many == 'with Wife':
                        sleep(1)
                        find_element(self.driver, By.XPATH, '//*[@id="main"]/div[6]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/span').click()
                        self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], "Tong, Rachel" was reserved with you to [{text}]')

                    if self.how_many == 'with Guests':
                        sleep(1)
                        find_element(self.driver, By.XPATH, '//*[@id="main"]/div[6]/div/div[1]/div[2]/div[2]/ul/li[3]/div').click()
                        guest_button = find_element(self.driver, By.XPATH, '//*[@id="main"]/div[6]/div/div[1]/div[2]/div[2]/div[3]/div/div/div/span')
                        sleep(1)
                        guest_button.click()
                        sleep(1)
                        guest_button.click()
                        sleep(1)
                        guest_button.click()
                        self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], 3 Guests were reserved with you to [{text}]')
                    selects = self.driver.find_elements(By.TAG_NAME, 'select')
                    for select in selects:
                        try:
                            Select(select).select_by_value(trans)
                        except:
                            pass
                    sleep(1)
                    find_element(self.driver, By.CLASS_NAME, 'submit_request_button').click()
                    self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], Submitted')

                    while True:
                        dialogs = find_elements(self.driver, By.CLASS_NAME, 'ui-dialog-buttonset')
                        is_clicked = False
                        for dialog in dialogs:
                            buttons = dialog.find_elements(By.TAG_NAME, 'button')
                            if len(buttons) == 1:
                                sleep(1)
                                buttons[0].click()
                                self.message.append(f'[{datetime.now().strftime("%H:%M:%S")}], Continue button was clicked')
                                is_clicked = True
                        if is_clicked:
                            break
                        sleep(0.1)
                    break
            except:
                pass
        end_time = datetime.now()
        self.message.append(f'Reservation Time : {(end_time - start_time).seconds}s')
        self.is_running = False

def find_element(driver: webdriver.Chrome, by, value: str) -> WebElement:
    while True:
        try:
            element = driver.find_element(by, value)
            return element
        except:
            pass
        sleep(0.1)

def find_elements(driver: webdriver.Chrome, by, value: str) -> list[WebElement]:
    while True:
        try:
            elements = driver.find_elements(by, value)
            if len(elements) > 0:
                return elements
        except:
            pass
        sleep(0.1)

def send_keys(input: WebElement, content: str):
    for i in content:
        input.send_keys(i)
        sleep(0.1)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())