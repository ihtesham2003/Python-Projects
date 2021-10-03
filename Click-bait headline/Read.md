Learn how to make clickbait or catchy titles generator with python and you can put this into your portfolio.

Are you tired and you have a lot work to do like finding catchy article or blog headings if yes, this Click-bait generator will write millions of articles headers for you!!

Today we will be making this powerful Python project with the help of only one module which is `random`.

This program has functions for generating different kinds of clickbait titles. Each of them gets random words from STATES, NOUNS, PLACES,WHEN and list. This is a lot like Madlibs but it isn't madlibs because computer on by own do the work for us.

Tricking people into your website is easy but creative content is difficult! But clickbait title generator made work some how easy for us. Now, my friend in this program there are a lot of text but the code is really straightforward which will make your day/night great.

When you make this masterpiece you will:
* Know the basics of Python
* Know how to use functions
* Know format()
* Know how to manage things perfectly
* And will know how to smile! haha

Let's get started!!

##Code | Discussion
In this part we will just setting up the Constants.
```
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

```
####DISCUSSION:
* `import random` if you're not familiar with this thing (random) you should give `2` mins to read this [Click to read] (https://docs.python.org/3/library/random.html)
 *Random generate random numbers for integers and other stuff if you have read it!!
* `#The constants` In this part **OBJECT_PRONOUNS, SUSPECIOUS_PRONOUNS, PERSONAL_PRONOUNS, STATES, NOUNS, PLACES, AND WHEN** work as the words which will be used as filling the blanks words.

##Functions and loops
```
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
```
####DISCUSSION:
* `def main():` the main function will have everything like:
 * While loops 
 * for loops etc
* You can change the `print` points if you want to! like change the name with yours By ---
* `while loop` is the game changer this loop will generate the headlines or titles we want like if I want 1000 I will just input 1000 and it will generate it for me by this while loop.
* if have not read my previous python project discussion part so, I urge you to go the discussion part and this will become more easier to you.

```
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
```
####DISCUSSION:
* `for loop` is used after `break` method. This loop will organize the text like in consecutive order... one by one
* `random.randint(1,8)` is really important because with this we will have organize structured titles. The loop will take titles from. One from `millenialsKillinHeadline` and so on...
* `print()` the empty print is used because of the last line which is really funny and it's an order!!

```
 website = random.choice(['website', 'blog', 'Facebook', 'Google',
                             'Facebook', 'Tweeter', 'Instagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!')
```
####DISCUSSION:
* `website` has random.choice which will randomly choose in this list tuple one of the word which is in list and put in a sentence which you will see soon.
* `when` makes the when part lower with lower() method like small text.
* `print` has a warning! Post these to our (website) (randomly adopt from website list) one word. And when from WHEN.

#### The generator part!!
```
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
```
####Discussion:
* Each of `def` means functions returns a different kind of headline/title.
* Like `def generateAreMillennialsKillingHeadline():` will generate or returns `'Are Millennials Killing the {} Industry?'.format(noun)` don't get overwhelmed I'm here to help whenever you need I'm here!. So this line will generate some kind of headline like "Are millenials killing the {noun will be take randomly like athelete or something!}"
* All the others will be taken the same. Like `def generateWhatYouDontKnowHeadline():` this will generate or returns different kind of title... and so on..

####last!
```
#Let's generate some Clickbait catchy titles Play the button!
if __name__ == '__main__':
    main()
```
when you run after this part the code you will see a message for input (for number!) when you put number like 2000 or 100 or maybe 10 the clickbait generator will generate random titles for you!.

Now its your turn, play with this code! like change or add some other code to this and make it an amazing clickbait generator!.

When you do let me know!.
[Linkedin] (https://www.linkedin.com/in/ihtesham-haider-079887218/) [Medium] (https://medium.com/@ihteshamhaider) [Twitter] (https://twitter.com/techtimes101)

[Download the Code] (https://colab.research.google.com/drive/12PsH8wLCK7OtTIFpVLCxOW7pF178zlCd?usp=sharing)

