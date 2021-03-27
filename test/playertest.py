from survive.models.entity.player import Player

import unittest


class PlayerTestCase(unittest.TestCase):
    def test_check_health(self):
        print("Checking Health")
        player = Player("Test_Player")
        self.assertEqual(player.get_health(), 10)

if __name__ == '__main__':
    unittest.main()
