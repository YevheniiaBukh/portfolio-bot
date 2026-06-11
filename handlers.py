from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from keyboards import main_menu, projects_menu, back_button
from data import DEVELOPER, PROJECTS

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    text = (
        f"Hello, {message.from_user.first_name}!.\n\n"
        f"Welcome to my portfolio bot! *{DEVELOPER['name']}*.\n"
        f"_{DEVELOPER['title']}.\n\n"
        "Use the menu below to explore my skills, projects, and contact information."
        
    )
    await message.answer(text, reply_markup=main_menu())
    
    
@router.message(Command("menu"))    
async def cmd_menu(message: Message):
    await message.answer("Main Menu:", reply_markup=main_menu())
    
    
@router.callback_query(F.data == "about_me")
async def cb_about_me(callback: CallbackQuery):
    await callback.message.edit_text(DEVELOPER["about"], reply_markup=back_button())
    await callback.answer()
    
@router.callback_query(F.data == "skills")
async def cb_skills(callback: CallbackQuery):
    skills_text = "Skills:\n\n" + "\n".join(f"- {skill}" for skill in DEVELOPER["skills"])
    text = f"Skills:\n\n{skills_text}"
    await callback.message.edit_text(text, reply_markup=back_button())
    await callback.answer()
    
@router.callback_query(F.data == "portfolio")
async def cb_portfolio(callback: CallbackQuery):
    await callback.message.edit_text("Portfolio:\nChoose a project to learn more:",
          reply_markup=projects_menu())
    await callback.answer()
    
@router.callback_query(F.data.startswith("project_"))
async def cb_project(callback: CallbackQuery):
    project = next((p for p in PROJECTS if p["id"] == callback.data), None)
    if project:
        await callback.message.edit_text(
            f"{project['name']}\n\n{project['description']}",
              reply_markup=back_button())
    await callback.answer()
    
    
@router.callback_query(F.data == "contact")
async def cb_contact(callback: CallbackQuery):
    contact_info = (
        f"Email: {DEVELOPER['email']}\n"
        f"GitHub: {DEVELOPER['github']}\n"
        f"LinkedIn: {DEVELOPER['linkedin']}\n"
        "Write me an email or connect with me on GitHub or LinkedIn!"
    )
    await callback.message.edit_text(contact_info, reply_markup=back_button())
    await callback.answer()
    
@router.callback_query(F.data == "main_menu")
async def cb_main_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "Main Menu:",
        reply_markup=main_menu()
    )
    await callback.answer()
