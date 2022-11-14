class Questao1:

    @staticmethod
    def stringValida(string):
        #criando a pilha
        pilha = []
        
        #alimentando a pilha
        for item in string:
            
            #verificando se o caractere atual é fechando, se for temos que atualizar que o anterior será sempre o ultimo da pilha(que terá os abrindo)
            #e verificando se na lista tem algum elemento se não tiver já cai no falso pois indica que o primeiro elemento é algo fechando
            if item != '(' and item != '[' and item != '{' and len(pilha)>0:
                anterior = pilha[-1]
                
                #o anterior vai ser sempre abrindo então aqui verificamos se o item é fechando o ultimo caso não seja já retorna falso
                if (item == ")" and anterior == "(") or (item == "]" and anterior == "[") or (item == "}" and anterior == "{"):
                    pilha.pop()
                    
                #retornando falso pois o ultimo não foi fechado
                else:
                    print(False)
                    return False
                
            #se for abrindo algo ele vai entrar na pilha para ser verificado no if de cima
            else:
                pilha.append(item)
                
        #se a lista estiver vazia é porque todos foram abertos e fechados
        if len(pilha) == 0:
            print(True)
            return True
        
        #se não algo está errado
        else:
            print(False)
            return False