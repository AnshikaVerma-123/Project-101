import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token =  access_token

    def upload_file(self, filefrom, fileto):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(filefrom):

            for filename in files:
                localpath = os.path.join(root, filename)

                relative_path = os.path.relpath(localpath, filefrom)
                dropbox_path = os.path.join(fileto, relative_path)
                with open(localpath, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.AbKQY7cwlr949HZB7JxLOMrnYKuY39PSkiEnMjmzkLJ8mukldzSQjT8oLVfn_A-kB4yn6O0erRD07aV-9JeaGvvRPoLFEVvwg3_p2AufnKjhGlCgTVtpR4YV0SKhk6nbU2-ztZAB'
    transferData = TransferData(access_token)

    filefrom = str(input("Enter the folder path:- "))
    fileto = input("enter the path to upload to dropbox:- ")

    transferData.upload_file(filefrom,fileto)
    print("file has moved!!")

main()