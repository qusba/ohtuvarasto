import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_konstruktori_korjaa_negatiivisen_tilavuuden_nollaan(self):
        varasto = Varasto(-7)
        self.assertAlmostEqual(varasto.tilavuus,0)
    
    def test_konstruktori_korjaa_alku_saldon_oikein(self):
        varasto1 = Varasto(10,-7)
        varasto2 = Varasto(10,20)
        self.assertAlmostEqual(varasto1.saldo,0)
        self.assertAlmostEqual(varasto2.saldo,10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
    
    def test_negatiivinen_lisays_ei_tee_mitään(self):
        self.varasto.lisaa_varastoon(-3)
        #negatiivisen lisäyksen jälkeen määrän ei pitäisi muuttua
        self.assertAlmostEqual(self.varasto.saldo,0)

    def test_ylimalkainen_lisays_ei_lisaa_yli_kapasiteetin(self):
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.saldo,10)


    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_ottaminen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(self.varasto.saldo,8)

    def test_ylimalkainen_otto_antaa_vain_saldon_verran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara,8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_luokka_tulostuu_oikein(self):
        tuloste = str(self.varasto)

        self.assertEqual(tuloste,"saldo = 0, vielä tilaa 10")
