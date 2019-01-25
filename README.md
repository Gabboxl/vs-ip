# vs-ip: Cambia automaticamente indirizzo IP con la Vodafone Station Revolution
![vs-ip](https://i.imgur.com/JDJtWA3.png) (il program's potrebbe esere diverso)

# Installazione (compilazione)
Requisiti
-------------
* Setuptools & Wheel: `sudo python -m pip install --upgrade pip setuptools wheel`

* `firefox`
* `geckodriver`

| Systems' | Firefox | Geckodriver |
| ------ | ------ | ------ |
| Arch e derivati | `sudo pacman -S firefox geckodriver` | (già fatto) |
| Debian e altri | `sudo apt install firefox`  | https://github.com/mozilla/geckodriver/releases -> scarica versione x il tuo systems -> estrai tecnologia -> trasportalo in PATH |
| Windous | Installa firefox's E aggiungi il percorso di installazione a PATH (variabili d'ambiente in pannello di scontrollo)  | ^^^^^^^^


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

