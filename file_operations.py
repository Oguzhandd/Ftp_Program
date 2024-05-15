from ftplib import FTP

from ftplib import FTP

def upload_file(file_path, username, password, ftp_server="127.0.0.1", ftp_port=2342):
    try:
        ftp = FTP()
        ftp.connect(ftp_server, ftp_port)
        ftp.login(username, password)
        with open(file_path, 'rb') as file:
            ftp.storbinary('STOR ' + file_path, file)
        ftp.quit()
        return True
    except Exception as e:
        print(e)
        return False

def download_file(file_path, username, password, ftp_server="127.0.0.1", ftp_port=2342):
    try:
        ftp = FTP()
        ftp.connect(ftp_server, ftp_port)
        ftp.login(username, password)
        with open(file_path, 'wb') as file:
            ftp.retrbinary('RETR ' + file_path, file.write)
        ftp.quit()
        return True
    except Exception as e:
        print(e)
        return False

def create_directory(directory_name, username, password, ftp_server="127.0.0.1", ftp_port=2342):
    try:
        ftp = FTP()
        ftp.connect(ftp_server, ftp_port)
        ftp.login(username, password)
        ftp.mkd(directory_name)
        ftp.quit()
        return True
    except Exception as e:
        print(e)
        return False

def delete_file(file_name, username, password, ftp_server="127.0.0.1", ftp_port=2342):
    try:
        ftp = FTP()
        ftp.connect(ftp_server, ftp_port)
        ftp.login(username, password)
        ftp.delete(file_name)
        ftp.quit()
        return True
    except Exception as e:
        print(e)
        return False

