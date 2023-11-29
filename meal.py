def main():
    what = convert(input('What time is it? ').strip().lower())

    # what time is it?
    match int(what):
        case 7:
            print('breakfast time')
        case 13:
            print('lunch time')
        case 18:
            print('dinner time')
        case _:
            return 0

def convert(time):

    # seperates input to three pieces: hour, minutes, and that thing (a.m. and p.m.)
    hours, min_init = time.split(':')
    hr = int(hours)
    min = None
    indicator = ' '

    # handles 12-hour format
    if min_init.endswith('a.m.') or min_init.endswith('p.m.'):
        minutes, indicator = min_init.split(' ')
        min = int(minutes)
    else:
        min = int(min_init)

        if indicator.find('p.m.') != -1:
            hr = hr + 12

        # 12:00 a.m. || 12:00 p.m.
        if hr == 12 and indicator.find('a.m.') != -1:
            hr = 0
        elif hr == 24 and indicator.find('p.m.') != -1:
            hr = hr - 12

    return hr + (min / 60)

if __name__ == "__main__":
    main()