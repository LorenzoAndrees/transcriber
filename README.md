# Transcriber

## Correr el script

Ubicarnos, a través de la terminal, en la carpeta con los archivos.

Usar ls para ver las carpetas que hay en donde nos encontramos:

```console
ls
```

Usar "cd" para movernos a la carpeta que queremos. Por ejemplo, a la carpeta llamada "transcode":

```console
cd transcode-main
```

Una vez estando en la carpeta con el código, se debe ejecutar el siguiente comando para correr el script:

```console
python3 main.py
```

## Resultado

Una vez finalizada la transcripción, el script genera un archivo de texto con el mismo nombre del archivo de audio.

## Consideraciones

- Asegurarse de que los audios que se quieren transcribir estén dentro de la carpeta assets.
- Si el script se ejecuta por primera vez, se descargará el modelo de whisper.
- Se recomienda utilizar nombres simples de audios (evitando "/") ya que se debe ingresar el nombre completo del archivo de audio.
- El archivo de texto generado transcribe el audio en múltiples líneas, ya que whisper reconoce ventanas de tiempo del diálogo/la conversación.
