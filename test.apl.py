#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import random
import time


__SERVER_URL = 'http://localhost:5000/api/'


def prepare_consumable(hotelid, rack, level):
    api = __SERVER_URL+"SpxDXClient/PrepareConsumable?taskid="+new_task_id()
    return post(api, {'hotelId': hotelid, 'rackIndex': rack, 'index': level})


def accept_consumable(hotelid, rack, level):
    api = __SERVER_URL+"SpxDXClient/AcceptConsumable?taskid="+new_task_id()
    return post(api, {'hotelId': hotelid, 'rackIndex': rack, 'index': level})


def move_to(target):
    """
    机械臂移动到指定位置
    :param target: 目标位置
    :return:
    """
    api = __SERVER_URL+"SpxDXClient/MoveTo?taskid="+new_task_id()+"&targetDeviceId="+target
    return post(api)


def grasp(target):
    """
    机械臂抓取指定位置的耗材
    :param target:
    :return:
    """
    api = __SERVER_URL+"SpxDXClient/GrabConsumable?taskid="+new_task_id()+"&targetDeviceId="+target
    return post(api)


def lay_down(target):
    """
    机械臂放下耗材
    :param target:
    :return:
    """
    api = __SERVER_URL+"SpxDXClient/LayDownConsumable?taskid="+new_task_id()+"&targetDeviceId="+target
    return post(api)


def open_door(target):
    """
    堆栈开门
    :param target:
    :return:
    """
    api = __SERVER_URL+"SpxDXClient/LayDownConsumable?taskid="+new_task_id()+"&targetDeviceId="+target
    return post(api)


def retry(func):
    def wrapper(*args, **kwargs):
        while func(*args, **kwargs).status_code != 200:
            time.sleep(1)
    return wrapper


@retry
def post(url, data=None):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json-patch+json'}
    return requests.post(url, data=json.dumps(data), headers=headers)


def new_task_id():
    return str(random.randint(1, 9999999))


while True:
    move_to('HotelA')
    grasp('HotelA')
    move_to('MGISP100EX')
    lay_down('MGISP100EX')

    grasp('MGISP100EX')
    move_to('HotelA')
    lay_down('HotelA')
