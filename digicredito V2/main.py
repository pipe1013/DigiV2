# import endPoints as ep
# import os
# import multiprocessing as MP
# import time

# if "main" == __name__:
#     procesos = []
#     t = time.time()
#     while (time.time() - t) < 1200:
#         for i in range(10):
#             proceso = MP.Process(target=ep.main)
#             procesos.append(proceso)
#             proceso.start()
#         for proceso in procesos:
#             proceso.join()











# if __name__ == "__main__":
#     t = time.time()
#     while (time.time() - t) < 300:
#         hilos = []
#         for i in range(100):
#             tarea = MP.Process(target=flujo)
#             hilos.append(tarea)
#             tarea.start()

#         for tarea in hilos:
#             tarea.join()