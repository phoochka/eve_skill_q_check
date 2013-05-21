import api

def main():
    e_api = api.api()
    codes= {'keyID': '#######', 'vCode': 'abc'}
    print 'Checking skill queue'
    e_api.skill_check(codes)

if __name__ == '__main__':
    main()
