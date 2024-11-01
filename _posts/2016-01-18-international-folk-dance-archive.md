---
id: 294
title: 'International Folk Dance Archive'
date: '2016-01-18T22:59:34+00:00'
author: illest
layout: post
guid: 'https://centerofwow.com/?p=294'
permalink: /2016/01/18/international-folk-dance-archive/
categories:
    - Projects
tags:
    - archive
    - 'International Folk Dance'
    - quodlibet
---

Earier this year we received another grant from the [Puffin Foundation West](\"http://www.puffinwest.org\") for a project to develop the music database we use with [Pensacola International Folk Dancers](\"http://pensacolafolk.com\").

We\\’ve been using a combination of cassette tapes and a fairly un-maintained iTunes music collection and we had a few objectives for the project.

1. Digitize cassette collection
2. Archive some of our collective knowledge about the songs and dances
3. Ensure that all members of the group have access to the music
4. I need to check if this was part of the initial grant proposal, but we are also learning to play some of the repertoire as well as transcribing it and codifying with [lilypond software.](\"http://www.lilypond.org\")

[![\"Ciulandra\"](\"https://centerofwow.com/LIVE/wp-content/uploads/2016/01/Ciulandra-300x199.png\")](\"https://giggleoutloud.com/wp-content/uploads/2016/01/Ciulandra.png\")There have been many steps in this process. The first thing I did was to speak with [Larry Weiner](\"http://www.larryweiner.com\"), who is considered to be an expert in the field of International Folk Dance and specifically it\\’s archiving. One of the things we discussed were potential archival frameworks. Larry\\’s occupation for may years was as a database administrator and he had at one point built, from scratch so to speak, a music archiving system. He advised me against spending so much time developing a system that the archiving itself suffers. He also taught me the term, \\”Analysis Paralysis\\”, which comes into play because there are so many potential parameters to consider in terms of what information to archive.

Each \\”track\\” may be named by the dance it accompanies, may have multiple spellings in multiple languages. For each \\”track\\” there may be a specific archivist to whom it is attributed. There are performers, various music collections (albums) it may be sourced from. There may be images, ratings, composer, etc. So one thing we would need to consider is \\”how much information, and which information do we want to archive for each track?\\”

Then there is the question of how the tracks will be associated into categories and collections, which ties in with the content of the stored track data.

I\\’ll take a moment to mention here that this music is absolutely awesome and inspiring. So raw. So earthy. So tactile. Currently listening to [Aino Kchume, Assyrina folk dance](\"https://www.youtube.com/watch?v=HOV7g5RhU3s\"), Recorded in 1962 by the Shemiram Assyrian Folklore Groupe in Tehran, Iran. From the album \\”Assyrian Folk Dances\\”, Folkcraft LP-4. Why don\\’t we consider the Iranian culture when considering war with them? But that\\’s another (related) topic.

My next step was to explore options for a music archiving platform that would fulfill our needs. Larry recommended I join the [East European Folklife Center](\"http://East) mailing list, which I believe I was already on. I believe it was through them that I discovered the Wikipedia (yay croud-sourced information and Open Source) [comparison of audio player software](\"https://en.wikipedia.org/wiki/Comparison_of_audio_player_software\"). It needed to run on an Apple (OSX) computer, which is what the group (and Mad haPPy) have, and needed to be flexible in terms of track information configuration. [QuodLibet](\"http://quodlibet.readthedocs.org\") not only meets those qualifications, but it has longevity (released in 2004), is still being maintained and [supported](\"https://groups.google.com/forum/#!forum/quod-libet-development\"), is [open source](\"https://github.com/quodlibet/quodlibet\") and is written in Python, which is a computer language I know (to some degree, anyway). Perfect.

[![\"dupfinderCode\"](\"https://centerofwow.com/LIVE/wp-content/uploads/2016/01/dupfinderCode-300x200.png\")](\"https://giggleoutloud.com/wp-content/uploads/2016/01/dupfinderCode.png\")Now that our platform was determined (barring unforeseen glitches), it was time to look at our current digital collection and the first thing that needed doing was to get rid of the many many duplicate tracks. This would have been a really grueling manual task, but a cinch with a small [python script](\"https://github.com/MikeiLL/dupFinder\"), which compares the actual digital content of each file and moves all duplicates out into a separate directory.

Now we have a relatively clean version of our digital collection. But we need to get the cassettes digitized. It turns out that the cassettes were recorded from actual vinyl records some of our members have. But most of them are 4 and a half hours drive from here in Tuscaloosa, Alabama. It doesn\\’t make a ton of sense to digitize a cassette recording of vinyl when the vinyl is accessible. Driving 9 hours and humping literally hundreds of pounds of vinyl records, while it sounds fun, would be expensive and time-consuming, and being a lazy poet, I looked for a way to avoid it. Guess what? Larry Weiner tells me that there is a group in the Washington DC area that already has a digital database of international folk dance music that we may be able to get our hands on, and lo and behold there\\’s a guy who is quite close with a few members of our group that has a copy of it… somewhere.

Steve, who has the copy of the archive, lives a few hours away also and isn\\’t quite sure where it is. It takes us months to finally get the music into my hands. But here are like ten thousand old, rare international folk dance music tracks. I\\’ve already begun the process of transferring our cassette collection to digital, but let\\’s pause and check the database for a previously digitized version of each track first.

[![\"Duplicate](\"https://centerofwow.com/LIVE/wp-content/uploads/2016/01/dupfinder11-300x190.png\")](\"https://giggleoutloud.com/wp-content/uploads/2016/01/dupfinder11.png\")Well this database is also full of duplicates, including many tracks which include the word \\”delete\\” in their name. Let\\’s see what our `dupFinder.py` scripts thinks:

`python dupFinder.py -t FOLDER_WITH_10000_TRACKS`

The track names fly down the terminal screen for a long time. (There\\’s a folder called NJ Lame – hey what you saying about New Jersey?) This collection of music comes with small document that contains the acronym CIFD. Does this stand for [Charlottesville International Folk Dancers](\"http://www.charlottesvilleinternationalfolkdance.com\")? Wow. That script took like ten minutes to run. Running `du -sh FOLDER_WITH_10000_TRACKS` on the command line reveals that it is 46 Gigbytes!

Let\\’s run the script for real:

`python dupFinder.py FOLDER_WITH_10000_TRACKS`

Back in 20 minutes… or after a visit to the dentist… Dentist rocks! $15 fee? Sweet!

Our script appears to have removed 15 Gigabytes of duplicate data from the directory, leaving us at 31Gig. The directory of duplicates that was created contains 7.4G worth of data, which probably means that 7.6G were duplicates of duplicates. This was all done in our QNAP backup server, so let\\’s now run the script on the Seagate portable 1 terabyte system. Same result. Good.

It appears that there are tracks that ended up in the duplicate/removed track directories that don\\’t exist in the main directories, so perhaps our scripts needs to be revisited. In the meantime, we can just search the \\”removed\\” directories for tracks that can\\’t be found in the main collection to see if they exist there. If not – we\\’ll import them from cassette or vinyl.

[![\"playerwindow\"](\"https://centerofwow.com/LIVE/wp-content/uploads/2016/01/playerwindow-300x143.png\")](\"https://giggleoutloud.com/wp-content/uploads/2016/01/playerwindow.png\")In the meantime we can begin using the music collection and organizing the archive using the Quodlibet player. For each track we can ALT-CLICK the track to \\”edit tags\\” and add comments and description tags and content. Now we can click in the HEADER section of the main players track list and add columns to display the comments and description for each track. We can create numerous playlists and manage their tracks, and we can [configure Quodlibet to search](\"http://quodlibet.readthedocs.org/en/latest/guide/searching.html\") within specified playlists.

[![\"Quodlibet\'s](\"https://centerofwow.com/LIVE/wp-content/uploads/2016/01/globalfilter-300x240.png\")](\"https://giggleoutloud.com/wp-content/uploads/2016/01/globalfilter.png\")This achieved in one of two ways: `~playlists` is a *flag*, which accepts an argument which can be a single or set of playlists. For example: `~playlists=Standards` or `~playlists=|(\'Standards\',\'Repertoire\')`. This flag can either be placed in the track browser input bar or as a \\”Global Filter\\” in the preferences.

On our list of future Quodlibet TODO (learn)/feature requests are

- sub-categorize playlists
- generate playlists based on plays to automate archiving of selections per session
- display specified track tags more eloquently
- Move or copy [database/song info collection](\"http://quodlibet.readthedocs.org/en/latest/development/faq.html#what-format-is-the-song-database-in\") to portable drive

Listening to our massive collection (over 20,000 tracks) of International Folk Dance music and trying not to be overwhelmed by our ignorance. There’s a lot to learn about music, dance, culture and managing an archive of music. The members of Pensacola International Folk Dancers are giddy with the new influx of inspired energy, not to mention the ease with which we can now make use of the music collection. What used to be a matter of searching through old cassettes and hoping they would play in the old cassette player is now as simple as naming a dance and either playing it or selecting a track from an array of potential versions. The group has increased regular attendance and as well as session length, thanks in part to the support of Puffin West and as always we Puffins are grateful.