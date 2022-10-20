from datetime import datetime as dt

def result_loger(data):
    time = dt.now().strftime('%H:%M')
    with open('Output.txt', 'a') as file:
        file.write(f'{time}: Expression: {data}\n')