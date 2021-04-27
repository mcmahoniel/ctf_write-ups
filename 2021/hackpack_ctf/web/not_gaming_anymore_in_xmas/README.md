# "N"ot "G"am"I"ng a"N"ymore in "X"mas

## Challenge:

Can you login as admin? http://no-gaming-anymore-in-xmas.ctf2021.hackpack.club

## Solution:

We have a link to a web page with a password input and nothing else.

Using an apostrophe doesn’t result in an error or any messaging – perhaps this isn’t a SQL injection challenge.

The title of the challenge gives us a clue, this will have something to do with NGINX.

If we look at the page source, we can see a hidden debug field. Changing debug from `0` to `1` and submitting another password returns the entire NGINX configuration:

```
Let me check again my nginx conf:
server {
listen 80;
server_name localhost;

root /etc/nginx;
index index.html;

location /maybehereimportantstuff {
try_files $uri $uri/ =404;
}
}
```

If we navigate to `/maybehereimportantstuff`, we see our flag: `flag{ng1nx_m1sconf1g_c4n_b3_h4rmful}`.
