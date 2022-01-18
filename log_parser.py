import argparse
import json
import os
import re
from collections import defaultdict, namedtuple
from operator import itemgetter

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-p', dest='path', action='store', required=True)
args = arg_parser.parse_args()


req_info = namedtuple("ReqInfo", ('method', 'url', 'ip', 'duration', 'datetime'))


def parse_ip(line, ips):
    ip_match = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", line)
    if ip_match is not None:
        ip = ip_match.group()
        ips[ip] += 1
        return ip


def parse_method(line, methods):
    method_match = re.search(r"] \"(POST|GET|PUT|DELETE|HEAD)", line)
    if method_match is not None:
        method = method_match.group(1)
        methods[method] += 1
        return method


def create_json(top3ip, top_method, total_requests, durations):
    result = {
        "most_frequent_ips": top3ip,
        "most_frequent_method": top_method,
        "total_requests": total_requests,
        "longest_durations": [{
            "method": req.method,
            "url": req.url,
            "ip": req.ip,
            "duration": req.duration,
            "datetime": req.datetime
        } for req in durations]
    }
    return json.dumps(result, indent=4)


def parse_file(file_path):
    file_name = os.path.basename(file_path)
    methods = defaultdict(int)
    ips = defaultdict(int)
    durations = []
    with open(file_path) as file:
        for line in file.readlines():
            ip = parse_ip(line, ips)
            method = parse_method(line, methods)
            duration = int(line.split()[-1])
            if len(durations) < 3 or duration > min([element.duration for element in durations]):
                dt = re.search(r'\[.*]', line).group().strip('[]')
                url = re.search(r"(\"\S*){2}", line).group().strip('"')
                element = req_info(method, url, ip, duration, dt)
                durations.append(element)
                durations.sort(key=lambda x: x.duration, reverse=True)
                if len(durations) > 3:
                    durations.pop()
    top3ip = {key: value for key, value in sorted(ips.items(), key=itemgetter(1), reverse=True)[:3]}
    top_method = {key: value for key, value in sorted(methods.items(), key=itemgetter(1), reverse=True)[:1]}
    total_requests = sum(methods.values())
    result_json = create_json(top3ip, top_method, total_requests, durations)
    with open(f"{file_name}.json", 'w') as file:
        json.dump(result_json, file)
    print(f"{file_name}:\n{result_json}\n")


def main():
    if os.path.isfile(args.path):
        if args.path.endswith('.log'):
            parse_file(os.path.abspath(args.path))
        else:
            print('specify path to "*.log" file or directory')
    elif os.path.isdir(args.path):
        for file in [f for f in os.listdir(args.path) if f.endswith('.log')]:
            parse_file(os.path.abspath(file))
    else:
        print('path not found')


if __name__ == '__main__':
    main()
