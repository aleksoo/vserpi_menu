# VSERPi Menu

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](*usage)
* [Adding your own software to the list](#adding-your-own-software-to-the-list)
* [Future plans](#future-plans)

## General info

This little piece of software was written to handle selection of VSERPi software you want to run at the boot. It handles version 1.5 of the image. For more info about images and software please refer to Andrei's site: 

https://andreijaycreativecoding.com/VSERPI-hardware-and-images

## Technologies
  * Python 3.6
  * pyGame

## Setup
  Firstly, clone this repository.
  ```
  git clone git@github.com:aleksoo/vserpi_menu.git
  ```
  
  Secondly, download dependencies (run it from cloned "verspi_menu" directory):
  ```
  make init
  ```
  
  Thirdly, modify .bashrc (using any text editor you want, nano, pico, gnome, vim) to run this script instead of directly software:
  ```
  nano /home/pi/.bashrc
  ```
  
  Scroll down (tip: use "Page Down" key on your keyboard) and apply hash sign (#) before "cd" line (this will prevent excecution at the boot, so called "commenting code") and add different path:
  ```
  cd /home/pi/vserpi_menu
  #cd /home/pi/openFrameworks/apps/myApps/WAAAVE_POOL_4_5
  make run
  ```
  This way they won't execute at the boot. Note that path might vary depending on when you cloned repository. 
  
  Optionally (and recommended by me for maximum usage pleasure), you can change settings in "raspi-config" to use console boot instead of GUI:  
  ```
  sudo raspi-config
  ```
  
  then navigate using keyboard:
  ```
  3 Boot Options -> B1 Desktop / CLI -> B2 Console Autologin
  ```
  
  Now try rebooting and you should see menu at the screen.
  
  ![image](https://user-images.githubusercontent.com/32747300/153300410-0763f091-e733-4454-94b5-2406a2d94234.png)

  
## Usage
  It's late and I should go to sleep, GUI should be clear enough to use. 
  < , > - change "page" of software (only 5 from list is shown on the screen)
  A, B, C, D, E buttons - run software from the list on the right  
  
## Adding your own software to the list
  TBD, but if you're savy enough - follow existing scripts from "running_scripts" directory and add entry to the "softwareList" list in "ChoiceHandler.py". Should be pretty simple tho.
  
## Future plans
  I want to fully integrate touchosc2midi into this, so you can use VSERPi with your phone instead of Korg nanoKontrol controller (hence why there is "0" entry on the list).
