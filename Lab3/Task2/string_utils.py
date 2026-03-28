import re

class StringUtils:
    @staticmethod
    def find_word_boundary_left(text, col):
        if col == 0:
            return 0
        left = text[:col]
        if not left:
            return 0
        matches = list(re.finditer(r'([a-zA-Z]+|[^a-zA-Z]+)\s*', left))
        if not matches:
            return 0
        return matches[-1].start()

    @staticmethod
    def find_word_boundary_right(text, col):
        if col >= len(text):
            return len(text)
        right = text[col:]
        match = re.match(r'([a-zA-Z]+|[^a-zA-Z]+)\s*', right)
        if match:
            return col + match.end()
        return len(text)