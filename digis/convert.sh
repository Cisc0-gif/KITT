#! /bin/bash
figlet -f slant "convert d2s"
echo ================================================================
read -p 'Enter filename file.txt|.duck: ' filename
java -jar duckencoder.jar -i $filename -o inject.bin -l de
mv inject.bin duck2spark
cd duck2spark
python duck2spark.py -i inject.bin -l 1 -f 2000  -o $filename.ino
