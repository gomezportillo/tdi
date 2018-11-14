import os

# Define files
apps_file_array = ['..', 'data', 'google-play-store-apps', 'googleplaystore.csv']
reviews_file_array = ['..', 'data', 'google-play-store-apps', 'googleplaystore_user_reviews.csv']

apps_file = os.path.join(*apps_file_array)
reviews_file = os.path.join(*reviews_file_array)

print("Apps file: {}".format(apps_file))
print("Reviews file: {}".format(reviews_file))

# Parse both files

# Read apps
appsDict = {}
if os.path.isfile(apps_file):
    with open(apps_file, 'r', encoding="utf8") as fileApps:
        fileApps.readline() # avoid first line
        for line in fileApps:
            tokens = line.split(',')
            appsDict [tokens[0] ] = tokens[1:] #app name : list with rest of info

    print("Apps found {}".format( len(appsDict) ))
else:
    print("Can't find file {}".format(apps_file))

# Read reviews
reviewDict = {}
MAX_NUMBER_OF_REVIEWS = 5
if os.path.isfile(reviews_file):
    with open(apps_file, 'r', encoding="utf8") as fileRev:
        fileRev.readline() # avoid first line
        for line in fileRev:
            tokens = line.split(',')
            if tokens[0] not in reviewDict:
                reviewDict[ tokens[0] ] = []
                reviewDict[ tokens[0] ].append( tokens[0] )
            else:
                if len(reviewDict[ tokens[0] ]) <= MAX_NUMBER_OF_REVIEWS:
                    reviewDict[ tokens[0] ].append( tokens[0] )
                else:
                    pass # la review se descarta

    print("Reviews found {}".format( len(reviewDict) ))
else:
    print("Can't find file {}".format(apps_file))



# Adding reviews to app and saving to file
out_file_name = ['out', 'parsed_apps.csv']
out_file = os.path.join(*out_file_name)
with open(out_file, 'w', encoding="utf8") as fout:
    for app in appsDict:
        line = []
        line.append( app )
        line += appsDict[app]
        if app in reviewDict:
            line += reviewDict[app]

            line_with_commas = ",".join( [str(x) for x in line] )

            fout.write(line_with_commas)
        else:
            pass #if no comments in app avoid writing it
