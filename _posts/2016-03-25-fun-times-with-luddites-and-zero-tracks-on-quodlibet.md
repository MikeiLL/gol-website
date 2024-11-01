---
id: 348
title: 'Fun Times with Luddites and Zero Tracks on QuodLibet'
date: '2016-03-25T23:24:13+00:00'
author: illest
layout: post
guid: 'https://centerofwow.com/?p=348'
permalink: /2016/03/25/fun-times-with-luddites-and-zero-tracks-on-quodlibet/
categories:
    - Projects
tags:
    - 'Folk Dance Archive'
---

Wow. That was in-ter-es-ting!

So yes – a couple of the “older” folks were a little wary of moving from cassette to digital format, which put me in the awkward position of defending this archiving project. Kind of the opposite of Paul Bunyan – with the new technology fighting to justify it’s value.

Last week, Quodlibet was finding Zero (of over 17,000) tracks. So there I am unable to play ANY music. Fortunately the old system is still in place, but I’m sure my ears were looking a bit red around the tips.

I thought it might have been an issue with the external drive either in terms of data, format or drive type.

After way too much time experimenting I decided to try looking into the Qoudlibet database. Is it postgreSQL? No. Actually it’s not a database at all. QL uses a “pickled list of AudioFile instances”. “Pickling” is the Python (language) word for a compressed file.

As per the [FAQ](http://quodlibet.readthedocs.org/en/latest/development/faq.html), you’re supposed to be able to examine this “pickled” songs list:

```
Python 2.6.2 (r262:71600, Jun  4 2009, 15:54:27)
[GCC 4.3.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import quodlibet
>>> import cPickle
>>> with open(".quodlibet/songs", 'r') as songsfile:
...     songs = cPickle.load(songsfile)
...

```

(Note `import quodlibet` only worked for me when running the Python interactive interpreter from within the same directory as the main quodlibet.py file. I think there’s that directory could be added to the Python path, but haven’t looked into it yet.)

But the above was returning an error:

```
Traceback (most recent call last):
  File "/Users/mikekilmer/quodlibet/quodlibet/quodlibet/plugins/events.py", line 104, in __invoke
    handler(*args)
  File "/Users/mikekilmer/quodlibet/quodlibet/quodlibet/ext/events/viewlyrics.py", line 81, in plugin_on_song_started
    if not lyrics:
UnboundLocalError: local variable 'lyrics' referenced before assignment

```

Apparently in the current version of quodlibet you have to also initialize quodlibet: `quodlibet.init()`.

Still no luck. More errors. Back to the [Quodlibet Development Group](https://groups.google.com/forum/#!forum/quod-libet-development) on Google.

In the meantime I tried removing all but one of the directories from the Library. I tried replacing the `/.quodlibet/songs` cPickle file.

The `songs` pickle file resides in a directory named `.quodlibet` which is in your “home directory” and on Unix and Mac OSX this is referenced with the tilde: `~/`. It also contains the `playlists`, `lists`, `config` and a few other files and directories. So I backed up `~/.quodlibet` to `~/QLbackups` and reinstalled the application. Working again. Yay!

Finally I removed the entire `~/.quodlibet` directory (backing it up elsewhere), and through swapping components in and out between a fresh install’s `~/.quodlibet` directory and the previous one, I discovered that it was two lines under the `[browsers]` heading in the `~/.quodlibet/config` file that were causing the issue:

```
albums =
background = ketriketriketriketri # (this is the [whitespace ommited] name of one of the tracks from the collection)

```

Back in business. But wait. All of our playlist files are empty! Fortunately I back up the computer on our QNAP Network Attach Storage system using Time machine. So I was able to open the `~/.quodlibet` direcory in the finder (by entering it in the Go&gt;Go to folder field in the Mac finder) and then open TIme Machine, go back a few weeks and “restore” it.

Now we’re back in biz! Sweet.