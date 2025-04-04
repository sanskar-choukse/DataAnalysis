def addition(a,b):
    return a+b

def subtract(a,b):
    return a-b

def get_name(person):
    return person['name']

people=[
    {'name':'sanskar','age':21},
    {'name':'shiva','age':24},
    {'name':'shanker','age':22}
]

number=[1,2,3,4,5,6,7,8,9,10]



def arg_kwrgs(*args,**kwargs):
    print('args',args)
    print('kwargs',kwargs)

# arg_kwrgs("sanskar",1,2,3,name="shiv",age=21)
# arg_kwrgs('a','b','c',2,name='shukvimla',age=23) 

