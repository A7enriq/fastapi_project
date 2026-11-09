import requests

def get_all_items():
    url = 'http://127.0.0.1:8000/getitems/'
    response = requests.get(url)

    if response.status_code != 200:
        return "ERROR"
    else:
        return response.json()

def add_item(new_item):
    url = f'http://127.0.0.1:8000/add/{new_item}'
    response = requests.post(url)


    if response.status_code != 200:
        return "ERROR"
    else:
        return response.json()

if __name__ == '__main__':
    # print(get_all_items())
    print(add_item(145))

def delete_item(new_item):
    url = f'http://127.0.0.1:8000/deleteitem?item'{new_item}'
    response = requests.post(url)    