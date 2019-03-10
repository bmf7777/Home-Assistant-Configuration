# Home-AssistantConfig
My Home-Assistant and HADashboard configuration files
HA configuration uses packages to load yaml configuration files (packages: !include_dir_named packages)
conf directory is for AppDaemon to support HADashboard

My home automation system is based on HA running in an venv on an Intel NUC (Celeron) with 8Gb DRAM and 250Gb SSD with Ubuntu 18.x
I currently use 145 loaded components

1) my lighting is based on the UDI ISY994i using Insteon lighting control, garage door, fountains, outdoor lights and hidden door sensors (>150 instances)
2) security system is based on Blueiris with 25 cameras running on a Windows 10 Dell PC, doorbird, cameras are Foscam PTZ, Ubiquiti G3, G3 dome & micro along with reolink. I'm runing Tensorflow on four cameras to dectect people, cars and trucks. Various cameras are included in my HA lovelace dashboard and HADashboards mounted throughout my home. mqtt used for motion trigger. 
3) alarm system and doorlocks are monitored with Vera Edge with envisalink 4 connected to DSC alarm panel. I have 3 kwikset Z-wave doorlocks (one front door and two outdoor gates). Vera also controls AC/Heat shut off in event of open windows and doors .. I may move this automation to HA in the future. 
4) I used a second envisalink 4 to monitor open/close/motion events with HA since envisalink only support one instance connected at a time
5) I used wirelesstags to monitor for water leaks throughout my home and temp/hum for dataroom and wine storage (>22 instances)
6) car component for Tesla
7) nest component for 4 thermostats and 3 co/smoke detectors
8) pihole component for DNS AD blocking (pihole running on separate RPI3b)
9) doorbird DS101S doorbell camera component ... also, interfaces to blueiris and SIP phone with Obihan202
10) 3 logitech remotes 
11) 3 LG WebOS TVs (3 instances)
12) 4 media player components (3 denon, 1 JBL google home)
13) Roon Audio custom component (https://github.com/marcelveldt/roon-hass) ... roon core running on iMAC with 7 hifiberry AMP+ RPI3B outdoor zones and 6 indoor zones (denon/mkii, NAD and mcintosh)
14) presence detection using bayesian component, inputs include life360 custom_component, UBNT Unifi AP device_tracker, BT device_tracker, ping device_tracker and iOS device_tracker
15) generator monitor using (https://github.com/jgyates/genmon.git) for generac 11kW along with mqtt device messages
16) rainmachine sprinker controller component (two instances)
17) vacuum component with two Roomba vacuums
18) mail and package automation via (https://github.com/moralmunky/HomeAssistant_Mail_Card.git)
19) Using mosquitto mqtt broker running on HA host ... i found included mqtt broker used large amounts of CPU cycles
20) APC UPS monitoring with HA component and local daemon 
21) Netdata component (https://github.com/netdata/netdata.git) for server monitoring 
22) Appdademon for HADashboards...currently using four wall mounted panels. each panel is an iPad Mini 4 with vidabox holder and slim mount (https://www.vidabox.com/kiosks/vidamount-secure-fixed-wall-ipad-mini-4-tablet-enclosure-mount-light-grey.html) ... panels are located above an existing wall switch to allow for added power outlet (using usb enabled ac outlet). also supporting UHD TV with custom dashboards.
23) weather: darksky, Rainwise MKIII weather station with custom extraction script, netatmo indoor weather station
24) awair component for indoor AQI (2 instances) along with AQI component to monitor local area air quality indicator
25) Speedtest component to check internet access performance
26) Ping component to check for local servers on-line
27) Pentair Pool control ... installed Pool Control for Pentair Intellitouch & Easytouch by (http://www.autelis.com/) located inside high voltage outdoor controller box, interfaces as a remote keypad (self powered via RS-422) and connect via Ethernet Cable ... many templates and scripts required for lovelace badge
28) Insteon garage door control and cover templates
29) Power monitoring via Rainforest Automation Eagle-200...using local API to extract instantaneous_demand with scripts and templates
30) Solar monitoring with Enphase energy monitor component 
31) Google calendar, date and time
32) Using Ubiquiti ER-8, 12 APs (3 outdoor, 9 indoor) with layer-3 switching (8 switches), vlan for Games boxes that require UPNP and guest network
33) will upload shell-scripts and python scripts after reviewing for embedded passwords

