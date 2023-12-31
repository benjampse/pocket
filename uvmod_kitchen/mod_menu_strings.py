# choose the replacement strings for all of the menu options
# each entry follows the pattern of {address, name, size, string}, where string is what you want to edit and size is the maximum characters allowed

strings = [
    # menu strings
    (0xDC96+7*0 , 'Parler'                          , 6, 'SQL'   ),
    (0xDC96+7*1 , 'Marche'                          , 6, 'STEP'  ),
    (0xDC96+7*2 , 'Transmission'                    , 6, 'TXP'   ),
    (0xDC96+7*3 , 'r dcs'                           , 6, 'R_DCS' ),
    (0xDC96+7*4 , 'r ctcs'                          , 6, 'R_CTCS'),
    (0xDC96+7*5 , 't dcs'                           , 6, 'T_DCS' ),
    (0xDC96+7*6 , 't ctcs'                          , 6, 'T_CTCS'),
    (0xDC96+7*7 , 'Emetteur de direction '          , 6, 'SFT-D' ),
    (0xDC96+7*8 , 'Emetteur de decalage'            , 6, 'OFFSET'),
    (0xDC96+7*9 , 'Large/Etroit'                    , 6, 'W/N'   ),
    (0xDC96+7*10, 'interference'                    , 6, 'SCR'   ),
    (0xDC96+7*11, 'Verrouillage PTT du canal'       , 6, 'BCL'   ),
    (0xDC96+7*12, 'Enregistrer le canal'            , 6, 'MEM-CH'),
    (0xDC96+7*13, 'Economiseur de batterie'         , 6, 'SAVE'  ),
    (0xDC96+7*14, 'Mode active par la voix'         , 6, 'VOX'   ),
    (0xDC96+7*15, 'Délai d’attente retroéclairage'  , 6, 'ABR'   ),
    (0xDC96+7*16, 'Montre double'                   , 6, 'TDR'   ),
    (0xDC96+7*17, 'Mode bande croisée'              , 6, 'WX'    ),
    (0xDC96+7*18, 'Montre double'                   , 6, 'BEEP'  ),
    (0xDC96+7*19, 'Temps d’arret emetteur'          , 6, 'TOT'   ),
    (0xDC96+7*20, 'Invite vocale'                   , 6, 'VOICE' ),
    (0xDC96+7*21, 'Mode de balayage'                , 6, 'SC-REV'),
    (0xDC96+7*22, 'Mode d’affichage des canaux'     , 6, 'MDF'   ),
    (0xDC96+7*23, 'Verrouillage automatique clavier', 6, 'AUTOLK'),
    (0xDC96+7*24, 'ch dans la liste d’analyse 1'    , 6, 'S-ADD1'),
    (0xDC96+7*25, 'ch dans la liste d’analyse 2'    , 6, 'S-ADD2'),
    (0xDC96+7*26, 'Elimination du son'              , 6, 'STE'   ),
    (0xDC96+7*27, 'Élimination tonalité repeteur'   , 6, 'RP-STE'),
    (0xDC96+7*28, 'Sensibilité du micro'            , 6, 'MIC'   ),
    (0xDC96+7*29, 'Un canal d’appel clé'            , 6, '1-CALL'),
    (0xDC96+7*30, 'Liste d’analyse active'          , 6, 'S-LIST'),
    (0xDC96+7*31, 'Parcourir liste analyses 1'      , 6, 'SLIST1'),
    (0xDC96+7*32, 'Parcourir liste analyses 2'      , 6, 'SLIST2'),
    (0xDC96+7*33, 'Mode d’alarme'                   , 6, 'AL-MOD'),
    (0xDC96+7*34, 'ID radio DTMF'                   , 6, 'ANI-ID'),
    (0xDC96+7*35, 'dtmf upcode'                     , 6, 'UPCODE'),
    (0xDC96+7*36, 'Codage ascendant DTMF'           , 6, 'DWCODE'),
    (0xDC96+7*37, 'DTMF à l’aide du clavier en PTT' , 6, 'D-ST'  ),
    (0xDC96+7*38, 'Mode de réponse DTMF'            , 6, 'D-RSP' ),
    (0xDC96+7*39, 'Temps de maintien DTMF'          , 6, 'D-HOLD'),
    (0xDC96+7*40, 'Temps de préchargement DTMF'     , 6, 'D-PRE' ),
    (0xDC96+7*41, 'Identification automatique NM'   , 6, 'PTT-ID'),
    (0xDC96+7*42, 'DTMF nécoute que les contacts'   , 6, 'D-DCD' ),
    (0xDC96+7*43, 'DTMF Liste/Appel Contacts'       , 6, 'D-LIST'),
    (0xDC96+7*44, 'Allumer l’écran'                 , 6, 'PONMSG'),
    (0xDC96+7*45, 'Tonalité de fin de discours'     , 6, 'ROGER' ),
    (0xDC96+7*46, 'Tension de la batterie'          , 6, 'VOL'   ),
    (0xDC96+7*47, 'Activer réception AM/bandes AM'  , 6, 'AM'    ),
    (0xDC96+7*48, 'Activer l’analyse NOAA'          , 6, 'NOAA_S'),
    (0xDC96+7*49, 'Supprimer le canal'              , 6, 'DEL-CH'),
    (0xDC96+7*50, 'Réinitialiser la radio'          , 6, 'RESET' ),
    (0xDC96+7*51, 'Activer émission bande 350 MHz'  , 6, '350TX' ), # the menu entries below are only visible when powering the radio up while holding PTT and side key 1 
    (0xDC96+7*52, 'Limite aux fréquences locales'   , 6, 'F-LOCK'),
    (0xDC96+7*53, 'Activer émission bande 200 MHz'  , 6, '200TX' ),
    (0xDC96+7*54, 'Activer émission bande 500 MHz'  , 6, '500TX' ),
    (0xDC96+7*55, 'Activer la bande 350 MHz'        , 6, '350EN' ),
    (0xDC96+7*56, 'Activer l’option Scrambler'      , 6, 'SCREN' ),

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
