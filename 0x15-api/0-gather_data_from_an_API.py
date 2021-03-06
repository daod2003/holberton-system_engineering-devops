#!/usr/bin/python3

import requests
from sys import argv

if __name__ == '__main__':
    idU = argv[1]
    urlUser = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(idU)).json()
    listTodo = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(idU)).json()
    pendingList = []
    for pending in listTodo:
        if pending.get('completed') is True:
            pendingList.append(pending.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(urlUser.get('name'),
                                                          len(pendingList),
                                                          len(listTodo)))
    print('\n'.join('\t {}'.format(pending) for pending in pendingList))
