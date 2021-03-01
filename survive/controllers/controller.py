from survive.view import View


class Controller(object):
    def __init__(self, player):
        self._view_text = {}
        self._view = View(self._view_text)
        self._player = player

    def start(self):
        self.game_loop()
        return self._player

    def game_loop(self):
        loop_condition = 0
        while loop_condition != 999:
            try:
                self._view.update_view()
                player_input = int(input("Enter an action.\n"))
                self._view.clear_view()
                loop_condition = self.game_loop_by_class(player_input, loop_condition)
            except ValueError:
                print("Please enter a number.\n")

    def game_loop_by_class(self, player_input, loop_condition):
        pass

    def get_view(self):
        return self._view

    def set_view(self, view):
        self._view = view

    def get_view_text(self):
        return self._view_text

    def set_view_text(self, view_text):
        self._view_text = view_text
