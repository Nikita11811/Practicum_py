class Info:
    def _func_1(self):
        print('It is the half-secret function')

    def __func_2(self):
        print('It is the completely secret function ')

    def func_3(self):
        print('It is the free function')


text = Info()

text._func_1()
text.func_3()
text.__func_2()
text.func_3()
