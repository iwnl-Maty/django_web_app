from django.db import models


class Hrac(models.Model):
    jmeno = models.CharField(
        max_length=80,
        verbose_name='Jméno hráče',
        help_text='Zadejte jméno hráče',
        error_messages={'blank': 'Jméno hráče musí být vyplněno'}
    )
    prijmeni = models.CharField(
        max_length=50,
        verbose_name='Příjmení hráče',
        help_text='Zadejte příjmení hráče',
        error_messages={'blank': 'Příjmení hráče musí být vyplněno'}
    )
    goly = models.IntegerField(
        verbose_name='Počet golů',
        help_text='Zadejte počet golů',
        error_messages={'blank': 'Počet golů musí být vyplněný'}
    )
    asistence = models.IntegerField(
        verbose_name='Počet asistencí',
        help_text='Zadejte počet asistencí',
        error_messages={'blank': 'Počet asistencí musí být vyplněný'}
    )
    pocet_zapasu = models.IntegerField(
        verbose_name='Počet zápasů',
        help_text='Zadejte počet zápasů',
        error_messages={'blank': 'Počet zápasů musí být vyplněný'}
    )

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Hráč'
        verbose_name_plural = 'Hráči'

    def __str__(self):
        return f'{self.prijmeni} {self.jmeno} {self.goly} {self.asistence} {self.pocet_zapasu}'


class Tym(models.Model):
    nazev_tymu = models.CharField(
        max_length=80,
        verbose_name='Název týmu',
        help_text='Zadejte název týmu',
        error_messages={'blank': 'Název týmu musí být vyplněno'}
    )
    goly = models.IntegerField(
        verbose_name='Počet golů',
        help_text='Zadejte počet golů',
        error_messages={'blank': 'Počet golů musí být vyplněný'}
    )
    vyhry = models.IntegerField(
        verbose_name='Počet výher',
        help_text='Zadejte počet výher',
        error_messages={'blank': 'Počet výher musí být vyplněný'}
    )
    prohry = models.IntegerField(
        verbose_name='Počet proher',
        help_text='Zadejte počet proher',
        error_messages={'blank': 'Počet proher musí být vyplněný'}
    )
    remizy = models.IntegerField(
        verbose_name='Počet remízy',
        help_text='Zadejte počet remízy',
        error_messages={'blank': 'Počet remíz musí být vyplněný'}
    )

    class Meta:
        ordering = ['nazev_tymu', 'goly', 'vyhry', 'prohry', 'remizy']
        verbose_name = 'Tým'
        verbose_name_plural = 'Týmy'

    def __str__(self):
        return f'{self.nazev_tymu} {self.vyhry} {self.prohry} {self.remizy}'


class Liga(models.Model):
    nazev_liga = models.CharField(
        max_length=80,
        verbose_name='Název ligy',
        help_text='Zadejte název ligy',
        error_messages={'blank': 'Název ligy musí být vyplněno'}
    )

    class Meta:
        ordering = ['nazev_liga']
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligy'

    def __str__(self):
        return f'{self.nazev_liga}'


class Zapas(models.Model):
    datum_zapasu = models.DateField(
        verbose_name='Datum zápasu',
        help_text='Zadejte datum zápasu',
        error_messages={'blank': 'Datum zápasu musí být vyplněný'}
    )
    domaci_tym = models.CharField(
        max_length=80,
        verbose_name='Název týmu',
        help_text='Zadejte název týmu',
        error_messages={'blank': 'Název týmu musí být vyplněný'}
    )
    hostujici_tym = models.CharField(
        max_length=80,
        verbose_name='Název týmu',
        help_text='Zadejte název týmu',
        error_messages={'blank': 'Název týmu musí být vyplněný'}
    )
    skore_domaci_tym = models.IntegerField(
        verbose_name='Počet golů domácích',
        help_text='Zadejte počet golů domácích',
        error_messages={'blank': 'Počet golů domácích musí být vyplněný'}
    )
    skore_hostujici_tym = models.IntegerField(
        verbose_name='Počet golů hostů',
        help_text='Zadejte počet golů hostů',
        error_messages={'blank': 'Počet golů hostů musí být vyplněný'}
    )

    class Meta:
        ordering = ['domaci_tym', 'hostujici_tym']
        verbose_name = 'Zápas'
        verbose_name_plural = 'Zápasy'

    def __str__(self):
        return (f'{self.datum_zapasu} {self.domaci_tym} {self.hostujici_tym}'
                f'{self.skore_domaci_tym} {self.skore_hostujici_tym}')
