from pathlib import Path
import openai
import json

def generate_audio(topic,text):

    speech_file_path = Path(__file__).parent /'audio'/ f"{topic.replace(' ','_')}.mp3"
    response = openai.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=text
    )
    response.write_to_file(speech_file_path)


if __name__=='__main__':
    configs = json.load(open('words.json','r'))
    for row in configs:
        topic = row['topic']
        print(topic)
        content = row['content']
        generate_audio(topic,content)