---
id: 371
title: 'Further Developments Latex and Lilypond now with Arara and International Unicode Text via XeLatex'
date: '2016-08-18T01:30:14+00:00'
author: illest
layout: post
guid: 'https://centerofwow.com/?p=371'
permalink: /2016/08/18/further-developments-latex-and-lilypond-now-with-arara-and-international-unicode-text-via-xelatex/
categories:
    - 'Concert Updates'
---

The title might be a white lie, because while I did get [arara](https://github.com/cereda/arara) working, in combination with a bash script, to automate the steps to render the hymnal.

`Good news. One of the arara developers helped me solve the problem. Stack overflow:`

The solution ends up being quiet simple. The only limitation is that we are not outputting the lilypond-book content to a subdirectory as originally planned.

At the top of the `music.lytex` file (after configuring arara as directed in the referenced post), add the following two directives:

```
% arara: lilypond: {options: "--pdf"}
% arara: pdflatex: { files: [ 'hymnal.tex' ] }

```

Now make a file called `render.sh` containing something like the following:

```
arara music.lytex
pdflatex music.tex
find . -maxdepth 1 -type d -name '??' -exec rm -rf {} \;
rm *.aux *.bcf *.dep *.out *.run.xml *.toc tmpx*
open music.pdf

```

And render *and* view the resultant pdf file by calling it with bash:

```
bash render.sh

```

The middle three lines in the bash script:

```
pdflatex music.tex

```

This is because pdflatex needs to be run a *second* time in order to generate the table of contents.

```
find . -maxdepth 1 -type d -name '??' -exec rm -rf {} \;

```

What this line does is remove all of the temporary directories created by the lilypond-book command, which would, if generating into a subdirectory (with the `--output=out`) flag, be neatly contained in there.

```
rm *.aux *.bcf *.dep *.out *.run.xml *.toc tmpx*

```

All the other temporary files that might interfere with subsequent renderings.

Thanks, arara crew. Long live the arara bird and Brazilian hospitality!

Note that two files needed to be created on my system in order for this to work. The `araraconfig.yaml` file located in my home directory:

``

```

    !config
    # Config file to use texmfhome as search path
    # # author: Mike iLL
    # # requires arara 3.0+
    paths:
    - /Users/mikekilmer/Library/texmf/scripts/arara/rules

    filetypes:
    - extension: lytex
      pattern: ^(\s)*%\s+
```

And a single rule, `lilypond.yaml`, located in the above referenced directory:

``

```

    !config
    # Mainfile rule for arara
    # author: Marco Daniel
    # requires arara 3.0+
    identifier: lilypond
    name: Lilypond
    command: <arara> lilypond-book @{format} @{options} @{output} "@{file}"
    arguments:
    - identifier: format
      flag: <arara> --format=@{parameters.latex-programm}
      default: <arara> --format=latex
    - identifier: options
      flag: <arara> @{parameters.options}
    - identifier: output
      flag: <arara> --output=@{parameters.output}
</arara></arara></arara></arara></arara>
```

But then as the text developed, I realized that some Sanscrit were cropping up. And `pdflatex` only deals with 256 characters, which is the beginning of the `utf8` *universal* character set. Fortunately I found [this post](http://tex.stackexchange.com/questions/123486/how-to-use-lilypond-book-with-custom-fonts) on the TeX StackExchange site, offering the following flag to tell lillypond-book to use XeLatex instead of pdflatex:

```
http://tex.stackexchange.com/questions/123486/how-to-use-lilypond-book-with-custom-fonts

```

And a [fine example](http://cikitsa.blogspot.com/2010/07/xelatex-for-sanskrit.html) of use of Sanscrit and various Hindi scripts in a LaTeX document:

```

```
{% raw %}
% This is a Unicode file.
\documentclass[12pt]{article}
\usepackage{multicol} % just to get narrow columns on one page
\usepackage{polyglossia} % the multilingual support package
% for XeLaTeX - includes Sanskrit.
% Next, from the polyglossia manual:
\setdefaultlanguage{english} % this is mostly going to be English text, with
\setotherlanguage{sanskrit} % some Sanskrit embedded in it.
% These will call appropriate hyphenation.
\usepackage{xltxtra} % standard for nearly all XeLaTeX documents
\defaultfontfeatures{Mapping=tex-text} % ditto
\setmainfont{Gandhari Unicode} %could be any Unicode font

% Now define some Devanagari fonts:
% At least *one* font family must be called \sanskritfont or \devanagarifont,
% so that XeTeX loads all hyphenation and other stuff for Sanskrit.
% Once the Sanskrit ``intelligence'' is loaded, it can be invoked at
% other places as needed using \selectlanguage{sanskrit}
%
% John Smith's Nakula, input using Velthuis transliteration
\newfontfamily
\sanskritfont [Script=Devanagari,Mapping=velthuis-sanskrit]{Nakula}
% John Smith's Sahadeva, input using Velthuis transliteration
\newfontfamily
\sahadevafont [Script=Devanagari,Mapping=velthuis-sanskrit]{Sahadeva}
% John's Sahadeva, input using scholarly romanisation in Unicode
\newfontfamily
\sahadevaunicodefont [Script=Devanagari,Mapping=RomDev]{Sahadeva}
% Microsoft's Mangal font (ugh!), input using standard romanisation in Unicode.
\newfontfamily
\mangalfont [Script=Devanagari,Mapping=RomDev]{Mangal}
% Somdev's RomDev.map is used above to get the mapping
% from Unicode -> Devanāgarī. Zdenek Wagner's velthuis-sanskrit.map
% is used to get the Velthuis->Devanāgarī mapping. These are the files
% that XeTeX uses to make all the conjunct consonants without needing
% any external preprocessor (like the old devnag.c program).
% % Set up the font commands:
%
\newcommand{\velt}[1]{{{\selectlanguage{sanskrit}\sanskritfont #1}}}
\newcommand{\saha}[1]{{{\selectlanguage{sanskrit}\sahadevafont#1}}}
\newcommand{\sahauni}[1]{{{\selectlanguage{sanskrit}\sahadevaunicodefont #1}}}
\newcommand{\mangaluni}[1]{{{\selectlanguage{sanskrit}\mangalfont #1}}}
% \textssanskrit, above, is a Polyglossia command that gets Sanskrit hyphenation right.
% ... and here we go!
\begin{document}
\begin{multicols}{2} % narrow cols to force plenty of hyphenation
\large % ditto.
\begin{enumerate}
\item[1]
With Xe\LaTeX\ it's easy to typeset Velthuis encoded Devanagari like the following example, without using a preprocessor:
\velt{sugataan sasutaan sadharmakaayaan pra.nipatyaadarato 'khilaa.m"sca vandyaan|
sugataatmajasa.mvaraavataara.m kathayi.syaami yathaagama.m samaasaat||} Bodhicaryāvatāra 1,1.
NB: automatic hyphenation.
\item[2]
A different Devanāgarī font:
\saha{sugataan sasutaan sadharmakaayaan pra.nipatyaadarato 'khilaa.m"sca vandyaan|
sugataatmajasa.mvaraavataara.m kathayi.syaami yathaagama.m samaasaat||} Bodhicaryāvatāra 1,1.
\item[3]
Another sentence: \saha{ratnojjvalastambhamanorame.su muktaamayodbhaasivitaanake.su|
svacchojjvalasphaa.tikaku.t.time.su sungandhi.su snaanag.rhe.su te.su||} 2,10.
\item[4]
Now, thanks to Somdev's RomDev.map, we can input in Unicode, using standard scholarly transliteration, and get Devanāgarī generated for us automatically:
\sahauni{āsīdrājā nalo nāma vīrsenasuto balī||\par }
\item[5]
Plain Unicode input, no tricks:
āsīdrājā nalo nāma vīrsenasuto balī||
\item[6]
Plain Unicode romanisation input, no tricks:
\mangaluni{āsīdrājā nalo nāma vīrsenasuto balī||\par }
Plain Unicode Devanāgarī input, no tricks:
{\mangalfont आसीद्राजा नलो नाम वीरसेनसुतो बली|\par}
\end{enumerate}
\end{multicols}

\noindent
English and Devanāgarī are both doing okay. The only thing that isn't hyphenating well yet is Sanskrit in roman transliteration.

Other nice stuff becomes easy. E.g., define a command \verb|\example| that prints a romanised word in Nāgarī, and then repeats it in romanisation, in parentheses:

\verb|\newcommand\example[1]{\sahauni{#1}~(\emph{#1})}|\newcommand\example[1]{\sahauni{#1}~(\emph{#1})}

Input: \verb|\example{ekadhā}|

Output: \example{ekadhā}
\end{document}
%that's all folks!
{% endraw %}
```

Once those required fonts were added to the system (all found for free via Search Engine), we had our Sanscrit (and Bengali).

So now I can run the following bash script to render:

``

```

    lilypond-book --latex-program=xelatex --pdf hymnal.lytex
    xelatex hymnal.tex
    xelatex hymnal.tex
    find . -maxdepth 1 -type d -name '??' -exec rm -rf {} \;
    rm *.aux *.bcf *.dep *.out *.run.xml *.toc tmpx* snippet-map* snippet-names*
    open hymnal.pdf
```

But I would like to also get xelatex working with arara…

That was easy:

``

```

    % arara: lilypond: {options: "--latex-program=xelatex --pdf"}
    % arara: xelatex: { files: [ 'hymnal.tex' ] }
```

The [raw files on GitHub](https://github.com/MikeiLL/hymnal-Vol-II).

&lt;!––nextpage––&gt;

Automatically creating an Index of terms took a little while to figure out. But it’s actually pretty simple.

We want the package:
 \\usepackage{imakeidx} % index

Then we need to call the `\makeindex` command *within* the preamble.

Wherever we want it within the book we add the command: `\printindex`, and within the document, for an item we want to include in the index we add:

```
\index{Shango}

```

To include images I think they need to be PDFs, supposedly [Inkscape](http://macappstore.org/inkscape/) can transform SVGs to PDF:

```
inkscape -D -z --file=AllOnePose.svg --export-pdf=poses/AllOnePose.pdf --export-latex

```

Now we can use Arabic via [ArabXeTeX](http://ctan.org/pkg/arabxetex):

``

```

\usepackage{arabxetex}

\begin{arab}[fullvoc]
لَا إِلٰهَ إِلَّا الله مُحَمَّدٌ رَسُولُ الله
\end{arab}
```

I had to install the [Amiri font](http://www.amirifont.org/) by Khaled Hosny.
