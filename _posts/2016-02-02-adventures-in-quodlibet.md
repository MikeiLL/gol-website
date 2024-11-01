---
id: 317
title: 'Adventures in QuodLibet'
date: '2016-02-02T03:35:31+00:00'
author: illest
layout: post
guid: 'https://centerofwow.com/?p=317'
permalink: /2016/02/02/adventures-in-quodlibet/
categories:
    - Projects
tags:
    - quodlibet
---

The vision of Steve Jobs and Apple products are beautiful and beautifully intuitive, but the magnitude of the company and it’s market share combined with it’s Closed Source approach create a bit of a Bog Brother feeling at times. As far as all of that goes, [Quodlibet](http://quodlibet.readthedocs.org) is pretty much the opposite. Open Source. Written in Python which is a classic Open Source programming language. Anyone in the world can make additions to the main code base or [create plugins](http://quodlibet.readthedocs.org/en/latest/development/plugins.html) to add or modify functionality. The public is welcome to look through the [list of issues](https://github.com/quodlibet/quodlibet/issues), tackle one or more and submit it to the applications maintainers for merging into the code base.

One thing I’d like to see is a more intuitive and useful interface for seeing and entering specific fields for each track – for example: description, comments, dance notes. You can download what’s called a [bundle](http://quodlibet.readthedocs.org/en/latest/downloads.html), which is basically a configured “application”, with an icon you click on and run as with your typical mail or internet browser program. You can “[clone](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)” the [source code](https://github.com/quodlibet/quodlibet) and build your own bundle, *or* you can do a combination of the two and install (download) the (pre-compiled) “bundle”, *but also* clone the code base and run the downloaded code base with the downloaded bundle. NOTE: my experience is with Mac/OS X and may differ for someone on a PC.

The way you run the bundle as development environment is by having the *bundle* run the cloned source code. On this computer you open the terminal program that resides in Applications/Utilities. It’s just a black and white window that puts you fairly directly in touch with the file system and features that run behind all the pretty windows of the GUI, or graphic user interface that some people pronounce, “gooey”. So you “move” into the Applications directory by typing `cd /Applications`. If you were to type `ls` you’d see a listing of all the applications that are in that directory (folder).

<figure aria-describedby="caption-attachment-319" class="wp-caption aligncenter" id="attachment_319" style="width: 300px">[![In the OS X Terminal](https://centerofwow.com/LIVE/wp-content/uploads/2016/02/Screen-Shot-2016-02-01-at-9.57.08-AM-300x140.png)](https://giggleoutloud.com/wp-content/uploads/2016/02/Screen-Shot-2016-02-01-at-9.57.08-AM.png)<figcaption class="wp-caption-text" id="caption-attachment-319">In the OS X Terminal</figcaption></figure>Then type something along the lines of the following:

`./QuodLibet.app/Contents/MacOS/run /Users/mikilmer/quodlibet/quodlibet/quodlibet.py`

Where the first part is `./` telling your computer this is a *script* to run, then `QuodLibet.app/Contents/MacOS/run` is the *path* to the part of the Quodlibet bundle that runs the application. It’s a “bash” (*born again* shell) script that looks something like this:

[![Screen Shot 2016-02-01 at 10.00.46 AM](https://centerofwow.com/LIVE/wp-content/uploads/2016/02/Screen-Shot-2016-02-01-at-10.00.46-AM-300x261.png)](https://giggleoutloud.com/wp-content/uploads/2016/02/Screen-Shot-2016-02-01-at-10.00.46-AM.png)

The last part of the line to run QuodLibet as a development environment, `/Users/mikilmer/quodlibet/quodlibet/quodlibet.py` is the *path* to the cloned codebase. I cloned it directly into my “home directory” located at `Users/mikilmer`.

I can test that I’m running from the cloned code base by adding a little bit of code to the main Quodlibet script referenced above:

```
def write():

    print('Creating new text file')
    name = raw_input('Enter name of text file: ')+'.txt'  # Name of text file coerced with +.txt

    try:
        file = open(name,'w')   # Trying to create a new file or open one
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python

write()

```

And when I run the *command* above the terminal prints “Creating new text file”, prompts to “Enter name of text file”: Mad Mike iLL, and creates a file called “Mad Mike iLL.txt” (But where?), then opens the player as normal. Ah. there’s the `Mad Mike iLL.txt` file in the `/Applications` directory where we actually ran the script from (as opposed to the directory the script/file is in). So we can `rm Mad\ Mike\ iLL.txt` which removes it from existence. Those back slashes “escape” the spaces to that `rm` doesn’t think it’s getting more than one *argument*. We don’t actually desire this “function” in the player so with the magic of Git we’ll revert back to the main code base: `git reset --hard HEAD`. (If I’m going to be making changes, I’ll want to add another “remote” branch to the git tree to which I am allowed to “push” code changes. This would be a “fork” of the main code base. And we want it to be [synced](https://help.github.com/articles/syncing-a-fork/) so we always have the latest version, or at least access to it.

To easily open QL this way from wherever in the directly system by simply typing `quod` in the terminal, I can create an [alias](https://www.digitalocean.com/community/tutorials/an-introduction-to-useful-bash-aliases-and-functions):

`alias quod="bash /Applications/QuodLibet.app/Contents/MacOS/run /Users/mikekilmer/quodlibet/quodlibet/quodlibet.py"`

So now we know that we can play with the Quodlibet code. Let’s see what’s going on with these “[plugins](http://quodlibet.readthedocs.org/en/latest/development/plugins.html)” that add various features.

We’d like to have a feature that auto generates a list of each song we have done in a given session. To make a plugin you can create a file in `~/.quodlibet/plugins/`. We’ll call ours `generatelist.py`, and I think it will be of the *class* `EventPlugin`. The EventPlugin [base class](https://github.com/quodlibet/quodlibet/tree/master/quodlibet/quodlibet/plugins). Hmmm. There are a bunch of EventPlugin subclasses (plugins) (found using `grep -rnw '/path/to/quodlibet/'- e "plugin_on_song_ended"`)  
that create an instance method called `plugin_on_song_ended` and by copying one of them I can see:

```
from quodlibet.plugins.events import EventPlugin

class GenerateList(EventPlugin):

    PLUGIN_ID = "generatelist"

    PLUGIN_NAME = _("Generate List")

    PLUGIN_DESC = _("Automatically add to playlist for current date."

                "Well for now let's just print song name out.")

    def plugin_on_song_ended(self, song, skipped):

        if song is not None:

            print song

```

That code printed out an “object reference” to the terminal, at the *ending* of a track playing. The “object reference” is just a line of code with object name and a hash of numbers. Then I could print out `dir(song)` which listed all the attributes and methods of the object (I think), one of which was `_song`. Printing `song._song` provided this:

```
    {comment': u'', 'composer': u'delete', 'genre': u'Line', 'tracknumber': u'04', '~mountpoint': '/Volumes/Pensacola International Folk Dance Music Archive', '~#laststarted': 1454363749, '~#skipcount': 2, 'album': u'33-12-07 Macedonian Folk Dances', '~#playcount': 7, '~#bitrate': 128, 'artist': u'Krivo Zensko Oro', '~#length': 153, 'title': u'Krivo Zensko Oro', '~#rating': 1.0, '~#added': 1448030939, '~#lastplayed': 1454274254, '~#mtime': 1100040376.0, '~filename': '/Volumes/Pensacola International Folk Dance Music Archive/SteveCollins/DVD 03/CIFD 33s part 6/Macedonian Folk Dances [LPY 50985]/04 Krivo Zensko Oro.mp3', '~#filesize': 2457600}

```

So one idea would be to write the values of `song._song['title']` for each track that plays through to a text file with current days date, creating a new file if one doesn’t exist. That might be a good first step. Next step would be adding the song to a playlist. Wait – it looks like playlists are [simply text files](http://quodlibet.readthedocs.org/en/latest/guide/browse/playlists.html) anyway, stored in `~/.quodlibet/playlists`.

Success! This plugin creates a playlist of all the tracks that have played through the end on any given day:

```
    '''
    This plugin creates a playlist of all the tracks that have played through the end on any given day.

    TODO: Add an enable disable button in GUI?
    '''

    from quodlibet.plugins.events import EventPlugin
    import time
    import os
    from os.path import expanduser

    class GenerateList(EventPlugin):
        PLUGIN_ID = "generatelist"
        PLUGIN_NAME = _("Generate List")
        PLUGIN_DESC = _("Automatically add to playlist for current date."
                        "Well for now let's just print song name out.")

        def plugin_on_song_ended(self, song, skipped):
            if song is not None:
                    print song._song['~filename']
                    self.write_to_playlist(song._song['~filename'])

        def write_to_playlist(self, filename):
            today = time.strftime("%F")
            home = expanduser("~")
            name = os.path.join(home, '.quodlibet/playlists', today)
            try:
                file = open(name, 'a')
                file.write(filename+'\n')
                file.close()
            except:
                print("Could not write file name out")

```

`

More later…