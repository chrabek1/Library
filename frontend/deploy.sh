#!/bin/bash

set -e

echo "Building the react app"

docker exec -it books_frontend bash -c 'npm run build' > /dev/null
echo "Done"

echo "Deploying to s3"

aws s3 sync /home/chrabek/dev/web/books/frontend/src/build s3://radek-library --acl public-read > /dev/null

echo "Done"

echo "Website public url:"
echo "http://radek-library.s3-website.eu-west-2.amazonaws.com/"

