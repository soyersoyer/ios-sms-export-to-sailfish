# Export iPhone SMS messages to Sailfish OS

## Steps
* Create a backup from your iPhone in the iTunes
* Get the ios-sms-export-to-sailfish.py
  * ```$ curl -O https://raw.githubusercontent.com/soyersoyer/ios-sms-export-to-sailfish/master/ios_sms_export_to_sailfish.py```
* Create a commhistory compatible json file from the message db
  * ```$ pyhton3 ios-sms-export-to-sailfish.py ~/Library/Application\ Support/MobileSync/Backup/<your last backup id>/3d/3d0d7e5fb2ce288813306e4d4636395e047a3d28 sms.json```
* Enable ssh in your sailfish device and enable the Developer mode
  * In the Settings > System > Developer tools pick the Developer mode and Remote connection
* Copy the sms.json to your sailfish device
  * ```$ scp sms.json nemo@<your-phone-ip>:~/```
* Ssh to your device
  * ```$ ssh nemo@<your-phone-ip>```
* Install the libcommhistory-qt5-tools
  * ```$ devel-su pkcon install libcommhistory-qt5-tools```
* Import the sms.json with commhistory-tool
  * ```$ commhistory-tool import-json sms.json```
* Done
