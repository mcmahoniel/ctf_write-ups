# Justin 2

## Challenge:

My friend is in danger and this was the only picture he could send me. Can you find the name of the street he is on? ex. UMDCTF-{Memory_Lane}

https://drive.google.com/drive/folders/1nfFmXuEMRuCOY6BvAAox1AWQPSCqgIhn?usp=sharing

## Solution:

We have what appears to be a still frame from a dashcam:

<img src="image.PNG" alt="Dashing" width="600">

We can see some text on the building to the right, it looks like “ЖИЛФОНД”. Google tells us this is Russian for “Housing”.

We can see a car license plate in front of us that appears to match the Russian plate format. The [three digit code on the right](https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Russia#Regional_codes) is for Novosibirsk Oblast, located in southwestern Siberia.

We can see a number of results for “ЖИЛФОНД” in that area. Clicking through, one sticks out. We’re shown a stadium with those large fixtures around the outside, containing lights and cellular antennae.

Navigating around the street, we eventually find our location:

<img src="place.png" alt="Gotcha" width="600">

The street name is our flag: `UMDCTF-{Ulitsa_Kamenskaya}`.
