from game.field import Field


class Writer:
    @staticmethod
    def parse_field_to_text(field: Field):
        text = ""

        for line in field.cells:
            text += ' '.join(
                str(cell.value) if cell.is_unpainted else "#" for cell in
                line)
            text += '\n'

        return text