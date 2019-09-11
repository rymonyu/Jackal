#! /bin/bash

while read -r my_ip
do
    echo "scan for $my_ip"
    scan_result=$(nmap -sP -oG - $my_ip | grep Jackal)
    if [ ! -z "$scan_result" ]; then
        echo "$scan_result"
        jackal_ip=$(echo "$scan_result" | awk '{ print $2 }')
    fi
done < <(ip -o -4 addr show | awk '{ if ($2 != "lo") print $4 }')

if [ -z "$jackal_ip" ]; then
    echo "Jackal Not Found"
    exit 1
else
    echo "Jackal IP = $jackal_ip"
    ssh administrator@$jackal_ip
fi
