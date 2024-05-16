# Techolay Forum Scraping Kodu

Bu Python kodu, Techolay forumundaki programlama bölümünden konu başlıklarını, yazarları, mesaj sayılarını ve görüntülenme sayılarını çeker.

## Kod Açıklaması

Bu kod, Techolay forumunun programlama bölümündeki altı sayfadan (1'den 6'ya kadar) veri çeker. Her sayfayı sırayla tarar ve her bir konunun başlığını, yazarını, mesaj sayısını ve görüntülenme sayısını alır. Bu veriler bir sözlük içinde toplanır ve bir liste olan `data_list` içine eklenir.

## Kullanılan Kütüphaneler

- `requests`: Web sayfalarını çekmek için kullanılır.
- `BeautifulSoup`: HTML içeriğini ayrıştırmak ve işlemek için kullanılır.

## Örnek Kullanım

```python
techolay()
```

## Notlar

- Kod, Techolay forumundaki programlama bölümünden konu başlıklarını, yazarları, mesaj sayılarını ve görüntülenme sayılarını çeker.
- Veriler bir liste içinde toplanır ve işlenir.

## Lisans

Bu kod [MIT lisansı](https://opensource.org/licenses/MIT) altında sunulmuştur.
