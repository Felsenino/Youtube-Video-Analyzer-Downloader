# Youtube-Video-Analyzer-Downloader

# ITALIANO
Ho messo insieme due librerie che non avevo mai usato prima (TextBlob e PyTube) e l'API di Google "YouTube Data API v3" per creare uno strumento utile quotidianamente.
Chiede in input l'URL di un video YouTube e restituisce titolo, numero di visualizzazioni e la polarita' media dei commenti grazie a TextBlob. Quest'ultima non e' ovviamente accurata al 100% per via del funzionamento della libreria stessa, ma aggiunge comunque una feature interessante.
Il tool infine permette all'utente di scegliere se scaricare il video in locale.

+ Per il corretto funzionamento del programma bisogna inserire all'interno del codice sorgente la propria chiave API nella linea 7, DEVELOPER_KEY="".


# ENGLISH 
I put together two libraries I have never used before (TextBlob and PyTube) and Google's API "YouTube Data API v3" to create an everyday useful tool.
It request as an input a YouTube video URL and prints title, views and the average comments polarity thanks to TextBlob. The average polarity isn't 100% accurate due to the library itself, but still adds an interesting new feature.
This tool at the end allows the user to choose if and where download the video.
 
+ In order to get the program to work you have to insert in the code you API Key at line 7, DEVELOPER_KEY="".
