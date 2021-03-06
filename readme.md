
# ISP WATCHDOG
 Ideally, you would put this in a Raspberry Pi. However, it supports on anything that can run Python and pip. 
 This program will ping three different IP addresses and get the average RTT value in milliseconds. 
 The values are then stored onto Ubidots for record keeping and analysis. 
 
 It is recommended that you install this under root user. This is because to send an ICMP packet, you need root privilege. 

# Requirements
 - Ubidots account (app.ubidots.com)
 - Pipenv
 - Root privileges (to send out ping/ICMP packets)
 
# Installation
### Part 1
1. Clone the repository.
2. Run `pipenv install` . This will install all the Python modules that the program will need. 
3. Login into your Ubidots account and copy the API key. 
4. Create a device and FOUR variables with one for the Hearbeat variable (choose the default variable if you are not sure) .
5. Copy down all the variable ID.
6. Edit the configuration file by typing `nano config.py` (refer to config.py.example)
7. Insert the appropriate API key and variable ID.
8. Test the program by typing `python isp_report.py`
9. Your results should be available on the dashboard on Ubidots.

![Variables you need](https://i.imgur.com/5rOiDhj.jpg)

### Part 2
Now we need to make it run periodically. Since it needed root privilege, you need to make sure to run it as root. 
1. Review the `cron.txt` and edit the path to point to the program. Also, edit the interval as you like. The deault is set to report every minute. 
2. Run `crontab cron.txt` to install the cronjob from the cron.txt into your machine. 
3. Observe Ubidots and make sure that your data is coming in. 

### Part 3 
To detect downtime and visualize your data, you would need to configure Ubidots dashboard a bit. 
1. Go to the dashboard section and create three graphs. This will be for your RTT value visualizations. 
2. Go to Events section, configure so that if the Heartbeat variable is inactive for X minutes, set itself to ZERO. 

![Variables you need](https://i.imgur.com/4RXZxbM.jpg)
![Variables you need](https://i.imgur.com/glesQr5.jpg)
