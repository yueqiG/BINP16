management advice:

no spaces in filenames or foldernames

#tweaking file formats:

cat my file.fna | tr acgtACGT tgcaTGCA > mynewfile.fna

cat myfile.csv | sed 's/,/ /' > mynewfile.txt 

#only change the first one

cat myfile.csv | sed 's/,/ /g' > mynewfile.txt 

##loops with a numberlist file 

for i in$(cat number.list)

do

echo "welcome $i times"

done

#loops 

for i in 1 2 3 4 5 hej

do

echo "welcome $i times"

done

while loops

#shell script:filename.sh

#count characters in file

cat mynewfile.fna | while read line; do echo -n $line | wc -c;done

r  #read

w  #write

x  #exacute

echo -e "acg\ngc\nattta" > file.fna

cat file.fna | while read line; do echo $line;done

