# -*- coding: utf-8 -*-
"""exercícios.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-UQFD-bQ7faz7G-2q6CVfZDUHndlTlja
"""

usuariosnovos = []

usuariosatuais = []

for user in range(0, 5):
  user1 = input('\nDigite um nome de usuário:\t')
  user2 = user1.lower()
  usuariosatuais.append(user2)

for newuser in range(0, 5):
  newuser1 = input('\nDigite um nome de usuário:\t')
  newuser2 = newuser1.lower()
  usuariosnovos.append(newuser2)

for un in usuariosatuais:
  if un in usuariosnovos: 
    print('\nO nome de usuário  ' + str(un) +'  já foi utilizado')
    print('\nVocê tem que escolher outro nome de usuário:\t')
    usuariosnovos.remove(un)
    novouser = input('\nDigite um novo nome de usuário:\t')
    novouser1 = novouser.lower()
    usuariosnovos.append(novouser1)
  

print()
usuariosatuais.extend(usuariosnovos)
print('\nA lista de usuários é essa:\t' + str(usuariosatuais))