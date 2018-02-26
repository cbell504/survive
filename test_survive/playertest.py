from survive.player.playermodel import Player

import unittest


class PlayerTestCase(unittest.TestCase):

    def basic_test(self):
        print("Test")
        player = Player("Test_Player")
        self.assertEqual(player.get_health(), 10)


if __name__ == '__main__':
    unittest.main()
