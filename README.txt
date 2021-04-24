REQUISITI AMAZON TIPS 

1) Utilizzare Chrome come browser.

2) Creare un bot telegram in modo semplice con bot father https://t.me/botfather e appuntare il TOKEN https ottenuto.



2) Creare un account affiliazione amazon-- https://programma-affiliazione.amazon.it/ (GRATUITO) con il profilo chrome di default (il primo mostrato quando lo si apre)
accertarsi che la barra SiteStripe si attiva/visibie sulla propria homepage amazon e su qualsiasi pagina di prodotti per ottenere il link.




3) Scaricare i driver chrome piu aggiornati tramite questo link https://sites.google.com/chromium.org/driver/

   Installare le seguenti librerie indicate anche nel file python:

pip install pyTelegramBotAPI
pip install selenium
pip install webdriver-manager



4) per vedere la posizione del profilo di installazione di chrome si puo scrivere sulla barra degli indirizzi 
   chrome://version/
   e sulla voce "percorso profilo" dovrebbe esserci un testo simile o uguale questo:  
    C:\Users\User\AppData\Local\Google\Chrome\User Data\Default   
    copiarlo e inserirlo nella riga 15 del codice (dopo "user-data-dir=") 

ricordare però di sostituire \ con \\ e di non includere il "\Default" finale. 
Al posto di "User" inserire il nome utente del proprio account per il percorso di installazione.


