import pytest
import requests

from tests.fixtures_yandex_disk import (
    get_token,
    setup_fixture,
    FIXTURES_CREATE_DIR
)


class TestYandexDisk:
    def _check_dir_created(self, dir_name):
        del_dir_url = self.dm.yd_url + 'resources'
        del_dir_params = {'path': dir_name}
        resp = requests.get(del_dir_url, headers={**self.dm.yandex_params}, params={**del_dir_params})
        return resp.status_code

    @pytest.mark.parametrize('dir_name, exp_result_create_dir, exp_result_check_dir', FIXTURES_CREATE_DIR)
    def test_create_directory_on_yandex_disk(self, dir_name, exp_result_create_dir, exp_result_check_dir):
        self.dir_name = dir_name
        assert self.dm.create_directory_on_yandex_disk(dir_name) == exp_result_create_dir
        assert self._check_dir_created(dir_name) == exp_result_check_dir

    def teardown_method(self, test_create_directory_on_yandex_disk):
        del_dir_url = self.dm.yd_url + 'resources'
        del_dir_params = {'path': self.dir_name}
        requests.delete(del_dir_url, headers={**self.dm.yandex_params}, params={**del_dir_params})