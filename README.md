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

Para correr el script con un modelo en específico usar --model. Por ejemplo, para correrlo con el modelo turbo usar:

```console
python3 main.py --model turbo
```

Los modelos son los siguientes (ordenados de menos inteligente a más inteligente):
| Modelo | Parámetros | Velocidad |
|----------|----------|----------|
| tiny | 39 millones | ~10x |
| base | 74 millones | ~7x |
| small | 244 millones | ~4x |
| medium | 769 millones | ~2x |
| large | 1550 millones | 1x |
| turbo | 809 millones | ~8x |

(El modelo turbo es el más eficiente en términos de inteligencia/velocidad).

## Resultado

Una vez finalizada la transcripción, el script genera un archivo de texto con el mismo nombre del archivo de audio.

## Consideraciones

- Asegurarse de que los audios que se quieren transcribir estén dentro de la carpeta assets.
- Si el script se ejecuta por primera vez, se descargará el modelo de whisper.
- Se recomienda utilizar nombres simples de audios (evitando "/") ya que se debe ingresar el nombre completo del archivo de audio.
- El archivo de texto generado transcribe el audio en múltiples líneas, ya que whisper reconoce ventanas de tiempo del diálogo/la conversación.
