# gdpr

## Challenge:

Foiled by gdpr again...

`chal.b01lers.com:1004`

## Solution:

We’re taken to a web page with a privacy policy. None of the links seem to be active, `robots.txt` doesn’t load, and the only thing that sticks out immediately is `comic_sans.woff2` (web font file) being downloaded.

If we refresh the page, we can see the entire page shifting. It looks like the policy we’re seeing is a GDPR modal popup.

If we view source and search for `flag`, we see a link to `/flag_policy`.

Navigating there, we receive our flag: `bctf{annoying_but_good?}`.
