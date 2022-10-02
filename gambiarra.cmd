@echo off

wsl -e sh -c "sed -i 's/\r$//' $(wslpath \"%1\") && bash $(wslpath \"%1\")"

PAUSE