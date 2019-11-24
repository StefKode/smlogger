#Stefan Koch, 2019

#ASKPASS=--ask-pass

all:
	ansible-playbook $(ASKPASS) -i hosts -s smlogger.yml
