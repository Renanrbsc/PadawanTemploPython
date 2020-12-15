from unittest import TestCase, mock
from unittest.mock import MagicMock, Mock, patch, call
from app.Model.model_map import Map


class TestMap(TestCase):

    def test_init(self) -> None:
        # Arrange
        object_map = Map()
        # Assertion
        self.assertIsInstance(object_map, Map, 'The instance of the called object is different!')

    def test_set_and_get_map_name(self) -> None:
        # Arrange
        input_value = 'Earth'
        object_map = Map()
        # Action
        object_map.set_map_name(input_value)
        method = object_map.get_map_name()
        # Assertion
        self.assertEqual(method, 'Earth',
                         'The return of the getter method is different from the input in the setter!')

    def test_set_and_get_map_size(self) -> None:
        # Arrange
        input_value = 50
        object_map = Map()
        # Action
        object_map.set_map_size(input_value)
        method = object_map.get_map_size()
        # Assertion
        self.assertEqual(method, 50,
                         'The return of the getter method is different from the input in the setter!')

    def test_create_random_map(self) -> None:
        # Arrange
        input_value = 50
        object_map = Map()
        # Action
        object_map.set_map_size(input_value)
        object_map.create_random_map()
        result = object_map.get_global_map()
        # Assertion
        self.assertIsInstance(result, str,
                              'The return is not string!')
        self.assertEqual(len(result), 50,
                         'The return of the string size is different from the input in the setter!')

    def test_create_continents_data_on_the_map(self) -> None:
        # Arrange
        input_global_map = '000000000X0000000XXX00X000X0X0X00'
        object_map = Map()
        # Action
        object_map.set_global_map(input_global_map)
        object_map.create_continents_data_on_the_map()
        result_num_country = object_map.get_number_country()
        result_population = object_map.get_population()
        # Assertion
        self.assertIsInstance(result_num_country, int,
                              'The return is not integer!')
        self.assertIsInstance(result_population, int,
                              'The return is not integer!')
        self.assertEqual(result_num_country, 7,
                         'The return value is different from the input in the setter!')
        self.assertEqual(result_population, 25,
                         'The return value is different from the input in the setter!')

    def test_generate_map_description_data(self) -> None:
        # Arrange
        input_none = None
        input_value = {"nome definido": 'Earth',
                       "tamanho": 50,
                       "continentes": 4,
                       "população": 46,
                       "mapa": '0000000000X00000000000000X00000000000XX00000000000',
                       "defin. oceano": 'X',
                       "defin. não infectado": '0'}
        return_none = {'nome definido': '',
                       'tamanho': 0,
                       'continentes': 0,
                       'população': 0,
                       'mapa': '',
                       'defin. oceano': 'X',
                       'defin. não infectado': '0'}
        object_map = Map()
        # Action
        object_map.generate_map_description_data(input_none)
        result_none = object_map.get_map_description()
        object_map.generate_map_description_data(input_value)
        result_value = object_map.get_map_description()
        # Assertion
        self.assertIsInstance(return_none, dict,
                              'The return is not dict!')
        self.assertIsInstance(result_value, dict,
                              'The return is not dict!')
        self.assertEqual(result_none, return_none,
                         'The return value is different from the input in the setter!')
        self.assertEqual(result_value, input_value,
                         'The return value is different from the input in the setter!')

    def test_print_str_model(self) -> None:
        # Arrange
        input_map_description = {"nome definido": 'Earth',
                                 "tamanho": 50,
                                 "continentes": 4,
                                 "população": 46,
                                 "mapa": '0000000000X00000000000000X00000000000XX00000000000',
                                 "defin. oceano": 'X',
                                 "defin. não infectado": '0'}
        expected_return = f"\n------ Mapa Atualizado -------------------------------\n" \
                          f"Nome definido: Earth\n" \
                          f"Tamanho: 50\n" \
                          f"Continentes: 4\n" \
                          f"População: 46\n" \
                          f"Mapa: 0000000000X00000000000000X00000000000XX00000000000\n" \
                          f"Defin. oceano: X\n" \
                          f"Defin. não infectado: 0\n" \
                          f"Enviando ao Mapa..."
        object_map = Map()
        # Action
        object_map.generate_map_description_data(input_map_description)
        expected_model = object_map.__str__()
        # Assertion
        self.assertEqual(expected_model, expected_return,
                         'the model printout is different than expected!')
