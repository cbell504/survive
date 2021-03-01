from survive.view import View


class Controller(object):
    def __init__(self):
        self._view_text = ""
        self._view = View(self._view_text)

    def get_view(self):
        return self._view

    def set_view(self, view):
        self._view = view

    def get_view_text(self):
        return self._view_text

    def set_view_text(self, view_text):
        self._view_text = view_text
