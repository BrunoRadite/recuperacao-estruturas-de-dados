class Questao4:
    
    @staticmethod
    def decodeString(string_codificada: str):
        # pilhas onde iremos armazenar respectivamente como a string final está atualmente,
        # o numero de vezes que será repetido, e as strings de dentro dos []
        atual, numeros, strings = [], [], []
        
        # o numero de vezes que será repetido, esse valor entrará na pilha numeros
        n = 0

        # vamos percorrer pela entrada
        for caractere in string_codificada:
            
            # verificamos se o caractere atual é um número
            if(caractere.isdigit()):
                # atualizaremos o valor de n
                # essa formula serve para caso tenha dois caracteres inteiros juntos ele concidere
                # que fazem parte de um único número 
                n = n * 10 + ord(caractere) - ord('0')
            
            # caso o caractere seja [   
            elif(caractere == '['):
                # vamos adicionar n em numeros
                numeros.append(n)
                
                # atualizar o valor de n para 0 para receber a próxima sequência de numeros, se ouver
                n = 0
                
                # guarda dentro de strings a string atual
                strings.append(atual)
                
                # limpa a string atual para a próxima(s) string(s) que vinher
                atual = []

            # verifica se caractere é igual a ]
            elif(caractere == ']'):
                # somente uma validação
                try:
                    # vamos adicionar todos os elementos da string atual * a quantidade
                    # que essa string deve ser repetida 
                    strings[-1].extend(atual * numeros.pop())
                    
                    # atualizamos a atual para receber a nova string já com os valores multiplicados
                    atual = strings.pop()
                    
                # somente em caso de erro
                except:
                    erro = 'String inválida verifique se todos os [] estão sendo respeitados'
                    print(erro)
                    return erro
            
            # se for uma string
            else:
                # adicionaremos ela na atual
                atual.append(caractere)
             
        # formatando a string atual para ser de fato uma string
        string_final = "".join(strings[-1]) if strings else "".join(atual)
        
        # mostrando no terminal
        print(string_final)
        
        # retornando caso esse valor necessite ser usado em outro metodo 
        return string_final
    