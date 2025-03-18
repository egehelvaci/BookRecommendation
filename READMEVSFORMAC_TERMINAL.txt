# VSCode'da Terminal Açma ve Projeyi Çalıştırma

## 1. Terminal Açma Yöntemleri
A) Kısayol ile:
   - Mac klavyenizde ⌘ (Command) tuşunu basılı tutun
   - Üstte, ESC tuşunun yanındaki ` (backtick/tırnak) tuşuna basın
   - Bu tuş genellikle Tab tuşunun üstündedir ve ~ işareti de aynı tuştadır

B) Menüden:
   - VSCode'un en üstündeki menü çubuğundan "Terminal" seçeneğine tıklayın
   - "New Terminal" seçeneğini tıklayın

C) Alternatif kısayol:
   - ⌘ + J tuşlarına basın (alt paneli açar)

## 2. Terminal'de Komutları Çalıştırma
1. Terminal açıldığında alt kısımda yeni bir panel belirecek

2. Terminal'de olduğunuzdan emin olun:
   - Terminal sekmesi seçili olmalı
   - İmleç yanıp sönüyor olmalı
   - Klasör yolu görünüyor olmalı (örn: berkecenkcivelek@Berke-MacBook-Pro KitapOneri %)

3. Şu komutu yazın ve Enter'a basın:
   ```
   source venv/bin/activate
   ```
   - Terminal'de (venv) yazısı görünecek

4. Ardından şu komutu yazın ve Enter'a basın:
   ```
   python gui.py
   ```

## 3. Terminal Panelini Özelleştirme
- Terminal panelini büyütmek için üst çizgisinden yukarı sürükleyin
- Yazı boyutunu büyütmek için ⌘ ve + tuşlarına basın
- Terminal'i kapatmak için çöp kutusu ikonuna tıklayın
- Yeni terminal açmak için + ikonuna tıklayın

## 4. Önemli Notlar
- Terminal'de (venv) yazısını görmüyorsanız sanal ortam aktif değil demektir
- Komutları yazarken küçük-büyük harfe dikkat edin
- Hata mesajları kırmızı renkte görünecektir
- Terminal'i kapatıp açmak için ⌘ + J kullanabilirsiniz 