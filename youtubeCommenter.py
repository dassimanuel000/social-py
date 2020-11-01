from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from apikey import apikey


class YoutubeBot:

    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)

    def getVids(self):
        searchString = input("Enter a search string: ")  # search paramter
        numOfResults = 0
        ids = [] #stores the video ids
        while numOfResults < 1 or numOfResults > 50:
            numOfResults = int(input(
                "How many videos do you want to like/comment? (50 is the max) "))  # number of videos the scraper will get, 50 is max

        youtube = build('youtube', 'v3', developerKey=apikey)
        req = youtube.search().list(q=searchString, part='snippet', type='video', maxResults=numOfResults)
        res = req.execute()
        print("You will be like/commenting on the following videos: ")
        for item in res['items']:
            print(item['snippet']['title'])
            ids.append((item['id']['videoId'], item['snippet']['channelId']))

        if input("Press enter to continue") != "":
            quit()
        return ids

    def likeVids(self):
        ids = self.getVids()
        for videoId in ids:
            self.youtube.videos().rate(rating='like', id=videoId[0]).execute()


    def commentVids(self):
        ids = self.getVids()
        message = input("What do you want to comment? ")
        for id in ids:
            self.insert_comment(id[1], id[0], message)


    def insert_comment(self, channel_id, video_id, text):
        self.youtube.commentThreads().insert(
            part="snippet",
            body=dict(
                snippet=dict(
                    channelId=channel_id,
                    videoId=video_id,
                    topLevelComment=dict(
                        snippet=dict(
                            textOriginal=text
                        )
                    )
                )
            )
        ).execute()


bot = YoutubeBot()
bot.commentVids()

