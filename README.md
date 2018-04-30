# reddit-auto-poster.py
Python script for posting to multiple subreddits automagically.


## Installation and Set-Up

Works on _Python 3.x_

The only required library is `praw`. Install it as
```console
$ pip3 install praw
```

Also, you'll have to create a Reddit app of type `script` from [here](https://www.reddit.com/prefs/apps/), and put the `CLIENT_ID`, `CLIENT_SECRET` and `USERNAME` in the file [`config.ini`](https://github.com/SkullTech/reddit-auto-poster.py/blob/master/config.ini).

## Usage

After specifying the details of the posts to be made in the `posts.json` file, run the as following. Use the provided sample [`posts.json`](https://github.com/SkullTech/reddit-auto-poster.py/blob/master/posts.json) file as template

```console
$ python3 reddit-auto-poster.py 
[*] Password for Reddit account SkullTech101: 
[*] JSON file containing posts: posts.json
[*] Posted "Test post..." on test. Post ID: 8e5k45
...
```
