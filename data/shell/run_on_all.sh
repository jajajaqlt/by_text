#!/bin/bash

for filedir in splits/*; do
    echo $filedir
    filename=$(echo $filedir| cut -d'/' -f 2)
    python3 combined_s2_preprocess.py $filedir output_jsons/$filename.json lists/$filename-titles lists/$filename-authors lists/$filename-venues &
done
