# choose the replacement strings for all of the menu options
# each entry follows the pattern of {address, name, size, string}, where string is what you want to edit and size is the maximum characters allowed

strings = [
    # menu strings
    (0xDC96+7*0 , 'Parler'                          , 2, 'Niveau Squelch'),
    (0xDC96+7*1 , 'Marche'                          , 2, 'pas de frequance'),
    (0xDC96+7*2 , 'Transmission'                    , 2, 'Puissance d'emission'),
    (0xDC96+7*3 , 'r dcs'                           , 2, 'Recevez DCS'),
    (0xDC96+7*4 , 'r ctcs'                          , 2, 'Recevoir CTCSS.'),
    (0xDC96+7*5 , 't dcs'                           , 2, 'Transmettre DCS'),
    (0xDC96+7*6 , 't ctcs'                          , 2, 'Transmettre CTCSS'),
    (0xDC96+7*7 , 'Emetteur de direction'           , 2, 'Réglage écart' ),
    (0xDC96+7*8 , 'Emetteur de decalage'            , 2, 'Fréquence de déviation'),
    (0xDC96+7*9 , 'Large/Etroit'                    , 2, 'Bande passante du canal'),
    (0xDC96+7*10, 'interference'                    , 2, 'Communication cryptée'   ),
    (0xDC96+7*11, 'Verrouillage PTT du canal'       , 2, 'Verrouillage du canal'   ),
    (0xDC96+7*12, 'Enregistrer le canal'            , 2, 'Sauvegarde de chaîne'),
    (0xDC96+7*13, 'Economiseur de batterie'         , 2, 'Économie de batterie'  ),
    (0xDC96+7*14, 'Mode active par la voix'         , 2, 'Réglage VOX'   ),
    (0xDC96+7*15, 'Délai d’attente retroéclairage'  , 2, 'Rétroéclairage automatique'  ),
    (0xDC96+7*16, 'Montre double'                   , 2, 'Double veille marche/arrêt'  ),
    (0xDC96+7*17, 'Mode bande croisée'              , 2, 'Réception/transmission cross-bande '    ),
    (0xDC96+7*18, 'Montre double'                   , 2, 'Contrôle BIP'  ),
    (0xDC96+7*19, 'Temps d’arret emetteur'          , 2, 'Time-Out-Timer '   ),
    (0xDC96+7*20, 'Invite vocale'                   , 2, 'Invite vocale' ),
    (0xDC96+7*21, 'Mode de balayage'                , 2, 'Mode de reprise du scan '),
    (0xDC96+7*22, 'Mode d’affichage des canaux'     , 2, 'Mode d’affichage du canal'   ),
    (0xDC96+7*23, 'Verrouillage automatique clavier', 2, 'Verrouillage automatique du clavier'),
    (0xDC96+7*24, 'ch dans la liste d’analyse 1'    , 2, 'S’il faut participer à l’analyse de la liste 1'),
    (0xDC96+7*25, 'ch dans la liste d’analyse 2'    , 2, 'S’il faut participer à l’analyse de la liste 2'),
    (0xDC96+7*26, 'Elimination du son'              , 2, 'Élimination du tonalité'   ),
    (0xDC96+7*27, 'Élimination tonalité repeteur'   , 2, 'Élimination de la tonalité du repeteur'),
    (0xDC96+7*28, 'Sensibilité du micro'            , 2, 'Sensibilité du micro'   ),
    (0xDC96+7*29, 'Un canal d’appel clé'            , 2, 'Canal d’appel à une touche'),
    (0xDC96+7*30, 'Liste d’analyse active'          , 2, 'Sélection de la liste de balayage des chaîne'),
    (0xDC96+7*31, 'Parcourir liste analyses 1'      , 2, 'SLIST1'),
    (0xDC96+7*32, 'Parcourir liste analyses 2'      , 2, 'SLIST2'),
    (0xDC96+7*33, 'Mode d’alarme'                   , 2, 'AL-MOD'),
    (0xDC96+7*34, 'ID radio DTMF'                   , 2, 'ANI-ID'),
    (0xDC96+7*35, 'dtmf upcode'                     , 2, 'UPCODE'),
    (0xDC96+7*36, 'Codage ascendant DTMF'           , 2, 'DWCODE'),
    (0xDC96+7*37, 'DTMF à l’aide du clavier en PTT' , 2, 'D-ST'  ),
    (0xDC96+7*38, 'Mode de réponse DTMF'            , 2, 'D-RSP' ),
    (0xDC96+7*39, 'Temps de maintien DTMF'          , 2, 'D-HOLD'),
    (0xDC96+7*40, 'Temps de préchargement DTMF'     , 2, 'D-PRE' ),
    (0xDC96+7*41, 'Identification automatique NM'   , 2, 'PTT-ID'),
    (0xDC96+7*42, 'DTMF nécoute que les contacts'   , 2, 'D-DCD' ),
    (0xDC96+7*43, 'DTMF Liste/Appel Contacts'       , 2, 'D-LIST'),
    (0xDC96+7*44, 'Allumer l’écran'                 , 2, 'PONMSG'),
    (0xDC96+7*45, 'Tonalité de fin de discours'     , 2, 'ROGER' ),
    (0xDC96+7*46, 'Tension de la batterie'          , 2, 'VOL'   ),
    (0xDC96+7*47, 'Activer réception AM/bandes AM'  , 2, 'AM'    ),
    (0xDC96+7*48, 'Activer l’analyse NOAA'          , 2, 'NOAA_S'),
    (0xDC96+7*49, 'Supprimer le canal'              , 2, 'DEL-CH'),
    (0xDC96+7*50, 'Réinitialiser la radio'          , 2, 'RESET' ),
    (0xDC96+7*51, 'Activer émission bande 350 MHz'  , 2, '350TX' ), # the menu entries below are only visible when powering the radio up while holding PTT and side key 1 
    (0xDC96+7*52, 'Limite aux fréquences locales'   , 2, 'F-LOCK'),
    (0xDC96+7*53, 'Activer émission bande 200 MHz'  , 2, '200TX' ),
    (0xDC96+7*54, 'Activer émission bande 500 MHz'  , 2, '500TX' ),
    (0xDC96+7*55, 'Activer la bande 350 MHz'        , 2, '350EN' ),
    (0xDC96+7*56, 'Activer l’option Scrambler'      , 2, 'SCREN' ),
    # option strings
    (0xDE25+4*0 , 'battery saver: off'              , 3, 'OFF'   ),
    (0xDE25+4*1 , 'battery saver: 1:1'              , 3, '1:1'   ),
    (0xDE25+4*2 , 'battery saver: 1:2'              , 3, '1:2'   ),
    (0xDE25+4*3 , 'battery saver: 1:3'              , 3, '1:3'   ),
    (0xDE25+4*4 , 'battery saver: 1:4'              , 3, '1:4'   ),
    (0xDE39+5*0 , 'tx power: low'                   , 4, 'LOW'   ),
    (0xDE39+5*1 , 'tx power: mid'                   , 4, 'MID'   ),
    (0xDE39+5*2 , 'tx power: high'                  , 4, 'HIGH'  ),
    (0xDE48+7*0 , 'bandwidth: wide'                 , 6, 'WIDE'  ),
    (0xDE48+7*1 , 'bandwidth: narrow'               , 6, 'NARROW'),
    (0xDE56+7*0 , 'multiple options 1: off'         , 6, 'OFF'   ),
    (0xDE56+7*1 , 'multiple options 1: chan a'      , 6, 'CHAN_A'),
    (0xDE56+7*2 , 'multiple options 1: chan b'      , 6, 'CHAN_B'),
    (0xDE6B+4*0 , 'multiple options 2: off'         , 3, 'OFF'   ),
    (0xDE6B+4*1 , 'multiple options 2: on'          , 3, 'ON'    ),
    (0xDE73+4*0 , 'voice prompt: off'               , 3, 'OFF'   ),
    (0xDE73+4*1 , 'voice prompt: chinese'           , 3, 'CHI'   ),
    (0xDE73+4*2 , 'voice prompt: english'           , 3, 'ENG'   ),
    (0xDE7F+5*0 , 'dtmf ptt id: off'                , 4, 'OFF'   ),
    (0xDE7F+5*1 , 'dtmf ptt id: upcode on ptt'      , 4, 'BOT'   ),
    (0xDE7F+5*2 , 'dtmf ptt id: downcode after ptt' , 4, 'EOT'   ),
    (0xDE7F+5*3 , 'dtmf ptt id: both'               , 4, 'BOTH'  ),
    (0xDE93+3*0 , 'scan mode: continue after 5s'    , 2, 'TO'    ),
    (0xDE93+3*1 , 'scan mode: stay while signal'    , 2, 'CO'    ),
    (0xDE93+3*2 , 'scan mode: stop on signal'       , 2, 'SE'    ),
    (0xDE9C+5*0 , 'channel display mode: freq'      , 4, 'FREQ'  ),
    (0xDE9C+5*1 , 'channel display mode: chan'      , 4, 'CHAN'  ),
    (0xDE9C+5*2 , 'channel display mode: name'      , 4, 'NAME'  ),
    (0xDEAB+4*0 , 'tx shift direction: off'         , 4, 'OFF'   ),
    (0xDEAB+4*1 , 'tx shift direction: +'           , 4, '+'     ),
    (0xDEAB+4*2 , 'tx shift direction: -'           , 4, '-'     ),
    (0xDEB7+5*0 , 'alarm mode: local'               , 4, 'SITE'  ),
    (0xDEB7+5*1 , 'alarm mode: local + remote'      , 4, 'TONE'  ),
    (0xDEC1+5*0 , 'power on screen: full'           , 4, 'FULL'  ),
    (0xDEC1+5*1 , 'power on screen: custom message' , 4, 'MSG'   ),
    (0xDEC1+5*2 , 'power on screen: batt voltage'   , 4, 'VOL'   ),
    (0xDED0+4*0 , 'reset: keep channel parameters'  , 3, 'VFO'   ),
    (0xDED0+4*1 , 'reset: reset everything'         , 3, 'ALL'   ),
    (0xDED8+6*0 , 'dtmf response: nothing'          , 5, 'NULL'  ),
    (0xDED8+6*1 , 'dtmf response: local ring'       , 5, 'RING'  ),
    (0xDED8+6*2 , 'dtmf response: auto call back'   , 5, 'REPLY' ),
    (0xDED8+6*3 , 'dtmf response: ring and call'    , 5, 'BOTH'  ),
    (0xDEF0+6*0 , 'end of talk tone: off'           , 5, 'OFF'   ),
    (0xDEF0+6*1 , 'end of talk tone: classic beep'  , 5, 'ROGER' ),
    (0xDEF0+6*2 , 'end of talk tone: MDC ID sound'  , 5, 'MDC'   ),
    (0xDF02+4*0 , 'f lock: none'                    , 3, 'OFF'   ),
    (0xDF02+4*1 , 'f lock: region FCC'              , 3, 'FCC'   ),
    (0xDF02+4*2 , 'f lock: region Europe'           , 3, 'CE'    ),
    (0xDF02+4*3 , 'f lock: region GB'               , 3, 'GB'    ),
    (0xDF02+4*4 , 'f lock: 430 band'                , 3, '430'   ),
    (0xDF02+4*5 , 'f lock: 438 band'                , 3, '438'   ),
]


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys

print('Running', os.path.basename(sys.argv[0]), 'mod...')

fw = bytearray(open(sys.argv[1], 'rb').read())

for address, description, size, string in strings:
    if (fw[address:address+size].decode('ascii').rstrip('\x00') != string.rstrip('\x00')): # only patch strings that are different from the original firmware
        
        print('Patching string: ', description)
        print('╰───', fw[address:address+size].decode('ascii'), ' ──▻ ', string)

        if(len(string) > size):
            raise ValueError(f"String '{string}' is longer than allowed size {size}")
        
        fw[address:address+size] = string.ljust(size, '\x00').encode()

open(sys.argv[1], 'wb').write(fw)
