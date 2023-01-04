#!/bin/bash
sudo nohup python bot/rat.py >database/bot.log &
tail -f database/bot.log