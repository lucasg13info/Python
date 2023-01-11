import pyautogui
import time

def pyautoguiStado():
    
    pyautogui.PAUSE = 1
    pyautogui.hotkey("win")
    pyautogui.write("db")
    pyautogui.press("enter")

    time.sleep(20)
    pyautogui.click(x=12, y=231)
    time.sleep(5)
    
    #Clica no Database
    pyautogui.click(x=37, y=265)
    time.sleep(2)
    
    pyautogui.click(x=67, y=525)
    
    time.sleep(1)
    pyautogui.click(x=84, y=579)
    
    #clica com o botão direito para abrir o menu
    time.sleep(1)
    pyautogui.rightClick(x=183, y=599)
    
    #Clica no exportar
    time.sleep(2)
    pyautogui.click(x=551, y=298)
    
    #Clica em CSV
    time.sleep(3)
    pyautogui.doubleClick(x=973, y=292)
    
    #Clica em next
    time.sleep(1)
    pyautogui.click(x=1225, y=835)
    
    #clica para listar os metas
    time.sleep(1)
    pyautogui.click(x=937, y=396)
    
    pyautogui.write("iso")
    
    #Seleciona ISO 8859-1
    time.sleep(1)
    pyautogui.click(x=856, y=119)
    
    #Selecionando pasta para salvar arquivo
    time.sleep(1)
    pyautogui.click(x=1617, y=318)
    
    #Selecionando a pasta Imagens
    time.sleep(1)
    pyautogui.click(x=724, y=473)
    
    #Abrindo a pasta Cargas
    time.sleep(1)
    pyautogui.doubleClick(x=946, y=594)
    
    time.sleep(1)
    pyautogui.click(x=1209, y=809)
    
    time.sleep(1)
    pyautogui.click(x=1228, y=832)
    
    #Clicando em start para começar a exportar planilha
    time.sleep(1)
    pyautogui.click(x=1343, y=834)
    
    #Comando para selecinar texto e limpar tela
    pyautogui.hotkey('ctrl', 'a')    
    time.sleep(90)



    #----------------------------------------------------------#    
    #   Finalizado o download da planilha
    #----------------------------------------------------------#   
    
    #Fechando a tb de consulta
    pyautogui.click(x=13, y=237)
    
    #Abrindo Banco prevendas B2B
    time.sleep(7)
    pyautogui.click(x=14, y=462)
    
    #Abrindo Banco prevendas B2B - ok
    time.sleep(1)
    pyautogui.click(x=39, y=492)
    
    #Abrindo Schemas - ok
    time.sleep(4)
    pyautogui.click(x=62, y=714)
    
    #Dar 10 cliques para subir a tela
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    
    #Abrindo arquitetura - ok
    time.sleep(10)
    pyautogui.click(x=86, y=742)
    
    #Dar 10 cliques para subir a tela
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    
    #Clica em arquitetura - ok
    time.sleep(1)
    pyautogui.click(x=110, y=773)
    
    #Dar 10 cliques para subir a tela
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    pyautogui.doubleClick(x=535, y=179)
    
    #Clica em tables - ok
    time.sleep(6)
    pyautogui.click(x=137, y=796)
    
    #Clicando com botão direito em rel_transicao2 - ok
    time.sleep(1)
    pyautogui.rightClick(x=298, y=851)
    
    #Clicando em read sql data para digitar comandos sql 
    time.sleep(1)
    pyautogui.click(x=579, y=647)
    
    #Clicando no espaço em branco 
    time.sleep(3)
    pyautogui.click(x=659, y=277) 
    
    time.sleep(2)
    pyautogui.hotkey("ctrl", "a") 
    
    time.sleep(1)
    pyautogui.hotkey("del")   
    
    #Digitando comaando truncate
    time.sleep(1)
    pyautogui.write("truncate table PREVENDAS_B2B.Arquitetura.rel_transicao2;")
    
    #Executando o truncate
    time.sleep(2)
    pyautogui.click(x=563, y=145) 
    
    
    
    
    #------------------------------------------------
    #   Carregando a planilha
    # ----------------------------------------------
    
    #Import
    time.sleep(2)
    pyautogui.rightClick(x=290, y=846) 
    
    #Import data
    time.sleep(1)
    pyautogui.click(x=544, y=569) 
    
    #CSV
    time.sleep(1)
    pyautogui.doubleClick(x=651, y=260)
    
    #Abrindo pasta Imagem
    time.sleep(1)
    pyautogui.click(x=698, y=468)
    
    #Abrindo pasta Planilha carga
    time.sleep(1)
    pyautogui.doubleClick(x=952, y=598)
    
    #Pegando a planilha
    time.sleep(1)
    pyautogui.doubleClick(x=912, y=390)
    
    #Next
    time.sleep(1)
    pyautogui.click(x=1237, y=835)
    
    #Next again
    time.sleep(5)
    pyautogui.click(x=1237, y=835)
    
    #Next again
    time.sleep(3)
    pyautogui.click(x=1237, y=835)
    
    #Start
    time.sleep(2)
    pyautogui.click(x=1385, y=827)
    
    
    time.sleep(170)   
    print("Carga realizada com sucesso!")
    
pyautoguiStado()


def enviaEmail():
    print("Essa função vai mandar e-mail com a planilha carregada e horário da carga")



def pegarPosicaoMouse():
    time.sleep(5)
    #pyautogui.position(x=12, y=231)
    #pyautogui.position(x=12, y=231)
    print(pyautogui.position())#rodar()
#pegarPosicaoMouse()