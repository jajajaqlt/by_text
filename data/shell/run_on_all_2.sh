#!/bin/bash

for filedir in output_jsons/*; do
    echo $filedir
    filename=$(echo $filedir| cut -d'/' -f 2)
    echo $filename
    filestem=$(echo $filename| cut -d'.' -f 1)
    echo $filestem
    python3 apply_dictionaries_s2_json.py $filedir ready_to_use/$filestem-ready.json lists/short-titles_0.9 lists/short-authors_5 lists/short-venues_50
done
