# Bad Traffic

## Challenge:

That APT might’ve compromised our networks. We’ve included a PCAP of suspicious activity. What tool is the APT using to steal data? (Wrap the answer in RS{})

https://drive.google.com/file/d/1UC0-huY5P_ymD8yQg5ag-3WA-crKjvOy/view?usp=sharing


## Solution:

The Google Drive link points to `bad_traffic.pcapng`. We could analyze this in Wireshark, but maybe an online tool like [A-Packets](https://apackets.com/) will give us what we need.

When we load it up, DNS immediately sticks out to us:

We can see suspicious names like `group`, `passwd`, and `shadow` at the end of each DNS query. Now we need to find what DNS exfiltration tool presents this way.

After a little Google searching (using terms like `dns exfiltration` and `dns “passwd” ctf`), we find [an article talking about DNS exfiltration](https://resources.infosecinstitute.com/topic/bypassing-security-products-via-dns-data-exfiltration/). Scrolling down to their Wireshark screenshots, they show very similar packets. Jumbles of encoded text followed by suspicious names.

We can see that they’re using a tool called [DNSteal](https://github.com/m57/dnsteal), and there’s our flag: `RS{dnsteal}`.
