class Herramientas:
    
    def lista_primo(self,lista):
        self.lista = lista
        
        lista_primos = []
        for i in self.lista:
            if verificar_primo(i):
                lista_primos.append(i)
        return lista_primos
    
    def verificar_primo(self,numero):
        self.numero = numero
        
        es_primo=False
        
        if self.numero < 2:
            return False
        
        for i in range(2,self.numero):
            if self.numero%i == 0:
                return False
        
        else:
            return True
        
    def factorial(self,numero):
        
        self.numero = numero
        
        lista_fac = []
        factorial = 1

        if type(self.numero) == int:
            for i in range(1, self.numero+1):
                factorial *= i
                lista_fac.append(factorial)
            return factorial

        elif type(self.numero) == list:
            for i in self.numero:
                temp_factorial = 1
                for j in range(1, i+1):
                    temp_factorial *= j
                lista_fac.append(temp_factorial)

            return lista_fac


    def moda(self,lista):
        self.lista = lista
        dic_moda ={}
    
        for i in self.lista:
            if i in dic_moda:
                dic_moda[i] += 1
            else:
                dic_moda[i] = 1

        valor_moda = max(dic_moda,key=lambda x : dic_moda[x])

        return(print(f'el valor que mas se repite es {valor_moda} unas {dic_moda[valor_moda]}'))

