import api

def main():
    e_api = api.api()
    phoo_codes = {'keyID': '1355209', 'vCode': 'KXBQZ1eAXiXI5BtOOb6FeIEUmBQHK7uiTqjLdnoTfG38pj9xUxbicojY4PiaGjzf'}
    melkor_codes = {'keyID': '2058644', 'vCode': 'icTlIoiKC1trZRk0qmp3SMliPb5p1OHCtfNlpLrFqKqu345J5QylWjVLA51tPbvP'}
    print 'Checking skill queue for Phoo'
    e_api.skill_check(phoo_codes)
    print 'Checking skill queue for Mel'
    e_api.skill_check(melkor_codes)

if __name__ == '__main__':
    main()
