#!/bin/bash
cd ../v4l2loopback
make && sudo make install
sudo depmod -a
cd ../v4l2loopback
sudo modprobe v412loopback