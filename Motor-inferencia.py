def BC():

   return [ {"¬Amiga(Ana,Nicolas)"},{"Amiga(Ana,Nicolas)"},{"¬EnviaMensaje(Ana,Nicolas)"},{"EnviaMensaje(Ana,Nicolas)"}
                         ,{"¬Responde(Nicolas, Ana)"},{"Responde(Nicolas, Ana)"}]

   


def NT():

    return {"¬Amiga(Ana,Nicolas)"}



def resolver(bc, objetivo):

    bc.append(objetivo)




    if resultado:
        print("El teorema ya estaba en la base de conocimientos. ")
    else:
        print("No se puede determinar el resultado")