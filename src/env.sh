#!/bin/bash

export $(grep -v '^#' .env.dev | xargs)


echo $FLASK_ENV
echo $DATABASE_URI
echo $DATABASE_USER
echo $DATABASE_PASSWORD
echo $DATABASE_NAME
echo $JWT_SECRET