import secrets
import uuid
import threading
from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import Tk, Toplevel, messagebox, Label, Entry, Button
import datetime

app = Flask(__name__)
server_thread = None
server_stop_event = threading.Event()

# E-posta ayarları
SMTP_SERVER = 'smtp-relay.brevo.com'
SMTP_PORT = 587
SMTP_USERNAME = '75c05d001@smtp-brevo.com'
SMTP_PASSWORD = 'XdQEK1RhsabPTFZy'
EMAIL_FROM = 'deneme@hackathlontest.com.tr'
EMAIL_TO = 'faraoney077@gmail.com'
EMAIL_SUBJECT = 'Dosya Açıldı Bildirimi'

# Kullanıcı adı ve şifre
USERNAME = 'hackathlontest'
PASSWORD = 'hackathlon'

def generate_token():
    token = f"{uuid.uuid4()}-{secrets.token_hex(16)}"
    messagebox.showinfo("Token Oluşturma", f"Yeni bir token oluşturuldu: {token}")
    print(f"Oluşturulan Token: {token}")
    return token

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print("Email sent successfully")
        messagebox.showinfo("Mail Gönderme", "Mail başarıyla gönderildi.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        messagebox.showerror("Mail Gönderme", f"Mail gönderme başarısız oldu: {e}")

@app.route('/notify', methods=['GET'])
def notify():
    token = request.args.get('token')
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    access_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if token:
        subject = 'Dosya Açıldı Bildirimi'
        body = f"Açılan Dosyanın Tokeni: {token}.\nIP Address: {ip_address}\nUser-Agent: {user_agent}\nGiriş Zamanı: {access_time}"
        send_email(subject, body)
        return "Notification received", 200
    else:
        return "No token provided", 400

def start_flask():
    server_stop_event.clear()
    app.run(host='0.0.0.0', port=5000, use_reloader=False)

def sunucu_calistirma():
    global server_thread
    server_thread = threading.Thread(target=start_flask)
    server_thread.start()
    messagebox.showinfo("Sunucu Çalıştırma", "Sunucu başlatılıyor...")

def sunucu_durdurma():
    if server_thread and server_thread.is_alive():
        server_stop_event.set()
        server_thread.join()
        messagebox.showinfo("Sunucu Durdurma", "Sunucu durduruldu.")
    else:
        messagebox.showwarning("Sunucu Durdurma", "Çalışan bir sunucu yok.")

def terminate_thread(thread):
    if thread.is_alive():
        import ctypes
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, 0)
            print('Exception raise failure')

def token_olusturma():
    generated_token = generate_token()
    print(f"Oluşturulan Token: {generated_token}")

def validate_login(username, password):
    return username == USERNAME and password == PASSWORD

def show_main_panel():
    main_panel = Toplevel(root)
    main_panel.title("Hackathon Uygulaması - Ana Panel")
    main_panel.geometry("600x400")
    main_panel.configure(bg="#0f3057")

    # Butonları oluşturma
    btn_sunucu = Button(main_panel, text="Sunucu Çalıştırma", command=sunucu_calistirma, bg="white")
    btn_sunucu.place(x=230, y=50, width=150, height=50)

    btn_sunucu_durdur = Button(main_panel, text="Sunucu Durdurma", command=sunucu_durdurma, bg="white")
    btn_sunucu_durdur.place(x=230, y=130, width=150, height=50)

    btn_token = Button(main_panel, text="TOKEN OLUŞTURMA", command=token_olusturma, bg="white")
    btn_token.place(x=230, y=210, width=150, height=50)

    def close_app():
        if server_thread and server_thread.is_alive():
            terminate_thread(server_thread)
        main_panel.destroy()

    def minimize_app():
        main_panel.iconify()

    def maximize_app():
        main_panel.state('zoomed')


# Kullanıcı Girişi için Panel
root = Tk()
root.title("Hackathon Uygulaması - Giriş")
root.geometry("600x400")
root.configure(bg="#0f3057")

username_label = Label(root, text="Kullanıcı Adı:", bg="#0f3057", fg="white")
username_label.place(x=150, y=120, width=100, height=30)
username_entry = Entry(root, bg="white")
username_entry.place(x=260, y=120, width=200, height=30)

password_label = Label(root, text="Şifre:", bg="#0f3057", fg="white")
password_label.place(x=150, y=160, width=100, height=30)
password_entry = Entry(root, show="*", bg="white")
password_entry.place(x=260, y=160, width=200, height=30)

def login():
    username = username_entry.get()
    password = password_entry.get()
    if validate_login(username, password):
        messagebox.showinfo("Giriş Başarılı", "Giriş başarılı! Ana panele yönlendiriliyorsunuz.")
        root.withdraw()
        show_main_panel()
    else:
        messagebox.showerror("Giriş Hatası", "Kullanıcı Adı veya Şifre Hatalı!")
        subject = 'Hatalı Giriş Bildirimi'
        body = f"Hatalı giriş denemesi:\nKullanıcı Adı: {username}\nŞifre: {password}\nGiriş Zamanı: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        send_email(subject, body)

login_button = Button(root, text="Giriş", command=login, bg="white")
login_button.place(x=260, y=200, width=100, height=30)

root.mainloop()
