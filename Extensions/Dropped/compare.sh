#!/bin/sh
echo 'Results without dropped classes:'
../../is_valid.pl no_drops_cons.txt no_drops_prefs.txt no_drops_sched.txt

echo '\n Results with dropped classes:'
../../is_valid.pl hav_cons.txt hav_prefs.txt hav_sched.txt
