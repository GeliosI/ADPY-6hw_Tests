import pytest

from tests.fixtures_data_manager import (
    init_documents, 
    init_directories, 
    setup_fixture,
    FIXTURES_ADD_DOCUMENTS, 
    FIXTURES_ADD_SHELF, 
    FIXTURES_DEL_DOC_BY_NUMBER,
    FIXTURES_MOVE_DOC
)


class TestDataManager:
    @pytest.mark.parametrize('doc_number, type_, name, dir_number, exp_result', FIXTURES_ADD_DOCUMENTS)
    def test_add_documents(self, doc_number, type_, name, dir_number, exp_result):
        assert self.dm.add_documents(doc_number, type_, name, dir_number) == exp_result

    @pytest.mark.parametrize('dir_number, exp_result', FIXTURES_ADD_SHELF)
    def test_add_shelf(self, dir_number, exp_result):
        assert self.dm.add_shelf(dir_number) == exp_result

    @pytest.mark.parametrize('doc_number, exp_result', FIXTURES_DEL_DOC_BY_NUMBER)
    def test_del_doc_by_number(self, doc_number, exp_result):
        assert self.dm.del_doc_by_number(doc_number) == exp_result        

    @pytest.mark.parametrize('doc_number, dir_number, exp_result', FIXTURES_MOVE_DOC)
    def test_move_doc(self, doc_number, dir_number, exp_result):
        assert self.dm.move_doc(doc_number, dir_number) == exp_result               