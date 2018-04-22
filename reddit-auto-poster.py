import praw
import configparser
import getpass
import json
import time



class Golem:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        try:
            self.config['CONFIG']['PASSWORD']
        except KeyError:
            self.config['CONFIG']['PASSWORD'] = getpass.getpass('[*] Password for Reddit account {}: '.format(config['CONFIG']['USERNAME']))
        self.reddit = praw.Reddit(client_id=self.config['CONFIG']['CLIENT_ID'], 
                             client_secret=self.config['CONFIG']['CLIENT_SECRET'],
                             username=self.config['CONFIG']['USERNAME'],
                             password=self.config['CONFIG']['PASSWORD'],
                             user_agent='Script by u/SkullTech101')

    def post(self, subreddit, title, url=None, text=''): 
        if url:
            submission = self.reddit.subreddit(subreddit).submit(title=title, url=url)
        else:
            submission = self.reddit.subreddit(subreddit).submit(title=title, selftext=text)
        return submission


def main():
    golem = Golem()
    ifile = input('[*] JSON file containing Post details [default: posts.json]: ') or 'posts.json'
    with open(ifile) as f:
        posts = json.load(f)

    for post in posts['Posts']:
        for sr in post['Subreddits']:
            try:
                sub = golem.post(sr, post['Title'], url=post['URL'])
            except praw.exceptions.APIException:
                sub = golem.post(sr, post['Title'], text=post['Text'])

            print('[*] Posted on {}. Post ID: {}'.format(sr, sub.id))
            time.sleep(1000)


if __name__=='__main__':
    main()
