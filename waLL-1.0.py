#O projeto vai ser um robô feito para conversar e  para dar informação
#Chegar proximo a Uma linguagem humana✅
#pesquisar- Api de pesquisa
#opção criança✅
#Compartimento de Remedios, codigo usuario, reconhecimento de rosto, codigo de liberação, timer pra avisar
#avisa sobre eventos ou ocassioes
#se locomover
#ter reação colocar telinha de led e programar reações
#Modo


nome_usuario = input("Qual seu nome ?")
codigo_usario = "1"
print("""
1-Adulto
2-Criança
3-Idoso
""")

modo_comuni = (input("Qual modo você deseja"))
if modo_comuni == "2":
    print("Seja bem vindo Meu Anjinho {} qual e sua necessidade".format(nome_usuario))
    print("""
    
    1-Saude Fisica
    2-Ajuda Psicologica
    3-Quero achar Meus Pais
    4-Preciso de Ajuda
    
    """)
    tipo_necessi = input("Qual seu tipo de necessidade ?")
    if tipo_necessi == "1":
        print("i")
    elif tipo_necessi =="2":
        print("t")
    elif tipo_necessi == "3":
        print("h")
    elif tipo_necessi == "4":
        print("m")
    else:
        print("Escolha de uma opções acima")
elif modo_comuni == "1":
    print("Seja Bem Vindx {}".format(nome_usuario))
    print("Seja bem vindo {} qual e sua necessidade".format(nome_usuario))
    print("""

    1-Saude Fisica
    2-Ajuda Psicologica
    3-Quero achar Meus Pais
    4-Saber Horarios

    """)
    tipo_necessi = input("Qual seu tipo de necessidade ?")
    if tipo_necessi == "1":
        print("i")
    elif tipo_necessi == "2":
        print("t")
    elif tipo_necessi == "3":
        print("h")
    elif tipo_necessi == "4":
        input("Qual seu codigo ?")
    if codigo_usario == "1":
        print("""Seus Horarios são 
        
        Seg|10:40-12:20|Lazer
        Quinta|17:00-20:25|Sessão de Cinema
        
        """)
    else:
        print("Escolha de uma opções acima")
else:
    print("Seja Bem Vindx Senhora(o) {}".format(nome_usuario))
    print("Seja Bem Vindx {}".format(nome_usuario))
    print("Seja bem vindo {} qual e sua necessidade".format(nome_usuario))
    print("""

       1-Saude Fisica
       2-Ajuda Psicologica
       3-Saber Horarios

       """)
    tipo_necessi = input("Qual seu tipo de necessidade ?")
    if tipo_necessi == "1":
        print("i")
    elif tipo_necessi == "2":
        print("t")
    elif tipo_necessi == "3":
        input("Qual seu codigo ?")
    if codigo_usario == "1":
        print("""Seus Horarios são 

        Seg|10:40-12:20|Lazer
        Quinta|17:00-20:25|Sessão de Cinema""")
    else:
        print("Escolha de uma opções acima")
