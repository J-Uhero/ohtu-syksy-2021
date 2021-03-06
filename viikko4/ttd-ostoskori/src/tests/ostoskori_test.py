import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuote1 = Tuote("ES", 2)
        self.tuote2 = Tuote("kalja", 3)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_korin_hinta_sama_kuin_yhden_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.assertEqual(self.kori.hinta(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote2)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_hinta_on_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote2)
        self.assertEqual(self.kori.hinta(), 5)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_hinta_on_tuotteen_hinta_tuplana(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote1)
        self.assertEqual(self.kori.hinta(), 4)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tuote(self):
        self.kori.lisaa_tuote(self.tuote1)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_tuote_samanniminen_ja_lkm_yksi(self):
        self.kori.lisaa_tuote(self.tuote1)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "ES")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kaksi_eri_tuotetta_lisattya_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote2)
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kaksi_samaa_tuotetta_lisattya_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote1)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kaksi_samaa_tuotetta_lisattya_korin_ostoksen_lkm_kaksi(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote1)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "ES")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_toinen_korin_kahdesta_samasta_tuotteesta_poistetaan_niin_lkm_yksi(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.poista_tuote(self.tuote1)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kun_korin_yksi_tuote_poistetaan_niin_kori_tyhja(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.poista_tuote(self.tuote1)
        self.assertEqual(len(self.kori.ostokset()), 0)
    
    def test_tyhjenna_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote2)
        self.kori.tyhjenna()
        self.assertEqual(len(self.kori.ostokset()), 0)
