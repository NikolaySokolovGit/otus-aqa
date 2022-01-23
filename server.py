import http
import logging
import re
import socket
from collections import namedtuple

host = '192.168.0.102'
port = 8080
buf_size = 2048


logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)


def parse_data(data):
    ParsedData = namedtuple('ParsedData', ('method', 'status', 'headers'))
    data = data.decode()
    method = re.search(r"(GET|PUT|DELETE|POST|OPTIONS)", data).group()
    status = re.search(r"status=\d*", data)
    if status:
        status = status.group().split('=')[1]
    headers = [header for header in data.split('\r\n')[1:] if header]
    return ParsedData(method, status, headers)


def prepare_data(parsed_data, source_address):
    try:
        status = http.HTTPStatus(parsed_data.status)
    except ValueError:
        status = http.HTTPStatus(http.HTTPStatus.OK)
    status_line = f'HTTP/1.1 {status.value} {status.name}'
    headers = '\r\n'.join((status_line, *parsed_data.headers))
    body = '\r\n'.join((
        f'Request method: {parsed_data.method}',
        f'Request source: {source_address}',
        *parsed_data.headers
    ))
    result = '\r\n\r\n'.join((headers, body)).encode()
    return result


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(1)
        logger.info(f'Listening on {host}:{port}')

        while True:
            conn, address = sock.accept()
            while True:
                data = conn.recv(buf_size)
                logger.info(f'Request from {address}')
                if data:
                    logger.info(f'Request data:\n{data.decode()}')
                    response_data = prepare_data(parse_data(data), address)
                    conn.send(response_data)
                    logger.debug(f'Sent data:\n{response_data}')
                else:
                    conn.close()
                    break


if __name__ == '__main__':
    main()
