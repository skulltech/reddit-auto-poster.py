import praw
import configparser
import getpass
import json
import time



class Golem:
    def __init__(self, config):
        self.reddit = praw.Reddit(client_id=config['CONFIG']['CLIENT_ID'], 
                                  client_secret=config['CONFIG']['CLIENT_SECRET'],
                                  username=config['CONFIG']['USERNAME'],
                                  password=config['CONFIG']['PASSWORD'],
                                  user_agent='Script by u/SkullTech101')
        self.reddit.validate_on_submit = True

    def post(self, subreddit, title, url=None, text=''): 
        if url:
            submission = self.reddit.subreddit(subreddit).submit(title=title, url=url)
        else:
            submission = self.reddit.subreddit(subreddit).submit(title=title, selftext=text)
        return submission


def submit(golem, sr, post):
    try:
        sub = golem.post(sr, post['Title'], url=post['URL'])
    except KeyError:
        sub = golem.post(sr, post['Title'], text=post['Text'])
    return sub


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        config['CONFIG']['PASSWORD']
    except KeyError:
        config['CONFIG']['PASSWORD'] = getpass.getpass('[*] Password for Reddit account {}: '.format(config['CONFIG']['USERNAME']))
    try:
        WAIT = int(config['CONFIG']['WAIT'])
    except KeyError:
        WAIT = 1000

    golem = Golem(config)
    ifile = input('[*] JSON file containing posts: ') or 'posts.json'
    with open(ifile) as f:
        posts = json.load(f)

    first = True
    for post in posts['Posts']:
        for sr in post['Subreddits']:
            if not first:
                time.sleep(WAIT)
            else:
                first = False
            try:
                sub = submit(golem, sr, post)
            except Exception as exp:
                print('[*] Exception: {}'.format(exp))
            else:
                print('[*] Posted "{}..." on {}. Post ID: {}'.format(post['Title'][:10].rstrip(), sr, sub.id))


if __name__=='__main__':
    main()
