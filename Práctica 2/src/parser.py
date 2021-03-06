import os

from model.app import App

# Define files
apps_file_array = ['..', 'data', 'google-play-store-apps', 'googleplaystore.csv']
reviews_file_array = ['..', 'data', 'google-play-store-apps', 'googleplaystore_user_reviews.csv']

# Define test files
test_apps_file_array = ['tests', 'apps.csv']
test_reviews_file_array = ['tests', 'reviews.csv']

TESTING = False
if TESTING:
    apps_file = os.path.join(*test_apps_file_array)
    reviews_file = os.path.join(*test_reviews_file_array)
else:
    apps_file = os.path.join(*apps_file_array)
    reviews_file = os.path.join(*reviews_file_array)

print("Apps file: {}".format(apps_file))
print("Reviews file: {}".format(reviews_file))

# Parse both files

# Read apps
appsDict = {}
APP_HEADER = ''
if os.path.isfile(apps_file):
    with open(apps_file, 'r') as fileApps:
        APP_HEADER = fileApps.readline().replace('\n', '')
        for line in fileApps:
            app = App(line)
            appsDict [ app.name ] = app

    print("Apps found {}".format( len(appsDict) ))
else:
    print("Can't find file {}".format(apps_file))

# Read reviews
reviewDict = {}
MAX_NUMBER_OF_REVIEWS = 5
if os.path.isfile(reviews_file):
    with open(reviews_file, 'r') as fileRev:
        fileRev.readline() # avoid first line
        for line in fileRev:
            line = line.replace('\n', '')
            tokens = line.split(';')
            if tokens[0] not in reviewDict:
                reviewDict[ tokens[0] ] = []
                reviewDict[ tokens[0] ].append( tokens[1] )
            else:
                if len(reviewDict[ tokens[0] ]) <= MAX_NUMBER_OF_REVIEWS:
                    reviewDict[ tokens[0] ].append( tokens[1] )
                else:
                    pass # la review se descarta

    print("Apps with reviews found {}".format( len(reviewDict) ))
else:
    print("Can't find file {}".format(apps_file))



# Adding reviews to app and saving to file
out_file_name = ['out', 'parsed_apps.csv']
out_file = os.path.join(*out_file_name)

for x in range(MAX_NUMBER_OF_REVIEWS):
    APP_HEADER += ';Comment {}'.format(x + 1)
APP_HEADER += '\n'

with open(out_file, 'w', encoding="utf8") as fout:
    fout.write(APP_HEADER)
    for key in appsDict:
        app = appsDict[key]
        if app.name in reviewDict:
            app.addReviews( reviewDict[app.name] )
            fout.write( app.toCSV() )
        else:
            pass #if no comments in app avoid writing it
