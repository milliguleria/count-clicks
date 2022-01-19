import json
from unittest import result


def count_clicks(domain_dict):
    result = {}
    domain_dict = json.loads(domain_dict)

    for domain, val in domain_dict.items():
        try:
            result[domain] += val
        except:
            result[domain] = val
        all_dom = domain.split(".")[1:]
        temp = ""
        for idx, i in enumerate(reversed(all_dom)):
            temp = str(i) + "." + temp
            if idx == 0:
                temp = temp[:-1]
            try:
                result[temp] += val
            except:
                result[temp] = val
    return result


if __name__ == '__main__':
    domain_dict = '{"amazon.com":23,"google.co.uk":15,"google.com":7,"amazon.co.uk":9,"london.gov.uk":4}'
    result = count_clicks(domain_dict)
    print(result)
