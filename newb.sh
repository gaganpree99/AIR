#!/bin/bash


echo "convert to flac"
rec if.flac rate 16000 silence 1 1 25% 1 1.0 10%

echo "Processing..."
wget -q -U "Mozilla/5.0" --post-file if.flac --header "Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com/speech-api/v2/recognize?lang=en-us&client=chromium&key=AIzaSyDIF3dlJlnAs9VYq0SmBCPE9FpVOuofyto" | cut -d\" -f8 >stt1.txt 
echo -n "You Said: "
cat stt1.txt
python c.py "$(cat stt1.txt)" 



