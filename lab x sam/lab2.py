from pprint import pprint
my_dict = {'first': 'so easy'}
def dict_maker(**kwargs):
    my_dict.update(**kwargs)
dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name='Михаил', age=31, wight=70, eyes_color='blue')
pprint(my_dict)