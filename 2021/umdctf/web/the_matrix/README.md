# The Matrix

## Challenge:

Oh no! It looks like the robots have taken over! Infilitrate their site and save the world! But beware, they only allow one of them to access it.

`curl http://chals5.umdctf.io:4000`

## Solution:

The web page has a few links, with the most prominent being “Enter the matrix!” in the center.

If we click it, we’re told “This page is for robots only, you are not allowed to access this content!”.

If we update our user agent to `Googlebot/2.1 (+http://www.google.com/bot.html)`, we’re immediately given access and a hello, “Greetings Fellow Robot Overlord”.

Our flag is displayed for us: `UMDCTF-{r0b0t_r3b3ll!0n}`.
