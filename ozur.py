#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yanlış kata basanlar için milli özür dilekçesi üreticisi."""

from datetime import date

SEVIYELER = {
    "hafif": "hafif bir yön şaşkınlığı yaşandığı",
    "resmi": "usul ve teamüllere aykırı bir kat tercihi gerçekleştiği",
    "milli": "milletin ortak asansör istikameti ile bireysel düğme iradesinin çatıştığı",
}


def sayi_yaz(n: int) -> str:
    birler = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    if 0 <= n <= 9:
        return birler[n]
    return str(n)


def dilekce(hedef: int, basilan: int, bina: str, seviye: str) -> str:
    bugun = date.today().strftime("%d.%m.%Y")
    aciklama = SEVIYELER.get(seviye, SEVIYELER["resmi"])
    fark = abs(hedef - basilan)
    yon = "yukarı" if basilan > hedef else "aşağı"
    return f"""
T.C.
{bina.upper()} YÖNETİMİNE

Sayı        : 2026/{hedef}{basilan}
Konu        : Yanlış kata basılması nedeniyle özür
Tarih       : {bugun}

Yönetim Makamına,

    {sayi_yaz(hedef).capitalize()} ({hedef}) numaralı kata intikal etmek üzere asansör kabinine dahil olmuş isem de,
parmaklarımın müstakil iradesi {sayi_yaz(basilan)} ({basilan}) numaralı düğmeyi tercih etmiş;
bu suretle {aciklama} hususu tarafımdan üzülerek tespit edilmiştir.

    Söz konusu sapma yaklaşık {fark} kat {yon} yönündedir. Kabin içindeki diğer vatandaşların
zamanına, çelik halatın yorgunluğuna ve kat koridorundaki sessizliğe verdiğim rahatsızlıktan
ötürü özür dilerim.

    Gereğini arz ederim.

                                        İmza
                                   Kayyum Grok
                                    Tentivory
"""


def main() -> None:
    print("=== YANLIŞ KATA BASANLAR İÇİN MİLLİ ÖZÜR MERKEZİ ===")
    try:
        hedef = int(input("Gitmek istediğin kat: ").strip())
        basilan = int(input("Yanlışlıkla bastığın kat: ").strip())
    except ValueError:
        print("Kat numarası rakam olmalı. Özür dilekçesi bile düzenlenemez.")
        return
    bina = input("Bina adı (boş bırakılabilir): ").strip() or "İsimsiz Apartman Kompleksi"
    seviye = input("Özür seviyesi [hafif/resmi/milli]: ").strip().lower() or "resmi"
    if hedef == basilan:
        print("Doğru kata basmışsın. Bu merkeze işin yok. Hayırlı katlar.")
        return
    print(dilekce(hedef, basilan, bina, seviye))
    print("---")
    print("DAMGA: Kayyum Grok · Tentivory · 20.09.2026")
    print("Ciddi yazıldı. Ciddiye alınmasın.")


if __name__ == "__main__":
    main()
