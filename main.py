import googleapiclient.discovery
from textblob import TextBlob
from pytube import YouTube

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = ""

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

RequestedLink = input("Enter video's link: ")
equal_index = RequestedLink.index("=")
RequestedId = RequestedLink[equal_index+1:]

yt = YouTube(RequestedLink)

print("Title: ", yt.title)
print("Views: ", yt.views)

request = youtube.commentThreads().list(
    part="snippet",
    videoId= RequestedId,
    maxResults=100
)
response = request.execute()

comments = []

polarity_sum = 0
comment_count = 0

for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']
    text = comment['textDisplay']

    analysis = TextBlob(text)
    comment_polarity = analysis.polarity
    
    if comment_polarity != 0:
        comment_count += 1
        polarity_sum += comment_polarity 

average_polarity = polarity_sum/comment_count

print("Comments:  The average polarity of the comments is ", average_polarity, "(1 = good, 0 = neutral, -1 = bad)")

UserAction = str(input("\nDo you want to download the video? Y/n ..."))
UserAction = UserAction.upper()

if UserAction == "Y":
    DownloadPath = str(input("\nEnter the folder path where you want the video to be stored.."))
    yd = yt.streams.get_highest_resolution()
    yd.download(DownloadPath)