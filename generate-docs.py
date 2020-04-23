import sys
import os
import gzip
import json
import csv


if __name__ == '__main__':

    with open(sys.argv[2], mode='w') as dest_file:
        writer = csv.writer(dest_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i, fname in enumerate(os.listdir(sys.argv[1])):
            if fname.endswith('.gz'):
                with gzip.open(os.path.join(sys.argv[1], fname)) as f:
                    doc = json.dumps({'text': f.read()})
                    writer.writerow([doc])



