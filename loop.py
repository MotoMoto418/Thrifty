import multiprocessing
from utils import Utils
from firebaseinit import Firebase


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
            process = multiprocessing.Process(target=utils.monitor, args=(UID, ))
            processes.append(process)

        for process in processes:
            process.start()

        for process in processes:
            process.join()
        
        for process in processes:
            process.terminate()
