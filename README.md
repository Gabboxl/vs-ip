# vs-ip: Cambia automaticamente indirizzo IP con la Vodafone Station Revolution
![vs-ip](https://i.imgur.com/JDJtWA3.png)

# Installazione (compilazione)
Requisiti
-------------
Setuptools & Wheel: `sudo python -m pip install --upgrade pip setuptools wheel`

Installa i pacchetti `firefox geckodriver` (arch: `sudo pacman -S firefox geckodriver` 
altri systems:  `sudo apt install firefox` (per geckodriver -> https://github.com/mozilla/geckodriver/releases -> scarica versione x il tuo systems -> estrai il driver -> trasportalo in PATH)

Compilazione
------------
1) klona il project's
2) build: `python setup.py bdist_wheel`
3) installa con pip's::::  `sudo python -m pip install dist/vs_ip-0.2.5-py3-none-any.whl`

OPPURE;.,,

sckript comingsoon

Avviare
-------
`vs-ip`

Cambiare configurazione
-----------------------
`vs-ip setup`

