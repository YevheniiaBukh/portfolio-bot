from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data import PROJECTS

def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="About Me", callback_data="about_me")],      
        [InlineKeyboardButton(text="Skills", callback_data="skills")],
        [InlineKeyboardButton(text="Projects", callback_data="projects")],
        [InlineKeyboardButton(text="Contact", callback_data="contact")]
    ])
    
    
def projects_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=project["name"], callback_data=f"project_{project['id']}")]
        for project in PROJECTS
    ]
    buttons.append([InlineKeyboardButton(text="Back to Main Menu", callback_data="main_menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def back_button() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back to Main Menu", callback_data="main_menu")]
    ])