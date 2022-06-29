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
import random
import socket

# Dicionário de palavras do jogo
dic = ['Spock', 'Lagarto', 'Pedra', 'Papel', 'Tesoura'] 

# Seleciona aleatoriamente uma das opções do dicionário 
def select_random(dic): 
     return random.choice(dic)

rodadas=0
vitorias=0
derrotas=0
empates=0

# Mensagens para o cliente 

mensagem_inicio = "... Pedra, Papel , Tesoura, Lagarto, Spock ..."

mensagem_ganhador = "PARABÉNS !!! VOCÊ GANHOU !!!"

mensagem_empate = " EMPATE !!! TENTE OUTRA VEZ !!!"

mensagem_perdedor = " QUE PENA !!! NÃO FOI DESSA VEZ !!! "

mensagem_final = "********** FIM DE JOGO!!!! ********** "

# Criação e configuração do socket
socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip='127.0.0.1'

port=50000

origin=(ip,port)

socket_server.bind(origin)

socket_server.listen(1)

[socket_dados,info_cliente]=socket_server.accept()

# Configurações do jogo: 
while rodadas <3:
    
    # Envia mensagem de início do jogo 
      
     status=0
     rodadas+=1          
     
     # Manda a mensagem para o servidor
     
     pacote=len(mensagem_inicio).to_bytes(2,'big')+ mensagem_inicio.encode()
     socket_dados.send(pacote)
     
     # Recebe a mensagem do cliente
     print("Recebendo dados do servidor...")
     mensagem_client = socket_dados.recv(7)
     
          
     if not mensagem_client: 
          break
     
     jogada = str(mensagem_client.decode())
     
     print("Jogada do cliente: "  + jogada)
     jogada_server=select_random(dic)          
    
     
     ######### VERIFICAÇÃO DAS CONDIÇÕES DO JOGO ############     
    
     if jogada == "Spock":       
          if jogada_server == 'Lagarto' or jogada_server=='Papel':                             
               derrotas+=1
               status=1               
                              
          elif jogada_server=='Spock': 
               empates+=1
               status=2  
                              
          elif jogada_server == 'Pedra' or jogada_server=='Tesoura':
               vitorias+=1
               status=3               
               
     elif jogada == 'Tesoura':
          if jogada_server == 'Spock' or jogada_server=='Pedra':
               derrotas+=1
               status=1              
               
          elif jogada_server=='Tesoura': 
               empates+=1
               status=2          
               
          elif jogada_server == 'Papel' or jogada_server=='Lagarto':
               vitorias+=1
               status=3                  
              
     
     elif jogada == 'Papel':
          if jogada_server == 'Tesoura' or jogada_server=='Lagarto':
               derrotas+=1
               status=1    
                   
          elif jogada_server=='Papel':
               empates+=1
               status=2                       
               
          elif jogada_server == 'Pedra' or jogada_server=='Spock':
               vitorias+=1
               status=3      
               
                              
     elif jogada == 'Pedra':
          if jogada_server == 'Papel' or jogada_server=='Spock':
               derrotas+=1
               status=1         
               
          elif jogada_server=='Pedra': 
               empates+=1
               status=2                      
               
          elif jogada_server == 'Tesoura' or jogada_server=='Lagarto':
               vitorias+=1
               status=3    
                    
     elif jogada == 'Lagarto':
          if jogada_server == 'Tesoura' or jogada_server=='Pedra':
               derrotas+=1
               status=1          
               
          elif jogada_server=='Lagarto':
               empates+=1
               status=2                
               
          elif jogada_server == 'Spock' or jogada_server=='Papel':
               vitorias+=1
               status=3          

     # Cria o pacote com as mensagens para enviar ao cliente
     if status==1:
        mensagem_pacote = 'Jogada do servidor: '+ str(jogada_server) + '\n=> RESULTADO: ' + mensagem_perdedor + '\n'
        pacote=len(mensagem_pacote).to_bytes(2,'big')+ mensagem_pacote.encode()
        socket_dados.send(pacote)
        
     if status==2:
        mensagem_pacote = 'Jogada do servidor: '+ str(jogada_server) + '\n=> RESULTADO: ' + mensagem_empate + '\n'
        pacote=len(mensagem_pacote).to_bytes(2,'big')+ mensagem_pacote.encode()
        socket_dados.send(pacote)     
     
     if status==3:
        mensagem_pacote = 'Jogada do servidor: '+ str(jogada_server) + '\n=> RESULTADO: ' + mensagem_ganhador + '\n'
        pacote=len(mensagem_pacote).to_bytes(2,'big')+ mensagem_pacote.encode()
        socket_dados.send(pacote)
     
# Condições para finalização do jogo
if rodadas==3:
        
        # Cria o pacote de mensagem final 
        mensagem_pacote = mensagem_final +'\n'+"Derrotas: " + str(derrotas)+ '\n' + "Empates: "+ str(empates)+ '\n' + "Vitorias: " +  str(vitorias)+'\n'  
        pacote= len(mensagem_pacote).to_bytes(2,'big')+ mensagem_pacote.encode()
        socket_dados.send(pacote)          
    

# Encerra as conexões
socket_dados.close()
socket_server.close()
