from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server():
    # Yetkilendirme için bir DummyAuthorizer oluşturuyoruz
    authorizer = DummyAuthorizer()

    # Bir kullanıcı eklemek (kullanıcı adı, şifre, dizin, izinler)
    authorizer.add_user("admin", "admin", r"C:\Users\Oğuzhan\Desktop\FTP_Root", perm="elradfmw")

    # Handler ve Server oluşturma
    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("127.0.0.1", 2342), handler)  # IP adresi ve port numarasını ayarlama

    # Sunucuyu başlatma
    server.serve_forever()

if __name__ == "__main__":
    start_ftp_server()
