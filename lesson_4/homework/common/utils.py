from messanger.lesson_4.homework.common.variables import *
from messanger.lesson_4.homework.errors import IncorrectDataRecivedError, NonDictInputError
import json
import sys
sys.path.append('../')
from messanger.lesson_4.homework.decos import log


# Утилита приёма и декодирования сообщения
# принимает байты выдаёт словарь, если приняточто-то другое отдаёт ошибку значения
@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        else:
            raise IncorrectDataRecivedError
    else:
        raise IncorrectDataRecivedError


# Утилита кодирования и отправки сообщения
# принимает словарь и отправляет его
@log
def send_message(sock, message):
    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
