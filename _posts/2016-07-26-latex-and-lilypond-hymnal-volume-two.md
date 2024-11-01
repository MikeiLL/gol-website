---
id: 356
title: 'Latex and Lilypond Hymnal Volume Two'
date: '2016-07-26T21:42:47+00:00'
author: illest
layout: post
guid: 'https://centerofwow.com/?p=356'
permalink: /2016/07/26/latex-and-lilypond-hymnal-volume-two/
categories:
    - Projects
---

So this time there are two new elements to the Hymnal.

1. It will be a smaller size, 5.5″ x 8″
2. It will blend text and music snippets more than the first book.

It’s fairly easy to make a [single sheet or even songbook ](http://lilypond.org/doc/v2.18/Documentation/notation/paper-size-and-automatic-scaling)a custom size:

```
#(set! paper-alist (cons '("my size" . (cons (* 5.5 in) (* 8 in))) paper-alist))

\paper {
  #(set-paper-size "my size")
}

```

And this can be [included in a text document](http://lilypond.org/doc/v2.18/Documentation/usage/an-example-of-a-musicological-document):

```
\documentclass[a4paper]{article}

\begin{document}

Documents for \verb+lilypond-book+ may freely mix music and text.
For example,

\begin{lilypond}
\relative c' {
  c2 e2 \tuplet 3/2 { f8 a b } a2 e4
}
\end{lilypond}

Options are put in brackets.

\begin{lilypond}[fragment,quote,staffsize=26,verbatim]
  c'4 f16
\end{lilypond}

Larger examples can be put into a separate file, and introduced with
\verb+\lilypondfile+.

\lilypondfile[quote,noindent]{gayatri_mantra.ly}

(If needed, replace @file{screech-and-boink.ly} by any @file{.ly} file
you put in the same directory as this file.)

\end{document}

```

Supposedly there’s a tutorial [here](http://lilypondblog.org/2013/07/creating-songbooks-with-lilypond-and-latex/), but the link is broken. There is the main [Open LilyLib site.](https://openlilylib.org)

[This repository](https://github.com/uliska/musicexamples) looks like it’s exactly what I need, but it’s a few years without update and not terribly well documented. It also appears to be unfinished.

I cloned to repository and am trying to compile one of the LateX files in it’s documentation directory:

`\usepackage{musicexamplesStyles}` gives the error that the code is requiring the package, musicexamplesStyles, when what is available is musicexamplesStyles (singular). So I updated that code to: `\usepackage{musicexamplesStyle}`.

Then it was looking for a file called `musicexamples.sty`. I see one called `musicexamplesStyles.sty` in the directory with the `tex` file so copying it to `musicexamples.sty`. Now am getting an error that it’s looking for a native Linux Font: Linux Libertine 0, which is not found on this OS X machine. Neither can “Linus Biolinum 0”, “Inconsolata”.

There’s a program that came with LaTeX called Tex Live, that doesn’t seem to be working, but there’s also a program in there called FixMacTex, which I am running now, and supposedly will fix some issues.

Wait. The musicexampleStyles docs say

```
The main requirement to make use of the present material is to make the \package{musicexamples} package available to your \LaTeX{} distribution.
If you have obtained \package{musicexamples} as an archived download archive you may just unpack it into a folder inside your \dir{texmf/tex/latex} directory.
Depending on your (operating and \LaTeX) system you may have to run \env{texhash} afterwards.
If you aren't sure what this means, please consult your \LaTeX{} documentation or a book.

```

Seems to be an issue with TexLive, which I’m guessing is like a package manager for TeX/LaTeX. Looks like my version of LaTeX is out of date so dowlnoading the 2 GigaByte newer version. In the meantime I do have `texhash` installed. It’s a small database that keeps track of all the locations of various TeX files.

```
which texhash
/usr/texbin/texhash


```

Will try running it.

```
$ texhash
texhash: /usr/local/texlive/2014/texmf-config: directory not writable. Skipping...
texhash: /usr/local/texlive/2014/texmf-dist: directory not writable. Skipping...
texhash: /usr/local/texlive/2014/texmf-var: directory not writable. Skipping...
texhash: /usr/local/texlive/texmf-local: directory not writable. Skipping...
texhash: Done.
mikekilmer@jamaaladeen-2:~/Documents/Vault/Hymnal/musicexamples/documentation$ sudo !!
sudo texhash
Password:
texhash: Updating /usr/local/texlive/2014/texmf-config/ls-R... 
texhash: Updating /usr/local/texlive/2014/texmf-dist/ls-R... 
texhash: Updating /usr/local/texlive/2014/texmf-var/ls-R... 
texhash: Updating /usr/local/texlive/texmf-local/ls-R... 
texhash: Done.


```

Hmmm. Same errors. Maybe this repository won’t be the best route at the moment.

This looks promising: https://github.com/openlilylib/snippets

Not sure, but the LaTeX booklet posts I’m seeing refer to sizes `A4, A5, A6`. This [posting](http://tex.stackexchange.com/questions/154777/a5-booklet-printing-title-page-and-toc-are-missing) seems to offer some useful information:

```
\documentclass[12pt]{article}
\usepackage[a5paper,verbose]{geometry}
\usepackage{lipsum}  % this package is for creating filler text

\author{N.~N}
\title{The booklet}

\begin{document}

\maketitle

\tableofcontents

\section{Europe}
\subsection{Berlin}
\lipsum[4]
\subsection{Paris}
\lipsum[1-3]
\subsection{Vienna}
\lipsum[10]
\subsection{Rome}
\lipsum[15]
\section{Africa}
\lipsum[1-4]
\subsection{Accra}
\lipsum[5-8]
\subsection{Johannesburg}
\lipsum[9-11]
\subsection{Casablanca}
\lipsum[11-12]
\lipsum[5-6]
\section{Asia}
\lipsum[1-4]
\subsection{Tokyo}
\lipsum[5-8]
\subsection{Beijing}
\lipsum[9-11]
\subsection{Mumbai}
\lipsum[11-12]
\lipsum[5-6]

\end{document}

```

and if the above was saved as `filler.tex`:

```
\documentclass[12pt]{article}
\usepackage[a4paper]{geometry}
\usepackage{pdfpages}
    \includepdfset{pages=-}

\author{N.~N}
\title{The booklet}

\begin{document}

    \includepdf[pages=-,nup=1x2,landscape,signature=20]{filler.pdf}


\end{document}

```

So if that’s going to be the method for now, the only big piece of the puzzle is determining margin and/or page sizes on the `lilypond-book` coding.

While searching for that, I came across [this post](http://tex.stackexchange.com/questions/111055/how-to-run-latex-and-lilypond-book-in-one-command) inf which someone asks if it’s possible to run lilypond and LaTeX as one a single command. Apparently a library called `arara` is the key, which seems to require a Java runtime environment, Downloading Java JDE now.

Meanwhile the latest LaTeX is 20% downloaded. JDE installed and now:

```
$arara
  __ _ _ __ __ _ _ __ __ _ 
 / _` | '__/ _` | '__/ _` |
| (_| | | | (_| | | | (_| |
 \__,_|_|  \__,_|_|  \__,_|

arara 3.0 - The cool TeX automation tool
Copyright (c) 2012, Paulo Roberto Massa Cereda
All rights reserved.

usage: arara [file [--log] [--verbose] [--timeout N] [--language L] |
             --help | --version]
 -h,--help             print the help message
 -l,--log              generate a log output
 -L,--language <arg>   set the application language
 -t,--timeout <arg>    set the execution timeout (in milliseconds)
 -V,--version          print the application version
 -v,--verbose          print the command output

```

I read the really fun (really!) manual and finally [posted on Stack Exchange](http://tex.stackexchange.com/questions/321204/im-sorry-but-the-file-test-lytex-doesnt-exist), eventually sending an email to the awesome developer of Arara (Paulo, noted above) and got it worked out. The problem was simply that I was using the `.yml` (shortened) extension, while Arara (version 3.0) is looking for the full `.yaml` extension.

Getting closer and closer to the (simple) formula that will get this Hymnal properly formatted with some help from [this Stack Exchange answer](http://tex.stackexchange.com/a/85043/68905).

The current test scripts look like this:

First just a simple test A5 TeX document (`test.tex`):

```
\documentclass[a5paper,twoside,9pt]{extbook}
\usepackage[left=1.7cm,right=2.2cm,top=2cm,bottom=1.5cm]{geometry}

\begin{document}

Documents for \verb+lilypond-book+ may freely mix music and text.
For example,

(If needed, replace @file{screech-and-boink.ly} by any @file{.ly} file
you put in the same directory as this file.)

\end{document}

```

Good. Our song file (`song.ly`):

```
\version "2.19.45"

\header {
  title = "Gayatri Mantra"
  author = "anonymous"
  composer = "Music by Rivka and Mike iLL"
  tagline = "Copyright Rivka and Mike iLL Kilmer Creative Commons Attribution-NonCommercial BMI - Engraving by Lilypond"
}

#(set! paper-alist (cons '("hymnal" . (cons (* 5.5 in) (* 8 in))) paper-alist))

\paper {
  #(set-paper-size "hymnal")
  ragged-last-bottom = ##f
  print-page-number = ##f
}

melody = \relative c'' {
  \clef treble
  \key d \major
  \time 4/4
  \set Score.voltaSpannerDuration = #(ly:make-moment 4/4)
    \new Voice = "words" {
        g4( a) a2 | g8( a4) a8 a4 a | g8( a4.) a4 a | g8( a4) a4. cis4 | % Om bur ... maha
        g8( a4) a8 a4 a | g8( a4) a8 a4 a | g8( a4.) a4 r | a8( bes)~ bes2. | % Om sawaha... sat yam
        a4 a8-> r8 \times 2/3 { a4 a8 } g4 | a bes g2 | a4 \times 2/3 { a4 a8 } a4 g | a bes g2 | % Om tat savitur ... dimahi
        \times 2/3 { g4( a) a } \times 2/3 { a a a } | \times 2/3 { a a a } a4 r \bar "|." % Dhi yo yo... prachodhayat
        }
}

text =  \lyricmode {
    Om bhur | Om bhu -- ga -- ha  | Om swa -- ha | Om ma -- ha |
    Om ja -- na -- ha | Om ta -- pa -- ha | Om sat | yam |
    Om tat sa -- vi -- tur | bar -- vi -- nam | Bhar -- go  de -- va -- sya | Dhi -- ma -- hi |
    Dhi -- yo yo -- na -- ha | pra -- cho -- dha -- yat |
}


twochords = \chordmode { a1 | g:m | }

harmonies = {
    \twochords \twochords
    \twochords \twochords
    \twochords \twochords
    \twochords
}

\score {
  <<
    \new ChordNames {
      \set chordChanges = ##t
      \harmonies
    }
    \new Staff \with { \magnifyStaff #5/7 } {
        \new Voice = "one" { \melody }
    }
    \new Lyrics \lyricsto "words" \text
  >>
  \layout { 
   % #(layout-set-staff-size 14)
   }
  \midi { }
}

```

Being referenced by `song.lytex`:

```
\documentclass[a5paper,twoside,9pt]{extbook}
\usepackage[left=1.7cm,right=2.2cm,top=2cm,bottom=1.5cm]{geometry}

\begin{document}

Documents for \verb+lilypond-book+ may freely mix music and text.
For example,

\begin{lilypond}
\relative c' {
  c2 e2 \tuplet 3/2 { f8 a b } a2 e4
}
\end{lilypond}

Options are put in brackets.

\begin{lilypond}[fragment,quote,staffsize=26,verbatim]
  c'4 f16
\end{lilypond}

Larger examples can be put into a separate file, and introduced with
\verb+\lilypondfile+.

\lilypondfile[quote,noindent]{gayatri_mantra.ly}

(If needed, replace @file{screech-and-boink.ly} by any @file{.ly} file
you put in the same directory as this file.)

\end{document}

```

The terminal commands are:

```
lilypond-book --output=out --pdf song.lytex 

```

This creates a directory called `out`, inside of which we need to run the command:

```
pdflatex song.tex

```

Then finally `open song.pdf`. Still some margin issues. Then Need to work on using Arara in the workflow.

Close! Removing the following paper settings from the included `song.ly` file helped. Now just need to reduce the margins in the outer document.

```
#(set! paper-alist (cons '("hymnal" . (cons (* 5.5 in) (* 8 in))) paper-alist))

\paper {
  #(set-paper-size "hymnal")
  ragged-last-bottom = ##f
  print-page-number = ##f
}

```

That’s it! Just needed to update following setting (second line, in this case) in `song.lytex`:

```
\usepackage[left=.7cm,right=.7cm,top=2cm,bottom=1.5cm]{geometry}


```

Meanwhile, Mom did proofreading on the first Hymnal, and offered to help on this one too, but I realized that probably the main reason lilypond *creates* midi files is so you can use your own ears to proof the writing. How do you play midi files on OS X? [Quicktime Player 7](http://osxdaily.com/2014/07/20/run-quicktime-player-7-in-mac-os-x/) (and old version) seems to be the answer.

To make Quicktime 7 open the files from the command line I add this to `~/.bashrc` (then run `source ~/.bashrc`):

```
#play midi files using Quicktime 7
alias midi="open -a /Applications/Utilities/QuickTime\ Player\ 7.app"

```

Of note `~/.bash_profile` contains the following directive:

```
if [ -f ~/.bashrc ]; then
   source ~/.bashrc
fi

```

Now I need to set a tempo in lilypond, I guess ’cause DAMN is that file playing slowly.

Simple answer: `\tempo 4 = 125`.

At the moment the process for viewing updates:

```
rm -rf out
lilypond-book --output=out --pdf hymnal.lytex 
cd out && pdflatex hymnal.tex
pdflatex hymnal.tex # have to run it a second time to generate the Table of Contents.
open hymnal.pdf
cd ../

```