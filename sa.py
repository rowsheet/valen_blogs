from textblob import TextBlob
testimonial = TextBlob("""
After an awkward exchange with a team official following Game 7 of the World Series in which he said he was "not employed by the team," free agent Gerrit Cole, a front-runner for the American League Cy Young Award, said his "thank you" to the Houston Astros and their fans via social media Thursday.

"Last night was a tough one for us and the heartbreak hasn't gotten any easier today," Cole tweeted Thursday. "Before I became an Astro I didn't know much about Houston, but after just two years you have made it feel like home. So here's what I know now. You have been overwhelmingly friendly, welcoming, and kind to my family and me. The Astros organization has been such a pleasure to play for, the Cranes are indeed special people and great owners. I've met lifelong friends on the team and in the community and learned a little about pitching along the way.

This is a relationship between a team and it's fans like no other that I know. Thank you for making us better people and better players. This was a great season. We have a lot to be proud of."
        """)
print(testimonial.sentiment)
