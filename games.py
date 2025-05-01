import random

async def play_game(event):
    # اختر لعبة عشوائية
    games = ["Tic Tac Toe", "Hangman", "Rock Paper Scissors"]
    selected_game = random.choice(games)

    await event.respond(f"اللعبة المختارة: {selected_game}\nابدأ اللعب!")

    # أضف المزيد من الألعاب حسب الحاجة
