#!/usr/bin/env bash

data_dir=/data/team-project/genres/

cd "${data_dir}"
for i in `find . -name \*.au -print`
do
    old_file="${i}"
    new_file="${old_file%.*}.wav"
    if ! [ -s ${new_file} ] ; then
        echo "Converting ${old_file} to ${new_file}"
        sox ${old_file} ${new_file}
    else
        echo "Already converted ${old_file}"
    fi
done
