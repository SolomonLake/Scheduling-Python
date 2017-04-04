#!/bin/sh
echo 'Results without majors'
cd ../
python get_haverford_info.py haverfordEnrollmentDataS14.csv prefs1.txt constraints1.txt
python make_schedule.py constraints1.txt prefs1.txt schedule1.txt
../is_valid.pl constraints1.txt prefs1.txt schedule1.txt

rm constraints1.txt
rm prefs1.txt
rm schedule1.txt

cd Majors/
echo '\n Results with majors'
python get_haverford_info.py haverfordEnrollmentDataS14.csv prefs1.txt constraints1.txt
python ../get_haverford_info.py haverfordEnrollmentDataS14.csv legit_prefs.txt legit_cons.txt
python make_schedule.py constraints1.txt prefs1.txt schedule1.txt
../../is_valid.pl legit_cons.txt legit_prefs.txt schedule1.txt

rm constraints1.txt
rm prefs1.txt
rm schedule1.txt
rm legit_prefs.txt
rm legit_cons.txt
