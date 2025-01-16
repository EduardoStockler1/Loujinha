#from inspect import signature
from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt-BR')
#print(signature(fake.random_number))

def make_product():
    return{
        'id': fake.random_number(fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'created_at': fake.date_time(),
        'updated_at': fake.date_time(),
        'price': fake.pricetag(),
        'quantity': randint(1, 100),
        'author':{
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category':{
            'name': fake.word(),
        },
        'cover': {
            'url': 'https://loremflickr.com/%d/%d/' % rand_ratio(),
        },

    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_product())