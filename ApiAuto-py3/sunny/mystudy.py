#随机数据
# from mimesis import Person
# person=Person('en')
# a=person.full_name()
# b=person.occupation()
# c=person.email()
# d=person.telephone()
# print(a,'\n',b,'\n',c,'\n',d)
#测试库：memesis
# from mimesis.schema import Field,Schema
# from mimesis.enums import Gender
# _=Field('en')
# description=(
#     lambda:{
#         'id':_('uuid'),
#         'name':_('text.word'),
#         'version':_('version',pre_release=True),
#         'timestamp':_('timestamp',posix=False),
#         'owner':{
#             'email':_('person.email',key=str.lower),
#             'token':_('token_hex'),
#             'creator':_('full_name',gender=Gender.FEMALE)
#         }
#
#     }
# )
# schema=Schema(schema=description)
# a=schema.create(iterations=1)
# print (a)



