import tkinter as tk
from tkinter import messagebox, filedialog
from ftplib import FTP
from file_operations import upload_file, download_file, create_directory, delete_file

class FTPProgram:
    def __init__(self, root):
        self.root = root
        self.root.title("FTP Programı")
        self.root.geometry("800x600")

        # Kullanıcı adı ve şifre etiketleri ve giriş kutuları
        tk.Label(root, text="Kullanıcı Adı:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        tk.Label(root, text="Şifre:").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # Giriş yap düğmesi
        tk.Button(root, text="Giriş Yap", command=self.login).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.open_ftp_window()
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

    def open_ftp_window(self):
        self.root.withdraw()
        ftp_window = tk.Toplevel(self.root)
        ftp_window.title("FTP İşlemleri")

        # Dosya işlemleri butonları
        tk.Button(ftp_window, text="Dosya Yükle", command=self.upload_file_gui).pack()
        tk.Button(ftp_window, text="Dosya İndir", command=self.download_file_gui).pack()
        tk.Button(ftp_window, text="Dizin Oluştur", command=self.create_directory_gui).pack()
        tk.Button(ftp_window, text="Dosya Sil", command=self.delete_file_gui).pack()

    def upload_file_gui(self):
        self.root.withdraw()
        upload_window = tk.Toplevel(self.root)
        upload_window.title("Dosya Yükle")

        tk.Label(upload_window, text="Dosya Yolu:").pack()
        self.upload_file_path_entry = tk.Entry(upload_window)
        self.upload_file_path_entry.pack()

        tk.Button(upload_window, text="Dosya Seç", command=self.browse_file).pack()
        tk.Button(upload_window, text="Dosyayı Yükle", command=self.upload_file).pack()

    def download_file_gui(self):
        self.root.withdraw()
        download_window = tk.Toplevel(self.root)
        download_window.title("Dosya İndir")

        tk.Label(download_window, text="Dosya Adı:").pack()
        self.download_file_name_entry = tk.Entry(download_window)
        self.download_file_name_entry.pack()

        tk.Button(download_window, text="Dosyayı İndir", command=self.download_file).pack()

    def create_directory_gui(self):
        self.root.withdraw()
        create_directory_window = tk.Toplevel(self.root)
        create_directory_window.title("Dizin Oluştur")

        tk.Label(create_directory_window, text="Dizin Adı:").pack()
        self.directory_name_entry = tk.Entry(create_directory_window)
        self.directory_name_entry.pack()

        tk.Button(create_directory_window, text="Dizini Oluştur", command=self.create_directory).pack()

    def delete_file_gui(self):
        self.root.withdraw()
        delete_file_window = tk.Toplevel(self.root)
        delete_file_window.title("Dosya Sil")

        tk.Label(delete_file_window, text="Dosya Adı:").pack()
        self.delete_file_name_entry = tk.Entry(delete_file_window)
        self.delete_file_name_entry.pack()

        tk.Button(delete_file_window, text="Dosyayı Sil", command=self.delete_file).pack()

    def browse_file(self):
        file_path = tk.filedialog.askopenfilename()
        self.upload_file_path_entry.insert(tk.END, file_path)

    def upload_file(self):
        file_path = self.upload_file_path_entry.get()
        if not file_path:
            messagebox.showerror("Hata", "Dosya yolu giriniz!")
            return

        username = self.username_entry.get()
        password = self.password_entry.get()

        if upload_file(file_path, username, password):
            messagebox.showinfo("Başarılı", "Dosya başarıyla yüklendi!")
        else:
            messagebox.showerror("Hata", "Dosya yüklenirken bir hata oluştu!")

    def download_file(self):
        file_name = self.download_file_name_entry.get()
        if not file_name:
            messagebox.showerror("Hata", "Dosya adı giriniz!")
            return

        username = self.username_entry.get()
        password = self.password_entry.get()

        if download_file(file_name, username, password):
            messagebox.showinfo("Başarılı", "Dosya başarıyla indirildi!")
        else:
            messagebox.showerror("Hata", "Dosya indirilirken bir hata oluştu!")

    def create_directory(self):
        directory_name = self.directory_name_entry.get()
        if not directory_name:
            messagebox.showerror("Hata", "Dizin adı giriniz!")
            return

        username = self.username_entry.get()
        password = self.password_entry.get()

        if create_directory(directory_name, username, password):
            messagebox.showinfo("Başarılı", "Dizin başarıyla oluşturuldu!")
        else:
            messagebox.showerror("Hata", "Dizin oluşturulurken bir hata oluştu!")

    def delete_file(self):
        file_name = self.delete_file_name_entry.get()
        if not file_name:
            messagebox.showerror("Hata", "Dosya adı giriniz!")
            return

        username = self.username_entry.get()
        password = self.password_entry.get()

        if delete_file(file_name, username, password):
            messagebox.showinfo("Başarılı", "Dosya başarıyla silindi!")
        else:
            messagebox.showerror("Hata", "Dosya silinirken bir hata oluştu!")

