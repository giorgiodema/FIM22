import random
random.seed(9)

N = 1000

nomim = """Agostino, Alberto, Alessandro, Alessio, Alfio, Alfonso, Amedeo, Angelo, Antonio, Aurelio,
Baldassarre, Baldo, Bastiano, Bartolo, Bartolomeo, Benito,  Bernardo, Biagio, Boris, Bruno,
Calogero, Carlo, Carmelo,  Casimiro, Cesare, Cirillo, Ciro,  Claudio, Corrado, Cosimo,
Daniele, Danilo, Dante, Dario, Davide, Diego, Dino, Dionisio, Domenico, Duccio,
Egidio, Elio, Eliseo, Emanuele, Emiliano, Emilio, Ennio,  Enrico, Enzo, Ezio,
Fabiano, Fabio, Fabrizio, Fausto, Fedele, Felice, Filippo, Flavio, Fortunato, Francesco,
Gabriele, Gaetano, Gaspare, Gennaro, Gerlando, Giacomo, Giancarlo, Giovanni, Giulio, Giuseppe,
Iacopo, Ignazio, Igor, Isacco, Isaia, Iside, Isidoro, Italo, Ivano, Ivo,
Leandro, Leo, Lino, Livio, Lorenzo, Loris, Luca, Luciano, Lucio, Luigi,
Manuele, Marcello, Marco, Mario, Martino, Massimo, Matteo, Mattia, Michele, Mirco,
Narciso, Natale, Nazario, Nazzareno, Nestore, Nico, Nicola, Nino, Noè, Nunzio,
Oliviero, Omar , Omero, Onofrio, Orazio, Orlando, Oscar,  Osvaldo, Otello, Ottavio,
Paolo, Pasquale, Patrizio, Paride, Pierluigi, Piero, Pietro, Pio, Pippo, Prisco,
Raffaele, Raimondo, Renato, Renzo, Riccardo, Rino, Roberto, Rocco, Romolo, Ruggero,
Salvatore, Salvo, Samuele, Sandro, Saverio, Savino, Sebastiano, Sergio, Silvio, Stefano,
Taddeo, Tancredi, Tarso, Teodoro, Teogene, Tiberio, Tito, Tiziano, Tobia, Tullio,
Ubaldo, Uberto, Ugo, Ulisse, Ulrico, Ultimo, Umberto, Uranio, Urbano, Ursino,
Valter , Vasco, Valentino, Valerio, Velio, Viliberto, Vincenzo, Virgilio, Virone, Vittorio,
Zabedeo, Zaccaria, Zaccheo, Zanobi, Zefiro, Zeno, Zenobio, Zenone, Zetico, Zoilo
"""

nomif = """Angela, Ada, Adelaide, Anna, Antonella, Anita, Alice, Amelia, Anna, Agnese, Alessandra, Alessia,
Aurora, Angelica,
Barbara, Betty, Beatrice,
Calogera, Claudia, Carlotta, Carmen, Carola, Caterina, Cinzia, Clara, Clarissa, Clelia, Concetta,
Corinna, Cristina,
Daniela, Dina, Domenica, Debora, Denise, Danila, Dorotea,
Emanuela, Emilia, Evelyn, Erica, Elena, Elisa, Eva,
Fiorella, Francesca, Federica, Fabiola, Flavia, Floriana,
Giovannna, Gabriella, Gerlanda, Giulia, Giuseppina, Giorgia, Gaia, Gemma, Greta,
Ida, Iole, Iolanda, Irene, Isabella, Iside,
katia, Ketty,
Luciana, Laura, Lorena, Loredana, Lucia, Lea, Letizia, Lia, Linda, Luisa,
Maria, Marcella, Martina, Marzia, Mara, Marisa, Marta, Mirella, Miriam,
Noemi, Nada,
Ornella,
Patrizia, Paola, Piera, Pamela, Piera,
Roberta, Regina, Raffaella, Rosella,
Salvatrice, Silvia, Sofia, Sabrina, Sara, Serena, Silvana, Simona, Stefania, Susanna,
Tiziana, Tea, Teresa,
Valentina, Valeria"""

cognomi="""
Rossi
Russo
Ferrari
Esposito
Bianchi
Romano
Colombo
Ricci
Marino
Greco
Bruno
Gallo
Conti
De Luca
Mancini
Costa
Giordano
Rizzo
Lombardi
Moretti
Barbieri
Fontana
Santoro
Mariani
Rinaldi
Caruso
Ferrara
Galli
Martini
Leone
Longo
Gentile
Martinelli
Vitale
Lombardo
Serra
Coppola
De Santis
D'angelo
Marchetti
Parisi
Villa
Conte
Ferraro
Ferri
Fabbri
Bianco
Marini
Grasso
Valentini
Messina
Sala
De Angelis
Gatti
Pellegrini
Palumbo
Sanna
Farina
Rizzi
Monti
Cattaneo
Morelli
Amato
Silvestri
Mazza
Testa
Grassi
Pellegrino
Carbone
Giuliani
Benedetti
Barone
Rossetti
Caputo
Montanari
Guerra
Palmieri
Bernardi
Martino
Fiore
De Rosa
Ferretti
Bellini
Basile
Riva
Donati
Piras
Vitali
Battaglia
Sartori
Neri
Costantini
Milani
Pagano
Ruggiero
Sorrentino
D'amico
Orlando
Damico
"""

f = open("06_exercise/data/Elenco-comuni-italiani.csv","r",encoding="utf-8")
comuni = f.readlines()
f.close()
comuni = list(map(lambda x:x.split(","),comuni[1:]))
comuni = list(map(lambda x:x[5].strip(),comuni))

nomim = nomim.split(",")
nomif = nomif.split(",")
cognomi = cognomi.split("\n")
nomim = list(map(lambda x:x.strip(),nomim))
nomif = list(map(lambda x:x.strip(),nomif))
cognomi = list(map(lambda x:x.strip(),cognomi))

nomim = list(filter(lambda x:x!="",nomim))
nomif = list(filter(lambda x:x!="",nomif))
cognomi = list(filter(lambda x:x!="",cognomi))

pazienti = set()
for i in range(N):
    nomi = nomim if i%2 == 0 else nomif

    sesso = "M" if i%2 == 0 else "F"
    nome = nomi[random.randint(0,len(nomi)-1)]
    cognome = cognomi[random.randint(0,len(cognomi)-1)]
    data = F"{random.randint(1,28)}/{random.randint(1,12)}/{random.randint(1920,2020)}"
    comune = comuni[random.randint(0,len(comuni)-1)]
    while "/" in comune:
        comune = comuni[random.randint(0,len(comuni)-1)]
    pazienti.add(f"{nome},{cognome},{data},{comune},{sesso}\n")

f = open("06_exercise/data/pazienti.csv","w",encoding="utf-8")
f.write("nome,cognome,data,comune,sesso\n")
for p in pazienti:
    f.write(p)
f.close()
    
