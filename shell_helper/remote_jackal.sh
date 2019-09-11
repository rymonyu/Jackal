#! /bin/bash

my_network_adaptor=eth0

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
    return 1
else
    echo "Jackal IP = $jackal_ip"
fi

my_ip=$(ip -o -4 addr show | awk -v my_network_adaptor="$my_network_adaptor" '{ if ($2 == my_network_adaptor) print $4 }' | cut -d'/' -f 1)

if [ -z "$my_ip" ]; then
    echo "My IP Not Found"
    return 1
else
    echo "My IP = $my_ip"
fi

export ROS_MASTER_URI="http://$jackal_ip:11311"
export ROS_IP=$my_ip

echo "ROS_MASTER_URI=$ROS_MASTER_URI"
echo "ROS_IP=$ROS_IP"
