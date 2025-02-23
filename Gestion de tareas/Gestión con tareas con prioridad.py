import heapq

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority):
        priority_dict = {'Alta': 1, 'Media': 2, 'Baja': 3}
        heapq.heappush(self.tasks, (priority_dict[priority], task))

    def process_task(self):
        if self.tasks:
            priority, task = heapq.heappop(self.tasks)
            print(f"Procesando tarea: {task} con prioridad {priority}")
        else:
            print("No hay tareas pendientes")

    def show_tasks(self):
        if not self.tasks:
            print("No hay tareas pendientes")
            return
        sorted_tasks = sorted(self.tasks, key=lambda x: x[0])
        for priority, task in sorted_tasks:
            print(f"Tarea: {task}, Prioridad: {priority}")

    def delete_task(self, task):
        self.tasks = [t for t in self.tasks if t[1] != task]
        heapq.heapify(self.tasks)

def main():
    manager = TaskManager()
    while True:
        print("1. Agregar nueva tarea")
        print("2. Procesar tarea mas urgente")
        print("3. Mostrar lista de tareas")
        print("4. Salir")
        option = input("Seleccione una opcion: ")
        if option == '1':
            task = input("Ingrese la tarea: ")
            priority = input("Ingrese la prioridad (Alta, Media, Baja): ")
            manager.add_task(task, priority)
        elif option == '2':
            manager.process_task()
        elif option == '3':
            manager.show_tasks()
        elif option == '4':
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()
