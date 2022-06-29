####################################################################################################################################
#                                                  Prática - Redes de Computadores 1                                               #
#                                                  Aluna: Fernanda Azevedo/1912623                                                 #
#                                                 Jogo: Pedra, papel, tesoura, lagarto, Spock                                      #
####################################################################################################################################
# REGRAS : Tesoura corta papel                                                                                                     #
#            Papel cobre pedra                                                                                                     #
#              Pedra esmaga lagarto                                                                                                #
#               Lagarto envenena Spock                                                                                             #
#                 Spock esmaga (ou derrete) tesoura                                                                                #
#                    Tesoura decapita lagarto                                                                                      #
#                      Lagarto come papel                                                                                          #
#                        Papel refuta Spock                                                                                        #
#                         Spock vaporiza pedra                                                                                     #
#                           Pedra amassa tesoura                                                                                   #
####################################################################################################################################

# Bibliotecas necessárias
import socket

# Criação e configuração do socket
socket_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip='127.0.0.1'

port=50000

dest=(ip,port)

socket_client.connect(dest)

rodadas_jogo=0

print("""     
      !!!!!!!!!!!!!!! BEM - VINDO AO JOGO !!!!!!!!!!!!!
      ******************** REGRAS: ********************
      ************* Tesoura corta papel  **************
      *************  Papel cobre pedra    ************* 
      ************* Pedra esmaga lagarto  ************* 
      ************ Lagarto envenena Spock  ************ 
      ************ Spock derrete tesoura  *************
      *********** Tesoura decapita lagarto ************
      ************* Lagarto come papel  ***************
      ************* Papel refuta Spock  ***************
      ************ Spock vaporiza pedra ***************
      ************* Pedra amassa tesoura ************** """+'\n')

while rodadas_jogo<3:   
    
    rodadas_jogo+=1
    tam_mensagem=int.from_bytes(socket_client.recv(2),'big') # Verifica o tamanho da mensagem 
    mensagem_server=socket_client.recv(tam_mensagem).decode()
   
     
    # Imprime a quantidade de rodadas (máximo 3)
    print("Rodada: " + str(rodadas_jogo) + "/3") 
    print(mensagem_server)    
     
    # Aquisição das entradas do cliente              
    text=input('Digite sua jogada: ') #Adquire a entrada do cliente
    #Verifica as entradas
    if text == "Spock" or text == "Tesoura" or "Papel" or "Lagarto" or "Pedra":            
       pacote_client = text.encode()   # Codifica o pacote com a entrada do cliente
       socket_client.send(pacote_client) # Manda dados para o servidor
       tam_mensagem=int.from_bytes(socket_client.recv(2),'big') # Verifica o tamanho da mensagem
       mensagem_server=socket_client.recv(tam_mensagem).decode() # Decodifica a mensagem do servidor
       print(mensagem_server)
       
    else: 
      print("Palavra inválida, conexão encerrada !!!")
      socket_client.close()   # Caso a entrada seja inválida encerra a conexão                                     


# Verifica as condições para fim de jogo e imprime a mensagem final
if rodadas_jogo==3:     
  tam_mensagem=int.from_bytes(socket_client.recv(2),'big')
  mensagem_server=socket_client.recv(tam_mensagem).decode()
  print(mensagem_server)   
  socket_client.close()
# Encerra a conexão
socket_client.close()           
