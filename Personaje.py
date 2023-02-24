class Personaje:
    #Definimos el constructor de personaje
    def __init__(self,esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    

    #Metodos Personaje

    def correr(self,status):
        if(status):
            print("El personaje "+ self.__nombre +" esta corriendo")
        else:
            print("El personaje "+ self.__nombre +"cse detuvo")

    def lanzarGranadas(self):
        print("El personaje "+ self.__nombre +" lanzo una granada")

    def recargarArma(self, municiones):
        cargador= 10
        cargador= cargador + municiones
        print("El arma tiene "+ str(cargador) +" balas")
    
    def __pensar(self):                                           #Agregar una función de pensar y tiene que ser privado
        print("Estoy pensando.................")
    
    #Declarar Getters y Setter de atributos
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nom):
        self.__nombre= nom
        
    def getEspecie(self):
        return self.__especie
    def setEspecie(self,esp):
        self.__especie= esp
        
    def getAltura(self):
        return self.__altura
    def setAltura(self,alt):
        self.__altura= alt    
    