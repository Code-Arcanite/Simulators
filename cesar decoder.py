#cifrado cesar
print("█▀▀ █▀▀ █▀ ▄▀█ █▀█   █▀▄ █▀▀ █▀▀ █▀█ █▀▄ █▀▀ █▀█\n█▄▄ ██▄ ▄█ █▀█ █▀▄   █▄▀ ██▄ █▄▄ █▄█ █▄▀ ██▄ █▀▄")
print("█░█   █▀█ ░ ▄█   █▄▄ █▀▀ ▀█▀ ▄▀█   █▀▀ █▀▄ █ ▀█▀ █ █▀█ █▄░█\n▀▄▀   █▄█ ▄ ░█   █▄█ ██▄ ░█░ █▀█   ██▄ █▄▀ █ ░█░ █ █▄█ █░▀█")
control={'determine', 'drive', 'boat', 'mass', 'table', 'measure', 'sent', 'far', 'world', 'pretty', 'bank', 'carry', 'rub', 'nation', 'represent', 'are', 'machine', 'bar', 'apple', 'sand', 'except', 'check', 'leg', 'grand', 'three', 'during', 'term', 'write', 'planet', 'master', 'jumps', 'here', 'over', 'chord', 'force', 'material', 'rule', 'edge', 'send', 'up', 'dry', 'usual', 'bring', 'has', 'period', 'special', 'money', 'enter', 'group', 'summer', 'quite', 'earth', 'company', 'held', 'must', 'number', 'offer', 'could', 'pass', 'than', 'does', 'each', 'help', 'yes', 'process', 'other', 'too', 'hour', 'drink', 'go', 'colony', 'touch', 'fly', 'steel', 'shop', 'suggest', 'find', 'yellow', 'course', 'us', 'together', 'silver', 'connect', 'friend', 'move', 'buy', 'suffix', 'minute', 'sense', 'got', 'bone', 'show', 'meant', 'cover', 'nor', 'favor', 'test', 'chair', 'mouth', 'evening', 'law', 'card', 'plane', 'red', 'rose', 'nose', 'late', 'circle', 'string', 'hello', 'oxygen', 'fig', 'bit', 'fast', 'his', 'went', 'flower', 'believe', 'million', 'a', 'duck', 'corn', 'so', 'against', 'burn', 'gone', 'roll', 'winter', 'race', 'instant', 'quick', 'once', 'young', 'follow', 'region', 'crease', 'column', 'mix', 'doctor', 'great', 'only', 'party', 'ride', 'throw', 'led', 'salt', 'change', 'particular', 'wave', 'history', 'exact', 'speak', 'gentle', 'my', 'snow', 'able', 'head', 'well', 'sun', 'charge', 'south', 'sleep', 'slip', 'probable', 'map', "don't", 'big', 'hot', 'half', 'turn', 'fun', 'night', 'tail', 'depend', 'heat', 'atom', 'include', 'that', 'climb', 'tie', 'liquid', 'motion', 'captain', 'modern', 'if', 'wash', 'electric', 'imagine', 'children', 'child', 'hill', 'blood', 'branch', 'possible', 'silent', 'simple', 'fat', 'compare', 'season', 'line', 'organ', 'mountain', 'life', 'as', 'last', 'just', 'parent', 'cent', 'age', 'prove', 'example', 'think', 'eight', 'difficult', 'necessary', 'place', 'finish', 'score', 'bat', 'opposite', 'skill', 'had', 'broke', 'vowel', 'cry', 'watch', 'dog', 'letter', 'clean', 'there', 'feed', 'told', 'come', 'mount', 'top', 'should', 'day', 'shoulder', 'produce', 'music', 'spell', 'fraction', 'stone', 'how', 'have', 'press', 'am', 'allow', 'wear', 'laugh', 'cross', 'moment', 'her', 'might', 'been', 'fall', 'decide', 'moon', 'neck', 'copy', 'open', 'please', 'front', 'sugar', 'gather', 'reply', 'suit', 'hair', 'separate', 'famous', 'rail', 'thank', 'village', 'flow', 'coast', 'question', 'invent', 'fear', 'verb', 'ball', 'reach', 'one', 'art', 'which', 'energy', 'molecule', 'while', 'and', 'indicate', 'six', 'wood', 'page', 'phrase', 'grow', 'similar', 'floor', 'ear', 'he', 'problem', 'add', 'bear', 'talk', 'seem', 'new', 'less', 'better', 'saw', 'present', 'town', 'after', 'third', 'locate', 'week', 'require', 'proper', 'toward', 'want', 'seven', 'supply', 'spot', 'came', 'soil', 'speech', 'country', 'level', 'lone', 'who', 'green', 'happen', 'settle', 'take', 'soft', 'quotient', 'view', 'stand', 'fox', 'original', 'word', 'hat', 'say', 'noun', 'repeat', 'fell', 'agree', 'equal', 'notice', 'spring', 'station', 'what', 'heard', 'about', 'seed', 'dictionary', 'speed', 'wind', 'quiet', 'happy', 'remember', 'wish', 'run', 'band', 'subtract', 'sky', 'slow', 'experiment', 'on', 'often', 'idea', 'many', 'short', 'always', 'much', 'major', 'note', 'the', 'food', 'put', 'equate', 'large', 'same', 'gray', 'thick', 'enough', 'distant', 'claim', 'off', 'continent', 'team', 'basic', 'anger', 'star', 'cell', 'hurry', 'animal', 'receive', 'since', 'case', 'gas', 'teeth', 'mile', 'live', 'temperature', 'two', 'magnet', 'log', 'rather', 'method', 'total', 'serve', 'visit', 'draw', 'afraid', 'old', 'rich', 'middle', 'spend', 'home', 'your', 'vary', 'deep', 'why', 'melody', 'face', 'smile', 'dear', 'fruit', 'swim', 'window', 'every', 'contain', 'raise', 'wide', 'was', 'sight', 'surprise', 'few', 'protect', 'work', 'be', 'get', 'double', 'wild', 'make', 'lady', 'shine', 'pattern', 'shore', 'cat', 'save', 'even', 'tool', 'least', 'heart', 'road', 'search', 'any', 'river', 'center', 'share', 'ask', 'pay', 'small', 'win', 'continue', 'sound', 'stay', 'instrument', 'object', 'ship', 'enemy', 'break', 'plural', 'this', 'close', 'high', 'gave', 'paint', 'air', 'tire', 'year', 'own', 'size', 'arrange', 'joy', 'human', 'would', 'mother', 'piece', 'yet', 'language', 'market', 'fill', 'capital', 'lot', 'nine', 'occur', 'teach', 'such', 'deal', 'thing', 'trouble', 'baby', 'shout', 'hole', 'list', 'never', 'whether', 'store', 'hear', 'forest', 'an', 'give', 'chief', 'car', 'for', 'fight', 'iron', 'gold', 'found', 'but', 'behind', 'step', 'camp', 'thought', 'expect', 'good', 'very', 'mean', 'appear', 'excite', 'kind', 'broad', 'little', 'cool', 'solution', 'glass', 'design', 'first', 'twenty', 'color', 'she', 'neighbor', 'side', 'dead', 'rise', 'see', 'weight', 'catch', 'heavy', 'boy', 'spoke', 'loud', 'describe', 'sing', 'port', 'board', 'forward', 'both', 'kept', 'yard', 'wrong', 'poem', 'shell', 'mark', 'to', 'between', 'with', 'value', 'stead', 'learn', 'choose', 'men', 'consonant', 'before', 'death', 'those', 'element', 'no', 'order', 'reason', 'long', 'let', 'still', 'look', 'hit', 'wire', 'caught', 'feet', 'woman', 'observe', 'leave', 'street', 'girl', 'may', 'crop', 'four', 'flat', 'hard', 'knew', 'soldier', 'clock', 'noon', 'lay', 'pitch', 'lost', 'valley', 'complete', 'lead', 'felt', 'sign', 'know', 'ten', 'blow', 'trip', 'wheel', 'corner', 'govern', 'numeral', 'blue', 'hundred', 'cut', 'sell', 'sure', 'guide', 'else', 'through', 'ice', 'clear', 'self', 'where', 'bought', 'select', 'bread', 'condition', 'sentence', 'tube', 'dream', 'tone', 'post', 'some', 'desert', 'cost', 'month', 'rope', 'ring', 'coat', 'family', 'box', 'sharp', 'time', 'also', 'century', 'insect', 'born', 'sea', 'it', 'island', 'name', 'need', 'wtf', 'their', 'natural', 'form', "won't", 'pair', 'pull', 'crowd', 'train', 'weather', 'works', 'egg', 'radio', 'call', 'final', 'triangle', 'sudden', 'wife', 'glad', 'join', 'bright', 'ease', 'house', 'brown', 'bad', 'voice', 'ground', 'best', 'chart', 'length', 'shape', 'common', 'seat', 'past', 'warm', 'pose', 'like', 'west', 'symbol', 'soon', 'at', 'stream', 'substance', 'fish', 'most', 'nature', 'again', 'him', 'square', 'solve', 'cotton', 'play', 'cold', 'milk', 'property', 'paragraph', 'practice', 'key', 'beat', 'drop', 'multiply', 'is', 'way', 'result', 'out', 'student', 'power', 'book', 'smell', 'sit', 'in', 'section', 'track', 'keep', 'control', 'wing', 'syllable', 'body', 'strange', 'among', 'rain', 'thousand', 'fact', 'tiny', 'act', 'garden', 'by', 'walk', 'second', 'listen', 'hope', 'people', 'tree', 'space', 'early', 'slave', 'several', 'lie', 'ready', 'start', 'white', 'dress', 'match', 'king', 'meat', 'do', 'tall', 'ago', 'next', 'song', 'root', 'populate', 'wrote', 'stick', 'danger', 'poor', 'point', 'from', 'brother', 'man', 'base', 'inch', 'low', 'feel', 'door', 'bottom', 'industry', 'either', 'our', 'wonder', 'free', 'quart', 'sat', 'answer', 'mind', 'pound', 'office', 'wait', 'path', 'lazy', 'skin', 'story', 'can', 'operate', 'oil', 'hold', 'thin', 'jump', 'picture', 'die', 'differ', 'stretch', 'love', 'of', 'farm', 'consider', 'eye', 'read', 'science', 'stop', 'scale', 'part', 'record', 'plain', 'metal', 'done', 'paper', 'bell', 'arm', 'rest', 'women', 'build', 'round', 'horse', 'whole', 'system', 'black', 'hand', 'create', 'push', 'cook', 'fire', 'said', 'room', 'state', 'whose', 'plant', 'develop', 'did', 'huge', 'kill', 'truck', 'miss', 'grass', 'grew', 'cause', 'division', 'exercise', 'above', 'busy', 'brought', 'lake', 'thus', 'row', 'steam', 'stood', 'certain', 'try', 'full', 'dollar', 'main', 'count', 'school', 'more', 'use', 'east', 'all', 'near', 'they', 'arrive', 'current', 'spread', 'end', 'experience', 'person', 'degree', 'straight', 'shoe', 'now', 'war', 'product', 'area', 'were', 'finger', 'single', 'sheet', 'clothe', 'land', 'made', 'chick', 'interest', 'wall', 'when', 'correct', 'study', 'until', 'true', 'sister', 'divide', 'light', 'pick', 'fine', 'safe', 'though', 'figure', 'ocean', 'noise', 'plan', 'nothing', 'success', 'unit', 'hunt', 'mine', 'direct', 'begin', 'ran', 'effect', 'cloud', 'bed', 'guess', 'sail', 'event', 'fair', 'down', 'right', 'north', 'written', 'lift', 'son', 'then', 'shall', 'meet', 'chance', 'range', 'surface', 'perhaps', 'fresh', 'under', 'type', 'set', 'position', 'cow', 'gun', 'these', 'field', 'father', 'them', 'support', 'oh', 'dark', 'print', 'matter', 'trade', 'me', 'discuss', 'bird', 'strong', 'decimal', 'will', 'subject', 'especially', 'engine', 'beauty', 'provide', 'five', 'eat', 'ever', 'we', 'water', 'began', 'general', 'class', 'back', 'morning', 'city', 'real', 'or', 'segment', 'fit', 'care', 'prepare', 'dance', 'you', 'job', 'travel', 'character', 'game', 'tell', 'foot', 'dad', 'took', 'rock', 'left', 'collect', 'block'}

def quitar_no_letras(mensaje):
    solo_letras=[]
    letras_v="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for simbolo in mensaje:
        if simbolo in letras_v:
            solo_letras.append(simbolo)
    
    return "".join(solo_letras)
    
def break_caesar(message):
    print("encrypted message:-->",message)
    message=message.upper()
    letras="abcdefghijklmnopqrstuvwxyz"
    print("the length of the dictionary is:",len(letras))
    letras=letras.upper()
    mensaje=""
    lector=[]
    for k in range(len(letras)):
        for i in message:
            if i in letras:
                cilindro_A=letras.find(i)
                cilindro_A-=k
                if cilindro_A<0:
                    cilintro_A=cilindro_A+len(letras)
                mensaje+=letras[cilindro_A]
            elif i not in letras:
                mensaje+=i
        print(mensaje)
        lector.append(mensaje)
        mensaje=""
    mi_diccionario={}
    for K_control in control:
        mi_diccionario[K_control.upper()]=None
    nivel=0
    for r in lector :


        solo_letras_1=quitar_no_letras(r)
        posibilidad=solo_letras_1.split(" ")
        count=0
        for posibilidad_1 in posibilidad:
#            print("posiblidad_1:",posibilidad_1,"con llave :",nivel)
            
        
            if posibilidad_1 in mi_diccionario :
                count+=1
#                print("posibilidad encontrada")
            if (count/len(posibilidad))*100>=65:
                print("possible decrypted message:",r,"\n possible key:",nivel)           
                return nivel
        nivel+=1         
 

            


break_caesar("Gur dhvpx oebja sbk whzcf bire gur ynml qbt.")



'''
test.assert_equals(break_caesar(""), 7) 
test.assert_equals(break_caesar("Mjqqt, btwqi!"), 5)
test.assert_equals(break_caesar("Gur dhvpx oebja sbk whzcf bire gur ynml qbt."), 13)
'''
