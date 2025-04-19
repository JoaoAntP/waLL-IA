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
acesso_usuario = input("Qual seu codigo de acesso ?")
codigo_usuario = acesso_usuario
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
        print(""""
        
        1-Assitencia (Urgente)
        2-Dor no corpo
        3-Doença Contagiosa
        4-Fratura
        5-Remedio
        
        
        """)
    tp_ncf = input("Qual seu numero você deseja selecionar")
    if tp_ncf == "1":
        print("Um aviso foi enviado!, Um medico chegara em breve")
    elif tp_ncf == "2":
        print(""" Em qual região do seu corpo a dor se encontra ?
        
        1-Cabeça
        2-Costa
        3-Peito
        4-Braços
        5-Pernas
        
        """)
        local_dor = input("Qual das opções acima")
        if local_dor == "1":
            print("a")
        elif local_dor == "2":
            print("b")
        elif local_dor == "3":
            print("c")
        elif local_dor == "4":
            print("d")
        elif local_dor == "5":
            print("e")
        else:
            print("Erro")
    elif tipo_necessi =="3":
        nivel_parentesco = input("Quem estava com você Pai/Mãe/Avô")
        nome_pais = input("Nome do seu responsalvel")
        msg1= "Vamos chamar seu(a) {} Vamos chamar por {} nos altos falantes".format(nivel_parentesco, nome_pais)
        print(msg1)
    elif tipo_necessi == "4":
        print("h")
    elif tipo_necessi == "5":
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
    if codigo_usuario == "1":
        print("""Seus Horarios são 
        
        Seg|10:40-12:20|Lazer
        Quinta|17:00-20:25|Sessão de Cinema
        
        """)
    else:
        print("Escolha de uma opções acima")
elif modo_comuni == "3":
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
else:
    print("Erro")