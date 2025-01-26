# AutoBib: Automatically adding bibtex citations to LaTeX files
It is cumbersome to add bibtex citations to LaTeX files manually.
You copy the paper title to Google Scholar, search, click the bibtex citing, copy, and paste.
Whoof, it is a lot of repeated works to do.

Now, things are getting better 😄

You need just add the paper title(s) in a json file `references.json` like the following:
```json
[
    ...
    [
        "", # keep an empty string for a newly-added title; will be filled by get_bib.py
        "Improved baselines with visual instruction tuning"
    ],
    ...
]
```
Then, simply run `python get_bib.py`. This will automatically add bibtex citations from Google Scholar to your bib file `egbib.bib`, and filling the empty string with the citaion key. Those that have been added will not be processed again.
