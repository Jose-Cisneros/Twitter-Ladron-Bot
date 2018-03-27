# Twitter-Ladron-Bot
Bot de Twitter que roba twits y seguidores a cuentas especificadas.

Bot simple escrito en un rato libre por diversión, hecho en python usando la libreria Tweepy(www.tweepy.org/)

El funcionamiento es simple, primero se registra la api con las credenciales de la cuenta con la API

Después se cargan cuentas "objetivo" en un arreglo, se elige una al azar y se copia uno de los últimos 20 twitts del usuario

A su vez existe la chance de que le de follow desde 7 a 15 personas que sigan a la cuenta "victima".

Se eligió ese número bajo para evitar de que twitter bloquee el bot por spam.

A su vez al ejecutarse le da unfollow a todas las cuentas que no hicieron follow-back

El script está pensado para correr una vez al día, el mismo ahora está alojado en www.pythonanywhere.com con el plan gratuito

El bot está creado con el fin de aprender a usar la API de Twitter y para ver si realmente la gente lo sigue e interactúa con él.

Una cuenta que está utilizando el script es: https://twitter.com/soyunfernet_


