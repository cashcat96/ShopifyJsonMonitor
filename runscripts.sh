#!/bin/bash

dir="<directory which houses all the scripts>"

cd $dir

python3 productpuller_new.py

python3 compareproduct.py

sleep 1

mv products_new.txt products_old.txt
