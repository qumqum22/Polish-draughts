""" Main module. """
import board
import design
import punktacja as pkt


def rozgrywka():
    """ Main function """
    board.uklad_poczatkowy()
    board.wyswietl()
    pkt.punkty_start()
    pkt.wyswietl_punktacje()
    design.run_window()


rozgrywka()

#funkcja ocen pozycje - liczy laczną pozycje gracza po ruchu pomocnicza do evaluate


#UWAGI
# pygame.kdasdas do maina wrzucic :!, stałe duzymi napisac
# nie musze robic klas
# rekurencyjne sprawdzanie skoku
# tekst w sposob inny
