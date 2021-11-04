#-- ============================================================================== --
#-- Authors: William Rodrigues Delmanto e Jaqueline Freitas Jardim
#-- Description: Sistema bancario QuemPoupaTem
#-- ============================================================================== --

#--------------------------------------------------------------------
#
#                             Bibliotecas
#
#--------------------------------------------------------------------
import os
import sys
import datetime

Path = os.getcwd() #Caminho Completo

while True:
    #--------------------------------------------------------------------
    #
    #            Funcao que Verifica o Arquivo Clientes.txt
    #
    #--------------------------------------------------------------------
    def Verify_Clientes(): #Verifica se o arquivo Clientes.txt existe
        if (os.path.isfile(F'{Path}\Clientes.txt')) == False: #Verifica se o arquivo Clients.txt existe, Se Nao Existe, Cria
            DB_txt = open(F'{Path}\Clientes.txt', 'w+') #Abre o Arquivo em Modo Escrita
            DB_txt.close() #Fecha o Arquivo
            
    #--------------------------------------------------------------------
    #
    #            Funcao que Verifica o Arquivo AuditLogs.txt
    #
    #--------------------------------------------------------------------
    def Verify_AuditLogs(): #Verifica se o arquivo AuditLogs.txt existe
        if (os.path.isfile(F'{Path}\AuditLogs.txt')) == False: #Verifica se o arquivo AuditLogs.txt existe, Se Nao Existe, Cria
            DB_txt = open(F'{Path}\AuditLogs.txt', 'w+') #Abre o Arquivo em Modo Escrita
            DB_txt.close()#Fecha o Arquivo
            
    #--------------------------------------------------------------------
    #
    #            Funcao que Adiciona Novos Clientes
    #
    #--------------------------------------------------------------------
    def New_Client(): #Adiciona Novos Usuarios
        print('---------------------------------')
        print('Favor Preencher os Dados Abaixo:')
        
        Nome = str(input('Nome: ')) #Inserir Entrada na Variavel
        CPF = str(input('CPF: ')) #Inserir Entrada na Variavel
        
        T_Conta = int(input('Tipo de Conta (1 - Conta Salario, 2 - Conta Comum, 3 - Conta Plus): ')) #Inserir Entrada na Variavel
        if T_Conta not in (1, 2, 3): #Verificacao
            print('Opcao invalida')
            return
        
        Valor_Inicial = float(input('Valor Inicial da Conta: ')) #Inserir Entrada na Variavel            
        if Valor_Inicial < 0: #Nao é permitido abrir contas negativas
            print('Valor Invalido')
            return
            
        Senha = str(input('Senha: ')) #Inserir Entrada na Variavel
        
        Verify_Clientes() #Verifica se o arquivo Clientes.txt existe
        Verify_AuditLogs() #Verifica se o arquivo AuditLogs.txt existe
        
        Clientes = open(F'{Path}\Clientes.txt','r') #Abre o Arquivo em Modo Leitura
        
        Saved_Lines = [line.split(',') for line in Clientes.readlines()] #Salva os Usuarios existentes em uma variavel
        
        User_Exists = 0 #Verificacao da Existencia do Usuario
        for Line in Saved_Lines: #Para Cada Linha em Saved_Lines
            if CPF == Line[0]: #Se o CPF ja Existe
                User_Exists = 1 #Seta que o Usuario Existe
                print('---------------------------------')
                print('O CPF Ja Esta Cadastrado')
        
        Clientes.close() #Fecha o Arquivo
            
        if User_Exists == 0: #Se o Usuario Nao Existe, Cria o Usuario
            Clientes = open(F'{Path}\Clientes.txt','a+') #Abre o Arquivo no Modo de Insercao
            L = F'{CPF},{Nome},{T_Conta},{Valor_Inicial},{Senha}\n' #Informacoes Agruda para Insercao
            Clientes.write(L) #Adiciona o Usuario
            Clientes.close() #Fecha o Arquivo
            
            Day_Of_Today = str(datetime.datetime.now().strftime('%Y-%m-%d')) #Format = AAAA-MM-DD #Dia de Hoje
            Time_Now = str(datetime.datetime.now().strftime('%H:%M')) #Format = mm:ss # Horario de Agora
            Data = Day_Of_Today + ' ' + Time_Now #Juncao de Data e Hora
            
            AuditLogs = open(F'{Path}\AuditLogs.txt','a+') #Abre o Arquivo no Modo de Insercao
            L = F'{CPF},{Data},{Valor_Inicial},0.0,{Valor_Inicial}\n' #Informacoes Agruda para Insercao
            AuditLogs.write(L) #Adiciona na Auditoria
            AuditLogs.close() #Fecha o Arquivo
            
            print('---------------------------------')
            print('Cliente ', Nome, ' Adicionado')
        
        print('---------------------------------')
        
    #--------------------------------------------------------------------
    #
    #            Funcao que Deleta Clientes e Suas Auditorias
    #
    #--------------------------------------------------------------------
    def Delete_Client(): #Deleta Usuarios
        print('---------------------------------')
        print('Favor Preencher os Dados Abaixo:')
        
        CPF = str(input('CPF: ')) #Inserir Entrada na Variavel
        
        Verify_Clientes() #Verifica se o arquivo Clientes.txt existe
        Verify_AuditLogs() #Verifica se o arquivo AuditLogs.txt existe
        
        Clientes = open("Clientes.txt", "r") #Abre o Arquivo em Modo Leitura
        
        Saved_Lines = [line.split(',') for line in Clientes.readlines()] #Salva os Usuarios existentes em uma variavel
        
        Clientes.close() #Fecha o Arquivo
        
        AuditLogs = open("AuditLogs.txt", "r") #Abre o Arquivo em Modo Leitura
        
        AuditLogs_Saved_Lines = [line.split(',') for line in AuditLogs.readlines()] #Salva os Usuarios existentes em uma variavel
        
        AuditLogs.close() #Fecha o Arquivo
        
        Clientes = open("Clientes.txt", "w") #Abre o Arquivo em Modo Escrita
        
        User_Exists = 0 #Verificacao da Existencia do Usuario
        for Line in Saved_Lines: #Para Cada Linha em Saved_Lines
            if CPF == Line[0]: #Se o CPF Existe
                User_Exists = 1 #Seta que o Usuario Existe e Foi Deletado (Nao Foi Adicionado no Else Abaixo)
                Nome = Line[1]
                print('---------------------------------')
                print(F'Usuario {Nome} Deletado')
            else: #Sobreescreve o Arquivo e Adiciona Todos os Usuarios Novamente
                _CPF = Line[0] #Inserir Entrada na Variavel
                _Nome = Line[1] #Inserir Entrada na Variavel
                _T_Conta = Line[2] #Inserir Entrada na Variavel
                _Saldo = Line[3] #Inserir Entrada na Variavel
                _Senha = Line[4] #Inserir Entrada na Variavel
                L = F'{_CPF},{_Nome},{_T_Conta},{_Saldo},{_Senha}' #Informacoes Agruda para Insercao
                Clientes.write(L) #Adiciona o Usuario
                
        Clientes.close() #Fecha o Arquivo
        
        AuditLogs = open("AuditLogs.txt", "w") #Abre o Arquivo em Modo Escrita
        
        for Line in AuditLogs_Saved_Lines: #Para Cada Linha em AuditLogs_Saved_Lines
            if CPF == Line[0]: #Se o CPF Existe
                User_Exists = 1 #Seta que o Usuario Existe
            else: #Sobreescreve o Arquivo e Adiciona Todos os Usuarios Novamente
                _CPF = Line[0] #Inserir Entrada na Variavel
                _Data = Line[1] #Inserir Entrada na Variavel
                _Valor = Line[2] #Inserir Entrada na Variavel
                _Tarifa = Line[3] #Inserir Entrada na Variavel
                _Saldo = Line[4] #Inserir Entrada na Variavel
                L = F'{_CPF},{_Data},{_Valor},{_Tarifa},{_Saldo}' #Informacoes Agruda para Insercao
                AuditLogs.write(L) #Adiciona o Usuario
                
        AuditLogs.close() #Fecha o Arquivo
            
        if User_Exists == 0: #Se o CPF Nao Existe
            print('---------------------------------')
            print('CPF Não Encontrado')
        
        print('---------------------------------')
        
    #--------------------------------------------------------------------
    #
    #                        Funcao de Bebito
    #
    #--------------------------------------------------------------------
    def Debit():
        print('---------------------------------')
        print('Favor Preencher os Dados Abaixo:')
        
        CPF = str(input('CPF: ')) #Inserir Entrada na Variavel
        
        Senha = str(input('Senha: ')) #Inserir Entrada na Variavel
        
        Debito = float(input('Valor: ')) #Inserir Entrada na Variavel
        if Debito < 0: #Nao é Permitido Debitar Valores Negativos
            Debito = -Debito #Ajuste Para Entrar na Conta Depois
            
        Verify_Clientes() #Verifica se o arquivo Clientes.txt existe
        Verify_AuditLogs() #Verifica se o arquivo AuditLogs.txt existe
        
        Clientes = open("Clientes.txt", "r") #Abre o Arquivo em Modo Leitura
        
        Saved_Lines = [line.split(',') for line in Clientes.readlines()] #Salva os Usuarios existentes em uma variavel
        
        Clientes.close() #Fecha o Arquivo
        
        Clientes = open("Clientes.txt", "w") #Abre o Arquivo em Modo Escrita
        
        User_Exists = 0 #Verificacao da Existencia do Usuario
        for Line in Saved_Lines: #Para Cada Linha em Saved_Lines
            _CPF = Line[0] #Inserir Entrada na Variavel
            _Nome = Line[1] #Inserir Entrada na Variavel
            
            _T_Conta = Line[2] #Inserir Entrada na Variavel
            if _T_Conta == '1': #Para Conta Salario
                Tarifa = Debito*0.05 #5% de Tarifa
                Valor_Min = 0 #Saldo Negativo Maximo
            elif _T_Conta == '2': #Para Conta Comum
                Tarifa = Debito*0.03 #3% de Tarifa
                Valor_Min = 500 #Saldo Negativo Maximo
            else: #Para Conta Plus
                Tarifa = Debito*0.01 #1% de Tarifa
                Valor_Min = 5000 #Saldo Negativo Maximo
            
            if CPF == Line[0]: #Se o CPF Existe
                if Line[4].replace('\n', '') == Senha: #Se a Senha Coincide
                    User_Exists = 1 #Seta que o Usuario Existe
                    if float(Line[3]) - Debito - Tarifa >= -Valor_Min: #Verifica se Nao vai Ficar com Saldo Minimo
                        _Saldo = float(Line[3]) - Debito - Tarifa #Saldo Teorico Após Debito
                        
                        AuditLogs = open("AuditLogs.txt", "a+") #Abre o Arquivo em Modo Escrita
        
                        Day_Of_Today = str(datetime.datetime.now().strftime('%Y-%m-%d')) #Format = AAAA-MM-DD #Dia de Hoje
                        Time_Now = str(datetime.datetime.now().strftime('%H:%M')) #Format = mm:ss # Horario de Agora
                        Data = Day_Of_Today + ' ' + Time_Now #Juncao de Data e Hora
        
                        L = F'{_CPF},{Data},-{Debito},{Tarifa},{_Saldo}\n' #Informacoes Agruda para Insercao
        
                        AuditLogs.write(L) #Adiciona o Usuario
                
                        AuditLogs.close() #Fecha o Arquivo
                        
                        print('---------------------------------')
                        print('Debito Feito com Sucesso')
                
                    else:
                        _Saldo = Line[3] #Inserir Entrada na Variavel Sem Debito
                        print('---------------------------------')
                        print('Saldo Insuficiente')
                else:
                    _Saldo = Line[3]
            else:
                _Saldo = Line[3]
                
            _Senha = Line[4] #Inserir Entrada na Variavel
            L = F'{_CPF},{_Nome},{_T_Conta},{_Saldo},{_Senha}' #Informacoes Agruda para Insercao
            Clientes.write(L) #Adiciona o Usuario
                
        Clientes.close() #Fecha o Arquivo
        
        
        
        if User_Exists == 0: #Se o CPF Nao Existe
            print('---------------------------------')
            print('Valores Invalidos')
        
        print('---------------------------------')
        
    #--------------------------------------------------------------------
    #
    #                       Funcao de Deposito
    #
    #--------------------------------------------------------------------
    def Deposit(): #Deposito
        print('---------------------------------')
        print('Favor Preencher os Dados Abaixo:')
        
        CPF = str(input('CPF: ')) #Inserir Entrada na Variavel
        
        Deposito = float(input('Valor do Deposito: ')) #Inserir Entrada na Variavel            
        if Deposito < 0: #Nao é Permitido Depositar Valores Negativos
            print('Valor Invalido')
            return
        
        Verify_Clientes() #Verifica se o arquivo Clientes.txt existe
        Verify_AuditLogs() #Verifica se o arquivo AuditLogs.txt existe
        
        Clientes = open("Clientes.txt", "r") #Abre o Arquivo em Modo Leitura
        
        Saved_Lines = [line.split(',') for line in Clientes.readlines()] #Salva os Usuarios existentes em uma variavel
        
        Clientes.close() #Fecha o Arquivo
        
        Clientes = open("Clientes.txt", "w") #Abre o Arquivo em Modo Escrita
        
        User_Exists = 0 #Verificacao da Existencia do Usuario
        for Line in Saved_Lines: #Para Cada Linha em Saved_Lines
            _CPF = Line[0] #Inserir Entrada na Variavel
            _Nome = Line[1] #Inserir Entrada na Variavel
            _T_Conta = Line[2] #Inserir Entrada na Variavel
            
            if CPF == Line[0]: #Se o CPF Existe
                _Saldo = float(Line[3]) + Deposito #Inserir Entrada na Variavel + Deposito
                User_Exists = 1 #Seta que o Usuario Existe
                
                AuditLogs = open("AuditLogs.txt", "a+") #Abre o Arquivo em Modo Escrita
        
                Day_Of_Today = str(datetime.datetime.now().strftime('%Y-%m-%d')) #Format = AAAA-MM-DD #Dia de Hoje
                Time_Now = str(datetime.datetime.now().strftime('%H:%M')) #Format = mm:ss # Horario de Agora
                Data = Day_Of_Today + ' ' + Time_Now #Juncao de Data e Hora
        
                L = F'{_CPF},{Data},{Deposito},0.0,{_Saldo}\n' #Informacoes Agruda para Insercao
        
                AuditLogs.write(L) #Adiciona o Usuario
                
                AuditLogs.close() #Fecha o Arquivo
                
                print('---------------------------------')
                print('Deposito Feito com Sucesso')
                
                #
                
            else:
                _Saldo = Line[3] #Inserir Entrada na Variavel Sem Deposito
            
            _Senha = Line[4] #Inserir Entrada na Variavel
            L = F'{_CPF},{_Nome},{_T_Conta},{_Saldo},{_Senha}' #Informacoes Agruda para Insercao
            Clientes.write(L) #Adiciona o Usuario
                
        Clientes.close() #Fecha o Arquivo
            
        if User_Exists == 0: #Se o CPF Nao Existe
            print('---------------------------------')
            print('CPF Não Encontrado')
        
        print('---------------------------------')
        
    #--------------------------------------------------------------------
    #
    #                   Funcao que Exibe o Saldo
    #
    #--------------------------------------------------------------------
    def Balance(): #Exibe o Saldo
        print('---------------------------------')
        print('Favor Preencher os Dados Abaixo:')
        
        CPF = str(input('CPF: ')) #Inserir Entrada na Variavel
        Senha = str(input('Senha: ')) #Inserir Entrada na Variavel
        
        Verify_Clientes() #Verifica se o arquivo Clientes.txt existe
        Verify_AuditLogs() #Verifica se o arquivo AuditLogs.txt existe
        
        Clientes = open("Clientes.txt", "r") #Abre o Arquivo em Modo Leitura
        
        Saved_Lines = [line.split(',') for line in Clientes.readlines()] #Salva os Usuarios existentes em uma variavel
        
        Clientes.close() #Fecha o Arquivo
        
        User_Exists = 0 #Verificacao da Existencia do Usuario
        for Line in Saved_Lines: #Para Cada Linha em Saved_Lines
            if Line[0] == CPF: #Se o CPF Existe
                if Line[4].replace('\n', '') == Senha: #Se a Senha Coincide
                    Saldo = Line[3] #Inserir Entrada na Variavel
                    print('---------------------------------')
                    print('Saldo: R$ ',Saldo) #Exibe o Saldo
                    User_Exists = 1#Seta que o Usuario Existe)
                
        Clientes.close() #Fecha o Arquivo
            
        if User_Exists == 0: #Se o Usuario ou Os Valores Sao Invalidos Nao Existe
            print('---------------------------------')
            print('Valores Invalidos')
        
        print('---------------------------------')
        
    #--------------------------------------------------------------------
    #
    #                   Funcao que Exibe o Extrato
    #
    #--------------------------------------------------------------------
    def Extract():
        print('---------------------------------')
        print('Favor Preencher os Dados Abaixo:')
        
        CPF = str(input('CPF: ')) #Inserir Entrada na Variavel
        Senha = str(input('Senha: ')) #Inserir Entrada na Variavel
        
        Verify_Clientes() #Verifica se o arquivo Clientes.txt existe
        Verify_AuditLogs() #Verifica se o arquivo AuditLogs.txt existe
        
        Clientes = open("Clientes.txt", "r") #Abre o Arquivo em Modo Leitura
        
        Saved_Lines = [line.split(',') for line in Clientes.readlines()] #Salva os Usuarios existentes em uma variavel
        
        Clientes.close() #Fecha o Arquivo
        
        AuditLogs = open("AuditLogs.txt", "r") #Abre o Arquivo em Modo Leitura
        
        AuditLogs_Saved_Lines = [line.split(',') for line in AuditLogs.readlines()] #Salva os Usuarios existentes em uma variavel
        
        AuditLogs.close() #Fecha o Arquivo
        
        User_Exists = 0 #Verificacao da Existencia do Usuario
        for Line in Saved_Lines: #Para Cada Linha em Saved_Lines
            if CPF == Line[0] and Line[4].replace('\n', '') == Senha: #Se o CPF Existe
                User_Exists = 1 #Seta que o Usuario Existe e Foi Deletado (Nao Foi Adicionado no Else Abaixo)
                Nome = Line[1]
                
                _T_Conta = Line[2]
                if _T_Conta == '1': #Para Conta Salario
                    T_Conta = 'Salario'
                elif _T_Conta == '2': #Para Conta Comum
                    T_Conta = 'Comum'
                else: #Para Conta Plus
                    T_Conta = 'Plus'
                    
                print('---------------------------------')
                print('Nome: ', Nome)
                print('CPF:  ', CPF)
                print('Conta:', T_Conta)
                print('---------------------------------')
        
        for Line in AuditLogs_Saved_Lines: #Para Cada Linha em AuditLogs_Saved_Lines
            if CPF == Line[0] and User_Exists == 1: #Se o CPF Existe           
                _Data = Line[1] #Inserir Entrada na Variavel
                _Valor = Line[2] #Inserir Entrada na Variavel
                _Tarifa = Line[3] #Inserir Entrada na Variavel
                _Saldo = Line[4] #Inserir Entrada na Variavel
                
                print('Data:', _Data, '|', _Valor, '|', 'Tarifa:', _Tarifa, '|', 'Saldo:', _Saldo.replace('\n', ''))

        if User_Exists == 0: #Se o CPF Nao Existe
            print('---------------------------------')
            print('Valores Invalidos')
        
        print('---------------------------------')

    #--------------------------------------------------------------------
    #
    #                            Menu
    #
    #--------------------------------------------------------------------
    print('---------------------------------')
    print('Escolha uma das Seguintes Opções:')
    print('1 - Novo Cliente')
    print('2 - Apaga Cliente')
    print('3 - Debita')
    print('4 - Deposita')
    print('5 - Saldo')
    print('6 - Extrato')
    print('')
    print('0 - Sair')
    print('---------------------------------')
    
    Entry = int(input('-> ')) #Inserir Entrada na Variavel
    
    if Entry == 0: #Executa se a Entrada Coincidir
        print('---------------------------------')
        print('     O QuemPoupaTem Agradece'     )
        print('---------------------------------')
        sys.exit() #Para o Programa
    
    if Entry == 1: #Executa se a Entrada Coincidir
        New_Client() #Executa a Funcao
        
    if Entry == 2: #Executa se a Entrada Coincidir
        Delete_Client() #Executa a Funcao
        
    if Entry == 3: #Executa se a Entrada Coincidir
        Debit() #Executa a Funcao
        
    if Entry == 4: #Executa se a Entrada Coincidir
        Deposit() #Executa a Funcao
        
    if Entry == 5: #Executa se a Entrada Coincidir
        Balance() #Executa a Funcao
        
    if Entry == 6: #Executa se a Entrada Coincidir
        Extract() #Executa a Funcao
        
    if Entry not in (0, 1, 2, 3, 4, 5, 6): #Executa se Nenhuma Entrada Coincidir
        print('---------------------------------')
        print('Opcao Invalida')