# #OSINTChallenge

## Challenge:

The CEO of Geno’s company loves local art and nature. Where was she when she took the photo in her Twitter background? (Wrap the answer in RS{} and use underscores between each word.)

## Solution:

Let’s go back to Geno’s LinkedIn profile and visit his company’s page. Unfortunately, all employee names there are private so we can see our CEO’s picture but we don’t know their name.

Luckily for us, LinkedIn profiles are often indexed by search engines. A Google search for "Chief Executive Officer at Bridgewater Investigations" gives us a name: JoAnne Turner-Frey. Clicking through at first blocks our access. But, trying again, we can view her profile directly and even see her contact details.

That contact information on the profile doesn’t give us a Twitter account, but we do get an email: joanne.m.turner94@gmail.com. Unfortunately it doesn’t show up anywhere. But if we go to Twitter and search “Bridgewater Investigations”, we find her profile.

The header image on her profile is our only clue:

<img src="peace.jpg" alt="An artistic peace sign." width="600">

As expected, reverse image search doesn’t help us. We’ll need to figure this out with the information we have.

We know this is likely near Rochester, and we know JoAnne is a fan of Lake Ontario. If we run a Google search for `"peace sign" rochester park ny` we get our flag: `RS{Durand_Eastman_Park}`.
