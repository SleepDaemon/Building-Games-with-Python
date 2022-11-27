# series of questions to ask the user to guess the user's location of birth
print('Hello! I am going to try to guess your location of birth based on your answers to a series of questions.')
print('Please answer the following questions with a "yes" or "no" answer.')

# Start Process
def start():
    while True:
        try:
            continent = input('Which continent is your location of birth in? ' )
            if continent == 'North America':
                NA()
                break
            elif continent == 'South America':
                SA()
                break
            elif continent == 'Europe':
                EU()
                break
            elif continent == 'Asia':
                AS()
                break
            elif continent == 'Africa':
                AF()
                break
            elif continent == 'Other':
                OC()
                break
        except ValueError:
            print("Invalid input, only 'yes' or 'no'")
            continue

# North America Module
def NA():
    while True:
        try:
            north = input('Are you from a English speaking country? ')
            if north == 'yes':
                north = input('Are you from the United States? ')
                if north == 'yes':
                    print('I think you are from the United States!')
                else:
                    print('I think you are from Canada!')
            elif north == 'no':
                north = input('Are you from Mexico? ')
                if north == 'yes':
                    print('I think you are from Mexico!')
                    break
                elif north == 'no':
                    print('I think you are from a country that I do not know! Narnia???')
        except ValueError:
            print("Invalid input, only 'yes' or 'no'")
            continue

# South America Module
def SA():
    while True:
        try:
            south = input('Are you from a Spanish speaking country? ')
            if south == 'yes':
                south = input('Are you from Argentina? ')
                if south == 'yes':
                    print('I think you are from Argentina!')
                    break
                elif south == 'no':
                    south = input('Are you from Chile? ')
                    if south == 'yes':
                        print('I think you are from Chile!')
                        exit
                    elif south == "no":
                        south = input('Are you from Colombia? ')
                        if south == 'yes':
                            print('I think you are from Colombia!')
                            break
                        elif south == 'no':
                            south = input('Are you from Ecuador? ')
                            if south == 'yes':
                                print('I think you are from Ecuador!')
                                break
                            elif south == 'no':
                                south = input('Are you from Peru? ')
                                if south == 'yes':
                                    print('I think you are from Peru!')
                                    break
                                elif south == 'no':
                                    south = input('Are you from Uruguay? ')
                                    if south == 'yes':
                                        print('I think you are from Uruguay!')
                                        break
                                    elif south == 'no':
                                        south = input('Are you from Venezuela? ')
                                        if south == 'yes':
                                            print('I think you are from Venezuela!')
                                            break
                                        elif south == 'no':
                                            south = input('Are you from Brazil? ')
                                            if south == 'yes':
                                                print('I think you are from Brazil!')
                                                break
                                            elif south == 'no':
                                                print('I think you are from a country that I do not know! Narnia???')
                                                break
                elif south == 'no':
                    south = input('Are you from Brazil? ')
                    if south == 'yes':
                        print('I think you are from Brazil!')
                        break
                    elif south == 'no':
                        print('I think you are from a country that I do not know! Narnia???')
                        break
        except ValueError:
            print("Invalid input, only 'yes' or 'no'")
            continue

# Europe Module
def EU():
    while True:
        try:
            europe = input('Are you from a English speaking country? ')
            if europe == 'yes':
                europe = input('Are you from the United Kingdom? ')
                if europe == 'yes':
                    print('I think you are from the United Kingdom!')
                    break
                elif europe == 'no':
                    print('I think you are from Ireland!')
                    break        
            elif europe == 'no':
                europe = input('Are you from a French speaking country? ')
                if europe == 'yes':
                    europe = input('Are you from France? ')
                    if europe == 'yes':
                        print('I think you are from France!')
                        break
                    elif europe == 'no':
                        europe = input('Are you from Belgium? ')
                        if europe == 'yes':
                            print('I think you are from Belgium!')
                            break
                        elif europe == 'no':
                            europe = input('Are you from Switzerland? ')
                            if europe == 'yes':
                                print('I think you are from Switzerland!')
                                break
                            elif europe == 'no':
                                europe = input('Are you from Luxembourg? ')
                                if europe == 'yes':
                                    print('I think you are from Luxembourg!')
                                    break
                                elif europe == 'no':
                                    print('I think you are from Monaco!')
                                    break
                elif europe == 'no':
                    europe = input('Are you from a German speaking country? ')
                    if europe == 'yes':
                        europe = input('Are you from Germany? ')
                        if europe == 'yes':
                            print('I think you are from Germany!')
                            break
                        elif europe == 'no':
                            europe = input('Are you from Austria? ')
                            if europe == 'yes':
                                print('I think you are from Austria!')
                                break
                            elif europe == 'no':
                                europe = input('Are you from Switzerland? ')
                                if europe == 'yes':
                                    print('I think you are from Switzerland!')
                                    break
                                elif europe == 'no':
                                    europe = input('Are you from Belgium? ')
                                    if europe == 'yes':
                                        print('I think you are from Belgium!')
                                        break
                                    elif europe == 'no':
                                        print('I think you are from Luxembourg!')
                                        break

                elif europe == 'no':
                    europe = input('Are you from a Dutch speaking country? ')
                    if europe == 'yes':
                        europe = input('Are you from the Netherlands? ')
                        if europe == 'yes':
                            print('I think you are from the Netherlands!')
                            break
                        elif europe == 'no':
                            europe = input('Are you from Belgium? ')
                            if europe == 'yes':
                                print('I think you are from Belgium!')
                                break
                elif europe == 'no':
                    europe = input('Are you from a Italian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Italy!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Portuguese speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Portugal!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Russian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Russia!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Swedish speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Sweden!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Danish speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Denmark!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Norwegian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Norway!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Finnish speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Finland!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Greek speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Greece!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Hungarian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Hungary!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Polish speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Poland!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Czech speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Czech Republic!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Slovak speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Slovakia!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Romanian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Romania!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Bulgarian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Bulgaria!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Croatian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Croatia!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Slovenian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Slovenia!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Serbian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Serbia!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Bosnian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Bosnia and Herzegovina!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Macedonian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Macedonia!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Albanian speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Albania!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Montenegrin speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Montenegro!')
                        break
                elif europe == 'no':
                    europe = input('Are you from a Turkish speaking country? ')
                    if europe == 'yes':
                        print('I think you are from Turkey!')
                        break
                elif europe == 'no':
                    print('I think you are from a country that I do not know! Narnia???')
        except ValueError:
            print("Invalid input, only 'yes' or 'no'")
            continue

# Asia Module
def AS():
    while True:
        try:
            asia= input('Are you from an Arabic speaking country? ')
            if asia == 'yes':
                asia = input('Are you from Bahrain? ')
                if asia == 'yes':
                    print('I think you are from Bahrain')
                    break
                elif asia == 'no':
                    asia = input('Are you from Iraq? ')
                    if asia == 'yes':
                        print('I think you are from Iraq')
                        break
                    elif asia == 'no':
                        asia = input('Are you from Jordan? ')
                        if asia == 'yes':
                            print('I think you are from Jordan')
                            break
                        elif asia == 'no':
                            asia = input('Are you from Kuwait? ')
                            if asia == 'yes':
                                print('I think you are from Kuwait')
                                break
                            elif asia == 'no':
                                asia = input('Are you from Lebanon? ')
                                if asia == 'yes':
                                    print('I think you are from Lebanon')
                                    break
                                elif asia == 'no':
                                    asia = input('Are you from Oman? ')
                                    if asia == 'yes':
                                        print('I think you are from Oman')
                                        break
                                    elif asia == 'no':
                                        asia = input('Are you from Palestine? ')
                                        if asia == 'yes':
                                            print('I think you are from Palestine')
                                            break
                                        elif asia == 'no':
                                            asia = input('Are you from Qatar? ')
                                            if asia == 'yes':
                                                print('I think you are from Qatar')
                                                break
                                            elif asia == 'no':
                                                asia = input('Are you from Saudi Arabia? ')
                                                if asia == 'yes':
                                                    print('I think you are from Saudi Arabia')
                                                    break
                                                elif asia == 'no':
                                                    asia = input('Are you from Syria? ')
                                                    if asia == 'yes':
                                                        print('I think you are from Syria')
                                                        break
                                                    elif asia == 'no':
                                                        asia = input('Are you from the United Arab Emirates? ')
                                                        if asia == 'yes':
                                                            print('I think you are from the United Arab Emirates')
                                                            break
                                                        elif asia == 'no':
                                                            asia = input('Are you from Yemen? ')
                                                            if asia == 'yes':
                                                                print('I think you are from Yemen')
                                                                break
                                                            elif asia == 'no':
                                                                print('I think you are from a country that I do not know! Narnia???')
                                                                break
            elif asia == 'no':                                                
                asia= input('Are you from a Chinese speaking country? ')
                if asia == 'yes':
                    print('I think you are from China')
                    break
                elif asia == 'no':
                    asia = input('Are you from Singapore? ')
                    if asia == 'yes':
                        print('I think you are from Singapore')
                        break
                    elif asia == 'no':
                        asia = input('Are you from Taiwan? ')
                        if asia == 'yes':
                            print('I think you are from Taiwan')
                            break
                        elif asia == 'no':
                            asia = input('Are you from Hong Kong? ')
                            if asia == 'yes':
                                print('I think you are from Hong Kong')
                                break
                            elif asia == 'no':
                                asia = input('Are you from Hindi speaking country? ')
                                if asia == 'yes':
                                    print('I think you are from India')
                                    break
                                elif asia == 'no':
                                    asia = input('Are you from Pakistan? ')
                                    if asia == 'yes':
                                        print('Then you are from Pakistan')
                                        break
                                    elif asia == 'no':
                                        asia = input('Are you from a Japanese speaking country? ')
                                        if asia == 'yes':
                                            print('Then you are from Japan')
                                            break
                                        elif asia == 'no':
                                            asia = input('Are you from Thailand ')
                                            if asia == 'yes':
                                                print('Then you are from Thailand?')
                                            elif asia == 'no':
                                                asia = input('Are you from Vietnam? ')
                                                if asia == 'yes':
                                                    print('Then you are from Vietnam')
                                                    break
                                                elif asia == 'no':
                                                    asia = input('Are you from North Korea? ')
                                                    if asia == 'yes':
                                                        print('Then you are from North Korea')
                                                        break
                                                    elif asia == 'no':
                                                        asia = input('Are you from South Korea? ')
                                                        if asia == 'yes':
                                                            print('Then you are from South Korea')
                                                            break
                                                        elif asia == 'no':
                                                            asia = input('Are you from Indonesia? ')
                                                            if asia == 'yes':
                                                                print('Then you are from Indonesia')
                                                                break
                                                            elif asia == 'no':
                                                                asia = input('Are you from the Philippines? ')
                                                                if asia == 'yes':
                                                                    print('Then you are from the Philippines')
                                                                    break
                                                                elif asia == 'no':
                                                                    asia = input('Are you from Malaysia? ')
                                                                    if asia == 'yes':
                                                                        print('Then you are from Malaysia')
                                                                        break
                                                                    elif asia == 'no':
                                                                        print('I think you are from a country that I do not know! Narnia???')
                                                                        break
        except ValueError:
            print("Invalid input, only 'yes' or 'no'")
            continue

# Africa Module
def AF():
    while True:
        try: 
            africa= input('Are you from an Arabic speaking country? ')
            if africa == 'yes':
                africa = input('Are you from Algeria? ')
                if africa == 'yes':
                    print('You are from Algeria')
                    break
                elif africa == 'no':
                    africa = input('Are you from Egypt? ')
                    if africa == 'yes':
                        print('You are from Egypt')
                        break
                    elif africa == 'no':
                        africa = input('Are you from Libya? ')
                        if africa == 'yes':
                            print('You are from Libya')
                            break
                        elif africa == 'no':
                            africa = input('Are you from Morocco? ')
                            if africa == 'yes':
                                print('You are from Morocco')
                                break
                            elif africa == 'no':
                                africa = input('Are you from Sudan? ')
                                if africa == 'yes':
                                    print('You are from Sudan')
                                    break
                                elif africa == 'no':
                                    africa = input('Are you from Tunisia? ')
                                    if africa == 'yes':
                                        print('You are from Tunisia')
                                        break
                                    elif africa == 'no':
                                        print('I think you are from a country that I do not know! Narnia???')
                                        break
            elif africa == 'no':
                africa = input('Are you from Chad? ')
                if africa == 'yes':
                    print('You are from Chad')
                    break
                elif africa == 'no':
                    africa = input('Are you from Niger? ')
                    if africa == 'yes':
                        print('You are from Niger')
                        break
                    elif africa == 'no':
                        africa = input('Are you from Nieria? ')
                        if africa == 'yes':
                            print('You are from Nigeria')
                            break
                        elif africa == 'no':
                            africa = input('Are you from Kenya? ')
                            if africa == 'yes':
                                print('You are from Kenya')
                                break
                            elif africa == 'no':
                                africa = input('Are you from Somalia? ')
                                if africa == 'yes':
                                    print('You are from Somalia')
                                    break
                                elif africa == 'no':
                                    africa = input('Are you from South Africa? ')
                                    if africa == 'yes':
                                        print('You are from South Africa')
                                        break
                                    elif africa == 'no':
                                        print('I think you are from a country that I do not know! Narnia???')
                                        break
        except ValueError:
            print("Invalid input, only 'yes' or 'no'")
            continue

# Other Country Module
def OC():
    while True:
        try:
            other = input('Are you an Aussie? ')
            if other == 'yes':
                print('Then you are from Australia? ')
                break
            elif other == 'no':
                other = input('Are you a Kiwi? ')
                if other == 'yes':
                    print('Then you are from New Zealand')
                    break
                elif other == 'no':
                    print('I think you are from a country that I do not know! Narnia???')
                    break
        except ValueError:
            print("Invalid input, only 'yes' or 'no'")
            continue

start()