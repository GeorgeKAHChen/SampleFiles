#!/bin/bash
#==========================================================
#CONFIG AREA
mkdir /home/shadowsocksr
location="/home/shadowsocksr"
loc_port=1070
#You can setting the install location here
#If the location is null, the SSR will be installed in your command working location
#==========================================================
pwd > current_location



echo "===================Pre-treatment===================="
#Determine the location if using 
if [ -z "$location" ]; then
    location=$(pwd)
fi
#Add "/"sign after location 

str1="${location:-1}"
str2="/"
if [ "$str1" != "$str2" ]; then
    location="${location}/"
fi

mkdir $location







echo "============Install tools, SSR and Cover============"
#Normal package install 
sudo apt update && sudo apt upgrade -y
sudo apt install wget zip unzip python-m2crypto libsodium23 git apache2 openssl -y

cd $location

#SSR download
git clone https://github.com/shadowsocksrr/shadowsocksr.git

#Sample website download
git clone https://github.com/arcdetri/sample-blog.git


 



echo "================Implement the Cover================"
#Cover website install and delete tmp files
sudo cp -rf sample-blog/html/* /var/www/html/
rm -rf sample-blog/





echo "=================Implement the SSR================="
#Initial
cd shadowsocksr
sudo bash initcfg.sh

#Get random passwd and port
passwd=$(openssl rand -base64 24)
port=$(shuf -i 20000-50000 -n 1)

#Write the config file
printf '%s%s%s%s%s' '{
    "server": "0.0.0.0",
    "server_ipv6": "::",
    "server_port": '\
$port \
',
    "local_address": "127.0.0.1",
    "local_port": 1080,

    "password": "' \
$passwd \
'",
    "method": "aes-128-ctr",
    "protocol": "auth_aes128_md5",
    "protocol_param": "",
    "obfs": "tls1.2_ticket_auth_compatible",
    "obfs_param": "",
    "speed_limit_per_con": 0,
    "speed_limit_per_user": 0,

    "additional_ports" : {}, 
    "additional_ports_only" : false,
    "timeout": 120,
    "udp_timeout": 60,
    "dns_ipv6": false,
    "connect_verbose_info": 0,
    "redirect": "",
    "fast_open": false
}
' > user-config.json


#Creative A Service
sudo rm -rf /etc/systemd/system/shadowsocksr.service
printf "%s%s%s%s%s%s%s%s%s" "[Unit]
Description=ShadowsocksR server
After=network.target
Wants=network.target

[Service]
Type=forking
PIDFile=/var/run/shadowsocksr.pid
ExecStart=/usr/bin/python3 "\
$location \
"shadowsocksr/shadowsocks/server.py --pid-file /var/run/shadowsocksr.pid -c "\
$location \
"/shadowsocksr/user-config.json -d start
ExecStop=/usr/bin/python3 "\
$location \
"/shadowsocksr/shadowsocks/server.py --pid-file /var/run/shadowsocksr.pid -c "\
$location \
"/shadowsocksr/user-config.json -d stop
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=always

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/shadowsocksr.service


#Server Start
sudo systemctl stop shadowsocksr.service
sudo systemctl enable shadowsocksr.service
sudo systemctl start shadowsocksr.service
sudo ss -tulpn | grep 80


#Get IP
ifconfig | grep Bcast > tmpoutput
list=$(cat tmpoutput)

declare -a arr
index=0
for i in $list
do
    arr[$index]=$i
    let "index+=1"
done

ip=${arr[1]}
rm -rf tmpoutput





#Final output
echo "




"
printf '%s%s%s%s%s%s%s%s%s' '{
    "server": "'\
$ip \
'",
    "server_ipv6": "::",
    "server_port": '\
$port \
',
    "local_address": "127.0.0.1",
    "local_port": '\
$loc_port \
',

    "password": "' \
$passwd \
'",
    "method": "aes-128-ctr",
    "protocol": "auth_aes128_md5",
    "protocol_param": "",
    "obfs": "tls1.2_ticket_auth_compatible",
    "obfs_param": "",
    "speed_limit_per_con": 0,
    "speed_limit_per_user": 0,

    "additional_ports" : {}, 
    "additional_ports_only" : false,
    "timeout": 120,
    "udp_timeout": 60,
    "dns_ipv6": false,
    "connect_verbose_info": 0,
    "redirect": "",
    "fast_open": false
}
'
echo "//config file end"


















