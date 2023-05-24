# Linux Typing Speed Monitor
A simple Linux program to record one's typing speed, meant to be run from the terminal.

### Set-Up
***
* **Install Dependancies** 
```
$ pip3 install pynput pyspellchecker statistic matplotlib scipy
```
&nbsp;
* **Set File Path** 
```
$ sudo nano wpm.sh
```
Replace ```main_path=.../Typing-Speed-Monitor/src``` with correct path.

&nbsp;
* **Add Alias**
```
$ sudo nano ~/.bashrc
```
Add ```alias wpm='location_of_file/wpm.sh'``` to last line

&nbsp;
* **Configure to Run on Startup**

Follow steps listed [here](https://www.baeldung.com/linux/run-script-on-startup#3-using-initd):
```
$ sudo nano /etc/init.d/wpm_wrapper.sh
```
```
! /bin/sh
# chkconfig: 345 99 10
case "$1" in
  start)
    # Executes our script
    sudo sh location_of_file/wpm.sh start
    ;;
  *)
    ;;
esac
exit 0
```
```
$ update-rc.d wpm_wrapper.sh defaults
```
***
### Features
Once Set-Up steps are completed, the following commands are available in the terminal.
```
$ wpm start

# starts new recording. 
# Does not check if a recording is already in progress
# It is not nessessary to run this manualy if it has been configured to run at startup
```
```
$ wpm lst

# lists all recordings in a verticle numbered list
```
```
$ wpm dp {int, filename, or empty}

# displays a graph of the recording given my the first parameter.
# The parameter may be the integer index of the file as given by $ wpm lst
# or the name of the file,
# Leaving the parameter blank displays the most recent recording.
```
```
$ wpm del {filename}

# deletes the given recording
```