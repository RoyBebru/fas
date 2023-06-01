#!/bin/sh

mkdir -p ./locale/uk/LC_MESSAGES
[ ! -f ./locale/uk/LC_MESSAGES/fas.po ] && \
    cp messages.pot ./locale/uk/LC_MESSAGES/fas.po && \
    echo "Translate messages in ./locale/uk/LC_MESSAGES/fas.po"
