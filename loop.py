import multiprocessing
from utils import Utils
from firebaseinit import Firebase
import yagmail


utils = Utils()
fire = Firebase()


if __name__ == '__main__':
    count = 0
    processes = []
    data = fire.db.child('users').get()

    while True:
        processes = []
            
        for UID in data.each():
            UID = UID.key()
            print(UID)
            process = multiprocessing.Process(target=utils.monitor, args=(UID, ))
            processes.append(process)

        for process in processes:
            print(process)
            process.start()
            print(process.is_alive())

        for process in processes:
            process.join()
            print(process.is_alive())
        
        for process in processes:
            process.terminate()
            print(process.is_alive())
