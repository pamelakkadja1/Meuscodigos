usuarios=[]
usuariologado={}
cadastrodecarona={}
reservacarona={"Carro":["A1","A2","A3","A4"],
               "Moto":["B1"]}

print("*" * 50)
print("Seja bem vindo!")
print("*" * 50)

#PRIMEIRO MENU: CADASTRO DO USUARIO PARA TER O LOGIN
while True:
    opcao=input("ESCOLHA O QUE VOCÊ DESEJA FAZER\n\n"
                "0 - Sair do aplicativo\n"\
                "1 - Cadastro do usuário\n"\
                "2 - LOGIN\n"\
                "\nDIGITE A OPÇÃO ESCOLHIDA : ")
    
#QUEBRA PARA SAIR DO APLICATIVO  
    if(opcao=="0"):
        print("Até a proxima!")
        break

#CADASTRO 
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
        print("*" * 50)


#LOGIN,SEGUNDO MENU APARTIR DO LOGIN
    if(opcao=="2"):
        email=input("Digite o seu email: ")
        senha=input("Digite sua senha: ")
        login=False
        for usu in usuarios:
            if(email==usu["email"] and senha==usu["senha"] ):
                login=True
                usuariologado=usu
                break
        if(login==False):
            print("Erro no login,algo está errado!") 
         
#SEGUNDO MENU(SO USUARIOS LOGADOS)
        while(login==True):
            opcao2=input("ESCOLHA O QUE DESJA FAZER\n\n"
                    "0 -Logout\n"\
                    "1 - Cadastro de carona\n"\
                    "2 - Lista de caronas disponiveis\n"\
                    "3 - Buscar carona\n"\
                    "4 - Reserva de Carona\n"\
                        "\nDIGITE O QUE ESCOLHEU: ")
            
#LOGOUT(QUEBRA PARA VOLTAR PARA O PRIMEIRO MENU)
            if(opcao2=="0"):
                print("Até mais!")
                break
            
#CADASTRO DE UMA CARONA       
            if(opcao2=="1"):
                cadastrodecarona=[]
                    
                print("Informe as seguintes informaçoes!")
                emaildomotorista=usuariologado["email"]
                tipoveiculo=input("Digite o tipo do veiculo(moto ou carro): ").lower()
                nomedoveiculo=input("Digite o nome do veiculo (Onix,Prisma, POP100):")
                cordoVeiculo=input("Digite a cor do veiculo: ")
                placa=input("Digite a placa do veiculo :").upper()
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
                        
                while (len(placa)<7):
                    print("Placa invalida!Não é padrão do mercosul")
                    print("Escreva-a corretamente agora!")
                    placa=input("Digite a placa do veiculo :").upper()
                            
                while(tipoveiculo=="aviao" 
                    or tipoveiculo=="navio"
                    or tipoveiculo=="barco"
                    or tipoveiculo=="canoa"
                    or tipoveiculo=="van"
                    or tipoveiculo=="onibus"):
                    print("Veiculo impossivel de registrar")
                    print("Cadastre outro veiculo")
                    tipoveiculo=input("Digite o tipo do veiculo(moto,carro,van e etc): ").lower()
                            
                if(valorPorVaga>20):
                    pergunta=input("Tem certeza(s/n):").lower()
                    if(pergunta!="s"):
                        print("Coloque um novo valor")
                        valorPorVaga=float(input("Digite o valor por cada vaga : "))
                            
                        cadastrodecarona.append({"emaildomotorista":emaildomotorista,
                                                    "tipodeveiculo":tipoveiculo,
                                                    "nomedoveiculo":nomedoveiculo,
                                                    "cordoveiculo":cordoVeiculo,
                                                    "placa":placa,
                                                    "origem":origem,
                                                    "destino":destino,
                                                    "data":data,
                                                    "vagas":vagas,
                                                    "valorporVaga":valorPorVaga})
                print("Carona cadrastada com sucesso!!!")
                
#LISTA DE CARONAS CADASTRADAS (Não aparecendo no terminal)
            if(opcao2=="2"):
                print("*"*50)
                print("\nLista de Caronas\n")
                for car in cadastrodecarona:
                    if(car["vagas"]>0):
                        print(f"Email do motorista:{car["emaildomotorista"]} ")
                        print(f"Veiculo: {car["tipodeveiculo"]}")
                        print(f"Nome do veiculo: {car["nomedoveiculo"]}")
                        print(f"Cor do veiculo: {car["cordoveiculo"]}")
                        print(f"A placa do veiculo: {car["placa"]}")
                        print(f"Saída da viagem : {car["origem"]}")
                        print(f"Destino da viagem: {car["destino"]}")
                        print(f"Data da viagem : {car["data"]}")
                        print(f"Vagas disponiveis: {car["vagas"]}")
                        print(f"Valor por vaga: {car["valorporVaga"]}")
#BUSCA POR CARONA
            if(opcao=="3"):
                saidabusca=input("Digite de onde vai sair: ") 
                destinobusca=input("Digite para onde voce quer ir: ")
                caronaencontrada=False
                if(saidabusca == {car["origem"]} and destinobusca == {car["destino"]}):
                    caronaencontrada=True
                    print("Encontrou uma carona!\n\n")
                    print("-" * 50)
                    print(f"Origem: {car["origem"]}")
                    print(f"Destino: {car["destino"]}")
                    print("-" * 50)

#RESERVA DE UMA CARONA(Não tenho certeza se esta certo)
            if(opcao2=="4"):
                escolhamotorista=input("Digite o email do motorista desejado:")
                if(escolhamotorista in {car["emaildomotorista"]}):
                    print("Carona encontrada!")
                    print(f"Email do motorista:{car["emaildomotorista"]}")
                    print(f"Veiculo:{car["tipodoveiculo"]}")  
                    print(f"Nome do veiculo : {car["nomedoveiculo"]}")    
                    print(f"Cor: {car["cordoveiculo"]}")
                    print(f"A placa do veiculo: {car["placa"]}")
                    print(f"Saída da viagem : {car["origem"]}")
                    print(f"Destino da viagem: {car["destino"]}")
                    print(f"Data da viagem : {car["data"]}")
                    print(f"Vagas disponiveis: {car["vagas"]}")
                    print(f"Valor por vaga: {car["valorporVaga"]}")
                    escolha=input("Deseja realmente reservar? (s/n): ").lower()
                    if(escolha=="s"):
                        if(tipoveiculo=="carro"):
                            print(f"Assentos disponiveis: {reservacarona['Carro']}")
                            assentoescolha=input("Digite o assento desejado:")
                            reservacarona["Carro"]-=1
                            print("Reserva feita!")
                        if(tipoveiculo=="moto"):   
                            print(f"Assentos disponiveis: {reservacarona['Moto']}")  
                            assentoescolha=input("Confirme o assento desejado:") 
                            reservacarona["Moto"]-=1
                            print("Reserva feita!")
                    else:
                        print("Reserva não concluida")
                while(escolhamotorista not in {car["emaildomotorista"]}):
                    print("Carona não encontrada!") 
                    print("Tente novamente")
                    escolhamotorista=input("Digite o email do motorista desejado:")