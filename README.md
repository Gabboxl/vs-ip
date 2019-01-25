# vs-ip: Cambia automaticamente indirizzo IP con la Vodafone Station Revolution
![vs-ip](https://i.imgur.com/JDJtWA3.png) (il program's potrebbe esere diverso)

# Installazione (compilazione)
Requisiti
-------------
* Setuptools & Wheel: `sudo python -m pip install --upgrade pip setuptools wheel`

* I pacchetti `firefox` e `geckodriver`: 
Arch e derivati (es. Manjaro)= `sudo pacman -S firefox geckodriver`; 
altri systems (es. debian): `sudo apt install firefox` POI -> *geckodriver* -> https://github.com/mozilla/geckodriver/releases -> scarica versione x il tuo systems -> estrai il driver -> trasportalo in PATH

Compilazione + installazione
------------
1) klona il project's (`git clone https://github.com/Gabboxl/vs-ip.git`) ((((entra poi nella cartella))))
2) builda: `python setup.py bdist_wheel`
3) installa con pip's::::  `sudo python -m pip install dist/vs_ip-0.2.5-py3-none-any.whl`

OPPURE;.,,

sckript comingsoon

Avviare
-------
`vs-ip`

Cambiare configurazione
-----------------------
`vs-ip setup`

