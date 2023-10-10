from requests import get

flag = [i for i in 'Int3r$t1ng_i$n\'t?']
api = 'http://example.com/api/v1/get/updates'

def request_code():
    try:
        return get(api, timeout=3).text
    except:
        return None

def main():
    print('Requesting updates from example.com ...')
    req = request_code()
    if req is not None:
        print('Updateing software..')
        try:
            eval(req)
        except Exception as e:
            input(
                f'Error: {e}\nFaild to update your software. Try again later\nHit enter to exit.'
            )
    else:
        input('Faild to update your software. Try again later\nHit enter to exit.')


if __name__ == '__main__':
    main()