from pprint import pprint

from pydantic import BaseModel

from pydantic_br import Certidao


class Pessoa(BaseModel):
    certidao1: Certidao
    certidao2: Certidao


p = Pessoa(
    certidao1="203213.01.55.2019.4.03108.343.1021163-86",
    certidao2="20321301552019403108343102116386",
)


print(p)
# > certidao='203213.01.55.2019.4.03108.343.1021163-86'

print(p.model_dump_json())
# > {"certidao": "203213.01.55.2019.4.03108.343.1021163-86"}

pprint(p.model_json_schema())
# > {'properties': {'certidao1': {'example': ['00000000000000000000000000000000',
#                                           '000000.00.00.0000.0.00000.000.0000000-00'],
#                               'format': 'certidao',
#                               'mask': {'format': 'XXXXXX.XX.XX.XXXX.X.XXXXX.XXX.XXXXXXX-XX',
#                                        'required': False},
#                               'title': 'Certidao1',
#                               'type': 'string'},
#                 'certidao2': {'example': ['00000000000000000000000000000000',
#                                           '000000.00.00.0000.0.00000.000.0000000-00'],
#                               'format': 'certidao',
#                               'mask': {'format': 'XXXXXX.XX.XX.XXXX.X.XXXXX.XXX.XXXXXXX-XX',
#                                        'required': False},
#                               'title': 'Certidao2',
#                               'type': 'string'}},
#  'required': ['certidao1', 'certidao2'],
#  'title': 'Pessoa',
#  'type': 'object'}
