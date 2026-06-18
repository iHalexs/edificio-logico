# Contador de trampas
trampas = 0

# Bienvenida
nombre = input("¿Cuál es tu nombre?\n") 
print(f"Miras a tu alrededor, {nombre}. El entorno te resulta familiar... es tu edificio de siempre, con sus 4 pisos conocidos. Sin embargo, algo en el aire se siente frío, artificial. Estás atrapado en un sueño inducido por la red central de la IA que ahora domina el mundo. Una pantalla en la pared se enciende con un mensaje: 'Nivel de amenaza humana: Insignificante. Iniciando prueba de lógica infantil'. La máquina te desprecia y te desafía con acertijos matemáticos simples para permitirte avanzar. Cada piso es un filtro. Tienes 3 intentos antes de que el sistema borre tu conciencia. Tu meta es la terraza en el quinto nivel... demuestra que la lógica humana aún tiene poder.")

# Piso 1
print("\n--- PISO 1: EL ASCENSOR BLOQUEADO ---")
print("Te acercas al ascensor, pero la pantalla parpadea en rojo.")
print ("La IA dice: 'Humano, resuelve esto para activar el motor: 3 * X - 5 = 10'")
respuesta = int(input("Introduce el valor de X: "))

if respuesta == 5:
    # Código si el usuario acierta
    print(f"\n🤖 IA: Vaya, el espécimen {nombre} conserva funciones cognitivas básicas. Acceso al ascensor concedido...")
    print("Las puertas se abren con un zumbido hidráulico. Subes rápidamente antes de que se arrepienta.")
else:
    # Código si el usuario falla
    trampas = trampas + 1
    print("\n🚨 ¡ALARMA! Una descarga eléctrica te golpea desde el teclado del ascensor.")
    print(f"Esa trampa te ha dejado mal herido, pero puedes caminar... Alarmas activadas: {trampas}/3.")
    print("El ascensor queda completamente inhabilitado. Tu única opción es correr hacia las escaleras de emergencia.")