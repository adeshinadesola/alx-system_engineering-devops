# Firewall Configuration - README

This repository contains the solution for configuring a firewall using UFW (Uncomplicated Firewall) to block all incoming traffic except for specific TCP ports. The configuration is applied to the web-01 server, as per the project requirements.

## Requirements

- UFW (Uncomplicated Firewall) should be installed on the server.
- The following TCP ports should be allowed for incoming traffic:
  - Port 22 (SSH)
  - Port 443 (HTTPS SSL)
  - Port 80 (HTTP)

## Instructions

To configure the firewall and apply the necessary rules, follow these steps:

1. SSH into the web-01 server.
2. Install UFW if it's not already installed: `sudo apt-get install ufw`.
3. Set the default incoming policy to deny all traffic: `sudo ufw default deny incoming`.
4. Allow incoming SSH connections on port 22: `sudo ufw allow 22/tcp`.
5. Allow incoming HTTPS connections on port 443: `sudo ufw allow 443/tcp`.
6. Allow incoming HTTP connections on port 80: `sudo ufw allow 80/tcp`.
7. Enable UFW to start blocking incoming traffic according to the rules: `sudo ufw enable`.
8. Check the status of UFW to verify that the rules are applied correctly: `sudo ufw status`.

Please note that the above instructions are specific to the web-01 server. Feel free to adapt them if you want to apply the configuration to other servers (lb-01, web-02) as well.

## Support

If you have any questions or issues regarding this firewall configuration, please feel free to reach out.
