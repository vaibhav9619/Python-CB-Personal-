import time
def download(text1):
    for i in range(5):
        time.sleep(1)
        print("We have Downloaded",i,"of file")
    print(text1,"succesfully downloaded")
download("hello")
print("Helllo")#it will execute after 5 sec only so its the main problem so we use multithreading concept