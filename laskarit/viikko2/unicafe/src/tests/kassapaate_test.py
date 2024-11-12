import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    #konstruktori
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_konstruktori_asettaa_myydyt_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_konstruktori_asettaa_myydyt_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    #edulliset kateisella
    def test_syo_edullisesti_kateisella_kasvattaa_saldoa_lounaan_hinnalla(self):
        self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
    
    def test_syo_edullisesti_kateisella_palauttaa_vaihtorahan(self):
        vastaus = self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(vastaus, 10)
    
    def test_syo_edullisesti_kateisella_kasvattaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kateisella_riittamaton_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_syo_edullisesti_kateisella_riittamaton_palauttaa_kaikki(self):
        vastaus = self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(vastaus, 230)

    def test_syo_edullisesti_kateisella_riittamaton_myydyt_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.edulliset, 0)
    
    #maukkaat kateisella
    def test_syo_maukkaasti_kateisella_kasvattaa_saldoa_lounaan_hinnalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
    
    def test_syo_maukkaasti_kateisella_palauttaa_vaihtorahan(self):
        vastaus = self.kassapaate.syo_maukkaasti_kateisella(410)

        self.assertEqual(vastaus, 10)
    
    def test_syo_maukkaasti_kateisella_kasvattaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kateisella_riittamaton_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_syo_maukkaasti_kateisella_riittamaton_palauttaa_kaikki(self):
        vastaus = self.kassapaate.syo_maukkaasti_kateisella(390)

        self.assertEqual(vastaus, 390)

    def test_syo_maukkaasti_kateisella_riittamaton_myydyt_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)

        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    #edulliset kortilla
    def test_syo_edullisesti_kortilla_veloittaa_kun_saldo_riittaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        
        self.assertEqual(self.kortti.saldo_euroina(), 7.6)
    
    def test_syo_edullisesti_kortilla_true_kun_saldo_riittaa(self):
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(vastaus, True)
    
    def test_syo_edullisesti_kortilla_kasvattaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kortilla_ei_veloita_kun_saldo_ei_riita(self):
        kortti = Maksukortti(230)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 2.3)

    def test_syo_edullisesti_kortilla_false_kun_saldo_ei_riita(self):
        kortti = Maksukortti(230)
        vastaus = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(vastaus, False)
    
    def test_syo_edullisesti_kortilla_ei_kasvata_myytyja_kun_saldo_ei_riita(self):
        kortti = Maksukortti(230)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.edulliset, 0)
    
    #maukkaat kortilla
    def test_syo_maukkaasti_kortilla_veloittaa_kun_saldo_riittaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        
        self.assertEqual(self.kortti.saldo_euroina(), 6.0)
    
    def test_syo_maukkaasti_kortilla_true_kun_saldo_riittaa(self):
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(vastaus, True)
    
    def test_syo_maukkaasti_kortilla_kasvattaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kortilla_ei_veloita_kun_saldo_ei_riita(self):
        kortti = Maksukortti(390)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 3.9)

    def test_syo_maukkaasti_kortilla_false_kun_saldo_ei_riita(self):
        kortti = Maksukortti(390)
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(vastaus, False)
    
    def test_syo_maukkaasti_kortilla_ei_kasvata_myytyja_kun_saldo_ei_riita(self):
        kortti = Maksukortti(390)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)
    