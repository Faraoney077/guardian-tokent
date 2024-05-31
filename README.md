# guardian-token

# Giriş
Bir Flask web sunucusuna rastgele tokenler entegre etmek , bu tokenleri SMTP kullanarak giriş yapıldığında bildirim mailine göndermenizi sağlar. Önemli olan dosyalarınızın içerisine bu tokenleri makro ile entegre ettiğinizde dosyalarınız çalındığında ve başka bir cihazda açıldığında size bildirim gönderilmesini sağlar

# İndirme
Uygulama Flask çalıştırabilen bütün cihazlara uyumludur. Flask sunucusu açıldıktan sonra SMTP ayarları yapılarak kullanılabilir

# Linux Tabanlı İşletim Sistemleri İçin

1. `$ git clone https://github.com/Faraoney077/guardian-token`

2. `$ cd guardian-token`

3. `$ python3 guardian-token`


# Kullanım

Uygulamayı indirdikten sonrasında bulunduğu dosyayı açınız ve `python3 guardian-token.py` komutu ile başlatınız. Daha sonrasında kullanıcı adı ve şifrenizi `(Default Kullanıcı Adı: hackathlontest , Default Şifre : hackathlon)` giriniz ve sunucuyu başlat butonuna tıklayınız. Başlattıktan sonrasında Token Oluşturma butonuna tıklayınız. Tokeniniz oluştuğunda hem bir mesaj olarak size gözükecektir hem de terminaliniz üzerinde kopyalayabileceğiniz bir şekilde yazacaktır. Tokeninizi terminal üzerinden kopyaladıktan sonrasında `http://<localip>:5000//notify?token=<Your-Secret-Token>` adresindeki doldurmanız gereken bölümleri doldurunuz. Daha sonrasında bu http url'sini istediğiniz programa entegre edebilir ve çalıştırıldığında mail alabilirsiniz

# Ayarlar

Kod bölümlerinde bulunan EMAIL_TO bölümüne kendi mail adresinizi eklemeniz gerekiyor. Kullanıcı adı ve şifre isteğe bağlı olarak kodlar üzerinden değiştirilebilir. Bu ayarlarınızı yaptıktan sonrasında büyük bir keyif ile kullanabilirsiniz. 

Not: SMTP sunucusunu değiştirecekseniz eğer sunucunun size verdiği kullanıcı adı ve şifreyi de değiştirmeniz gerekiyor. Ayrıca sunucunuz özel bir port numarası atıyorsa bu port numarasını da program üzerinden değiştirmeniz gerekiyor

# Kötüye Kullanım

Bu program tamamen sistemdeki dosyaları korumak için tasarlanmıştır. Kötüye kullanım olduğunda hiçbir şekilde sorumluluk kabul etmiyoruz
