import storage

storage_set_flag = True
local_repository = ""


def set_up_storage(value):
    storage.remount('/', value)


def save_to_database(content):
    global storage_set_flag
    if storage_set_flag:
        try:
            print("Saving to text-file...")
            with open("database.txt", "w+") as file:
                file.write(read_database() + content)
        except OSError:
            storage_set_flag = False
            print("Tried opening via text-file, but failed. Switching to local repository")
    else:
        print("Saving to local repository...")
        global local_repository
        local_repository += content


def read_database():
    with open("database.txt", "r") as file:
        lines = file.readlines()

    if storage_set_flag:
        return lines
    else:
        return lines + local_repository

