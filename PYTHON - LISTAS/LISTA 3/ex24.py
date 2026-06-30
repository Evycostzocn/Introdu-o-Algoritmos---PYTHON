# 24. Crie uma classe chamada Cronometro, responsável por representar um intervalo
# de tempo por meio dos atributos:
# • horas;
# • minutos;
# • segundos.
# 15
# O construtor deve criar o cronômetro inicialmente com 0:0:0.
# Implemente os métodos:
# • avancar_segundo(): acrescenta um segundo ao horário;
# • retroceder_segundo(): reduz um segundo, sem permitir valores negativos;
# • reiniciar(): retorna o cronômetro para zero;
# • converter_para_segundos(): retorna o tempo total em segundos;
# • exibir_tempo(): apresenta o tempo no formato hh:mm:ss.
# O método avancar_segundo() deve atualizar corretamente os minutos e as horas. Por exemplo, depois de 00:59:59, o tempo deve passar para 01:00:00.
# No programa principal, crie dois cronômetros e realize operações diferentes em cada
# um, demonstrando que os objetos mantêm estados independentes.

# --- CLASSE CRONOMETRO ---
class Cronometro:
    def __init__(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0

    def avancar_segundo(self):
        self.segundos += 1
        if self.segundos == 60:
            self.segundos = 0
            self.minutos += 1
            if self.minutos == 60:
                self.minutos = 0
                self.horas += 1

    def retroceder_segundo(self):
        if self.horas == 0 and self.minutos == 0 and self.segundos == 0:
            return  # Já está em zero, não faz nada

        self.segundos -= 1
        if self.segundos < 0:
            self.segundos = 59
            self.minutos -= 1
            if self.minutos < 0:
                self.minutos = 59
                self.horas -= 1

    def reiniciar(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0

    def converter_para_segundos(self):
        return (self.horas * 3600) + (self.minutos * 60) + self.segundos

    def exibir_tempo(self):
        print(f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}")


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    c1 = Cronometro()
    c2 = Cronometro()

    # --- Operações no Cronômetro 1 (Avanço com virada de tempo) ---
    print("--- CRONÔMETRO 1 ---")
    # Forçando um estado próximo da virada para testar a lógica
    c1.horas = 0
    c1.minutos = 59
    c1.segundos = 58
    
    print("Tempo inicial:")
    c1.exibir_tempo()
    
    c1.avancar_segundo()
    c1.avancar_segundo()  # Deve virar para 01:00:00
    print("Após avançar 2 segundos:")
    c1.exibir_tempo()
    print(f"Total em segundos: {c1.converter_para_segundos()}s\n")

    # --- Operações no Cronômetro 2 (Retrocesso e Independência de estado) ---
    print("--- CRONÔMETRO 2 ---")
    c2.horas = 1
    c2.minutos = 0
    c2.segundos = 1
    
    print("Tempo inicial:")
    c2.exibir_tempo()
    
    c2.retroceder_segundo()
    c2.retroceder_segundo()  # Deve virar para 00:59:59
    print("Após retroceder 2 segundos:")
    c2.exibir_tempo()
    
    c2.reiniciar()
    print("Após reiniciar:")
    c2.exibir_tempo()