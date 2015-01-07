#!/usr/bin/env bash

# This was a sample shell provisioner for Vagrant.
# Just leaving it here as an example.

yum update -y

yum install httpd -y

if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi
