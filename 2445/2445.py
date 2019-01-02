import sys

N = int(sys.stdin.readline())

star_counts = 1
blank_counts = N - 1
need_to_print = []

while(star_counts < N and blank_counts > 0):
    for i in range(star_counts):
        need_to_print.append('*')
    for i in range(blank_counts):
        need_to_print.append(' ')
    for i in range(blank_counts):
        need_to_print.append(' ')
    for i in range(star_counts):
        need_to_print.append('*')
    print(''.join(need_to_print))
    need_to_print.clear()
    star_counts += 1
    blank_counts -= 1

while(star_counts >= 1 and blank_counts <= N - 1):
    for i in range(star_counts):
        need_to_print.append('*')
    for i in range(blank_counts):
        need_to_print.append(' ')
    for i in range(blank_counts):
        need_to_print.append(' ')
    for i in range(star_counts):
        need_to_print.append('*')
    print(''.join(need_to_print))
    need_to_print.clear()
    star_counts -= 1
    blank_counts += 1