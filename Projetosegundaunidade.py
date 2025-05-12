usuarios=[]
usuariologado={}
cadastrodecarona=[]
reserva=[]

print("="*35)
print("========CAJAZEIRAS CARONAS=========")
print("="*35)

#PRIMEIRO MENU: CADASTRO DO USUARIO PARA TER O LOGIN

while True:
    print("========MENU DE CADASTRO========")
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
    elif(opcao=="1"):
        print("========CADASTRO========")
        nome=input("Digite seu nome: ")
        
        while len(nome)<3:
            print("Nome invalido!")
            print("Tente novamente!")
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
        
        while("@gmail.com" not in email 
              and "@hotmail.com.br" not in email
              and "@outlook.com" not in email
              and "@yahoo!mail.com" not in email
              and "@iCloudMail.com" not in email):
            print("Email inválido!")
            print("Tente novamente!")
            email=input("Digite seu email: ")
            if(" " in email):
                print("Email inválido!")
                print("Tente novamente!")
                email=input("Digite seu email: ")
            
        senha=input("Digite sua senha: ")
        senha2=input("Confirme sua senha: ")
    
        while senha2!=senha:
            print("A senhas não coincidem!")
            print("Tente novamente!")
            senha2=input("Digite sua senha novamente: ")

        while len(senha)<6 :
            print("Senha curta demais!")
            print("Tente novamente!")
            senha=input("Digite sua senha: ")
            senha2=input("Confirme sua senha: ")
            
        usuarios.append({"nome":nome,
                         "email":email,
                         "senha":senha
                    })
        
        print("Cadastro feito com sucesso!!")
        print("=" * 32)


#LOGIN,SEGUNDO MENU APARTIR DO LOGIN
    if(opcao=="2"):
        print("=======LOGIN=========")
        email=input("Digite o seu email: ")
        senha=input("Digite sua senha: ")
        login=False
        for usu in usuarios:
            if(email==usu["email"] and senha==usu["senha"] ):
                login=True
                usuariologado=usu
                print("Login efetuado com sucesso!!")
                break
            elif(login==False):
                print("Erro no login,algo está errado!") 
         
#SEGUNDO MENU(SO USUARIOS LOGADOS)
        while(login==True):
            print("========MENU DE LOGIN=========")
            opcao2=input("ESCOLHA O QUE DESJA FAZER\n\n"
                    "0 -Logout\n"\
                    "1 - Cadastro de carona\n"\
                    "2 - Lista de caronas disponiveis\n"\
                    "3 - Buscar carona por origem e destino\n"\
                    "4 - Buscar por data\n"\
                    "5 - Reserva de Carona\n"\
                    "6 - Minhas caronas\n"\
                    "7 - Remoção de Carona\n"\
                    "8 - Cancelar reserva\n"
                    "\nDIGITE O QUE ESCOLHEU: ")
            
#LOGOUT(QUEBRA PARA VOLTAR PARA O PRIMEIRO MENU)
            if(opcao2=="0"):
                print("Até mais!")
                break
            
#CADASTRO DE UMA CARONA       
            elif(opcao2=="1"): 
                print("Informe as seguintes informaçoes!")
                nomedomotorista=usuariologado["nome"]
                emaildomotorista=usuariologado["email"]
                tipoveiculo=input("Digite o tipo do veiculo(moto ou carro): ").lower()
                nomedoveiculo=input("Digite o nome do veiculo (Onix,Prisma, POP100):")
                cordoVeiculo=input("Digite a cor do veiculo: ")
                placa=input("Digite a placa do veiculo :").upper()
                origem=input("Digite de onde o veiculo vai sair : ")
                destino=input("Digite o destino da viagem: ")
                vagas=int(input("Digite quantas vagas tem  no veiculo : "))
                valorPorVaga=float(input("Digite o valor por cada vaga : "))
                horario=(input("Digite o horario da viagem (10:00 PM ou AM) : "))
                data=input("Digite a data da viagem (Formarto em dd/mm/aaaa): ")
                dia=int(data[0:2])
                mes=int(data[3:5])
                ano=int(data[6:10])
                validado="N"
                ebissexto="N"
                
                while(ano<2025):
                    print("Ano inválido!")
                    print("Digite a data novamente!")
                    data=input("Digite a data da viagem (Formarto em dd/mm/aaaa): ")
                    dia=int(data[0:2])
                    mes=int(data[3:5])
                    ano=int(data[6:10])
                    
                if(ano % 4 == 0):
                    ebissexto="S"
                elif(ano % 100==0 and ano %400!=0):
                    ebissexto="N"
                elif(mes==1 
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
                            
                    elif(validado=="S"):
                            print("É uma data valida")
                    else:
                            print("É uma data invalida")
                            
                while (len(placa)<7):
                    print("Placa invalida!Não é padrão do mercosul")
                    print("Escreva-a corretamente agora!")
                    placa=input("Digite a placa do veiculo :").upper()
                            
                while(tipoveiculo=="aviao" 
                    and tipoveiculo=="navio"
                    and tipoveiculo=="barco"
                    and tipoveiculo=="canoa"
                    and tipoveiculo=="van"
                    and tipoveiculo=="onibus"):
                    print("Veiculo impossivel de registrar")
                    print("Cadastre outro veiculo")
                    tipoveiculo=input("Digite o tipo do veiculo(moto ou carro): ").lower()
                            
                if(valorPorVaga>20):
                    pergunta=input("Tem certeza(s/n):").lower()
                    if(pergunta!="s"):
                        print("Coloque um novo valor")
                        valorPorVaga=float(input("Digite o valor por cada vaga : "))
                            
                cadastrodecarona.append([{"nomedomotorista":nomedomotorista,
                                                "emaildomotorista":emaildomotorista,
                                                "tipodeveiculo":tipoveiculo,
                                                "nomedoveiculo":nomedoveiculo,
                                                "cordoveiculo":cordoVeiculo,
                                                "placa":placa,
                                                "origem":origem,
                                                "destino":destino,
                                                "data":data,
                                                "horario":horario,
                                                "vagas":vagas,
                                                "valorporVaga":valorPorVaga}])
                
                print("Carona cadrastada com sucesso!!!")
                
#LISTA DE CARONAS DISPONIVEIS 
            elif(opcao2=="2"):
                print("="*32)
                print("\nLista de Caronas\n")
                for car in cadastrodecarona:
                    if(car["vagas"]>0):
                        print(f"Nome do motorista : {car["nome"]}")
                        print(f"Email do motorista:{car["emaildomotorista"]} ")
                        print(f"Veiculo: {car["tipodeveiculo"]}")
                        print(f"Nome do veiculo: {car["nomedoveiculo"]}")
                        print(f"Cor do veiculo: {car["cordoveiculo"]}")
                        print(f"A placa do veiculo: {car["placa"]}")
                        print(f"Saída da viagem : {car["origem"]}")
                        print(f"Destino da viagem: {car["destino"]}")
                        print(f"Data da viagem : {car["data"]}")
                        print(f"Horário da viagem :{car["horario"]}")
                        print(f"Vagas disponiveis: {car["vagas"]}")
                        print(f"Valor por vaga: {car["valorporVaga"]}")
                print("="*32)

#BUSCA POR CARONA (DESTINO E ORIGEM)
            elif(opcao=="3"):
                saidabusca=input("Digite de onde vai sair: ") 
                destinobusca=input("Digite para onde voce quer ir: ")
                caronaencontrada=False
                if(saidabusca == {car["origem"]} and destinobusca == {car["destino"]}):
                    caronaencontrada=True
                    print("Encontrou uma carona!\n\n")
                    print("-" * 50)
                    print(f"Email do motorista:{car["emaildomotorista"]} ")
                    print(f"Veiculo: {car["tipodeveiculo"]}")
                    print(f"Nome do veiculo: {car["nomedoveiculo"]}")
                    print(f"Cor do veiculo: {car["cordoveiculo"]}")
                    print(f"A placa do veiculo: {car["placa"]}")
                    print(f"Saída da viagem : {car["origem"]}")
                    print(f"Destino da viagem: {car["destino"]}")
                    print(f"Data da viagem : {car["data"]}")
                    print(f"Horário da viagem :{car["horario"]}")
                    print(f"Vagas disponiveis: {car["vagas"]}")
                    print(f"Valor por vaga: {car["valorporVaga"]}")
                    print("-" * 50)
                    
#RESERVA DE UMA CARONA
            elif(opcao2=="5"):
                escolhamotorista=input("Digite o email do motorista desejado:")
                escolhadata=input("Digite a data da carona (dd/mm/aaaa): ")
                caronaencontrada=False
                
                for car in cadastrodecarona:
                    if(escolhamotorista in {car["emaildomotorista"]} and escolhadata in {car["data"]}):
                        caronaencontrada=True
                        print("Carona encontrada!")
                        print(f"Email do motorista:{car["emaildomotorista"]}")
                        print(f"Veiculo:{car["tipodoveiculo"]}")  
                        print(f"Nome do veiculo : {car["nomedoveiculo"]}")    
                        print(f"Cor: {car["cordoveiculo"]}")
                        print(f"A placa do veiculo: {car["placa"]}")
                        print(f"Saída da viagem : {car["origem"]}")
                        print(f"Destino da viagem: {car["destino"]}")
                        print(f"Data da viagem : {car["data"]}")
                        print(f"Horário da viagem :{car["horario"]}")
                        print(f"Vagas disponiveis: {car["vagas"]}")
                        print(f"Valor por vaga: {car["valorporVaga"]}")
                        if(car[vagas]>0):
                            escolha=input("Deseja realmente reservar? (s/n): ").lower()
                            if(escolha=="s"):
                                car["vagas"]-=1
                                reserva.append([{"emailpassageiro": usuariologado["email"],
                                                        "emailmotorista": escolhamotorista,
                                                                        "data": escolhadata}])
                                print("Reserva feita com sucesso!")
                            else:
                                print("Reserva cancelada.")
                        else:
                            print("Essa carona não tem mais vagas.")
                            break
                    if(caronaencontrada==False):
                        print("Carona inexistente!")
#LISTA DE CARONAS CADASTRADAS PELO USUÁRIO
            elif(opcao2=="6"):
                print("Caronas cadastradas")
                if(emaildomotorista==usuariologado["email"]):
                    print(f"Email do motorista:{car["emaildomotorista"]}")
                    print(f"Veiculo:{car["tipodoveiculo"]}")  
                    print(f"Nome do veiculo : {car["nomedoveiculo"]}")    
                    print(f"Cor: {car["cordoveiculo"]}")
                    print(f"A placa do veiculo: {car["placa"]}")
                    print(f"Saída da viagem : {car["origem"]}")
                    print(f"Destino da viagem: {car["destino"]}")
                    print(f"Data da viagem : {car["data"]}")
                    print(f"Horário da viagem :{car["horario"]}")
                    print(f"Vagas disponiveis: {car["vagas"]}")
                    print(f"Valor por vaga: {car["valorporVaga"]}")
                    
#BUSCA DE CARONA POR DATA
            elif(opcao2=="4"):
                escolhamotorista=input("Digite o email do motorista desejado:")
                dataprocurada=input("Digite uma data (dd/mm/aaaa): ")
                dia=int(data[0:2])
                mes=int(data[3:5])
                ano=int(data[6:10])
                validado="N"
                ebissexto="N"
                
                while(ano<2025):
                    print("Ano inválido!")
                    print("Digite a data novamente!")
                    data=input("Digite a data da viagem (Formarto em dd/mm/aaaa): ")
                    dia=int(data[0:2])
                    mes=int(data[3:5])
                    ano=int(data[6:10])

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
                if(dataprocurada in {car["data"]}):
                    print("Carona encontrada!")
                    print(f"Saída da viagem : {car["origem"]}")
                    print(f"Destino da viagem: {car["destino"]}")
                    print(f"Data da viagem : {car["data"]}")
                    print(f"Horário da viagem :{car["horario"]}")
                    print(f"Vagas disponiveis: {car["vagas"]}")
                    print(f"Valor por vaga: {car["valorporVaga"]}")
                else:
                    print("Não existe carona para essa data!")

#REMOVER CARONA CADASTRADA
            elif(opcao2=="7"):
                emaildomotorista=input("Digite o seu email: ")
                senha3=input("Digite a sua senha:")
                dataprocurada2=input("Digite a data da carona(dd/mm/aaaa): ")
                caronaremovida=False
                for car in cadastrodecarona:
                    if(emaildomotorista==usuariologado["email"]
                    and dataprocurada==car["data"]
                    and senha3==usuariologado["senha"]):
                        cadastrodecarona.remove(car)
                        print("Carona removida com sucesso!!")
                        caronaremovida=True
                    else:
                        print("Voce nao pode remover uma carona!")
                        break                  
#CANCELAR RESERVA
            elif(opcao2=="8"):
                emaildomotorista=input("Digite o email do motorista: ")
                dataprocurada3=input("Digite a data da carona(dd/mm/aaaa):")
                reservaremovida=False
                for r in reserva:
                    if(r["emailpassageiro"]==usuariologado["email"] 
                       and r["emaildomotorista"]==emaildomotorista 
                       and r["data"]==escolhadata):
                        reserva.remove(r)
                    for car in cadastrodecarona:
                        if(car["emaildomotorista"]==emaildomotorista
                           and car["data"]==escolhadata):
                            car["vagas"]+=1
                            print("Reserva cancelada com sucesso!!")
                            reservaremovida=True
                            break
                            