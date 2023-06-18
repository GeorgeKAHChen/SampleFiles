#!/bin/bash

if [ ! -n "$1" ]; then
    echo "Usage: ./heic_to_jpg_resize.sh directory"
    exit
fi

heic_files="$(find "$1" -iname '*.heic')"
for file in $heic_files; do
    # Get the heic/HEIC file and find the new file name .jpg
    outfile=${file/%.HEIC/.jpg}
    outfile=${outfile/%.heic/.jpg}
    
    # Initial resize
    magick convert "$file" -quality 90 "$outfile"
    
    rm ${file}
    echo "Finished converting: ${outfile}"
done