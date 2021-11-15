from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo
import re

#Loading the model 
#summarizer = pipeline("summarization")

video = "https://www.youtube.com/watch?v=d0b43w_Z8Iw"

#Splitting video at the equal separator to get video id
video_id = video.split("=")[1]

YouTubeVideo(video_id)
video_transcript = YouTubeTranscriptApi.get_transcript(video_id)

result = " "
for i in video_transcript:
    result += " " + i['text']

# Loading the model
summarizer = pipeline("summarization")

# creating batches
num_iters = int(len(result)/1000)
summarized_text = []
for i in range(0, num_iters + 1):
    start = 0
    start = i * 1000
    end = (i + 1) * 1000
    output = summarizer(result[start:end])
    output = output[0]
    output = output['summary_text']
    summarized_text.append(output)


print(summarized_text)

