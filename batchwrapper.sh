#!/bin/bash

# Make a symlink to this script
# (or copy it) to /app/bin/batchwrapper.

source /etc/profile.d/fh_path.sh

#
# remove local user-customisations to python behavior
unset PYTHONPATH
unset PYTHONUSERBASE
unset PYTHONHOME

PYTHON=python
SCRIPT=/app/local/fredhutch_batch_wrapper/env/bin/batchwrapper

ml Python/3.6.4-foss-2016b-fh1
$PYTHON $SCRIPT $@
