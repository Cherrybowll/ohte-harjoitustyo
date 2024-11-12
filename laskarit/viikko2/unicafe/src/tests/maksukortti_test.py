import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 11.0)
    
    def test_rahan_ottaminen_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9.0)
    
    def test_rahan_ottaminen_palauttaa_true_jos_saldo_riittaa(self):
        vastaus = self.maksukortti.ota_rahaa(100)

        self.assertEqual(vastaus, True)

    def test_rahan_ottaminen_ei_muuta_saldoa_jos_liian_vahan_rahaa(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_rahan_ottaminen_palauttaa_false_jos_liian_vahan_rahaa(self):
        vastaus = self.maksukortti.ota_rahaa(1100)

        self.assertEqual(vastaus, False)