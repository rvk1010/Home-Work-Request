import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                        'Authorization': f'OAuth {token}'}

    def upload(self, file_path: str, replace: str):
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        res = requests.get(f'{URL}/upload?path={file_path}&overwrite={replace}', headers=self.headers).json()
        with open(file_path, 'rb') as f:
            try:
                requests.put(res['href'], files={'file': f})
            except KeyError:
                print(res)


path_to_file = ""
token = ""

uploader = YaUploader(token)
print(uploader.upload(path_to_file, "true"))
