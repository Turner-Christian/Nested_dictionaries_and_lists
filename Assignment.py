# 1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1
x[1][0] = 15
# 2
students[0]['last_name'] = 'Bryant'
# 3
sports_directory['soccer'][0] = 'Andres'
# 4
z[0]['y'] = 30



# 2
def iterateDictionary(student):
    for i in range(len(student)):
        firstName = student[i]['first_name']
        lastName = student[i]['last_name']
        print(f'first_name - {firstName}, last_name - {lastName}')


# 3
def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])

# 4
def printInfo(some_dict):
    for dict in some_dict:
        print('')
        print(len(some_dict[dict]), dict.upper())
        for i in range(len(some_dict[dict])):
            print(some_dict[dict][i])