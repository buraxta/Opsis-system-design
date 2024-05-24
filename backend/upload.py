import paramiko


def sftp_upload(local_file, remote_file, hostname='192.168.207.166', username='buraxta', password='buraxta'):
    try:
        # SSH istemcisi oluştur ve bağlan
        print("SSH istemcisi oluşturuluyor...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        print("SSH bağlantısı başarılı.")

        # SFTP istemcisi oluştur
        print("SFTP istemcisi oluşturuluyor...")
        sftp = ssh.open_sftp()
        print("SFTP bağlantısı başarılı.")

        # Dosyayı yükle
        print(f"'{local_file}' dosyası '{remote_file}' olarak yükleniyor...")
        sftp.put(local_file, remote_file)
        print("Dosya başarıyla yüklendi.")

        # SFTP ve SSH bağlantılarını kapat
        sftp.close()
        ssh.close()
        
    except Exception as e:
        print("Dosya yüklenirken hata oluştu:", e)


hostname = '192.168.207.166'
username = 'buraxta'
password = 'buraxta'
local_file = r'C:\\Users\\burak\\OneDrive\\Masaüstü\\yavız\\OPSIS RAPOR.doc'
remote_file = '/home/buraxta/Desktop/OPSIS RAPOR.doc'  # Ubuntu'daki tam hedef yol

sftp_upload(hostname, username, password, local_file, remote_file)

