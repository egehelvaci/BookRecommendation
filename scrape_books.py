import json

def create_turkish_books_database():
    books = {
        "books": [
            {
                "title": "İnce Memed",
                "author": "Yaşar Kemal",
                "genre": "roman",
                "description": "Çukurova'da geçen, eşkıyalık ve adalet temalı epik bir roman.",
                "keywords": ["çukurova", "eşkıya", "adalet", "köy", "anadolu"]
            },
            {
                "title": "Tutunamayanlar",
                "author": "Oğuz Atay",
                "genre": "modern",
                "description": "Modern Türk edebiyatının başyapıtlarından, varoluşsal sorunları ele alan roman.",
                "keywords": ["varoluş", "modernizm", "aydın", "toplum", "yabancılaşma"]
            },
            {
                "title": "Kürk Mantolu Madonna",
                "author": "Sabahattin Ali",
                "genre": "romantik",
                "description": "Aşk ve toplumsal sınıf farklılıklarını anlatan etkileyici bir roman.",
                "keywords": ["aşk", "sınıf", "toplum", "yalnızlık", "drama"]
            },
            {
                "title": "Suç ve Ceza",
                "author": "Dostoyevski",
                "genre": "psikolojik",
                "description": "İnsanın karanlık yönlerini ve vicdan kavramını sorgulayan psikolojik bir başyapıt.",
                "keywords": ["suç", "vicdan", "psikoloji", "felsefe", "toplum"]
            },
            {
                "title": "Şeker Portakalı",
                "author": "Jose Mauro De Vasconcelos",
                "genre": "dram",
                "description": "Yoksul bir çocuğun gözünden hayatı anlatan duygusal bir hikaye.",
                "keywords": ["çocukluk", "yoksulluk", "sevgi", "büyüme", "hayat"]
            },
            {
                "title": "Simyacı",
                "author": "Paulo Coelho",
                "genre": "felsefi",
                "description": "Kişisel yolculuk ve kendini keşfetme temalı felsefi bir roman.",
                "keywords": ["yolculuk", "keşif", "kişisel gelişim", "felsefe", "maneviyat"]
            },
            {
                "title": "1984",
                "author": "George Orwell",
                "genre": "distopya",
                "description": "Totaliter bir rejimi ve gözetim toplumunu anlatan distopik roman.",
                "keywords": ["distopya", "totaliterizm", "gözetim", "özgürlük", "siyaset"]
            },
            {
                "title": "Fareler ve İnsanlar",
                "author": "John Steinbeck",
                "genre": "dram",
                "description": "Dostluk ve hayatta kalma mücadelesini anlatan etkileyici bir roman.",
                "keywords": ["dostluk", "yoksulluk", "umut", "drama", "yaşam"]
            },
            {
                "title": "Dönüşüm",
                "author": "Franz Kafka",
                "genre": "absürt",
                "description": "Bir insanın böceğe dönüşmesini anlatan absürt ve alegorik bir roman.",
                "keywords": ["metamorfoz", "yabancılaşma", "absürt", "aile", "varoluş"]
            },
            {
                "title": "Sefiller",
                "author": "Victor Hugo",
                "genre": "klasik",
                "description": "Adalet, merhamet ve aşkı konu alan epik bir toplumsal roman.",
                "keywords": ["adalet", "merhamet", "aşk", "toplum", "mücadele"]
            },
            {
                "title": "Yabancı",
                "author": "Albert Camus",
                "genre": "felsefi",
                "description": "Varoluşçu felsefenin temel taşlarından, toplumsal yabancılaşmayı anlatan roman.",
                "keywords": ["varoluşçuluk", "yabancılaşma", "absürt", "felsefe", "toplum"]
            },
            {
                "title": "Beyaz Diş",
                "author": "Jack London",
                "genre": "macera",
                "description": "Bir kurt köpeğinin vahşi doğa ve medeniyet arasındaki mücadelesini anlatan roman.",
                "keywords": ["doğa", "hayatta kalma", "macera", "dostluk", "özgürlük"]
            },
            {
                "title": "Uçurtma Avcısı",
                "author": "Khaled Hosseini",
                "genre": "dram",
                "description": "Dostluk, ihanet ve kefareti konu alan, Afganistan'da geçen etkileyici bir roman.",
                "keywords": ["dostluk", "aile", "savaş", "kefaret", "çocukluk"]
            },
            {
                "title": "Satranç",
                "author": "Stefan Zweig",
                "genre": "psikolojik",
                "description": "İnsan zihninin sınırlarını zorlayan, psikolojik gerilim dolu bir novella.",
                "keywords": ["satranç", "psikoloji", "obsesyon", "delilik", "zeka"]
            },
            {
                "title": "Fahrenheit 451",
                "author": "Ray Bradbury",
                "genre": "distopya",
                "description": "Kitapların yakıldığı bir gelecekte geçen, düşünce özgürlüğünü savunan distopik roman.",
                "keywords": ["distopya", "sansür", "özgürlük", "kitaplar", "toplum"]
            },
            {
                "title": "Martı",
                "author": "Anton Çehov",
                "genre": "tiyatro",
                "description": "Sanat, aşk ve yaşam üzerine düşündüren klasik bir tiyatro eseri.",
                "keywords": ["sanat", "aşk", "yaşam", "tiyatro", "edebiyat"]
            },
            {
                "title": "Bir İdam Mahkumunun Son Günü",
                "author": "Victor Hugo",
                "genre": "dram",
                "description": "İdam cezasının insanlık dışılığını anlatan, güçlü bir toplumsal eleştiri.",
                "keywords": ["idam", "adalet", "toplum", "vicdan", "hukuk"]
            },
            {
                "title": "Otomatik Portakal",
                "author": "Anthony Burgess",
                "genre": "distopya",
                "description": "Şiddet, özgür irade ve toplumsal kontrol üzerine düşündüren distopik roman.",
                "keywords": ["şiddet", "özgür irade", "toplum", "kontrol", "gençlik"]
            },
            {
                "title": "Hayvan Çiftliği",
                "author": "George Orwell",
                "genre": "politik",
                "description": "Totaliter rejimleri alegorik olarak eleştiren politik bir hiciv.",
                "keywords": ["politika", "totaliterizm", "devrim", "propaganda", "toplum"]
            },
            {
                "title": "Mai ve Siyah",
                "author": "Halid Ziya Uşaklıgil",
                "genre": "roman",
                "description": "Servet-i Fünun döneminin başyapıtlarından, bir gencin hayalleri ve hayal kırıklıklarını anlatan roman.",
                "keywords": ["edebiyat", "aşk", "hayal kırıklığı", "sanat", "İstanbul"]
            },
            {
                "title": "Araba Sevdası",
                "author": "Recaizade Mahmut Ekrem",
                "genre": "roman",
                "description": "Tanzimat döneminin önemli eserlerinden, züppe tipini eleştiren satirik bir roman.",
                "keywords": ["tanzimat", "modernleşme", "züppe", "komedi", "İstanbul"]
            },
            {
                "title": "Çalıkuşu",
                "author": "Reşat Nuri Güntekin",
                "genre": "roman",
                "description": "Genç bir öğretmenin Anadolu'daki yaşamını ve aşkını anlatan klasik bir roman.",
                "keywords": ["anadolu", "öğretmen", "aşk", "fedakarlık", "eğitim"]
            },
            {
                "title": "Yalnızız",
                "author": "Peyami Safa",
                "genre": "psikolojik",
                "description": "Modernleşme sürecinde bireyin iç dünyasını ve yalnızlığını anlatan psikolojik roman.",
                "keywords": ["yalnızlık", "modernleşme", "psikoloji", "aşk", "felsefe"]
            },
            {
                "title": "Tehlikeli Oyunlar",
                "author": "Oğuz Atay",
                "genre": "modern",
                "description": "Modern Türk edebiyatının önemli eserlerinden, bir aydının iç dünyasını anlatan roman.",
                "keywords": ["modernizm", "yabancılaşma", "aydın", "oyun", "toplum"]
            },
            {
                "title": "Dokuzuncu Hariciye Koğuşu",
                "author": "Peyami Safa",
                "genre": "roman",
                "description": "Hasta bir gencin hastane günlerini ve aşkını anlatan otobiyografik roman.",
                "keywords": ["hastalık", "aşk", "hastane", "gençlik", "mücadele"]
            },
            {
                "title": "Eylül",
                "author": "Mehmet Rauf",
                "genre": "roman",
                "description": "Yasak aşkı ve evlilik kurumunu sorgulayan psikolojik bir roman.",
                "keywords": ["aşk", "evlilik", "ihanet", "psikoloji", "burjuvazi"]
            },
            {
                "title": "Madam Bovary",
                "author": "Gustave Flaubert",
                "genre": "roman",
                "description": "Taşra yaşamından bunalan bir kadının yasak aşklarını anlatan klasik roman.",
                "keywords": ["aşk", "evlilik", "taşra", "kadın", "toplum"]
            },
            {
                "title": "Babalar ve Oğullar",
                "author": "Ivan Turgenyev",
                "genre": "roman",
                "description": "Kuşak çatışmasını ve değişen Rusya'yı anlatan klasik roman.",
                "keywords": ["kuşak çatışması", "değişim", "aile", "ideoloji", "gençlik"]
            },
            {
                "title": "Sineklerin Tanrısı",
                "author": "William Golding",
                "genre": "roman",
                "description": "Issız bir adada mahsur kalan çocukların vahşileşme sürecini anlatan alegorik roman.",
                "keywords": ["vahşilik", "medeniyet", "çocuk", "toplum", "güç"]
            },
            {
                "title": "Bülbülü Öldürmek",
                "author": "Harper Lee",
                "genre": "roman",
                "description": "Irkçılık ve adaleti bir çocuğun gözünden anlatan Pulitzer ödüllü roman.",
                "keywords": ["ırkçılık", "adalet", "çocukluk", "toplum", "hukuk"]
            },
            {
                "title": "Küçük Prens",
                "author": "Antoine de Saint-Exupéry",
                "genre": "felsefi",
                "description": "Çocuksu bir masalın ardında derin felsefi anlamlar barındıran klasik eser.",
                "keywords": ["felsefe", "masumiyet", "dostluk", "sevgi", "yaşam"]
            },
            {
                "title": "Dune",
                "author": "Frank Herbert",
                "genre": "bilimkurgu",
                "description": "Uzak gelecekte geçen, politik entrikalar ve gezegen ekolojisini konu alan epik bilimkurgu.",
                "keywords": ["bilimkurgu", "politika", "ekoloji", "din", "güç"]
            },
            {
                "title": "Cesur Yeni Dünya",
                "author": "Aldous Huxley",
                "genre": "distopya",
                "description": "Teknoloji ve konfora dayalı totaliter bir toplumu anlatan distopik roman.",
                "keywords": ["distopya", "teknoloji", "toplum", "mutluluk", "özgürlük"]
            },
            {
                "title": "Gazap Üzümleri",
                "author": "John Steinbeck",
                "genre": "roman",
                "description": "Büyük Buhran döneminde bir ailenin hayatta kalma mücadelesini anlatan roman.",
                "keywords": ["yoksulluk", "göç", "aile", "umut", "mücadele"]
            },
            {
                "title": "Yeraltından Notlar",
                "author": "Dostoyevski",
                "genre": "psikolojik",
                "description": "Modern insanın yabancılaşmasını ve iç çatışmalarını anlatan psikolojik roman.",
                "keywords": ["yabancılaşma", "modernizm", "psikoloji", "toplum", "birey"]
            },
            {
                "title": "Şibumi",
                "author": "Trevanian",
                "genre": "gerilim",
                "description": "Bir suikastçının hayatını ve Doğu felsefesini harmanlayan gerilim romanı.",
                "keywords": ["gerilim", "doğu", "felsefe", "sanat", "mücadele"]
            },
            {
                "title": "Körlük",
                "author": "Jose Saramago",
                "genre": "roman",
                "description": "Gizemli bir körlük salgınının toplumu nasıl etkilediğini anlatan alegorik roman.",
                "keywords": ["körlük", "toplum", "kaos", "insanlık", "medeniyet"]
            },
            {
                "title": "Nutuk",
                "author": "Mustafa Kemal Atatürk",
                "genre": "tarih",
                "description": "Türk Kurtuluş Savaşı'nı ve Cumhuriyet'in kuruluşunu anlatan tarihi eser.",
                "keywords": ["tarih", "cumhuriyet", "bağımsızlık", "mücadele", "devrim"]
            },
            {
                "title": "Sherlock Holmes - Kızıl Soruşturma",
                "author": "Arthur Conan Doyle",
                "genre": "polisiye",
                "description": "Sherlock Holmes'un ilk macerası, karmaşık bir cinayet soruşturmasını konu alır.",
                "keywords": ["dedektif", "cinayet", "gizem", "mantık", "soruşturma"]
            },
            {
                "title": "Da Vinci Şifresi",
                "author": "Dan Brown",
                "genre": "gerilim",
                "description": "Tarihi sırlar ve komplo teorilerini içeren heyecan dolu bir macera.",
                "keywords": ["gizem", "tarih", "komplo", "macera", "din"]
            },
            {
                "title": "Androidler Elektrikli Koyun Düşler Mi?",
                "author": "Philip K. Dick",
                "genre": "bilimkurgu",
                "description": "İnsan ve android arasındaki sınırları sorgulayan distopik bilimkurgu.",
                "keywords": ["yapay zeka", "distopya", "bilinç", "teknoloji", "gelecek"]
            },
            {
                "title": "Hobbit",
                "author": "J.R.R. Tolkien",
                "genre": "fantastik",
                "description": "Orta Dünya'da geçen, bir hobbiti beklenmedik bir maceraya sürükleyen fantastik roman.",
                "keywords": ["fantastik", "macera", "ejderha", "hazine", "kahramanlık"]
            },
            {
                "title": "Saatleri Ayarlama Enstitüsü",
                "author": "Ahmet Hamdi Tanpınar",
                "genre": "roman",
                "description": "Zaman, modernleşme ve bürokrasi üzerine ironik bir roman.",
                "keywords": ["zaman", "modernleşme", "bürokrasi", "ironi", "toplum"]
            },
            {
                "title": "İstanbul Hatırası",
                "author": "Ahmet Ümit",
                "genre": "polisiye",
                "description": "İstanbul'un tarihi dokusunda geçen, geçmişle bugünü birleştiren polisiye roman.",
                "keywords": ["istanbul", "tarih", "cinayet", "gizem", "arkeoloji"]
            },
            {
                "title": "Huzursuzluk",
                "author": "Zülfü Livaneli",
                "genre": "roman",
                "description": "Ortadoğu'da yaşanan dramı ve insani değerleri sorgulayan çağdaş roman.",
                "keywords": ["savaş", "aşk", "ortadoğu", "göç", "kimlik"]
            },
            {
                "title": "Kafamda Bir Tuhaflık",
                "author": "Orhan Pamuk",
                "genre": "roman",
                "description": "İstanbul'un değişimini bir boza satıcısının gözünden anlatan roman.",
                "keywords": ["istanbul", "değişim", "aşk", "göç", "modernleşme"]
            },
            {
                "title": "Anna Karenina",
                "author": "Lev Tolstoy",
                "genre": "klasik",
                "description": "Yasak aşk ve toplumsal normları konu alan Rus edebiyatının başyapıtı.",
                "keywords": ["aşk", "toplum", "evlilik", "rusya", "ahlak"]
            },
            {
                "title": "Yüzyıllık Yalnızlık",
                "author": "Gabriel Garcia Marquez",
                "genre": "büyülü gerçekçilik",
                "description": "Buendia ailesinin yedi kuşağını anlatan büyülü gerçekçilik başyapıtı.",
                "keywords": ["aile", "latin amerika", "büyü", "tarih", "yalnızlık"]
            },
            {
                "title": "Doğu Ekspresinde Cinayet",
                "author": "Agatha Christie",
                "genre": "polisiye",
                "description": "Ünlü dedektif Hercule Poirot'nun kar fırtınasında mahsur kalan bir trendeki cinayet soruşturması.",
                "keywords": ["dedektif", "tren", "cinayet", "gizem", "soruşturma"]
            },
            {
                "title": "Başlangıç",
                "author": "Dan Brown",
                "genre": "gerilim",
                "description": "Bilim ve din çatışmasını konu alan, semboloji profesörü Robert Langdon'ın macerası.",
                "keywords": ["bilim", "din", "teknoloji", "gizem", "macera"]
            },
            {
                "title": "Vakıf",
                "author": "Isaac Asimov",
                "genre": "bilimkurgu",
                "description": "Galaktik İmparatorluğun çöküşünü ve yeni bir medeniyetin kuruluşunu anlatan bilimkurgu klasiği.",
                "keywords": ["gelecek", "bilim", "medeniyet", "uzay", "toplum"]
            },
            {
                "title": "Neuromancer",
                "author": "William Gibson",
                "genre": "bilimkurgu",
                "description": "Siberpunk türünün öncüsü, sanal gerçeklik ve yapay zekayı konu alan roman.",
                "keywords": ["siberpunk", "hacker", "yapay zeka", "teknoloji", "gelecek"]
            },
            {
                "title": "Kırmızı Saçlı Kadın",
                "author": "Orhan Pamuk",
                "genre": "roman",
                "description": "Baba-oğul ilişkisi ve Doğu-Batı çatışmasını ele alan çağdaş roman.",
                "keywords": ["baba", "oğul", "gelenek", "modernlik", "mitoloji"]
            },
            {
                "title": "Sevgili Arsız Ölüm",
                "author": "Latife Tekin",
                "genre": "roman",
                "description": "Büyülü gerçekçilik öğeleriyle Anadolu yaşamını anlatan roman.",
                "keywords": ["köy", "büyü", "yoksulluk", "aile", "göç"]
            },
            {
                "title": "Karamazov Kardeşler",
                "author": "Dostoyevski",
                "genre": "klasik",
                "description": "Ahlak, inanç ve aile ilişkilerini sorgulayan felsefi roman.",
                "keywords": ["ahlak", "din", "aile", "suç", "felsefe"]
            },
            {
                "title": "Don Kişot",
                "author": "Miguel de Cervantes",
                "genre": "klasik",
                "description": "Şövalyelik romanlarını hicveden, modern romanın öncüsü kabul edilen başyapıt.",
                "keywords": ["şövalye", "macera", "hiciv", "dostluk", "hayal"]
            },
            {
                "title": "Bin Muhteşem Güneş",
                "author": "Khaled Hosseini",
                "genre": "dram",
                "description": "Afganistan'da iki kadının hayatını ve dostluğunu anlatan etkileyici bir roman.",
                "keywords": ["kadın", "dostluk", "savaş", "afganistan", "mücadele"]
            },
            {
                "title": "Puslu Kıtalar Atlası",
                "author": "İhsan Oktay Anar",
                "genre": "fantastik",
                "description": "17. yüzyıl İstanbul'unda geçen, gerçekle hayali harmanlayan postmodern roman.",
                "keywords": ["istanbul", "tarih", "fantastik", "osmanlı", "gizem"]
            },
            {
                "title": "Kuyucaklı Yusuf",
                "author": "Sabahattin Ali",
                "genre": "roman",
                "description": "Taşra yaşamını ve toplumsal adaletsizliği anlatan gerçekçi bir roman.",
                "keywords": ["taşra", "adalet", "aşk", "toplum", "yozlaşma"]
            },
            {
                "title": "Aylak Adam",
                "author": "Yusuf Atılgan",
                "genre": "modern",
                "description": "Modern kent insanının yalnızlığını ve yabancılaşmasını anlatan roman.",
                "keywords": ["yalnızlık", "modernizm", "kent", "arayış", "yabancılaşma"]
            },
            {
                "title": "Bir Dinozorun Anıları",
                "author": "Mina Urgan",
                "genre": "anı",
                "description": "Türk edebiyatının önemli akademisyenlerinden birinin yaşam öyküsü.",
                "keywords": ["anı", "edebiyat", "akademi", "cumhuriyet", "kadın"]
            },
            {
                "title": "Gece",
                "author": "Bilge Karasu",
                "genre": "modern",
                "description": "Karanlık ve alegorik bir anlatımla totalitarizmi eleştiren roman.",
                "keywords": ["totalitarizm", "alegori", "karanlık", "şiddet", "korku"]
            },
            {
                "title": "Kaplumbağalar",
                "author": "Fakir Baykurt",
                "genre": "köy",
                "description": "Anadolu köy yaşamını ve köylülerin mücadelesini anlatan roman.",
                "keywords": ["köy", "anadolu", "mücadele", "yoksulluk", "değişim"]
            },
            {
                "title": "Anayurt Oteli",
                "author": "Yusuf Atılgan",
                "genre": "psikolojik",
                "description": "Bir otel kâtibinin iç dünyasını ve yalnızlığını anlatan psikolojik roman.",
                "keywords": ["yalnızlık", "obsesyon", "taşra", "cinsellik", "bunalım"]
            },
            {
                "title": "Huzur",
                "author": "Ahmet Hamdi Tanpınar",
                "genre": "roman",
                "description": "İstanbul'un kültürel dokusunu ve bir aşk hikâyesini anlatan roman.",
                "keywords": ["istanbul", "müzik", "aşk", "kültür", "medeniyet"]
            },
            {
                "title": "Kırk Mantolu Madonna",
                "author": "Sabahattin Ali",
                "genre": "roman",
                "description": "Bir aşk hikâyesi üzerinden toplumsal sınıf farklılıklarını anlatan roman.",
                "keywords": ["aşk", "sınıf", "yoksulluk", "almanya", "gurbet"]
            },
            {
                "title": "Ve Perde İndi",
                "author": "Agatha Christie",
                "genre": "polisiye",
                "description": "Hercule Poirot'nun son vakası, ölümcül bir seri katili durdurmak için verdiği mücadele.",
                "keywords": ["dedektif", "cinayet", "gizem", "suç", "final"]
            },
            {
                "title": "Sessiz Çığlık",
                "author": "Angela Marsons",
                "genre": "polisiye",
                "description": "Dedektif Kim Stone'un, bir çocuk cinayetini araştırırken ortaya çıkardığı karanlık sırlar.",
                "keywords": ["dedektif", "cinayet", "psikolojik", "gizem", "gerilim"]
            },
            {
                "title": "Kızıl Dosya",
                "author": "Arthur Conan Doyle",
                "genre": "polisiye",
                "description": "Sherlock Holmes'un ilk macerası, intikam ve gizem dolu bir cinayet soruşturması.",
                "keywords": ["dedektif", "cinayet", "mantık", "gizem", "londra"]
            },
            {
                "title": "Karanlık Orman",
                "author": "Tana French",
                "genre": "polisiye",
                "description": "Dublin Cinayet Masası dedektiflerinin, bir çocuğun kaybolmasıyla başlayan karmaşık soruşturması.",
                "keywords": ["dedektif", "kayıp", "psikolojik", "irlanda", "gizem"]
            },
            {
                "title": "Millennium Üçlemesi",
                "author": "Stieg Larsson",
                "genre": "polisiye",
                "description": "Gazeteci Mikael Blomkvist ve hacker Lisbeth Salander'in karanlık sırları ortaya çıkardığı sürükleyici seri.",
                "keywords": ["hacker", "gazetecilik", "suç", "İsveç", "gerilim"]
            },
            {
                "title": "Baskerville'lerin Köpeği",
                "author": "Arthur Conan Doyle",
                "genre": "polisiye",
                "description": "Sherlock Holmes'un lanetli bir ailenin gizemli köpek vakasını çözdüğü efsanevi macera.",
                "keywords": ["dedektif", "gizem", "korku", "lanet", "İngiltere"]
            },
            {
                "title": "Cinayet Alfabesi",
                "author": "Agatha Christie",
                "genre": "polisiye",
                "description": "Hercule Poirot'nun alfabetik sırayla işlenen cinayetleri çözmeye çalıştığı soluksuz roman.",
                "keywords": ["dedektif", "seri katil", "gizem", "mantık", "İngiltere"]
            },
            {
                "title": "Ejderha Dövmeli Kız",
                "author": "Stieg Larsson",
                "genre": "polisiye",
                "description": "Kayıp bir kızın hikayesini araştıran gazeteci ve dahi hacker'ın karanlık sırları ortaya çıkarması.",
                "keywords": ["hacker", "İsveç", "suç", "gizem", "teknoloji"]
            },
            {
                "title": "Kar Kokusu",
                "author": "Jo Nesbø",
                "genre": "polisiye",
                "description": "Dedektif Harry Hole'un Oslo'da işlenen seri cinayetleri araştırdığı gerilim dolu roman.",
                "keywords": ["dedektif", "İskandinav", "kar", "seri katil", "Norveç"]
            },
            {
                "title": "Çakallar",
                "author": "Ahmet Ümit",
                "genre": "polisiye",
                "description": "İstanbul'un karanlık sokaklarında işlenen cinayetleri araştıran Başkomiser Nevzat'ın hikayesi.",
                "keywords": ["İstanbul", "cinayet", "tarih", "gizem", "dedektif"]
            },
            {
                "title": "Yıldızlararası İmparatorluk",
                "author": "Isaac Asimov",
                "genre": "bilimkurgu",
                "description": "Galaktik İmparatorluğun çöküşünü engellemek için mücadele eden bilim insanlarının hikayesi.",
                "keywords": ["uzay", "gelecek", "bilim", "imparatorluk", "medeniyet"]
            },
            {
                "title": "Zaman Makinesi",
                "author": "H.G. Wells",
                "genre": "bilimkurgu",
                "description": "Bir mucit'in geleceğe yaptığı yolculukta insanlığın evrimini keşfetmesi.",
                "keywords": ["zaman yolculuğu", "gelecek", "evrim", "toplum", "bilim"]
            },
            {
                "title": "Solaris",
                "author": "Stanisław Lem",
                "genre": "bilimkurgu",
                "description": "Gizemli bir gezegenin insan psikolojisiyle etkileşimini anlatan felsefi bilimkurgu.",
                "keywords": ["uzay", "psikoloji", "iletişim", "yabancı", "bilinç"]
            },
            {
                "title": "Fahrenheit 451",
                "author": "Ray Bradbury",
                "genre": "bilimkurgu",
                "description": "Kitapların yasaklandığı ve yakıldığı distopik bir gelecekte geçen roman.",
                "keywords": ["distopya", "kitaplar", "sansür", "toplum", "özgürlük"]
            },
            {
                "title": "Yüksek Şato",
                "author": "Philip K. Dick",
                "genre": "bilimkurgu",
                "description": "Alternatif bir tarihte Nazi Almanyası ve Japonya'nın kazandığı bir dünyayı anlatan roman.",
                "keywords": ["alternatif tarih", "savaş", "distopya", "politika", "gerçeklik"]
            },
            {
                "title": "Silmarillion",
                "author": "J.R.R. Tolkien",
                "genre": "fantastik",
                "description": "Orta Dünya'nın yaratılışını ve ilk çağlarını anlatan mitolojik fantastik destan.",
                "keywords": ["mitoloji", "elf", "savaş", "yaratılış", "kahramanlık"]
            },
            {
                "title": "Rüzgarın Adı",
                "author": "Patrick Rothfuss",
                "genre": "fantastik",
                "description": "Efsanevi bir büyücünün gençlik yıllarını ve maceralarını anlatan epik fantastik roman.",
                "keywords": ["büyü", "müzik", "akademi", "macera", "efsane"]
            },
            {
                "title": "Kara Kule",
                "author": "Stephen King",
                "genre": "fantastik",
                "description": "Son silahşor Roland'ın Kara Kule'ye olan destansı yolculuğunu anlatan seri.",
                "keywords": ["silahşor", "yolculuk", "paralel dünyalar", "kader", "macera"]
            },
            {
                "title": "Yerdeniz Büyücüsü",
                "author": "Ursula K. Le Guin",
                "genre": "fantastik",
                "description": "Genç bir büyücünün güç ve bilgelik arayışını anlatan felsefi fantastik roman.",
                "keywords": ["büyü", "ejderha", "bilgelik", "denge", "güç"]
            },
            {
                "title": "Amber Kronikleri",
                "author": "Roger Zelazny",
                "genre": "fantastik",
                "description": "Paralel dünyalar arasında geçen, bir prensin taht mücadelesini anlatan fantastik seri.",
                "keywords": ["paralel dünyalar", "savaş", "entrika", "büyü", "aile"]
            },
            {
                "title": "Ulysses",
                "author": "James Joyce",
                "genre": "klasik",
                "description": "Dublin'de bir günde geçen, modern edebiyatın başyapıtlarından deneysel roman.",
                "keywords": ["modernizm", "bilinç akışı", "İrlanda", "mitoloji", "gündelik yaşam"]
            },
            {
                "title": "Savaş ve Barış",
                "author": "Lev Tolstoy",
                "genre": "klasik",
                "description": "Napolyon Savaşları döneminde Rus toplumunu ve aristokrasisini anlatan epik roman.",
                "keywords": ["savaş", "aşk", "Rusya", "tarih", "toplum"]
            },
            {
                "title": "Moby Dick",
                "author": "Herman Melville",
                "genre": "klasik",
                "description": "Kaptan Ahab'ın beyaz balinaya karşı takıntılı mücadelesini anlatan deniz destanı.",
                "keywords": ["deniz", "balina", "takıntı", "macera", "intikam"]
            },
            {
                "title": "Büyük Umutlar",
                "author": "Charles Dickens",
                "genre": "klasik",
                "description": "Yoksul bir çocuğun centilmen olma yolculuğunu anlatan Viktorya dönemi klasiği.",
                "keywords": ["sınıf atlama", "aşk", "İngiltere", "büyüme", "toplum"]
            },
            {
                "title": "Uğultulu Tepeler",
                "author": "Emily Brontë",
                "genre": "klasik",
                "description": "Tutkulu bir aşk ve intikam hikayesini anlatan karanlık romantik klasik.",
                "keywords": ["aşk", "intikam", "İngiltere", "hayalet", "trajedi"]
            },
            {
                "title": "Ses ve Öfke",
                "author": "William Faulkner",
                "genre": "modern",
                "description": "Güney Amerika'da bir ailenin çöküşünü anlatan deneysel modern roman.",
                "keywords": ["aile", "çöküş", "güney", "modernizm", "zaman"]
            },
            {
                "title": "Dönüşüm",
                "author": "Virginia Woolf",
                "genre": "modern",
                "description": "Bir kadının bir günlük yaşamını iç monologlarla anlatan feminist modern klasik.",
                "keywords": ["feminizm", "bilinç akışı", "kadın", "modernizm", "toplum"]
            },
            {
                "title": "Kör Baykuş",
                "author": "Sadegh Hedayat",
                "genre": "modern",
                "description": "İran edebiyatının başyapıtı, gerçekle rüyayı harmanlayan modern roman.",
                "keywords": ["halüsinasyon", "yalnızlık", "ölüm", "İran", "modernizm"]
            },
            {
                "title": "Petersburg",
                "author": "Andrei Bely",
                "genre": "modern",
                "description": "Rus modernizminin başyapıtı, devrim öncesi Petersburg'u anlatan deneysel roman.",
                "keywords": ["devrim", "Rusya", "sembolizm", "modernizm", "kent"]
            },
            {
                "title": "Berlin Alexanderplatz",
                "author": "Alfred Döblin",
                "genre": "modern",
                "description": "1920'lerin Berlin'inde bir adamın yaşamını anlatan modern şehir romanı.",
                "keywords": ["Berlin", "modernizm", "kent", "suç", "toplum"]
            },
            {
                "title": "Nausea",
                "author": "Jean-Paul Sartre",
                "genre": "psikolojik",
                "description": "Varoluşçu felsefenin temel eserlerinden, bir adamın varoluşsal bunalımını anlatan roman.",
                "keywords": ["varoluşçuluk", "bunalım", "felsefe", "yalnızlık", "anlam"]
            },
            {
                "title": "Görünmez Adam",
                "author": "Ralph Ellison",
                "genre": "psikolojik",
                "description": "Bir siyah adamın toplumsal görünmezliğini anlatan psikolojik roman.",
                "keywords": ["ırkçılık", "kimlik", "yabancılaşma", "toplum", "Amerika"]
            },
            {
                "title": "Malina",
                "author": "Ingeborg Bachmann",
                "genre": "psikolojik",
                "description": "Bir kadının iç dünyasını ve parçalanmış benliğini anlatan psikolojik roman.",
                "keywords": ["kadın", "kimlik", "travma", "aşk", "yalnızlık"]
            },
            {
                "title": "Aşk-ı Memnu",
                "author": "Halid Ziya Uşaklıgil",
                "genre": "psikolojik",
                "description": "Yasak aşkın psikolojik etkilerini anlatan Türk edebiyatının klasiği.",
                "keywords": ["aşk", "yasak", "evlilik", "toplum", "İstanbul"]
            },
            {
                "title": "Stiller",
                "author": "Max Frisch",
                "genre": "psikolojik",
                "description": "Kimlik ve benlik arayışını anlatan varoluşçu psikolojik roman.",
                "keywords": ["kimlik", "benlik", "varoluş", "yabancılaşma", "İsviçre"]
            },
            {
                "title": "Kızıl Veba",
                "author": "Jack London",
                "genre": "dram",
                "description": "Bir salgın sonrası dünyada hayatta kalan son insanların dramını anlatan roman.",
                "keywords": ["salgın", "hayatta kalma", "toplum", "medeniyet", "yıkım"]
            },
            {
                "title": "Acı Kahve",
                "author": "Necati Cumalı",
                "genre": "dram",
                "description": "Ege'de bir kasabada yaşanan imkansız bir aşkı ve toplumsal baskıyı anlatan roman.",
                "keywords": ["aşk", "toplum", "kasaba", "baskı", "gelenek"]
            },
            {
                "title": "Guguk Kuşu",
                "author": "Ken Kesey",
                "genre": "dram",
                "description": "Bir akıl hastanesinde geçen, özgürlük ve otoriteyi sorgulayan etkileyici roman.",
                "keywords": ["özgürlük", "hastane", "sistem", "başkaldırı", "kontrol"]
            },
            {
                "title": "Piyanist",
                "author": "Wladyslaw Szpilman",
                "genre": "dram",
                "description": "II. Dünya Savaşı'nda Varşova'da hayatta kalmaya çalışan bir müzisyenin gerçek hikayesi.",
                "keywords": ["savaş", "müzik", "hayatta kalma", "yahudi", "direniş"]
            },
            {
                "title": "Çocukluğun Soğuk Geceleri",
                "author": "Tezer Özlü",
                "genre": "dram",
                "description": "Bir genç kızın büyüme sancılarını ve toplumla çatışmasını anlatan otobiyografik roman.",
                "keywords": ["büyüme", "yalnızlık", "toplum", "kadın", "bunalım"]
            },
            {
                "title": "Aşk ve Gurur",
                "author": "Jane Austen",
                "genre": "romantik",
                "description": "19. yüzyıl İngiltere'sinde sınıf farkları ve önyargıları aşan bir aşk hikayesi.",
                "keywords": ["aşk", "sınıf", "evlilik", "toplum", "İngiltere"]
            },
            {
                "title": "Manon Lescaut",
                "author": "Abbé Prévost",
                "genre": "romantik",
                "description": "Tutkulu bir aşkın yıkıcı etkilerini anlatan klasik Fransız romanı.",
                "keywords": ["tutku", "aşk", "yıkım", "ahlak", "toplum"]
            },
            {
                "title": "Çalınmış Aşk",
                "author": "Gabriel García Márquez",
                "genre": "romantik",
                "description": "Yarım asır süren imkansız bir aşkı anlatan büyülü gerçekçi roman.",
                "keywords": ["aşk", "zaman", "bekleyiş", "sadakat", "tutku"]
            },
            {
                "title": "Genç Werther'in Acıları",
                "author": "Goethe",
                "genre": "romantik",
                "description": "Platonik bir aşkın genç bir adamı sürüklediği trajediyi anlatan romantik klasik.",
                "keywords": ["aşk", "acı", "mektup", "intihar", "romantizm"]
            },
            {
                "title": "Aşk-ı Memnû",
                "author": "Halid Ziya Uşaklıgil",
                "genre": "romantik",
                "description": "Osmanlı döneminde yasak bir aşkı ve toplumsal normları anlatan klasik.",
                "keywords": ["aşk", "yasak", "toplum", "İstanbul", "trajedi"]
            },
            {
                "title": "Böyle Buyurdu Zerdüşt",
                "author": "Friedrich Nietzsche",
                "genre": "felsefi",
                "description": "Üstinsan kavramını ve nihilizmi alegorik bir anlatımla sunan felsefi roman.",
                "keywords": ["felsefe", "üstinsan", "nihilizm", "değerler", "ahlak"]
            },
            {
                "title": "Siddharta",
                "author": "Hermann Hesse",
                "genre": "felsefi",
                "description": "Bir adamın aydınlanma ve kendini bulma yolculuğunu anlatan felsefi roman.",
                "keywords": ["budizm", "arayış", "aydınlanma", "spiritualizm", "doğu"]
            },
            {
                "title": "Zen ve Motosiklet Bakım Sanatı",
                "author": "Robert M. Pirsig",
                "genre": "felsefi",
                "description": "Baba-oğul yolculuğu üzerinden kalite ve değer kavramlarını sorgulayan roman.",
                "keywords": ["zen", "felsefe", "yolculuk", "teknoloji", "değer"]
            },
            {
                "title": "Sofie'nin Dünyası",
                "author": "Jostein Gaarder",
                "genre": "felsefi",
                "description": "Felsefe tarihini bir genç kızın gözünden anlatan eğitici roman.",
                "keywords": ["felsefe", "eğitim", "tarih", "düşünce", "gerçeklik"]
            },
            {
                "title": "İnsanlık Durumu",
                "author": "André Malraux",
                "genre": "felsefi",
                "description": "Çin Devrimi sırasında insanın varoluşsal mücadelesini anlatan roman.",
                "keywords": ["devrim", "varoluş", "politika", "mücadele", "ideoloji"]
            },
            {
                "title": "Define Adası",
                "author": "Robert Louis Stevenson",
                "genre": "macera",
                "description": "Genç bir çocuğun korsanlarla dolu tehlikeli hazine avını anlatan klasik macera.",
                "keywords": ["korsan", "hazine", "deniz", "macera", "cesaret"]
            },
            {
                "title": "80 Günde Devr-i Alem",
                "author": "Jules Verne",
                "genre": "macera",
                "description": "Dünyayı 80 günde dolaşma iddiası üzerine çıkılan muhteşem bir yolculuk.",
                "keywords": ["yolculuk", "dünya", "zaman", "macera", "keşif"]
            },
            {
                "title": "Robinson Crusoe",
                "author": "Daniel Defoe",
                "genre": "macera",
                "description": "Issız bir adada hayatta kalma mücadelesi veren bir adamın hikayesi.",
                "keywords": ["ada", "hayatta kalma", "yalnızlık", "macera", "medeniyet"]
            },
            {
                "title": "Altın Pusula",
                "author": "Philip Pullman",
                "genre": "macera",
                "description": "Paralel evrenlerde geçen, din ve bilimi sorgulayan epik macera.",
                "keywords": ["paralel evren", "din", "bilim", "macera", "büyüme"]
            },
            {
                "title": "Kaptan Grant'in Çocukları",
                "author": "Jules Verne",
                "genre": "macera",
                "description": "Kayıp bir kaptanı bulmak için dünyayı dolaşan bir kurtarma ekibinin hikayesi.",
                "keywords": ["arama", "yolculuk", "deniz", "macera", "keşif"]
            },
            {
                "title": "Parlayan",
                "author": "Stephen King",
                "genre": "gerilim",
                "description": "İzole bir otelde doğaüstü olaylarla karşılaşan bir ailenin psikolojik gerilimi.",
                "keywords": ["korku", "doğaüstü", "psikoloji", "izolasyon", "aile"]
            },
            {
                "title": "Kuzuların Sessizliği",
                "author": "Thomas Harris",
                "genre": "gerilim",
                "description": "FBI ajanı Clarice Starling'in seri katil Buffalo Bill'i yakalama mücadelesi.",
                "keywords": ["seri katil", "fbi", "psikoloji", "suç", "gerilim"]
            },
            {
                "title": "Gece Yarısı Kütüphanesi",
                "author": "Matt Haig",
                "genre": "gerilim",
                "description": "Yaşam ve ölüm arasında sıkışan bir kadının alternatif yaşamlarını keşfi.",
                "keywords": ["yaşam", "seçim", "pişmanlık", "kütüphane", "varoluş"]
            },
            {
                "title": "Köstebek",
                "author": "John le Carré",
                "genre": "gerilim",
                "description": "Soğuk Savaş döneminde İngiliz istihbaratındaki bir köstebeği arama operasyonu.",
                "keywords": ["casusluk", "soğuk savaş", "ihanet", "istihbarat", "sır"]
            },
            {
                "title": "Ruh Koleksiyoncusu",
                "author": "Sebastian Fitzek",
                "genre": "gerilim",
                "description": "Kaçırılan çocukları kurtarmaya çalışan bir psikiyatrın karanlık macerası.",
                "keywords": ["psikoloji", "kaçırılma", "gerilim", "suç", "gizem"]
            }
        ]
    }
    
    # JSON dosyasına kaydet
    with open('books_database.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)
    
    print(f"Toplam {len(books['books'])} kitap kaydedildi.")

if __name__ == "__main__":
    create_turkish_books_database() 