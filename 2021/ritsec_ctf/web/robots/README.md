# Robots

## Challenge:

Robots are taking over. Find out more.

`34.69.61.54:5247`

## Solution:

If we navigate to the provided site we don’t see much, but `/robots.txt` gives us a lot to go on.

If we search the page for `flag`, we quickly find a matching directive:

```
Allow: /flag/UlN7UjBib3RzX2FyM19iNGR9
```

Navigating to `/flag/UlN7UjBib3RzX2FyM19iNGR9` doesn’t work.

But if we Base64 decode `UlN7UjBib3RzX2FyM19iNGR9`, we get our flag: `RS{R0bots_ar3_b4d}`.
