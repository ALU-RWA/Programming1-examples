# I want you to only print the hashtags contained in the tweets above.
# In other words, out of all the words contained in all the tweets above, only print
# The ones that begin with the character '#'

tweet1 = "Meet Fred Nelson, founder of @Maliasili and speaker @ TheBusinessofConservationConference. He gravitates toward creating new organizations & ventures as a self-identifying ‘conservation entrepreneur’. He specializes in community-based conservation in Africa. #ConservationMatters"
tweet2 = "Let the drums roll...Our MBA application is open! Start your application today to begin your programme in March 2019! Apply at: https://mba.alusb.com/apply/  #AfricasMBA #LearnLead"
tweet3 = "Since taking office in Apr 2018, Ethiopian PM Abiy Ahmed has continued to deliver political and economic reforms. Edosa Leta and Eden Wagari both Ethiopians studying at @ALUEducation  in Rwanda will be joining me live on @cnbcafrica to analyse the news from their country. 1600hrs"
tweet4 = "Work Experience is so crucial we’ve made it part of our curriculum. Gain exposure to real industry problems and use the skills you've learned. When you graduate you'll have an entire year's worth of valuable work experience! #Internship #ALU #ALC #ProblemSolving #WorkExperience"
tweet5 = "'Africa needs to reimagine education completely. Remove focus from facts and figures and focus on learning how to learn and how to solve problems.' - @FredSwaniker #FutureProofAfrica"

tweets = [tweet1, tweet2, tweet3, tweet4, tweet5]
index = 0
while index < len(tweets):
    words = tweets[index].split(" ")

    n = 0
    while n < len(words):
        if words[n].startswith("#"):
            print(words[n])
        n += 1  # n = n + 1

    index = index + 1

example = "no one lo#oks at my #examples #youngLeaders"



