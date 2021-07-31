from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'gfIWnubk6tQAAAAAAAAAAbvfVdnYRmOzc-e9xIvHuyCdVBF3ZLNE7Qjkr4clFb_Y'
    transferdata = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("enter the full path to upload to dropbox- ")

    transferdata.upload_files(file_from,file_to)
    print("file has been moved")

main()

