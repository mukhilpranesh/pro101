import dropbox

class TransferData:
    def __init__(self,access_token):
     self.access_token=access_token
 
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.BrvKqdzEvmFIQPG_Y-urk_Sc4ngIa5-_a6dPPi74iV1YuPmAnzVjOwaYwzwkEpKJa12__o97XKQBk_jF8szPZeJI-FLECFnfCoXxgA9Q5FLZhtbLZw3F3wHO_Xau-fS85rupi0zeOy4Y"
    transferData=TransferData(access_token)
    file_from=input("enter the file path to transfer")
    file_to=input("enter the full path to upload to dropbox")
    #file_from='file1.txt'
    #file_to='/whj/file1.txt'
    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()