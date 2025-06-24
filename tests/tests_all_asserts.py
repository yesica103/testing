import unittest
SERVER = "server B"  # Simulando un servidor diferente
class AllAssertsTest(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(1, 1)
        self.assertEqual("hello", "hello")

    def test_assert_true(self):
        self.assertTrue(True)
        self.assertTrue(1 < 2)   

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int('No soy un  numero')
    def test_assert_in(self):
        self.assertIn(1, [1, 2, 3])
        self.assertIn("hello", "hello world")
        self.assertNotIn(4, [1, 2, 3])
    
    def test_assert_dicts_equal(self):
        user = {'name': 'Yesica', 'last_name': 'Tique', 'age': 27}

        self.assertDictEqual(user, {'name': 'Yesica', 'last_name': 'Tique', 'age': 27})
        self.assertNotEqual(user, {'name': 'Yesica', 'last_name': 'Tique', 'age': 30})

    def test_assert_set_equal(self):
        set1 = {1, 2, 3}
        set2 = {3, 2, 1}
        self.assertSetEqual(set1, set2)

    @unittest.skip("Trabajo en proceso, sera habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("hola", "chao" )
    
    @unittest.skipIf(SERVER == "server B", "Saltada porque no estamos en el servidor")
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 2, "Esto es un fallo esperado")

