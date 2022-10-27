from dataset_Database import get_items,add_items,delete_items,update_items

def test_get_items():
    print("testing get items")
    items = get_items()
    assert type(items) is list
    assert len(items) > 0
    assert type(items[0]) is dict
    assert 'id' in items[0].keys()
    assert 'description' in items[0].keys()
    assert type(items[0]['id']) is int
    assert type(items[0]['description']) is str
    items = get_items(id=1)
    assert type(items) is list
    assert len(items) == 1
    assert type(items[0]) is dict
    assert 'id' in items[0].keys()
    assert 'description' in items[0].keys()
    assert type(items[0]['id']) is int
    assert type(items[0]['description']) is str

import time

def random_string():
    return str(time.time())


def test_add_items():
    print("Testing Add items")
    description = random_string()
    quantity = 1
    add_items(description,quantity)
    items = get_items()
    item = items[-1]
    assert description == item['description']
    assert quantity == item['quantity']
    delete_items(item['id'])

def test_delete_items():
    print("testing delete items")
    description = random_string()
    quantity = 1
    add_items(description,quantity)
    items = get_items()
    item = items[-1]
    assert description == item['description']
    assert quantity == item['quantity']
    delete_items(item['id'])
    items = get_items()
    for item in items:
        assert description != item['description']

def test_update_items():
    print("testing Update items")
    description = random_string()
    quantity = 1
    add_items(description,quantity)
    items = get_items()
    item = items[-1]
    id = str(item['id'])
    description = item['description']
    new_desc = description.replace("1","9").replace(".",":")
    update_items(id,new_desc)
    items = get_items()
    new_found = False
    for item in items:
        if item['id'] == int(id):
            assert item['description'] == new_desc
            new_found = True
        assert item['description'] != description
    assert new_found

if  __name__ == "__main__":
    test_get_items()
    test_add_items()
    test_delete_items()
    test_update_items()
    print("done")