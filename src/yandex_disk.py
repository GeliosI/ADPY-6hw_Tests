import requests


class YandexDisk:
    yd_url = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self, ya_token):
        self.yandex_params = {'Authorization': f'OAuth {ya_token}'}

    def create_directory_on_yandex_disk(self, dir_name):
        """Сreates a new directory on Yandex disk

        Keyword Arguments:
            - dir_name -- directory to be created

        """

        create_dir_url = self.yd_url + 'resources'
        create_dir_params = {'path': dir_name}

        resp = requests.put(create_dir_url, headers={**self.yandex_params}, params={**create_dir_params})
        return resp.status_code
