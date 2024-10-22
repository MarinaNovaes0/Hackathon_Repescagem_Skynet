#Biblioteca
import os

#Lista vazia
usuarios = {}

#Menu
while True:
    os.system('cls')
    print()
    print (30*'*', 'Tech4U Menu', 30*'*')
    print('1. Cadastrar usuário')
    print('2. Listar usuário')
    print('3. Excluir usuário')
    print('4. Editar usuário')
    print('5. Sair')
    print(73*'*')
    print()
    
    #Irá receber as opções    
    opcao = input("Digite a opção desejada: ")
    
    #Cadastrar usuário
    if opcao == '1':
        os.system('cls')
        nome = input("Digite o nome que deseja cadastrar: ").upper()
        
        #Exibe se o usuário já estiver cadastrado
        if nome in usuarios:
            os.system('cls')
            print(35*'*')
            print('Usuário já cadastrado!')
            print(35*'*')
            input('Pressione enter para voltar para o menu: ')
        else: 
            while True:
                os.system('cls')
                idade = int(input('Digite a idade: '))
                
                #Exibe se a idade for negativa
                if idade <= 0:
                    os.system('cls')
                    print(40*'*')
                    print(f'A idade tem que ser um número positivo!')
                    print(40*'*')
                    input('Pressione enter para voltar para o menu: ')
                    
                #Exibe se a idade for maior do que 120
                elif idade > 120:
                    os.system('cls')
                    
                    #Recebendo confirmação se a idade está correta
                    option = input('Tem certeza que sua idade está correta? (s/n): ').upper()
                    
                    #Exibe se a idade estiver correta
                    if option == 'S':
                        break
                    
                    #Exibe se o usuário escolher mudar a idade
                    elif option == 'N':
                        pass
                    
                    #Exibe se na confirmação da idade o usuário não colocar S ou N
                    else: 
                        os.system('cls')
                        print(35*'*')
                        print('As opções são S ou N')
                        print(35*'*')
                        input('Pressione enter para recolocar a idade: ')
                
                #Exibe quando tudo estiver certo
                else:
                    break     
            usuarios[nome] = {'Nome' : nome ,'Idade': idade}
            os.system('cls')
            print(35*'*')    
            print('Usuário cadastrado com sucesso!')
            print(35*'*')
            input('Pressione enter para voltar para o menu: ')
            
    #Listar usuário             
    elif opcao == '2': 
        if usuarios:
            os.system('cls')
            print(50*'*')
            for idade, dados in usuarios.items(): 
                print(f'Nome: {dados['Nome']}; Idade: {dados['Idade']}')
            print(50*'*')
            input('Pressione enter para voltar para o menu: ')
            
        #Exibe se não tiver usuário cadastrados
        else:
            os.system('cls')
            print(35*'*')
            print("Nenhum usuário cadastrado!")
            print(35*'*')
            input('Pressione enter para voltar para o menu: ')
 
    #Excluir usuário        
    elif opcao == '3':
        
        #Exibe se não tiver usuário cadastrados
        if not usuarios:
            os.system('cls')
            print(35*'*')
            print("Nenhum usuário cadastrado!")
            print(35*'*')
            input('Pressione enter para voltar para o menu: ')
            
        #Excluindo usuário
        else:
            os.system('cls')
            print(50*'*')
            for dados in usuarios.values():  
                print(f'Nome: {dados['Nome']}; Idade: {dados['Idade']}')
            print(50*'*')
            remover = input("Digite o nome que você deseja excluir: ").upper()
            if remover in usuarios: 
                del usuarios[remover]
                os.system('cls')
                print(50*'*')
                print(f'Usuário {remover} excluído com sucesso!')
                print(50*'*')
                input('Pressione enter para voltar para o menu: ')
                
            #Exibe se o nome não estiver cadastrado
            else:
                os.system('cls')
                print(35*'*')
                print("O nome não está na lista!")
                print(35*'*')
                input('Pressione enter para voltar para o menu: ')
                
    #Editar usuário        
    elif opcao =='4':
        #Exibe se não tiver usuário cadastrados
        if not usuarios:
            os.system('cls')
            print(35*'*')
            print("Nenhum usuário cadastrado!")
            print(35*'*')
            input('Pressione enter para voltar para o menu: ')
            
        else:
            os.system('cls')
            print(50*'*')
            for dados in usuarios.values():  
                print(f'Nome: {dados['Nome']}; Idade: {dados['Idade']}')
            print(50*'*')
            print("ATENÇÃO: É possível apenas editar a idade")
            editar = input("Digite o nome que você deseja editar: ").upper()
            if editar in usuarios:
                for dados in usuarios.values():
                    if editar == dados['Nome']:
                        while True:
                            idade_nova = int(input('Digite a nova idade do usuário: '))
                            
                            #Exibe se a idade for negativa
                            if idade_nova < 0:
                                os.system('cls')
                                print(40*'*')
                                print('A idade tem que ser um número positivo.')
                                print(40*'*')
                                input('Pressione enter para recolocar a idade: ')
                           
                           #Exibe se a idade for maior do que 120
                            elif idade_nova > 120:
                                os.system('cls')
                                
                                #Recebendo confirmação se a idade está correta
                                option = input('Tem certeza que sua idade está correta? (s/n): ').upper()
                                
                                #Exibe se a idade estiver correta
                                if option == 'S':
                                    break
                                
                                #Exibe se o usuário escolher mudar a idade
                                elif option == 'N':
                                    pass
                               
                                #Exibe se na confirmação da idade o usuário não colocar S ou N
                                else: 
                                    os.system('cls')
                                    print(35*'*')
                                    print('As opções são S ou N')
                                    print(35*'*')
                                    input('Pressione enter para recolocar a idade: ')
                            
                            #Exibe quando tudo estiver certo
                            else:
                                break
                        dados['Idade'] = idade_nova
                        os.system('cls')
                        print(35*'*')
                        print('Idade alterada com sucesso!')
                        print(35*'*')
                        break
                    
            #Exibe se não tiver usuário cadastrados        
            else: 
                os.system('cls')
                print(35*'*')
                print('O usuário não está cadastrado!')
                print(35*'*')
            input('Pressione enter para voltar para o menu: ')
    #Sair
    elif opcao =='5':
        os.system('cls')
        print("FIM!")
        break
    
    #Se não for nenhuma opção válida
    else:
        os.system('cls')
        print(35*'*')
        print('Digite uma opção válida!')
        print(35*'*')
        input('Pressione enter para voltar para o menu: ')
