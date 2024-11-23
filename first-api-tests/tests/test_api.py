from tests_class import TestCase


class TestID:

    def test_first(self):
        test_case = TestCase()
        id_new_animal = test_case.create_animal('Orlock')
        id_find_animal = test_case.find_animal(id_new_animal)['id']
        assert id_new_animal == id_find_animal, (
            "[FAILED]: Ids doesnt match {} and {}".format(id_new_animal, id_find_animal))

    def test_two(self):
        test_case = TestCase()
        # id питомца
        id_new_animal = test_case.create_animal('Cat Cat Cat')
        id_find_animal = test_case.find_animal(id_new_animal)['id']
        assert id_new_animal == id_find_animal, (
            "[FAILED]: Ids doesnt match {} and {}".format(id_new_animal, id_find_animal))
        test_case.delete_animal(id_new_animal)
        id_new_find_animal = test_case.find_animal(id_new_animal)['id']
