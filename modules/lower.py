from mod_base import *


class Lower(Command):
    def run(self, app, editor):
        line_nums = []
        for cursor in editor.cursors:
            if cursor.y not in line_nums:
                line_nums.append(cursor.y)
                new_data = editor.lines[cursor.y].get_data().lower()
                editor.lines[cursor.y].data = new_data

module = {
    "class": Lower,
    "name": "lower",
}
