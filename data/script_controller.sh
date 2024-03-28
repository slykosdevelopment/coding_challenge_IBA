#!/bin/bash


if [ "$1" == "create_database" ]; then
    python3 createDatabase.py

elif [ "$1" == "launch_program" ]; then
    uvicorn main:app --host 0.0.0.0 --port 8000

else
    echo "specify option"
fi