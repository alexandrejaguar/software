"""

You've got the basics down so now create something for yourself!

A fun project would be to create yourself a Pomodoro Timer that
incorporates datetime rather than just the time module. Have it display
timestamps.

This could also be applied to a stopwatch app. Use time of course but
also throw in the timestamps and even some basic calculations on the
difference between the start and end timestamps.
"""

from datetime import datetime, timedelta

POMODORO_INTERVAL = 25
BREAK_INTERVAL = 5

def start_cycle(interval=25):

    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=interval)

    return start_time, end_time


for cycle in range(4):
    # starting a pomodoro.
    start_time, end_time = start_cycle(interval=POMODORO_INTERVAL)

    print('Pomodoro #' + str(cycle+1) + ' started at ' +
          start_time.strftime('%H:%M') + '.\n' + 
          'Pomodoro executing...')

    while end_time > datetime.now():
        continue
    else:
        print('Pomodoro ended. Take a break!')

    start_time, end_time = start_cycle(interval=BREAK_INTERVAL)

    print('Break started at ' + start_time.strftime('%H:%M') + '.\n' +
          'You are on a break. Go live a little!\n')

print('Congrats! You finished an entire pomodoro cycle at ' +
      datetime.now().strftime('%H:%M') + '.')
