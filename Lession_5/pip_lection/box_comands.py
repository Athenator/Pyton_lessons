from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from logger import *

async def hi_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'Athena blessed {update.effective_user.first_name}!')

async def time_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')

async def sum_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')


