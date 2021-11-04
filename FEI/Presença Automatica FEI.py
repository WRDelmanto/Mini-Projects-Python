from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('Programa para presença automatica')
print('FEI 2020')
print('Criado por Edueta =)')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('')
print('-----------------------------------------')
print('Versão 1.21: Funciona apenas para Chrome')
print('-----------------------------------------')
print('')
print('')
ini = input('Deseja iniciar a automatização de presença? (y/n) ')
print('')

if ini == 'y':
    print('---------------ATENÇÃO-------------------')
    print('Seus dados não ficarão salvos no programa')
    print('-----------------------------------------')
    login = input('Qual seu login? ')
    senha = input('Qual sua senha? ')
    print('')
    print('-----------------------------------------')
    print('-----Iniciando processos do navegador----')
    print('-----------------------------------------')
    print('Abrindo navegador')
    chrome = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
    print('Navegador aberto')
    chrome.maximize_window()
    chrome.get('https://interage.fei.org.br/secureserver/portal')
    print('Esperando portal do aluno')

    try:
        myElem = WebDriverWait(chrome,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="Usuario"]')))
        print('Portal do aluno pronto')
    except:
        print('Falha ao abrir o portal do aluno')
    chrome.find_element_by_xpath('//*[@id="Usuario"]').send_keys(login)
    chrome.find_element_by_xpath('//*[@id="Senha"]').send_keys(senha)
    chrome.find_element_by_xpath('//*[@id="btn-login"]').click()
    try:
        myElem = WebDriverWait(chrome,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="nav-home"]/li[10]/a')))
        print('Login feito')
    except:
        print('Erro de login ou senha')
    chrome.find_element_by_xpath('//*[@id="nav-home"]/li[10]/a').click()
    print('Pagina de Avaliação semanal aberta')
    try:
        myElem = WebDriverWait(chrome,100).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[1]/a')))
    except:
        print('Segunda feira nao encontrada!')

    #Para segunda feira
    chrome.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[1]/a').click()
    #Segunda Primeira aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-1"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-1"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-1"]')))
            chrome.find_element_by_xpath('//*[@id="faces-1"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-1"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-1"]').click()
            print('Primeira aula de segunda feira feita!')
        else:
            print('Primeira aula de segunda feira já estava preenchida')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-1"]')))
            chrome.find_element_by_xpath('//*[@id="faces-1"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-1"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-1"]').click()
            print('Primeira aula de segunda feira feita!')
        except:
            print('Primeira aula de segunda nao pode ser avaliada')
            pass
    #Segunda Segunda aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-2"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-2"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-2"]')))
            chrome.find_element_by_xpath('//*[@id="faces-2"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-2"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-2"]').click()
            print('Segunda aula de segunda feira feita!')
        else:
            print('Segunda aula de segunda feira já estava preenchida')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-2"]')))
            chrome.find_element_by_xpath('//*[@id="faces-2"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-2"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-2"]').click()
            print('Segunda aula de segunda feira feita!')
        except:
            print('Segunda aula de segunda nao pode ser avaliada')
            pass

    #Para terca feira
    chrome.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[2]/a').click()
    #Terca Primeira aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-3"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-3"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-3"]')))
            chrome.find_element_by_xpath('//*[@id="faces-3"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-3"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-3"]').click()
            print('Primeira aula de terca feira feita!')
        else:
            print('Primeira aula de terca feira já estava preenchida')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-3"]')))
            chrome.find_element_by_xpath('//*[@id="faces-3"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-3"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-3"]').click()
            print('Primeira aula de terca feira feita!')
        except:
            print('Primeira aula de terca nao pode ser avaliada')
            pass
    #Terca Segunda aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-4"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-4"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-4"]')))
            chrome.find_element_by_xpath('//*[@id="faces-4"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-4"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-4"]').click()
            print('Segunda aula de terca feira feita!')
        else:
            print('Segunda aula de terca feira já estava preenchida')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-4"]')))
            chrome.find_element_by_xpath('//*[@id="faces-4"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-4"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-4"]').click()
            print('Segunda aula de terca feira feita!')
        except:
            print('Segunda aula de terca nao pode ser avaliada')
            pass

    #Para quarta feira
    chrome.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[3]/a').click()
    #Quarta Primeira aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-5"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-5"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-5"]')))
            chrome.find_element_by_xpath('//*[@id="faces-5"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-5"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-5"]').click()
            print('Primeira aula de quarta feira feita!')
        else:
            print('Primeira aula de quarta feira já estava preenchida')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-5"]')))
            chrome.find_element_by_xpath('//*[@id="faces-5"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-5"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-5"]').click()
            print('Primeira aula de quarta feira feita!')
        except:
            print('Primeira aula de quarta nao pode ser avaliada')
            pass
    #Quarta Segunda aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-6"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-6"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-6"]')))
            chrome.find_element_by_xpath('//*[@id="faces-6"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-6"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-6"]').click()
            print('Segunda aula de quarta feira feita!')
        else:
            print('Segunda aula de quarta feira já estava preenchida')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-6"]')))
            chrome.find_element_by_xpath('//*[@id="faces-6"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-6"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-6"]').click()
            print('Segunda aula de quarta feira feita!')
        except:
            print('Segunda aula de quarta nao pode ser avaliada')
            pass

    #Para quinta feira
    chrome.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[4]/a').click()
    #Quinta Primeira aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-7"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-7"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-7"]')))
            chrome.find_element_by_xpath('//*[@id="faces-7"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-7"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-7"]').click()
            print('Primeira aula de quinta feira feita!')
        else:
            print('Primeira aula de quinta feira já estava preenchida')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-7"]')))
            chrome.find_element_by_xpath('//*[@id="faces-7"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-7"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-7"]').click()
            print('Primeira aula de quarta feira feita!')
        except:
            print('Primeira aula de quinta nao pode ser avaliada')
            pass
    #Quinta Segunda aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-8"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-8"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-8"]')))
            chrome.find_element_by_xpath('//*[@id="faces-8"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-8"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-8"]').click()
            print('Segunda aula de quinta feira feita!')
        else:
            print('Segunda aula de quinta feira já estava preenchida')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-8"]')))
            chrome.find_element_by_xpath('//*[@id="faces-8"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-8"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-8"]').click()
            print('Segunda aula de quarta feira feita!')
        except:
            print('Segunda aula de quarta nao pode ser avaliada')
            pass

    #Para sexta feira
    chrome.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[5]/a').click()
    #Sexta Primeira aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-9"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-9"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-9"]')))
            chrome.find_element_by_xpath('//*[@id="faces-9"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-9"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-9"]').click()
            print('Primeira aula de sexta feira feita!')
        else:
            print('Primeira aula de sexta feira já estava preenchida')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-9"]')))
            chrome.find_element_by_xpath('//*[@id="faces-9"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-9"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-9"]').click()
            print('Primeira aula de sexta feira feita!')
        except:
            print('Primeira aula de sexta nao pode ser avaliada')
            pass
    #Sexta Segunda aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-10"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-10"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-10"]')))
            chrome.find_element_by_xpath('//*[@id="faces-10"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-10"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-10"]').click()
            print('Segunda aula de sexta feira feita!')
        else:
            print('Segunda aula de sexta feira já estava preenchida')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-10"]')))
            chrome.find_element_by_xpath('//*[@id="faces-10"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-10"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-10"]').click()
            print('Segunda aula de sexta feira feita!')
        except:
            print('Segunda aula de sexta nao pode ser avaliada')
            pass

    #Para sabado
    chrome.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[6]/a').click()
    #Sabado Primeira aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-11"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-11"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-11"]')))
            chrome.find_element_by_xpath('//*[@id="faces-9"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-11"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-11"]').click()
            print('Primeira aula de sabado feito!')
        else:
            print('Primeira aula de sabado já estava preenchido')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-11"]')))
            chrome.find_element_by_xpath('//*[@id="faces-11"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-11"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-11"]').click()
            print('Primeira aula de sabado feito!')
        except:
            print('Primeira aula de sabado nao pode ser avaliado')
            pass
    #Sabado Segunda aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-12"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-12"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-12"]')))
            chrome.find_element_by_xpath('//*[@id="faces-12"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-12"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-12"]').click()
            print('Segunda aula de sabado feito!')
        else:
            print('Segunda aula de sabado já estava preenchido')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-12"]')))
            chrome.find_element_by_xpath('//*[@id="faces-12"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-12"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-12"]').click()
            print('Segunda aula de sabado feira feito!')
        except:
            print('Segunda aula de sabado nao pode ser avaliado')
            pass
    #Sabado Terceira aula
    try:
        myElem = WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="icone-13"]')))
        texto = chrome.find_element_by_xpath('//*[@id="consideracao-13"]').text
        if (texto == ""):
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-13"]')))
            chrome.find_element_by_xpath('//*[@id="faces-13"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-13"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-13"]').click()
            print('Terceira aula de sabado feito!')
        else:
            print('Terceira aula de sabado já estava preenchido')
    except:
        try:
            myElem = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consideracao-13"]')))
            chrome.find_element_by_xpath('//*[@id="faces-13"]/li[4]/label/img').click()
            chrome.find_element_by_xpath('//*[@id="consideracao-13"]').send_keys('Boa aula!')
            chrome.find_element_by_xpath('//*[@id="cadastrar-13"]').click()
            print('Terceira aula de sabado feira feito!')
        except:
            print('Terceira aula de sabado nao pode ser avaliado')
            pass
    chrome.close()
    print('')
    print('Aulas avaliadas!')

if ini == 'n':
    print('Cancelado!')