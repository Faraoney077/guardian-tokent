# guardian-token

# Giriş
Bir Flask web sunucusuna rastgele tokenler entegre etmek , bu tokenleri SMTP kullanarak giriş yapıldığında bildirim mailine göndermenizi sağlar. Önemli olan dosyalarınızın içerisine bu tokenleri makro ile entegre ettiğinizde dosyalarınız çalındığında ve başka bir cihazda açıldığında size bildirim gönderilmesini sağlar

# İndirme



# Kullanım

Uygulamayı indirdikten sonrasında bulunduğu dosyayı açınız ve python3 guardian-token.py komutu ile başlatınız. Daha sonrasında kullanıcı adı ve şifrenizi (Default Kullanıcı Adı: hackathlontest , Default Şifre : hackathlon) giriniz ve sunucuyu başlat butonuna tıklayınız. Başlattıktan sonrasında Token Oluşturma butonuna tıklayınız. Tokeniniz oluştuğunda hem bir mesaj olarak size gözükecektir hem de terminaliniz üzerinde kopyalayabileceğiniz bir şekilde yazacaktır. Tokeninizi terminal üzerinden kopyaladıktan sonrasında http://<localip>:5000//notify?token=<Your-Secret-Token> adresindeki doldurmanız gereken bölümleri doldurunuz. Daha sonrasında bu http url'sini istediğiniz programa entegre edebilir ve çalıştırıldığında mail alabilirsiniz
