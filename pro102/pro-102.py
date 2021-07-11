import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)

    vco = cv2.VideoCapture(0)

    result = True

    while(result):

        ret,frame = vco.read()

        iN="img" + str(number) + ".png"

        cv2.imwrite(iN, frame)

        start_time = time.time

        result=False

        
    return iN

    print("A snapshot was taken.")
    
    vco.release()

    cv2.destroyAllWindows()


take_snapshot()

def upload_file(iN):
    at = 'sl.A0bIH1FOvWIGcDhDm6P8GhQ8h7tJSE4_HZ0ny2ctDDsV8DFb8GDaQI2oJoVjJoPl54btc5E5igtmKEqWuOVsDywQLDYliq8kLwFWFrmQNCRoGlOSaJpCo_SZCU7jmYzBKZQIU0lwL-vJ'
    file = iN
    ff = file
    ft = "/image_folder/" + (iN)
    dbx = dropbox.Dropbox(at)

    with open(ff, "rb") as f:
        dbx.files_upload(f.read(), ft, mode=dropbox.files.WriteMode.overwrite)
        print("Your file has been uploaded to Dropbox.")

def main():
    while (True):
        if((time.time() - start_time)>=4):
            name=take_snapshot()
            upload_file(name)

main()
   
    