def ocupação(R:int, C:int, reservar:list, liberar:list):
    sala = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ]
    if sala[reservar[0]][reservar[1]] == 0:
        sala[reservar[0]][reservar[1]] = 1
        print("Seat reserved successfully!")
    else:
        print("Seat already occupied.")
    for r in sala:
        print(r)

    if sala[liberar[0]][liberar[1]] == 1:
        sala[liberar[0]][liberar[1]] = 0
        print("Seat freed successfully!")
    else:
        print("Seat already free.")
    for r in sala:
        print(r)

ocupação(3, 5, [1,2], [0,4])