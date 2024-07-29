my_dict = {'Битва на Калке': 1223, 'Невская битва': 1240, 'Ледовое побоище': 1242, }
print('Dict:', my_dict)
print('Existing value:', my_dict['Битва на Калке'])
print('Non existing value:', my_dict.get('Куликовская битва'))
my_dict.update({'Раковорская битва': 1268, 'Битва на Ворскле': 1399})
print('Deleted value:', my_dict.pop('Невская битва'))
print('Modified dictionary:', my_dict)
print("\n")
# множества:
my_set = {1240, 1242, 1242, True, 1378, 1378, 1382, True, False, 'Битвы XIII века', 'Битвы XIV века', }
print('Set:', my_set)
my_set.add('Битва на Пьяне')
my_set.add('Битва на Воже')
my_set.remove(False)
print('Modified set:', my_set)
