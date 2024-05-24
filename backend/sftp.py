# import paramiko
# import os

# def sftp_connection(func):
#     def wrapper(hostname, username, password, *args, **kwargs):
#         try:
#             # create SSH client
#             ssh = paramiko.SSHClient()
#             ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#             ssh.connect(hostname, username=username, password=password)

#             # create SFTP client
#             sftp = ssh.open_sftp() 

#             result = func(sftp, *args, **kwargs)


#             sftp.close()
#             ssh.close()

#             return result

#         except Exception as e:
#             print("Error while uploading file:", e)    

#     return wrapper

# @sftp_connection
# def sftp_upload(sftp, local_file, remote_file):
#     sftp.put(local_file, remote_file)

# @sftp_connection
# def sftp_download(sftp, local_file, remote_file):
#     sftp.get(remote_file, local_file)

# # def sftp_download(hostname, username, password, remote_file, local_file):
# #     try:
# #         print("SSH istemcisi oluşturuluyor...")
# #         ssh = paramiko.SSHClient()
# #         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #         ssh.connect(hostname, username=username, password=password)
# #         print("SSH bağlantisi başarili.")

# #         print("SFTP istemcisi oluşturuluyor...")
# #         sftp = ssh.open_sftp()
# #         print("SFTP bağlantisi başarili.")

# #         # Hedef dizinin yazılabilir olup olmadığını kontrol edin
# #         target_directory = os.path.dirname(local_file)
# #         if not os.path.exists(target_directory):
# #             os.makedirs(target_directory)
# #         if not os.access(target_directory, os.W_OK):
# #             raise PermissionError(f"Yazma izniniz yok: '{target_directory}'")

# #         print(f"'{remote_file}' dosyasi '{local_file}' olarak indiriliyor...")
# #         sftp.get(remote_file, local_file)
# #         print("Dosya başariyla indirildi.")

# #         sftp.close()
# #         ssh.close()
        
# #     except Exception as e:
# #         print("Dosya indirilirken hata oluştu:", e)

# @sftp_connection
# def sftp_remove(sftp, remote_file):
#     sftp.remove(remote_file)

# @sftp_connection
# def sftp_listdir(sftp, remote_path):
#     return sftp.listdir(remote_path)

# def getFiles():
#     hostname = '192.168.207.166'
#     username = 'buraxta'
#     password = 'buraxta'


#     # local_file = "C:\\Users\\Yavuz\\OneDrive\\Masaüstü\\test.txt"
#     # remote_file = '/home/buraxta/Desktop/sample/'
#     remote_path = '/home/buraxta/Desktop/sample/'

#     remote_files_and_dirs = sftp_listdir(hostname, username, password, remote_path)
#     return remote_files_and_dirs
# # print(getFiles())

# #sftp_upload(hostname, username, password, local_file, remote_file)
# sftp_download("192.168.207.166", "buraxta", "buraxta", "/home/buraxta/Desktop/sample/1.png", "C:\\Users\\burak\\OneDrive\\Masaüstü")
# #sftp_remove(hostname, username, password, remote_file)

import paramiko

def sftp_connection(func):
    def wrapper(hostname, username, password, *args, **kwargs):
        try:
            # create SSH client
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname, username=username, password=password)

            # create SFTP client
            sftp = ssh.open_sftp() 

            result = func(sftp, *args, **kwargs)


            sftp.close()
            ssh.close()

            return result

        except Exception as e:
            print("Error while uploading file:", e)    

    return wrapper

@sftp_connection
def sftp_upload(sftp, local_file, remote_file):
    sftp.put(local_file, remote_file)

@sftp_connection
def sftp_download(sftp, remote_file, local_file):
    sftp.get(remote_file, local_file)

@sftp_connection
def sftp_remove(sftp, remote_file):
    sftp.remove(remote_file)

@sftp_connection
def sftp_listdir(sftp, remote_path):
    return sftp.listdir(remote_path)

# hostname = '192.168.69.77'
# username = 'selim'
# password = 'bnt123BNT'

# buraxta = ""

# local_file = "C:\\Users\\Yavuz\\OneDrive\\Masaüstü\\test.txt"
# remote_file = '/home/selim/Desktop/sample/demo'
# remote_path = '/home/selim/Desktop/sample/'

# remote_files_and_dirs = sftp_listdir(hostname, username, password, remote_path)

def getFiles():
    hostname = '192.168.207.166'
    username = 'buraxta'
    password = 'buraxta'


    # local_file = "C:\\Users\\Yavuz\\OneDrive\\Masaüstü\\test.txt"
    # remote_file = '/home/buraxta/Desktop/sample/'
    remote_path = '/home/buraxta/Desktop/sample/'

    remote_files_and_dirs = sftp_listdir(hostname, username, password, remote_path)
    return remote_files_and_dirs


#sftp_upload(hostname, username, password, local_file, remote_file)
#sftp_download(hostname, username, password, remote_file, local_file)
#sftp_remove(hostname, username, password, remote_file)