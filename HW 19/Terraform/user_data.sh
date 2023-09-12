#!/bin/bash
echo "Copying the SSH Key to the server"
echo -e "ssh-rsa key" >> /home/ubuntu/.ssh/authorized_keys
EOF
