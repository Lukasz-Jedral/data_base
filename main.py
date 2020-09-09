from models import Database

if __name__ == "__main__":

    with Database('HomeLibrary_db.sqlite') as db:
        db.execute('CREATE TABLE IF NOT EXISTS authors ( \
                    id integer PRIMARY KEY AUTOINCREMENT, \
                    imie VARCHAR(250) NOT NULL, \
                    nazwisko VARCHAR(250) NOT NULL, \
                    opis text );')

        db.execute('CREATE TABLE IF NOT EXISTS publishers ( \
                    id integer PRIMARY KEY AUTOINCREMENT, \
                    nazwa VARCHAR(250) NOT NULL, \
                    siedziba VARCHAR(250) NOT NULL, \
                    opis text );')

        db.execute('CREATE TABLE IF NOT EXISTS genres ( \
                    id integer PRIMARY KEY AUTOINCREMENT, \
                    nazwa VARCHAR(250) NOT NULL );')

        db.execute('CREATE TABLE IF NOT EXISTS books ( \
                    id integer PRIMARY KEY AUTOINCREMENT,\
                    tytuł VARCHAR NOT NULL,\
                    author_id integer NOT NULL,\
                    opis text,\
                    rok_wydania YEAR NOT NULL, \
                    wydawnictwo_id integer NOT NULL,\
                    url_okładki VARCHAR,\
                    genre_id,\
                    FOREIGN KEY(author_id) REFERENCES authors(id),\
                    FOREIGN KEY(wydawnictwo_id) REFERENCES publishers(id),\
                    FOREIGN KEY(genre_id) REFERENCES genres(id) );')

        new_book_1 = ['Wiedźmin: Ostatnie Życzenie',
                    '1',
                    'zbiór opowiadań fantasy z 1993 roku, napisanych przez Andrzeja Sapkowskiego i stanowiących wstęp do cyklu o wiedźminie Geralcie.',
                    '2003',
                    '1',
                    'https://ecsmedia.pl/c/ostatnie-zyczenie-wiedzmin-tom-1-b-iext41816720.jpg',
                    '1']

        new_book_2 = ['Wiedźmin: Miecz przeznaczenia',
                      '1',
                      'zbiór opowiadań z gatunku fantasy z 1992 roku, napisanych przez Andrzeja Sapkowskiego.',
                      '2003',
                      '1',
                      'https://ecsmedia.pl/c/miecz-przeznaczenia-wiedzmin-tom-2-b-iext46968722.jpg',
                      '1']

        new_book_3 = ['Wiedźmin: Krew Elfów',
                      '1',
                      'Zagłębiając się w karty tego dzieła, zaczniesz odkrywać magiczny, wykreowany przez autora w sposób bardzo realistyczny, świat wiedźminów. Poznasz również samego Geralta, który postanawia zaopiekować się dzieckiem‑niespodzianką, którym jest dziewczyna o imieniu Ciri. Ważną postacią jest również czarodziejka Triss, która będzie miała duży wpływ na wychowanie dziecka.',
                      '2003',
                      '1',
                      'https://ecsmedia.pl/c/krew-elfow-wiedzmin-tom-3-w-iext44036191.jpg',
                      '1']

        new_book_4 = ['Wiedźmin: Czas Pogardy',
                      '1',
                      'Nastał czas pogardy, czas miecza i topora, czas wilczej zamieci. Wśród wojennej zawieruchy znaleźli się Geralt, Yennefer i Ciri, ale każde z nich gdzie indziej. Ciri czuje się porzucona, zapomniana, musi sama borykać się z trudami wędrówki przez obcy kraj, w którym się znalazła. Czy wiedźmin odnajdzie swoje przeznaczenie?',
                      '2003',
                      '1',
                      'https://ecsmedia.pl/c/czas-pogardy-wiedzmin-tom-4-w-iext46968716.jpg',
                      '1']

        #if new_book_1:
            #db.execute('INSERT INTO books (tytuł, author_id, opis, rok_wydania, wydawnictwo_id, url_okładki, genre_id) \
                       #VALUES(?,?,?,?,?,?,?)',(new_book_1))

        genres = ['Fantasy',
                    'Adventure',
                    'Romance',
                    'Contemporary',
                    'Dystopian',
                    'Mystery',
                    'Horror',
                    'Thriller',
                    'Paranormal',
                    'Historical Fiction'       
                    'Science Fiction',
                    'Memoir',
                    'Cooking',
                    'Art',
                    'Self - help / Personal',
                    'Development',
                    'Motivational',
                    'Health',
                    'History',
                    'Travel',
                    'Guide / How - to',
                    'Families & Relationships',
                    'Humor',
                    'Children’s']
        #if genres:
            #for genre in genres:
                #db.execute("INSERT INTO genres (nazwa) VALUES(?)", (genre,))

        authors = ['Andrzej',
                   'Sapkowski',
                   'Andrzej Sapkowski jest ikoną polskiej fantastyki oaz jednym z najczęściej tłumaczonych polskich pisarzy na świecie. Twórca Sagi o Wiedźminie, która przyniosła mu międzynarodową sławę zarówno wśród miłośników literatury, jak i filmu oraz gier komputerowych.']
        #if authors:
            #db.execute("INSERT INTO authors (imie, nazwisko, opis) VALUES (?,?,?)",(authors))

        publishers =['SuperNowa',
                     'ul. Nowowiejska 10/12 00-653 Warszawa',
                     ' Niezależna Oficyna Wydawnicza NOWA powstała jesienią 1977. Drukowała zakazane przez komunistyczne władze arcydzieła światowej literatury. Nie stroniła od fantastyki. Jej nakładem ukazały się m.in. książki Georgea Orwella, Kurta Vonneguta, Eugeniusza Zamiatina, Aleksandra Zinowiewa i Tadeusza Konwickiego, którego "Mała apokalipsa" weszła do kanonu lektur szkolnych.Jako pierwsi zajęliśmy się tematem skinowskiej subkultury w książce Ewy Wilk "Krucjata łysogłowych", ukazaliśmy prawdziwe oblicza postkomunistycznych prominentów w "Portretach w podczerwieni" Jerzego Morawskiego i opublikowaliśmy wstrząsające reportaże o ludziach skazanych na karę śmierci - "Czekając na kata"']
        #if publishers:
            #db.execute("INSERT INTO publishers (nazwa, siedziba, opis) VALUES (?,?,?)",(publishers))

        books  = db.query('SELECT books.tytuł, authors.imie, authors.nazwisko FROM books, authors WHERE books.author_id = authors.id')
        print(books)

        #db.del_table('genres')

        books_full = db.query('SELECT * FROM books')
        print(books_full)


        #db.update("books", 2 , opis='brak')