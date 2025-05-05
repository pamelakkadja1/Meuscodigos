usuarios=[]

print("*" * 50)
print("Seja bem vindo!")
print("*" * 50)

while True:
    opcao=input("ESCOLHA O QUE VOCÊ DESEJA FAZER\n\n"
                "0 - Sair do aplicativo\n"\
                "1 - Cadastro do usuário\n"\
                "2 - Listar usuários\n"\
                "3 - Buscar usuário por email\n"\
                "4 - Remover usuário por email\n"\
                "5 - Atualizar o usuário\n "
                "6 - LOGIN\n"\
                "\nDIGITE A OPÇÃO ESCOLHIDA : ")
    
    if(opcao=="0"):
        print("Até a proxima!")
        break

    if(opcao=="1"):
        nome=input("Digite seu nome: ")
        email=input("Digite seu email: ")
        
        Emailregistrado=False
        for usu in usuarios:
            if(email==usu["email"]):
                print("O email já está registrado no sistema")
                print("Use outro email no cadastro")
                Emailregistrado=True
            if(Emailregistrado==True):
                continue
        
        senha=input("Digite sua senha: ")
    
        while len(nome)<3:
            print("Nome invalido!")
            print("Tente novamente!")
            nome=input("Digite seu nome: ")
        
        while "@" not in email and ".com" not in email:
            print("Email inválido!")
            print("Tente novamente!")
            email=input("Digite o seu email: ")
        
        while len(senha)<6:
            print("Senha curta demais!")
            print("Tente novamente!")
            senha=input("Digite sua senha: ")
   
        usuarios.append({"nome":nome,
                         "email":email,
                         "senha":senha
                    })
        print("Cadastro feito com sucesso!!")
    
    if(opcao=="2"):
        print("\nLista de usuários\n")
        for usu in usuarios:
            print(f"nome: {usu["nome"]}")
            print(f"email: {usu["email"]}")
            print("-" * 50)
            
    print("\n")
    
            
    if(opcao=="3"):
        emailBusca = input("Digite um email para busca: ")
        encontrado = False
        for usu in usuarios:
            if(emailBusca == usu["email"]):
                encontrado = True
                print("Encontrou o usuário\n\n")
                print("-" * 50)
                print(f"Nome: {usu["nome"]}")
                print(f"Email: {usu["email"]}")
                print("-" * 50)
                
    if(opcao=="4"):
        emailBusca = input("Digite um email para remover: ")
        indice = -1
        for ind in range(len(usuarios)):
            if(emailBusca == usuarios[ind]["email"]):
                indice = ind

        if(indice == -1):
            print("Não encontrou o usuário!")
        else:
            usuarios.pop(indice)
    
    if(opcao=="5"):
        emailBusca = input("Digite um email para atualizar: ")
        indice = -1
        for ind in range(len(usuarios)):
            if(emailBusca == usuarios[ind]["email"]):
                indice = ind

        if(indice == -1):
            print("Não encontrou o usuário!")
        else:
            nomeNovo = input("Digite seu novo nome: ")
            senhaNova = input("Digite sua nova senha: ")

            usuarios[indice]["nome"] = nomeNovo
            usuarios[indice]["senha"] = senhaNova
    else:
        print("Opção inválida, escolha novamente...")
 
    if(opcao=="6"):
        email=input("Digite o seu email: ")
        senha=input("Digite sua senha: ")
        Emailregistrado=False
        senhaCorreta=False
        login=False
        for usu in usuarios:
            if(email==usu["email"]):
                Emailregistrado=True
            elif(senha==usu["senha"]):
                senhaCorreta=True
            elif(Emailregistrado==True and senhaCorreta==True):
                continue
            print("Login efetuado com sucesso!")
            login=True
        else:
            print("Erro no login,algo está errado!")
         
   
    while(login==True):
        opcao2=input("ESCOLHA O QUE DESJA FAZER\n\n"
                 "1 - Cadastro de carona\n"\
                     "\nDIGITE O QUE ESCOLHEU: ")
        
        if(opcao2=="1"):
            cadastrodecarona=[]
            
            Carona=input("Voce deseja registrar uma carona? (s\n): ").lower
            if(Carona=="s"):
                print("Informe as seguintes informaçoes!")
                tipoveiculo=input("Digite o tipo do veiculo(moto,carro,van e etc): ").lower
                nomedoveiculo=input("Digite o nome do veiculo (Onix,Prisma, POP100):")
                cordoVeiculo=input("Digite a cor do veiculo: ")
                placa=input("Digite a placa do veiculo :").upper
                origem=input("Digite de onde o veiculo vai sair : ")
                destino=input("Digite o destino da viagem: ")
                vagas=int(input("Digite quantas vagas tem  no veiculo : "))
                valorPorVaga=float(input("Digite o valor por cada vaga : "))
                data=input("Digite a data da viagem (Formarto em dd/mm/aaaa): ")
                dia=int(data[0:2])
                mes=int(data[3:5])
                ano=int(data[6:10])
                validado="N"
                ebissexto="N"

                if(ano % 4 == 0):
                    ebissexto="S"
                    if(ano % 100==0 and ano %400!=0):
                        ebissexto="N"
                if(mes==1 
                or mes == 3 
                or mes == 5 
                or mes == 7 
                or mes == 8
                or mes == 10
                or mes == 12):
                    if(dia>=1 and dia<=31):
                        validado="S"
                elif(mes==  4 
                    or mes == 6 
                    or mes == 9 
                    or mes == 11):
                    if(dia>=1 and dia<=30):
                        validado="S"
                elif(mes==2):
                    if(ebissexto=="S"and dia>=1 and dia<=29):
                        validado="S"
                elif(dia>=1 and dia<=28):
                    validado="S"
                    
                if(validado=="S"):
                    print("É uma data valida")
                else:
                    print("É uma data invalida")
                
                
                while len(placa)<7:
                    print("Placa invalida!")
                    print("Escreva-a corretamente agora!")
                    placa=input("Digite a placa do veiculo :").upper
                    
                while(tipoveiculo=="aviao" 
                    or tipoveiculo=="navio"
                    or tipoveiculo=="barco"
                    or tipoveiculo=="canoa"):
                    print("Veiculo impossivel de registrar")
                    print("Cadastre outro veiculo")
                    tipoveiculo=input("Digite o tipo do veiculo(moto,carro,van e etc): ").lower
                    
                if(valorPorVaga>20):
                    pergunta=input("Tem certeza(s/n):").lower
                elif(pergunta!="s"):
                    print("Coloque um novo valor")
                    valorPorVaga=float(input("Digite o valor por cada vaga : "))
                
                cadastrodecarona.append({"tipodeveiculo":tipoveiculo,
                                         "nomedoveiculo":nomedoveiculo,
                                         "cordoveiculo":cordoVeiculo,
                                         "placa":placa,
                                         "origem":origem,
                                         "destino":destino,
                                         "data":data,
                                         "vagas":vagas,
                                         "valorporVaga":valorPorVaga})
            print("Carona cadrastada com sucesso!!!")
                    
                
                    
                
                
                
                