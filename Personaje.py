class Personaje:
    #Definimos el constructor de personaje
    def __init__(self,esp,nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
    

    #Metodos Personaje

    def correr(self,status):
        if(status):
            print("El personaje "+ self.nombre +" esta corriendo")
        else:
            print("El personaje "+ self.nombre +"cse detuvo")

    def lanzarGranadas(self):
        print("El personaje "+ self.nombre +" lanzo una granada")

    def recargarArma(self, municiones):
        cargador= 10
        cargador= cargador + municiones
        print("El arma tiene "+ str(cargador) +" balas")
    