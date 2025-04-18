import os
import whisper
from argparse import ArgumentParser

def transcribe_audio(filename: str, transcriber, language, root_path) -> str:
  audio_path = os.path.join(
    os.path.dirname(__file__), os.path.join(root_path, filename)
  )
  try:
    if not os.path.exists(audio_path):
      print(f"Archivo de audio no encontrado: {audio_path}")
      return ''
    print("Transcribiendo el audio...")
    result = transcriber.transcribe(audio_path, language=language, fp16=False , word_timestamps=True)
    return result
  except Exception as e:
      print(f"Error al transcribir el audio {audio_path}: {e}")
      return ''
    
def main(hparams):

  model = whisper.load_model(hparams.model)
  filename = ""

  while(not filename.strip()):
    filename = input("Nombre del archivo: ")

  text = ""
  text_path = "{}.txt".format(filename.split(".")[0])
  try:
    text = transcribe_audio(filename, model, hparams.language, hparams.path)
    try:
      if text:
        with open(text_path, "w", encoding="utf-8") as text_file:
          for segment in text["segments"]:
            text_file.write(segment["text"]+"\n")
        print(f"Audio transcrito.")
    except Exception as e:
      print(f"Error al almacenar el texto: {e}")
  except Exception as e:
    pass

if __name__ == "__main__":

  parser = ArgumentParser()
  parser.add_argument("--model", default = "medium", type=str, help="Modelo de Whisper a usar")
  parser.add_argument("--language", default = "es", type=str, help="Idioma a usar")
  parser.add_argument("--path", default = "assets", type=str, help="Ruta de los archivos de audio")

  args = parser.parse_args()
  main(args)
