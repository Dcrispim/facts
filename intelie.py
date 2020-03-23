# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Considere um modelo de informação, onde um registro é representado por uma "tupla".
# Uma tupla (ou lista) nesse contexto é chamado de fato.

# Exemplo de um fato:
# ('joão', 'idade', 18, True)

# Nessa representação, a entidade (E) 'joão' tem o atributo (A) 'idade' com o valor (V) '18'.

# Para indicar a remoção (ou retração) de uma informação, o quarto elemento da tupla pode ser 'False'
# para representar que a entidade não tem
# para representar que a entidade não tem mais aquele valor associado aquele atributo.


# Como é comum em um modelo de entidades, os atributos de uma entidade pode ter cardinalidade 1 ou N (muitos).

# Segue um exemplo de fatos no formato de tuplas (i.e. E, A, V, added?)
facts = [
  ('gabriel', 'endereço', 'av rio branco, 109', True),
  ('joão', 'endereço', 'rua alice, 10', True),
  ('joão', 'endereço', 'rua bob, 88', True),
  ('joão', 'telefone', '234-5678', True),
  ('joão', 'telefone', '91234-5555', True),
  ('joão', 'telefone', '234-5678', False),
  ('gabriel', 'telefone', '98888-1111', True),
  ('gabriel', 'telefone', '56789-1010', True),
]
# Vamos assumir que essa lista de fatos está ordenada dos mais antigos para os mais recentes.


# Nesse schema,
# o atributo 'telefone' tem cardinalidade 'muitos' (one-to-many), e 'endereço' é 'one-to-one'.
schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]


# Nesse exemplo, os seguintes registros representam o histórico de endereços que joão já teve:
#  (
#   ('joão', 'endereço', 'rua alice, 10', True)
#   ('joão', 'endereço', 'rua bob, 88', True),
#)
# O objetivo desse desafio é escrever uma função que retorne quais são os fatos 
# vigentes sobre essas entidades.
# Ou seja, quais são as informações que estão valendo no momento atual.
# A função deve receber `facts` (todos fatos conhecidos) e `schema` como argumentos.


def current_facts(_facts, schema):
  Atributos = {}
  DB = {}
  for attr in schema:
    Atributos[attr[0]]=attr[-1]


  for _fact in _facts:

    if _fact[0] not in DB.keys():      
      DB[_fact[0]]={}
    
    _attr = _fact[1]

   
    _exclude = []
    if Atributos[_attr]=='one':
      for k in DB[_fact[0]].keys():
        if DB[_fact[0]][k] == _attr:
          _exclude.append(k)

    for at in _exclude:
      del DB[_fact[0]][at]  

    if _fact[-1]:

      DB[_fact[0]].update({

        _fact[2]:_fact[1]

    })
    else:
      try:
        del DB[_fact[0]][_fact[2]]
      except KeyError:
        pass


  out = []
  for key in DB.keys():
    for _attr in DB[key]:
      out.append((key, DB[key][_attr], _attr, True))
  
  return out




for t in current_facts(facts, schema):
  print(t)