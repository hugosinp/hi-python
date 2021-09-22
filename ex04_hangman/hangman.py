import random

def generate_word():
    word_list = [
        "aback", "abaft", "abandoned", "abashed", "aberrant", "abhorrent", "abiding", "abject", "ablaze",
        "able", "abnormal", "aboard", "aboriginal", "abortive", "abounding", "abrasive", "abrupt", "absent",
        "absorbed", "absorbing", "abstracted", "absurd", "abundant", "abusive", "accept", "acceptable",
        "accessible", "accidental", "account", "accurate", "achiever", "acid", "acidic", "acoustic",
        "acoustics", "acrid", "act", "action", "activity", "actor", "actually", "ad hoc", "adamant",
        "adaptable", "add", "addicted", "addition", "adhesive", "adjoining", "adjustment", "admire", "admit",
        "adorable", "adventurous", "advertisement", "advice", "advise", "afford", "afraid", "aftermath",
        "afternoon", "afterthought", "aggressive", "agonizing", "agree", "agreeable", "agreement", "ahead",
        "air", "airplane", "airport", "ajar", "alarm", "alcoholic", "alert", "alike", "alive", "alleged",
        "allow", "alluring", "aloof", "amazing", "ambiguous", "ambitious", "amount", "amuck", "amuse",
        "amused", "amusement", "amusing", "analyze", "ancient", "anger", "angle", "angry", "animal",
        "animated", "announce", "annoy", "annoyed", "annoying", "answer", "ants", "anxious", "apathetic",
        "apologise", "apparatus", "apparel", "appear", "applaud", "appliance", "appreciate", "approval",
        "approve", "aquatic", "arch", "argue", "argument", "arithmetic", "arm", "army", "aromatic", "arrange",
        "arrest", "arrive", "arrogant", "art", "ashamed", "ask", "aspiring", "assorted", "astonishing",
        "attach", "attack", "attempt", "attend", "attract", "attraction", "attractive", "aunt", "auspicious",
        "authority", "automatic", "available", "average", "avoid", "awake", "aware", "awesome", "awful",
        "axiomatic", "babies", "baby", "back", "bad", "badge", "bag", "bait", "bake", "balance", "ball", "ban",
        "bang", "barbarous", "bare", "base", "baseball", "bashful", "basin", "basket", "basketball", "bat",
        "bath", "bathe", "battle", "bawdy", "bead", "beam", "bear", "beautiful", "bed", "bedroom", "beds",
        "bee", "beef", "befitting", "beg", "beginner", "behave", "behavior", "belief", "believe", "bell",
        "belligerent", "bells", "belong", "beneficial", "bent", "berry", "berserk", "best", "better",
        "bewildered", "big", "bike", "bikes", "billowy", "bird", "birds", "birth", "birthday", "bit", "bite",
        "bite-sized", "bitter", "bizarre", "black", "black-and-white", "blade", "bleach", "bless", "blind",
        "blink", "blood", "bloody", "blot", "blow", "blue", "blue-eyed", "blush", "blushing", "board", "boast",
        "boat", "boil", "boiling", "bolt", "bomb", "bone", "book", "books", "boorish", "boot", "border",
        "bore", "bored", "boring", "borrow", "bottle", "bounce", "bouncy", "boundary", "boundless", "bow",
        "box", "boy", "brainy", "brake", "branch", "brash", "brass", "brave", "brawny", "breakable", "breath",
        "breathe", "breezy", "brick", "bridge", "brief", "bright", "broad", "broken", "brother", "brown",
        "bruise", "brush", "bubble", "bucket", "building", "bulb", "bump", "bumpy", "burly", "burn", "burst",
        "bury", "bushes", "business", "bustling", "busy", "butter", "button", "buzz", "cabbage", "cable",
        "cactus", "cagey", "cake", "cakes", "calculate", "calculating", "calculator", "calendar", "call",
        "callous", "calm", "camera", "camp", "can", "cannon", "canvas", "cap", "capable", "capricious",
        "caption", "car", "card", "care", "careful", "careless", "caring", "carpenter", "carriage", "carry",
        "cars", "cart", "carve", "cast", "cat", "cats", "cattle", "cause", "cautious", "cave", "ceaseless",
        "celery", "cellar", "cemetery", "cent", "certain", "chalk", "challenge", "chance", "change",
        "changeable", "channel", "charge", "charming", "chase", "cheap", "cheat", "check", "cheer", "cheerful",
        "cheese", "chemical", "cherries", "cherry", "chess", "chew", "chicken", "chickens", "chief",
        "childlike", "children", "chilly", "chin", "chivalrous", "choke", "chop", "chubby", "chunky", "church",
        "circle", "claim", "clam", "clammy", "clap", "class", "classy", "clean", "clear", "clever", "clip",
        "cloistered", "close", "closed", "cloth", "cloudy", "clover", "club", "clumsy", "cluttered", "coach",
        "coal", "coast", "coat", "cobweb", "coherent", "coil", "cold", "collar", "collect", "color",
        "colorful", "colossal", "colour", "comb", "combative", "comfortable", "command", "committee", "common",
        "communicate", "company", "compare", "comparison", "compete", "competition", "complain", "complete",
        "complex", "concentrate", "concern", "concerned", "condemned", "condition", "confess", "confuse",
        "confused", "connect", "connection", "conscious", "consider", "consist", "contain", "continue",
        "control", "cooing", "cook", "cool", "cooperative", "coordinated", "copper", "copy", "corn", "correct",
        "cough", "count", "country", "courageous", "cover", "cow", "cowardly", "cows", "crabby", "crack",
        "cracker", "crash", "crate", "craven", "crawl", "crayon", "crazy", "cream", "creator", "creature",
        "credit", "creepy", "crib", "crime", "crook", "crooked", "cross", "crow", "crowd", "crowded", "crown",
        "cruel", "crush", "cry", "cub", "cuddly", "cultured", "cumbersome", "cup", "cure", "curious", "curl",
        "curly", "current", "curtain", "curve", "curved", "curvy", "cushion", "cut", "cute", "cycle",
        "cynical", "dad", "daffy", "daily", "dam", "damage", "damaged", "damaging", "damp", "dance",
        "dangerous", "dapper", "dare", "dark", "dashing", "daughter", "day", "dazzling", "dead", "deadpan",
        "deafening", "dear", "death", "debonair", "debt", "decay", "deceive", "decide", "decision", "decisive",
        "decorate", "decorous", "deep", "deeply", "deer", "defeated", "defective", "defiant", "degree",
        "delay", "delicate", "delicious", "delight", "delightful", "delirious", "deliver", "demonic", "depend",
        "dependent", "depressed", "deranged", "describe", "descriptive", "desert", "deserted", "deserve",
        "design", "desire", "desk", "destroy", "destruction", "detail", "detailed", "detect", "determined",
        "develop", "development", "devilish", "didactic", "different", "difficult", "digestion", "diligent",
        "dime", "dinner", "dinosaurs", "direction", "direful", "dirt", "dirty", "disagree", "disagreeable",
        "disappear", "disapprove", "disarm", "disastrous", "discover", "discovery", "discreet", "discussion",
        "disgusted", "disgusting", "disillusioned", "dislike", "dispensable", "distance", "distinct",
        "distribution", "disturbed", "divergent", "divide", "division", "dizzy", "dock", "doctor", "dog",
        "dogs", "doll", "dolls", "domineering", "donkey", "door", "double", "doubt", "doubtful", "downtown",
        "drab", "draconian", "drag", "drain", "dramatic", "drawer", "dream", "dreary", "dress", "drink",
        "drip", "driving", "drop", "drown", "drum", "drunk", "dry", "duck", "ducks", "dull", "dust", "dusty",
        "dynamic", "dysfunctional", "eager", "ear", "early", "earn", "earsplitting", "earth", "earthquake",
        "earthy", "easy", "eatable", "economic", "edge", "educate", "educated", "education", "effect",
        "efficacious", "efficient", "egg", "eggnog", "eggs", "eight", "elastic", "elated", "elbow", "elderly",
        "electric", "elegant", "elfin", "elite", "embarrass", "embarrassed", "eminent", "employ", "empty",
        "enchanted", "enchanting", "encourage", "encouraging", "end", "endurable", "energetic", "engine",
        "enjoy", "enormous", "enter", "entertain", "entertaining", "enthusiastic", "envious", "equable",
        "equal", "erect", "erratic", "error", "escape", "ethereal", "evanescent", "evasive", "even", "event",
        "examine", "example", "excellent", "exchange", "excite", "excited", "exciting", "exclusive", "excuse",
        "exercise", "exist", "existence", "exotic", "expand", "expansion", "expect", "expensive", "experience",
        "expert", "explain", "explode", "extend", "extra-large", "extra-small", "exuberant", "exultant", "eye",
        "eyes", "fabulous", "face", "fact", "fade", "faded", "fail", "faint", "fair", "fairies", "faithful",
        "fall", "fallacious", "false", "familiar", "famous", "fanatical", "fancy", "fang", "fantastic", "far",
        "far-flung", "farm", "fascinated", "fast", "fasten", "fat", "faulty", "fax", "fear", "fearful",
        "fearless", "feeble", "feeling", "feigned", "female", "fence", "fertile", "festive", "fetch", "few",
        "field", "fierce", "file", "fill", "film", "filthy", "fine", "finger", "finicky", "fire", "fireman",
        "first", "fish", "fit", "five", "fix", "fixed", "flag", "flagrant", "flaky", "flame", "flap", "flash",
        "flashy", "flat", "flavor", "flawless", "flesh", "flight", "flimsy", "flippant", "float", "flock",
        "flood", "floor", "flow", "flower", "flowers", "flowery", "fluffy", "fluttering", "fly", "foamy",
        "fog", "fold", "follow", "food", "fool", "foolish", "foot", "force", "foregoing", "forgetful", "fork",
        "form", "fortunate", "found", "four", "fowl", "fragile", "frail", "frame", "frantic", "free",
        "freezing", "frequent", "fresh", "fretful", "friction", "friend", "friendly", "friends", "frighten",
        "frightened", "frightening", "frog", "frogs", "front", "fruit", "fry", "fuel", "full", "fumbling",
        "functional", "funny", "furniture", "furry", "furtive", "future", "futuristic", "fuzzy", "gabby",
        "gainful", "gamy", "gaping", "garrulous", "gate", "gather", "gaudy", "gaze", "geese", "general",
        "gentle", "ghost", "giant", "giants", "giddy", "gifted", "gigantic", "giraffe", "girl", "girls",
        "glamorous", "glass", "gleaming", "glib", "glistening", "glorious", "glossy", "glove", "glow", "glue",
        "godly", "gold", "good", "goofy", "gorgeous", "government", "governor", "grab", "graceful", "grade",
        "grain", "grandfather", "grandiose", "grandmother", "grape", "grass", "grate", "grateful", "gratis",
        "gray", "grease", "greasy", "great", "greedy", "green", "greet", "grey", "grieving", "grin", "grip",
        "groan", "groovy", "grotesque", "grouchy", "ground", "group", "growth", "grubby", "gruesome", "grumpy",
        "guarantee", "guard", "guarded", "guess", "guide", "guiltless", "guitar", "gullible", "gun", "gusty",
        "guttural", "habitual", "hair", "haircut", "half", "hall", "hallowed", "halting", "hammer", "hand",
        "handle", "hands", "handsome", "handsomely", "handy", "hang", "hanging", "hapless", "happen", "happy"
    ]

    word = random.choice(word_list)

    return word


def validate_letter(word, transparent_list, letter):

    occurence = word.count(letter)

    if occurence == 1:
        transparent_list.pop(word.index(letter))
        transparent_list.insert(word.index(letter), letter)

        print("Good guess !\n")
        print("==> "+' '.join(transparent_list))

    elif occurence > 1:
        index = word.index(letter)
        transparent_list.pop(index)
        transparent_list.insert(index, letter)

        for i in range(1, occurence):
            new_index = word.index(letter, index+1)
            print("new index : "+str(word.index(letter, index+1)))
            transparent_list.pop(new_index)
            transparent_list.insert(new_index, letter)

        print("Good guess !\n")
        print("==> "+' '.join(transparent_list))

    elif occurence == 0:
        print("Bad guess !\n")
        print("==> "+' '.join(transparent_list))
        return -1


def compare_result(word, list):

    if word == ''.join(list):
        print("Congratulations, the word was : "+word)
        return True
    else:
        return False


def play():

    word = generate_word()
    word_length = len(word)

    transparent_list = []
    tries = 5

    print("Hangman Game".center(50, "="))
    print("==> ", end="")
    # Initial Guess Loop
    for i in range(0, word_length):
        print("_ ", end="")
        transparent_list.append("_")


    # First Interaction 
    user_input = input("\nEnter a letter ! : ")
    if validate_letter(word, transparent_list, user_input) == -1:
        tries -= 1

    # Game Loop
    while compare_result(word, transparent_list) == False:
        
        print("Tries Remaining : "+str(tries))
        user_input = input("Enter a new letter ! : ")
        
        # Bad Input Loop
        while len(user_input) != 1:
            user_input = input("Enter one letter only : ")
            if(len(user_input) == 1):
                break

        # Game State Validation
        if validate_letter(word, transparent_list, user_input) == -1:
            tries -= 1

        if tries == 0:
            print("Too much tries, you lost. The word to guess was : "+word)
            break

if __name__ == "__main__":

    play()