location="/home/v2ray"
loc_port=1070

cd $location

# Install snapd
sudo apt update
sudo apt install nginx -y
sudo apt install snapd -y
sudo snap install core; sudo snap refresh core
sudo apt-get remove certbot
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo snap set certbot trust-plugin-with-root=ok
sudo snap install certbot-dns-cloudflare
git clone https://github.com/v2fly/fhs-install-v2ray
git clone https://github.com/arcdetri/sample-blog

sudo certbot renew --dry-run

sudo ufw allow 'Nginx HTTP'

systemctl enable nginx
systemctl start nginx


bash ./fhs-install-v2ray/install-release.sh 
systemctl enable v2ray

passwd=$(openssl rand -base64 24)
port=$(shuf -i 20000-50000 -n 1)
uuid=$(cat /proc/sys/kernel/random/uuid)

printf '
{
    "log": {
        "loglevel": "warning"
    },
    "inbounds": [
        {
            "port": 443,
            "protocol": "vless",
            "settings": {
                "clients": [
                    {
                        "id": "' \
$uuid \
'",
                        "level": 0,
                        "email": "kazukiamakawa@gmail.com"
                    }
                ],
                "decryption": "none",
                "fallbacks": [
                    {
                        "dest": 80
                    }
                ]
            },
            "streamSettings": {
                "network": "tcp",
                "security": "tls",
                "tlsSettings": {
                    "alpn": [
                        "http/1.1"
                    ],
                    "certificates": [
                        {
                            "certificateFile": "/path/to/fullchain.crt", // 换成你的证书，绝对路径
                            "keyFile": "/path/to/private.key" // 换成你的私钥，绝对路径
                        }
                    ]
                }
            }
        }
    ],
    "outbounds": [
        {
            "protocol": "freedom"
        }
    ]
}
'
> /usr/local/etc/v2ray/config.json

printf '
{
    "log": {
        "loglevel": "warning"
    },
    "inbounds": [
        {
            "port": 1090,
            "listen": "127.0.0.1",
            "protocol": "socks",
            "settings": {
                "udp": true
            }
        }
    ],
    "outbounds": [
        {
            "protocol": "vless",
            "settings": {
                "vnext": [
                    {
                        "address": "www.stlaplace.com",
                        "port": 443,
                        "users": [
                            {
                                "id": "' \
$uuid \
'",
                                "encryption": "none",
                                "level": 0
                            }
                        ]
                    }
                ]
            },
            "streamSettings": {
                "network": "tcp",
                "security": "tls"
            }
        }
    ]
}
'
systemctl start v2ray
