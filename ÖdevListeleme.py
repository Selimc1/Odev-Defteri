import atexit
import json

tasks = []


def save_data():
    filename = "ÖdevListesi.json"
    with open(filename, "w") as file:
        json.dump(tasks, file)


def load_data():
    try:
        with open("ÖdevListesi.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def add_task():
    task_name = input("Ödevin adını girin: ")
    task_details = input("Ödevin detaylarını girin: ")
    tasks.append({"name": task_name, "details": task_details, "completed": False})
    print("Ödev eklendi!")


def delete_task(index):
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"{deleted_task['name']} isimli ödev silindi!")
    else:
        print("Geçersiz ödev numarası!")


def list_tasks():
    for index, task in enumerate(tasks):
        status = "Tamamlandı" if task["completed"] else "Tamamlanmadı"
        print(f"{index + 1}. {task['name']} - {task['details']} ({status})")


def edit_task():
    list_tasks()
    task_index = int(input("Düzenlemek istediğiniz ödevin numarasını girin: ")) - 1
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        print(f"Düzenleniyor: {task['name']}")
        new_name = input("Yeni adı girin (boş bırakmak için Enter'a basın): ")
        new_details = input("Yeni detayları girin (boş bırakmak için Enter'a basın): ")

        if new_name:
            task["name"] = new_name
        if new_details:
            task["details"] = new_details

        print("Ödev düzenlendi!")
    else:
        print("Geçersiz ödev numarası!")


def edit_task2():
    list_tasks()
    task_index = int(input("Düzenlemek istediğiniz ödevin numarasını girin: ")) - 1
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        print(f"Düzenleniyor: {task['name']}")
        new_status = input("Yeni tamamlanma durumunu girin (True/False): ").lower()

        if new_status == "true":
            task["completed"] = True
        elif new_status == "false":
            task["completed"] = False

        print("Ödev düzenlendi!")
    else:
        print("Geçersiz ödev numarası!")


def main():
    global tasks
    tasks = load_data()

    while True:
        print("\nÖdev Yöneticisi")
        print("1. Ödev Ekle")
        print("2. Ödevleri Listele")
        print("3. Ödevleri Düzenle")
        print("4. Ödevlerin Tamamlanmasını Düzenle")
        print("5. Ödevleri Sil")
        print("6. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            edit_task2()
        elif choice == "5":
            list_tasks()
            task_index = int(input("Silmek istediğiniz ödevin numarasını girin: ")) - 1
            delete_task(task_index)
        elif choice == "6":
            save_data()
            break
        else:
            print("Geçersiz seçenek!")


if __name__ == "__main__":
    atexit.register(save_data)
    main()
    input("Çıkmak için Enter'a basınız")
