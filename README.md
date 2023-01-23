# ObjectDetectionWithHaar-Cascade
 Object detection with haar-cascade

Haar-Cascade üzerinde özel bir nesne tanımlamamız gerektiği zaman, ilk önce tanıtmak istediğimiz nesnenin veri setini oluşturmamız gereklidir. Tanıtmak istediğimiz özel nesnenin veri setini oluşturabilmemiz için seçtiğimiz nesnenin farklı ışık açıları altında, farklı yerlerde ve farklı saatlerde fotoğrafları çekilmelidir. 

![1](https://user-images.githubusercontent.com/73904811/214069504-99ea69e8-428c-4428-8030-ee6b176629b2.png)
 
İlk önce http://www.mediafire.com/file/1aq02tpidk105fv/dasar_haartrain.rar/file sitesinden zip dosyası indirilir ve bu dosya klasöre aktarılır.

 ![2](https://user-images.githubusercontent.com/73904811/214069637-b6017610-c73c-4797-b38e-5c54f8fd2ba9.png)

Çekilen bu nesne fotoğrafları positive/rawdata fotoğraf klasörüne eklenir ve daha sonra positive klasörü içerisindeki objectmarker.exe ile çektiğimiz nesne fotoğrafları üzerinde nesnenin konumu seçilip kaydedilir. 
Negative klasörü içinde nesnenin olmadığı fotoğraflar bulunmalıdır. İndirdiğimiz haarcascade paketinin içinde bulunan negative dosyasındaki fotoğraflara, nesneyi çektiğimiz ortamın fotoğraflarını eklenmelidir ve negative fotoğraf sayıları oluşturduğumuz positive veri seti fotoğraflarıyla orantılı olacak şekilde sayısı ayarlanmalıdır (Aralarında ortalama olarak %30-%40’lık bir fark olmalıdır). Daha sonra samples_creation.bat dosyası çalıştırılarak vector klasörü içinde nesne fotoğraflarımız aktarılmış olur. Sonrasında haarTraining.bat dosyasını düzenleme ekranı açılır ve -npos ve -nneg değerleri positive ve negative fotoğraf sayımıza göre güncellenir ve kaydedilir. Daha sonra aynı dosya üzerine çift tık yapılıp dosya çalıştırılır ve yapay zekanın eğitilmesi sağlanır. Yapayzekamız eğitildikten sonra convert.bat dosyası çalıştırılır ve klasörümüzün içerisinde myhaar.xml adında veri seti dosyamız oluşturulmuş olur.

![3](https://user-images.githubusercontent.com/73904811/214069716-e26a1510-79a8-461d-bfb7-8e136dbfe847.png)

Oluşan bu veri seti dosyası yazdığımız nesne tanıma kodumuz ile aynı klasöre atılır.

![4](https://user-images.githubusercontent.com/73904811/214069778-8720b877-7109-4665-8ade-1c7621332450.png)

Veri seti dosyamızı oluşturduktan sonra yazdığımız koda geldiğimizde kodlarımızda kütüphanelerimiz tanımlanır. ‘CascadeClassifier’ fonksiyonumuzla özel nesne olarak tanımladığımız nesnenin veri seti dosyasına ulaşılır. Daha sonra kamera açma fonksiyonumuzu çağırılır. Sonrasında fps değerini hesaplayabilmek için ilk zaman değişkenlerini tanımlıyoruz. Bu işlemleri gerçekleştirdikten sonra döngümüzü oluşturuyoruz ve ekranımızı tanımlayıp, ekran pikselleri üzerinde gezinmesi ve nesneleri tanıması sağlanır. Nesneyi tanıdığında nesne üzerinde dikdörtgen çizme kodu yazılır ve ekran boyutu yeniden boyutlandırılır(500x300). Daha sonra fps değerlendirmesi için anlık piksel hızlarına bakılır ve fps değerleri ekranın sol üst köşesine anlık olarak yazdırılır. Ekranın kapatılması ve kodun sonlandırılması için çıkış tuşu olarak esc(27) tuşu atanmıştır. Bu tuşa basıldığında ekran kapanır ve kod sonlanır.
