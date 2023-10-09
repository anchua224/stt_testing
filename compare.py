import os
import sys
import time
import json

def compare(transcript_path, captions_path):
    if os.path.exists(transcript_path):
        print("Getting " + os.path.basename(transcript_path) + " transcript file...")
    if os.path.exists(captions_path):
        print("Getting " + os.path.basename(captions_path) + " captions file...")
    with open(transcript_path, "r") as file:
    # Read the entire contents of the file into a string
        transcript = file.read()
    transcript = transcript.replace(',','')
    transcript = transcript.replace('.','')
    transcript = transcript.replace('\'', '')
    transcript = transcript.replace('-', ' ')
    transcript = transcript.lower()
    captions = ""
    with open(captions_path, "r") as file:
    # Read the entire contents of the file into a string
        line = file.readline()
        while line:
            # {'text': 'tonight the historic case former', 'start': 1.36, 'duration': 3.88}
            # Get first property in line : {'text': 'tonight the historic case former'
            text = line.split(',')[0]
            # Get text in line:  'tonight the historic case former'
            text = text.split(':')[1]
            text = text.replace('\'', '')
            text = text.replace('\"', '')
            text = text.replace('-', ' ')
            captions += text
            line.strip()
            # print(line.strip())  # Use .strip() to remove newline characters
            line = file.readline()
    captions = captions.lower()
    print(captions)
    print()
    print(transcript)
    count = 0
    transcript_words = transcript.split()
    caption_words = captions.split()
    for i in range(len(transcript_words)):

        str1 = transcript_words[i]
        str2 = caption_words[i]
        if  str1 == str2:
            print("Mathing: " + str1 + " - " + str2)
            count+=1
        else:
            str2 = caption_words[i+1]
            if (str1 == str2):
                count +=1
                print("Mathing: " + str1 + " - " + str2)
            else:
                print("Doesn't match: " + str1 + " - " + str2)
    print(f"Correct words: {count}")
    print(f"Transcript words: {len(transcript_words)}")
    print(f"Caption words: {len(caption_words)}")

# transcript_path = input("Enter file path for transcription: ")
# captions_path = input("Enter file path for captions: ")
transcript_path = sys.argv[1]
captions_path = sys.argv[2]
compare(transcript_path, captions_path)