from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def rate_kb(idx):
    rate = InlineKeyboardMarkup(row_width=2)
    rate_40 = InlineKeyboardButton(text="❌", callback_data=f"rate_40_|{idx}")
    rate_60 = InlineKeyboardButton(text="😒", callback_data=f"rate_60_|{idx}")
    rate_80 = InlineKeyboardButton(text="👍", callback_data=f"rate_80_|{idx}")
    rate_100 = InlineKeyboardButton(text="🔥🔥🔥", callback_data=f"rate_100_|{idx}")
    rate.add(rate_40, rate_60, rate_80)
    rate.add(rate_100)
    return rate
