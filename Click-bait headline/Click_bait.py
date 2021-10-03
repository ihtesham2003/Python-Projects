import random

#The constants
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
SUSPECIOUS_PRONOUNS = ['Her', 'His', 'They']
PERSONAL_PRONOUNS = ['She', 'His', 'Their']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor',
         'Parent', 'Cat','Dog', 'Chicken', 'Robot', 'Video Game',
         'Avocado', 'Plastic Straw', 'Seriel Killer','Telephone Pyschic']
PLACES = [
    'House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
    'Workplace', 'Donut Shop', 'Apocalypse Bunker'
]
WHEN = ['Soon', 'This Year', 'Later', 'RIGHT NOW', 'Next Week']

#The_main_Function
def main():
    print('|| Click Bait Headlline Generator ||')
    print('|| By Ihtesham Haider ||')

    print()
    print('Make your website Grow with Catchy Headlines!!')

    #The_main_loop
    while True:
        print('Please, enter the number of Click-Bait headlines to generate!: ')
        response = input('> ')

        if not response.isdecimal():
            print('Please Enter a number..')
        else:
            numberOfHeadlines = int(response)
            break

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 8)

        if clickbaitType ==1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickbaitType ==2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType ==3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType ==4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType ==5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType ==6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType ==7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType ==8:
            headline = generateJobAutomatedHeadline()

        print(headline)
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                             'Facesbook', 'Tweedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!')


#Now each of these functions will generate different type of Headline

def generateAreMillennialsKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millennials Killing the {} Industry?'.format(noun)

def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill You {}'.format(noun, pluralNoun, when)

def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)

def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(SUSPECIOUS_PRONOUNS)
    place = random.choice(PLACES)
    return 'You Won\'t Believe What This {} {} Found in {} {}'. format(state, noun, pronoun, place)

def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return 'What {} Don\'t Want You To Know About {}'.format(pluralNoun1, pluralNoun2)

def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)

def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    #number 2 should no longer than number1
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)

def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = SUSPECIOUS_PRONOUNS[i]
    pronoun2 = SUSPECIOUS_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong'.format(state, noun, pronoun1, pronoun2)


#Copy and paste...will work. 
if __name__ == '__main__':
    main()
