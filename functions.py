# Function to filter US reviews - change coordinates for any other filter
def places_filter(dataset, lat_l, lat_h, lon_l, lon_h):
    reviews_us = []
    for d in dataset:
        if (d['gps'] != None and d['price'] != None):
            if ((d['gps'][0] >= lat_l) \
              & (d['gps'][0] <= lat_h) \
             & (d['gps'][1] >= lon_l) \
            & (d['gps'][1] <= lon_h)):
                reviews_us.append(d)
    return reviews_us   

# Function to join the reviews with the filtered places of locality of interest. This is in a way reduces the number of reviews to be used during modelling - a trade-off between model fit computational power. 
def joined_data(places, reviews)
    placeGPS = defaultdict(list)
    placePrice = defaultdict(list)
    joined_data = []

    for d in places:
        placeGPS[d['gPlusPlaceId']] = d['gps'] 
        placePrice[d['gPlusPlaceId']] = d['price']
    # dataset is reviews data
    for d in reviews:
        if d['gPlusPlaceId'] in placeGPS:
            d['gps'] = placeGPS['gps']
            d['price'] = placePrice['price']
            joined_data.append(d)
    return (joined_data[:5l, len(joined_data))

# Function to calculation the MSE - Mean squared error
def MSE(predictions, labels):
    differences = [(x-y)**2 for x,y in zip(predictions,labels)]
    return sum(differences) / len(differences)

# Function to split reviewText into sentences                      
import re
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences
                        
### This was taken from stackoverflow which helped our purpose and idea. Credit: https://stackoverflow.com/users/5133085/d-greenberg
                      