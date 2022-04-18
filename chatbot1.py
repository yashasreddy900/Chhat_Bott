from nltk.chat.util import Chat#natural lan tool kit
#Pairs is a list of patterns and responses.#relections are like dictioart(key value pairs)
pair = [
    [
        r"(.*)my name is (.*)",#regex expressions, used to match as much as it can
        ["Hello , How are you today ?",]
    ],
    
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
    
     [
        r"(.*) your name ?",
        ["am a pogrammer, bt you can call me the gr8 YASHAS REDDY ",]
    ],
    
    [
        r"(.*)how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
         ],
    [
        r"(.*)created(.*)",
        ["Aman Kharwal created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['New Delhi, India',]
    ],
    
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    
    [
        r"(.*)", ['That is nice to hear']
    ],
    [
        r"(.*) what do you do(.*)",
        ["Hello %2,?",]
    ],
    [
        r"(.*)what are you wearing ?(.*)",
        ["Hello %2,jeans ",]
    ],
    [
        r"(.*)what is your favourite color ?(.*)",
        ["Hello %2,red ",]
    ],
    
    [
        r"(.*)what are your hobby? (.*)",
        ["Hello %2,watching series  ",]
    ],
    
    [
        r"(.*)what's for lunch ?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)whats for breakfast? (.*)",
        ["Hello %2, idli vada",]
    ],
    
    [
        r"(.*)what's for dinner ?(.*)",
        ["Hello %2, chiken fry",]
    ],
    
    [
        r"(.*)i like you ?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)say u like me ?(.*)",
        ["Hello %2,i like you too ",]
    ],
    
    [
        r"(.*)where do u live ?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*) what's your age ?(.*)",
        ["Hello %2,",]
    ],
    
    [
        r"(.*)what's your height ?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)what's the iphone price ? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)what's your favourite food ?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*) do u like travelling ?(.*)",
        ["Hello %2,",]
    ],
    
    [
        r"(.*)am getting hungry ?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)please help me ?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*) can you write my assignment ?(.*)",
        ["Hello %2,   ",]
    ],
    
    [
        r"(.*)hey you look beautiful ?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)how am looking today?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*) can i tell you something?(.*)",
        ["Hello %2,",]
    ],
    
    [
        r"(.*)my name is (.*)",
        ["Hello %2, what to do now?",]
    ],
    
    [
        r"(.*)how's your day?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)how's today's climate?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)what's the date today? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*) can you eat food?(.*)",
        ["Hello %2,",]
    ],
    [
        r"(.*)can you sleep? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)can you run? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)what makes you happy? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)do u think am a stupid?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)tell me something about me?(.*)",
        ["Hello %2, ",]
    ],
    [
        r"(.*)what's the time now?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)hey am getting sleep? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*) may i come in?(.*)",
        ["Hello %2,",]
    ],
    
    [
        r"(.*) what are you doing?(.*)",
        ["Hello %2,",]
    ],
    
    [
        r"(.*)what are you studying?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)who's india's prime minister? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)who's karnataka's's chief minister? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)who's india's richest cricketer? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)who's  dhoni? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)How are you today ?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)who's india's goat of all time?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)who's yadiyurappa? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)which is the highest peak in india? (.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)my name is (.*)",
        ["Hello %2, what is your nation name?",]
    ],
    
    [
        r"(.*)where is my home?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)where to order food?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)my name is where to order cloths?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)where to buy books?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*) how's my hairstyle?(.*)",
        ["Hello %2,",]
    ],
    
    [
        r"(.*) how do i look? (.*)",
        ["Hello %2,",]
    ],
    
    [
        r"(.*)what's my bike name?(.*)",
        ["Hello %2, ",]
    ],
    [
        r"(.*) do you like bikes?(.*)",
        ["Hello %2,",]
    ],
    
    [
        r"(.*)which is your favourite bike?(.*)",
        ["Hello %2, ",]
    ],
    
    [
        r"(.*)which is your favourite  car?(.*)",
        ["Hello %2, ",]
    ],
    
]
 

#default message at the start of chat
print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pair)#command to run chat.converse()
