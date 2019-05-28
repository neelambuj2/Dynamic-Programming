def get_inline( account_relation: dict, current_key):
    if type(account_relation) is dict:
        for key in account_relation.keys():
            iterable = get_inline(account_relation[key], key)
            for element in iterable:
                if element != key:
                    yield (key + "." + element)
                else:
                    yield key
    else:
        yield current_key


def get_inline2(user: dict):
    temp = []
    for key in user.keys():
        temp.append(key)

    return temp

account_relation =  {
        "Id": "79c911c6-ddb3-11e8-92eb-6067204e771a",
        "email_id": "abcd@trimble.com",
        "firstname": "Neelambuj",
        "surname": "singh",
        "places": [
            {
                "Isactive": "yes",
                "Start": "4444",
                "End": "1234",
                "place_id": "2345"
            }
        ],
        "contacts": {
            "phones": {
                "home": "123456",
                "work": "78894",
                "mobile": "789789",
                "other": "885588"
            },
            "emails": {
                "personal": "mymaill@trimble.com",
                "business": "mymail2@trimble.com",
                "other": "mymail3@trimble.com"
            }
        }
    }

#inline_dict = list(get_inline(account_relation, None))

print(get_inline2(account_relation))