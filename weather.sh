#!/bin/bash
while true; do
    clear
    current_date_time=$(date)
    echo "Last Updated: $current_date_time"
    curl wttr.in
    sleep 3600
done