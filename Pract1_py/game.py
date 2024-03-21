import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
word_displayed = ""
# Número máximo de intentos permitidos
failures = 0
total_failures = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []
vocales = ["a","e","i","o","u"]
letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print("1:Facil")
print("2.Medio")
print("3.Dificil")
opcion = int(input("Seleccione un nivel de dificultad: "))
match opcion:
 case 1:
     for letter in secret_word:
         if letter in vocales:
             letters.append(letter)
             guessed_letters.append(letter)
         else:
            letters.append("_")
     word_displayed = "".join(letters)
 case 2:
     for num in range(0,(len(secret_word))):
         if num == 0 or num == (len(secret_word) - 1):
             letters.append(secret_word[num])
         else:
             letters.append("_")
     word_displayed = "".join(letters)
 case 3:    
     word_displayed = "".join(letters) 
     word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while failures < total_failures:
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     if letter == "":
         print("No es posible ingresar un caracter vacío")
         continue
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         continue
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta
     if opcion == 2 :
         pri_ult = [secret_word[0],secret_word[len(secret_word)-1]]
         if letter in secret_word[1:-1]:
             print("¡Bien hecho! La letra está en la palabra.")
         elif letter in pri_ult:
              #explico que ya se esta mostrando en pantalla
              print('La letra ya está en la palabra, intenta con otra')
         else:
             print("Lo siento, la letra no está en la palabra.")
             failures = failures + 1
     # Mostrar la palabra parcialmente adivinada
         letters = []
     
         pos = 0
         for letter in secret_word:
             if letter in guessed_letters:
                 letters.append(letter)
             elif pos == 0 or pos == len(secret_word) - 1:
                 letters.append(letter)
             else:
                 letters.append("_")
             pos = pos + 1 
     else:
          if letter in secret_word:
             print("¡Bien hecho! La letra está en la palabra.")
          else:
             print("Lo siento, la letra no está en la palabra.")
             failures = failures + 1
          letters = []
          for letter in secret_word:
             if letter in guessed_letters:
                 letters.append(letter)
             else:
                 letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
         break
else:
     print(f"¡Oh no! Has alcanzado tus {total_failures} fallos.")
     print(f"La palabra secreta era: {secret_word}")