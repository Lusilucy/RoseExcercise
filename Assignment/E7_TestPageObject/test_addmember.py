import pytest
import yaml

from PageObiect.main_page import Main


with open('member.yaml') as f:
    for member in yaml.safe_load_all(f):
        print(member)


@pytest.mark.parametrize('name, id, Tel', member)
class TestAddmember:
    @pytest.mark.skip
    def test_addmember_by_contacts(self, name, id, Tel):
        main = Main()
        add_member = main.goto_contacts().click_add_member().add_member(name, id, Tel)
        list = add_member.list()
        assert Tel in list

    def test_addmember_by_main(self, name, id, Tel):
        main = Main()
        add_member = main.click_add_member().add_member(name, id, Tel)
        list = add_member.list()
        assert Tel in list
