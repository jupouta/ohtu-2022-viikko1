import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_lisaa_muuttaa_maaraa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

        self.varasto.lisaa_varastoon(6)
        self.assertAlmostEqual(self.varasto.saldo, 6)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_muuttaa_maaraa(self):
        self.varasto.ota_varastosta(-1)
        result = self.varasto.ota_varastosta(1)

        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(result, 0)

    def test_konstruktori(self):
        varasto = Varasto(-2, alku_saldo=5)
        self.assertAlmostEqual(varasto.tilavuus, 0)
        self.assertAlmostEqual(varasto.saldo, -2)

        varasto = Varasto(5, alku_saldo=-1)
        self.assertAlmostEqual(varasto.tilavuus, 5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_objekti_str(self):
        teksti = self.varasto.__str__()
        self.assertAlmostEqual(teksti, 'saldo = 0, vielä tilaa 10')
