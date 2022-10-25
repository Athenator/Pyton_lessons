# import matplotlib.pyplot as plt
# import numpy as np
#
# list = [1,2,3,2,7]
# plt.plot(list)
#
# plt.show()

# import emoji
#
# print(emoji.emojize('Python is :thumbs_up:'))

# from isOdd import isOdd
#
# print(isOdd(0))
# print(isOdd(4))

# from progress.bar import Bar
# import time
#
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from box_comands import *


app = ApplicationBuilder().token("5693192359:AAGZ9y6ORXnBAZhLA7AtwjsDiaptJBUHci8").build()

app.add_handler(CommandHandler("hi", hi_comand))
app.add_handler(CommandHandler("time", time_comand))
app.add_handler(CommandHandler("help", help_comand))
app.add_handler(CommandHandler("sum", sum_comand))

print('server start')
app.run_polling()