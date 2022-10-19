class Calculate:
    def __init__(self, phrase):
        self.phrase = phrase
        self.result = None
        self.run()

    def run(self):
        norm_phrase = self.normalization_phrase(self.phrase)
        self.result = self.calculate(norm_phrase)

    def calculate(self, expression: str):
        """Вычисление общего выражения"""
        s = str(expression)
        try:
            x = float(s)
            return x
        except ValueError:
            pass
        for c in ('-', '+', '*', '/'):
            left, op, right = s.partition(c)
            if op == '*':
                return self.calculate(left) * self.calculate(right)
            elif op == '/':
                return self.calculate(left) / self.calculate(right)
            elif op == '+':
                return self.calculate(left) + self.calculate(right)
            elif op == '-':
                return self.calculate(left) - self.calculate(right)

    def normalization_phrase(self, phrase: str):
        """Вычисление выражений внутри всех скобок"""
        if "(" in phrase and ')' in phrase:
            list_phrase = list(phrase)
            first_index = list_phrase.index('(')
            last_index = list_phrase.index(')')
            one_phrase = list_phrase[first_index + 1:last_index]
            one_phrase_str = ''.join(one_phrase)
            del list_phrase[first_index:last_index + 1]
            result = str(self.calculate(one_phrase_str))
            list_phrase.insert(first_index, result)
            phrase = ''.join(list_phrase)
            return self.normalization_phrase(phrase)
        return phrase
