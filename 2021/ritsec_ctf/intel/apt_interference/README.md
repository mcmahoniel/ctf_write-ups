# APT Interference

## Challenge:

Geno’s ex is speculated to be involved in his disappearance. Try to find some incriminating information on her social media. What nation-state is she working with? (Wrap the answer in RS{})

## Solution:

We had the solution to this when we finished Data Breach, but we didn’t know it at the time. Navigating to the root domain where the breached passwords were stored, https://ackaria.xyz/, we can see some questionable content:

<img src="ackaria.png" alt="Ransom" width="600">

That certainly looks like a suspicious nation-state. We have our flag: `RS{ackaria}`.
