import datetime
from collections import namedtuple, defaultdict
from subprocess import run


def parse_line(line):
    fields = ('user', 'pid', 'cpu', 'mem', 'vsz', 'rss', 'tty', 'stat', 'start', 'time', 'command')
    len_fields = len(fields)
    result = line.split()
    if len(result) > len_fields:
        last_idx = len_fields - 1
        result[last_idx] = ' '.join((elem for elem in result[last_idx:]))
        result = result[:len_fields]
    PSAux = namedtuple('PSAux', ('user', 'pid', 'cpu', 'mem', 'vsz', 'rss', 'tty', 'stat', 'start', 'time', 'command'))
    types = (str, int, float, float, int, int, str, str, str, str, str)
    return PSAux(*(tp(value) for tp, value in zip(types, result)))


def main():
    user_dict = defaultdict(int)
    total_cpu = 0
    total_mem = 0
    biggest_cpu = (None, -1)
    biggest_mem = (None, -1)
    result = run(('ps', 'aux'), capture_output=True)
    output = result.stdout.decode().strip().split('\n')
    for line in output[1:]:
        line = parse_line(line)
        user_dict[line.user] += 1
        total_cpu += line.cpu
        total_mem += line.mem
        if line.cpu > biggest_cpu[1]:
            biggest_cpu = (line.command, line.cpu)
        if line.mem > biggest_mem[1]:
            biggest_mem = (line.command, line.mem)
    user_proc = '\n'.join((f'{key}: {value}' for key, value in user_dict.items()))
    result = f"Отчет о состоянии системы:\n" \
             f"Пользователи системы: {', '.join(user_dict.keys())}\n" \
             f"Процессов запущено: {len(output) - 1}\n\n" \
             f"Пользовательских процессов:\n{user_proc}\n" \
             f"Всего памяти используется: {total_mem}%\n" \
             f"Всего CPU используется: {total_mem}%\n" \
             f"Больше всего памяти использует: {biggest_mem[0]}\n" \
             f"Больше всего CPU использует: {biggest_cpu[0][:20]}\n"
    print(result)

    with open(f'{datetime.datetime.now().strftime("%d-%m-%y-%H-%M-%S")}-scan.txt', 'w') as file:
        file.write(result)


if __name__ == '__main__':
    main()
