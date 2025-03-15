from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

# generate speech by cloning a voice using default settings
tts.tts_to_file(text="The Coca Cola company is not happy with me--that's okay, I'll still keep drinking that garbage.",
                file_path="output/out.wav",
                speaker_wav="voices/trump.wav",
                language="en",
                speed=1.8,
                split_sentences=False
                )

print('STOP')