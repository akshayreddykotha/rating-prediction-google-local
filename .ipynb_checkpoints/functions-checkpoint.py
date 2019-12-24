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