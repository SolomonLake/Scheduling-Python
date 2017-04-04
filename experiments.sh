#!/bin/sh
max=30
TIMEFORMAT=%R

#touch times.txt
rm values.txt


#First we vary number of students
echo 'Experiment 1 has 10 time slots, 12 rooms,  100 classes, and 1000
students \n'
echo 'Experiment 1' >> values.txt
#echo 'Experiment 1' >> times.txt

for i in `seq 1 $max`
do
    ./make_random_input.pl 12 100 10 1000 constraints_1.txt prefs_1.txt
    time python make_schedule.py constraints_1.txt prefs_1.txt schedule_1.txt
    ./exp_is_valid.pl constraints_1.txt prefs_1.txt schedule_1.txt >> values.txt
    echo '\t 4000' >> values.txt

    rm constraints_1.txt
    rm prefs_1.txt
    rm schedule_1.txt
done
echo '\n'

echo 'Experiment 2 has 10 time slots, 12 rooms,  100 classes, and 2000
students \n'
echo 'Experiment 2' >> values.txt
#echo 'Experiment 1' >> times.txt

for i in `seq 1 $max`
do
    ./make_random_input.pl 12 100 10 2000 constraints_1.txt prefs_1.txt
    time python make_schedule.py constraints_1.txt prefs_1.txt schedule_1.txt
    ./exp_is_valid.pl constraints_1.txt prefs_1.txt schedule_1.txt >> values.txt
    echo '\t 8000' >> values.txt

    rm constraints_1.txt
    rm prefs_1.txt
    rm schedule_1.txt
done
echo '\n'


echo 'Experiment 3 has 10 time slots, 12 rooms,  100 classes, and 4000
students \n'
echo 'Experiment 3' >> values.txt
#echo 'Experiment 1' >> times.txt

for i in `seq 1 $max`
do
    ./make_random_input.pl 12 100 10 4000 constraints_1.txt prefs_1.txt
    time python make_schedule.py constraints_1.txt prefs_1.txt schedule_1.txt
    ./exp_is_valid.pl constraints_1.txt prefs_1.txt schedule_1.txt >> values.txt
    echo '\t 16000' >> values.txt

    rm constraints_1.txt
    rm prefs_1.txt
    rm schedule_1.txt
done
echo '\n'


#Now vary number of classes
echo 'Experiment 4 has 10 time slots, 24 rooms,  200 classes, and 1000 students'
echo 'Experiment 4' >> values.txt
for i in `seq 1 $max`
do
    ./make_random_input.pl 24 200 10 1000 constraints_2.txt prefs_2.txt
    time python make_schedule.py constraints_2.txt prefs_2.txt schedule_2.txt
    ./exp_is_valid.pl constraints_2.txt prefs_2.txt schedule_2.txt >> values.txt
    echo '\t 4000' >> values.txt

    rm constraints_2.txt
    rm prefs_2.txt
    rm schedule_2.txt
done
echo '\n'

echo 'Experiment 5 has 10 time slots, 48 rooms,  400 classes, and 1000 students'
echo 'Experiment 5' >> values.txt
for i in `seq 1 $max`
do
    ./make_random_input.pl 48 400 10 1000 constraints_3.txt prefs_3.txt
    time python make_schedule.py constraints_3.txt prefs_3.txt schedule_3.txt
    ./exp_is_valid.pl constraints_3.txt prefs_3.txt schedule_3.txt >> values.txt
    echo '\t 4000' >> values.txt

    rm constraints_3.txt
    rm prefs_3.txt
    rm schedule_3.txt
done
echo '\n'

echo 'Experiment 6 has 10 time slots, 96 rooms,  800 classes, and 1000 students'
echo 'Experiment 6' >> values.txt
for i in `seq 1 $max`
do
    ./make_random_input.pl 96 800 10 1000 constraints_4.txt prefs_4.txt
    time python make_schedule.py constraints_4.txt prefs_4.txt schedule_4.txt
    ./exp_is_valid.pl constraints_4.txt prefs_4.txt schedule_4.txt >> values.txt
    echo '\t 4000' >> values.txt

    rm constraints_4.txt
    rm prefs_4.txt
    rm schedule_4.txt
done
echo '\n'

# This is varying students again
echo 'Experiment 7 has 10 time slots, 12 rooms,  100 classes, and 8000
students \n'
echo 'Experiment 3' >> values.txt
#echo 'Experiment 1' >> times.txt

for i in `seq 1 $max`
do
    ./make_random_input.pl 12 100 10 8000 constraints_1.txt prefs_1.txt
    time python make_schedule.py constraints_1.txt prefs_1.txt schedule_1.txt
    ./exp_is_valid.pl constraints_1.txt prefs_1.txt schedule_1.txt >> values.txt
    echo '\t 32000' >> values.txt

    rm constraints_1.txt
    rm prefs_1.txt
    rm schedule_1.txt
done
echo '\n'

echo 'Experiment 8 has 10 time slots, 12 rooms,  100 classes, and 16000
students \n'
echo 'Experiment 8' >> values.txt
#echo 'Experiment 1' >> times.txt

for i in `seq 1 $max`
do
    ./make_random_input.pl 12 100 10 16000 constraints_1.txt prefs_1.txt
    time python make_schedule.py constraints_1.txt prefs_1.txt schedule_1.txt
    ./exp_is_valid.pl constraints_1.txt prefs_1.txt schedule_1.txt >> values.txt
    echo '\t 64000' >> values.txt

    rm constraints_1.txt
    rm prefs_1.txt
    rm schedule_1.txt
done
echo '\n'

# and this is classes
echo 'Experiment 9 has 10 time slots, 192 rooms,  1600 classes, and 1000 students'
echo 'Experiment 9' >> values.txt
for i in `seq 1 $max`
do
    ./make_random_input.pl 192 1600 10 1000 constraints_4.txt prefs_4.txt
    time python make_schedule.py constraints_4.txt prefs_4.txt schedule_4.txt
    ./exp_is_valid.pl constraints_4.txt prefs_4.txt schedule_4.txt >> values.txt
    echo '\t 4000' >> values.txt

    rm constraints_4.txt
    rm prefs_4.txt
    rm schedule_4.txt
done
echo '\n'




