# usare %s nel modulo logging

nome = "Mario"
eta = 30


messaggio = "Ciao %s" % nome
# Ciao Mario


messaggio = "Ciao %s , hai %s anni" % (nome, eta)
# Ciao Mario , hai 30 anni


messaggio2 = "Ciao %(nome)s , hai %(eta)s anni" % {"nome": nome, "eta": eta}
# Ciao Mario , hai 30 anni
