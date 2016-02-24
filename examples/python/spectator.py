h#!/usr/bin/python

#####################################################################
# This script presents SPECTATOR mode. In SPECTATOR mode you play and
# your agent can learn from it.
# gguration is loaded from "../config/<SCENARIO_NAME>.cfg" file.
# 
# To see the scenario description go to "../../scenarios/README"
# 
#####################################################################
from __future__ import print_function
from vizia import *
from time import sleep

game = DoomGame()

# Choose scenario config file you wish to watch.
# Don't load two configs cause the second will overrite the first one.
# Multiple config files are ok but combining these ones doesn't make much sense.

#game.load_config("../config/basic.cfg")
#game.load_config("../config/deadly_corridor.cfg")
game.load_config("../config/deathmatch.cfg")
#game.load_config("../config/defend_the_center.cfg")
#game.load_config("../config/defend_the_line.cfg")
#game.load_config("../config/health_gathering.cfg")
#game.load_config("../config/my_way_home.cfg")
#game.load_config("../config/predict_position.cfg")
#game.load_config("../config/take_cover.cfg")

game.set_screen_resolution(ScreenResolution.RES_640X480)
# Adds mouse support for fun:
game.add_available_button(Button.TURN_LEFT_RIGHT_DELTA)
#TODO up and down doesnt work doesn't work!
#game.add_available_button(Button.LOOK_UP_DOWN_DELTA)

# Enables spectator mode, so you can play. Sounds strange but it is agent who is supposed to watch not you.
game.set_window_visible(True)
game.set_mode(Mode.SPECTATOR)
# Add some mouse support for fun.
# TODO game.add_available_button(Button.???)

game.init()

episodes = 10
print("")
for i in range(episodes):
	print("Episode #" +str(i+1))
	
	game.new_episode()
	while not game.is_episode_finished():
		
		s = game.get_state()
		img = s.image_buffer
		misc = s.game_variables

		game.advance_action()
		a = game.get_last_action()
		r = game.get_last_reward()
		
		print("state #"+str(s.number))
		print("game variables: ", misc)
		print("action:", a)
		print("reward:",r)
		print("=====================")

	
	print("episode finished!")
	print("summary reward:", game.get_summary_reward())
	print("************************")
	sleep(2.0)

game.close()
