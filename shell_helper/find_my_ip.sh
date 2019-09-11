#! /bin/bash

my_network_adaptor=eth0

my_ip=$(ip -o -4 addr show | awk -v my_network_adaptor="$my_network_adaptor" '{ if ($2 == my_network_adaptor) print $4 }' | cut -d'/' -f 1)

if [ -z "$my_ip" ]; then
    echo "My IP of $my_network_adaptor Not Found"
    exit 1
else
    echo "My IP = $my_ip"
fi
