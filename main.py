import os
import whisper

LANGUAGE = "es"
ROOT_PATH = "assets"
TRANSCRIBER = whisper.load_model("medium")

def transcribe_audio(filename: str) -> str:
    audio_path = os.path.join(
      os.path.dirname(__file__), os.path.join(ROOT_PATH, filename)
    )
    try:
        if not os.path.exists(audio_path):
          print(f"Archivo de audio no encontrado: {audio_path}")
          return ''
        result = TRANSCRIBER.transcribe(audio_path, language=LANGUAGE, fp16=False , word_timestamps=False)
        return result
    except Exception as e:
        print(f"Error al transcribir el audio {audio_path}: {e}")
        return ''

if __name__ == "__main__":

  filename = ""
  while(not filename.strip()):
    filename = input("Nombre del archivo: ")

  text = ""
  text_path = "{}.txt".format(filename.split(".")[0])
  try:
    text = transcribe_audio(filename)
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
