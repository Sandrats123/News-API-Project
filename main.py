# main.py
from crud.insert import create_user
from crud.read import get_user
from crud.update import update_user
from crud.delete import delete_user
from crud.news_fetch import fetch_news_data
from crud.create_table import create_users_table  # Import the new

def main():
    # Create the users table if it doesn't exist
    #create_users_table()
        # Converting the previous 30 English news entries into the required format:

    create_user(
        id=1,
        timestamp="2025-01-15T04:35:10Z",
        author="Investing.com",
        sentiments_score=0.0,
        description="China’s UBTech Robotics rallies on Foxconn partnership."
    )

    create_user(
        id=2,
        timestamp="2025-01-15T04:32:33Z",
        author="Investor's Business Daily",
        sentiments_score=-0.0625,
        description="The Nasdaq fell again in a mixed session, with Nvidia and Tesla reversing lower. CPI inflation is due while JPMorgan leads bank earnings."
    )

    create_user(
        id=3,
        timestamp="2025-01-15T04:17:31Z",
        author="aol.com",
        sentiments_score=-0.0875,
        description="The rise of Tesla Inc‘s Cybertruck sales in the U.S. last year weighed heavily upon the company’s other luxury offerings, including the Model S sedan and the Model X SUV, according to recent data from automotive research firm Kelley Blue Book."
    )

    create_user(
        id=4,
        timestamp="2025-01-15T04:11:03Z",
        author="Ross O'keefe",
        sentiments_score=0.275,
        description="Donald Trump has received an honor indicative of his particular love for soda with his inauguration less than a week away: his own inaugural Diet Coke bottle."
    )

    create_user(
        id=5,
        timestamp="2025-01-15T04:06:27Z",
        author="zerohedge.com",
        sentiments_score=0.0067,
        description="China's BYD Is Only Real Contender To Tesla's Global EV Market Share Dominance."
    )

    create_user(
        id=6,
        timestamp="2025-01-15T04:02:01Z",
        author="TOI World Desk",
        sentiments_score=0.0367,
        description="Southern California is facing critical wildfire conditions due to dry winds and parched terrain. With significant evacuation orders in place, power outages affecting thousands, and arrests made for wildfire-related offenses, the National Weather Service warns..."
    )

    create_user(
        id=7,
        timestamp="2025-01-15T03:33:16Z",
        author="Steve Hanley",
        sentiments_score=0.15,
        description="If you are following the EV revolution in China, you can be forgiven if you are confused. The latest headline from the Associated Press says, 'China’s electric car sales grew in 2024 as sales of gasoline cars plunged.'"
    )

    create_user(
        id=8,
        timestamp="2025-01-15T03:21:41Z",
        author="Cynthia Littleton",
        sentiments_score=0.0111,
        description="The Securities and Exchange Commission filed a lawsuit Tuesday against Elon Musk, accusing the owner of X of failing to properly disclose his purchases of Twitter stock prior to his acquisition of the social media platform in 2022."
    )

    create_user(
        id=9,
        timestamp="2025-01-15T03:11:17Z",
        author="cnbc.com",
        sentiments_score=1.0,
        description="The Nasdaq fell for the fifth day in a row. All Magnificent Seven stocks dropped, with Meta, Tesla, and Nvidia registering the biggest losses, in that order."
    )

    create_user(
        id=10,
        timestamp="2025-01-15T03:10:57Z",
        author="webdesk@voanews.com (Reuters)",
        sentiments_score=-0.0205,
        description="Elon Musk was sued on Tuesday by the U.S. Securities and Exchange Commission, which accused the world's richest person of waiting too long to disclose in 2022 he had amassed a large stake in Twitter."
    )

    create_user(
        id=11,
        timestamp="2025-01-15T03:04:40Z",
        author="RT",
        sentiments_score=0.0563,
        description="Elon Musk is facing a lawsuit over accusations that he failed to promptly disclose his initial acquisition of a significant stake in Twitter."
    )

    create_user(
        id=12,
        timestamp="2025-01-15T03:01:42Z",
        author="Al Jazeera",
        sentiments_score=-0.3167,
        description="US Securities and Exchange Commission says Musk's failure to disclose stake allowed him to underpay $150m for shares."
    )

    create_user(
        id=13,
        timestamp="2025-01-15T02:58:25Z",
        author="LSW Team",
        sentiments_score=0.082,
        description="Why is Rivian Stock So Low? Rivian, an American electric vehicle (EV) manufacturer, has been a highly anticipated stock among investors."
    )

    create_user(
        id=14,
        timestamp="2025-01-15T02:47:00Z",
        author="Martha Kelner",
        sentiments_score=-0.0667,
        description="At 4.30pm last Tuesday afternoon, a dark grey smoke cloud loomed over North Mount Holyoke Avenue in Pacific Palisades, obscuring the setting sun."
    )

    create_user(
        id=15,
        timestamp="2025-01-15T02:37:35Z",
        author="dpa",
        sentiments_score=0.0,
        description="Elon Musk meldete beim Twitter-Kauf zu spät das Überschreiten einer wichtigen Beteiligungs-Marke. Das is seit Jahren bekannt."
    )

    create_user(
        id=16,
        timestamp="2025-01-15T02:23:40Z",
        author="Zerohedge.com",
        sentiments_score=0.0563,
        description="Tesla's dominance faces growing competition, but it's still the EV leader in many global markets."
    )

    create_user(
        id=17,
        timestamp="2025-01-15T02:16:41Z",
        author="nieuwsblad.be",            
        sentiments_score=-0.1,           
        description="De Amerikaanse markttoezichthouder, Securities and Exchange Commission (SEC), heeft Elon Musk bij een federale rechtbank in Washington aangeklaagd vanwege een vermeende overtreding van de effectenwetgeving."
    )

    create_user(
        id=18,
        timestamp="2025-01-15T06:16:47Z",
        author="Oliver Schwuchow",            
        sentiments_score=-0.0,           
        description="In China kann man das neue Tesla Model Y seit ein paar Tagen bestellen, doch jetzt geht es auch in Europa los, denn diese Woche ist das erste Model Y mit der neuen Optik vom Band gerollt."
    )

    create_user(
        id=19,
        timestamp="2025-01-15T07:10:30Z",
        author="The Verge",            
        sentiments_score=0.4,           
        description="Apple is reportedly working on a foldable iPad for release in 2026. The device is expected to feature a hybrid OLED display and could potentially replace the iPad Pro lineup."
    )

    create_user(
        id=20,
        timestamp="2025-01-15T08:42:12Z",
        author="BBC News",            
        sentiments_score=0.2,           
        description="A major breakthrough in cancer research could revolutionize treatment methods. Scientists have developed a new drug targeting resistant tumor cells."
    )

    create_user(
        id=21,
        timestamp="2025-01-15T09:15:49Z",
        author="Reuters",            
        sentiments_score=-0.3,           
        description="Global markets faced turbulence today as inflation fears pushed stocks lower. Analysts predict continued volatility in the coming weeks."
    )

    create_user(
        id=22,
        timestamp="2025-01-15T10:20:55Z",
        author="TechCrunch",            
        sentiments_score=0.5,           
        description="OpenAI announces GPT-5, the next evolution of its AI language model, which boasts unprecedented accuracy and contextual understanding."
    )

    create_user(
        id=23,
        timestamp="2025-01-15T11:35:00Z",
        author="Al Jazeera",            
        sentiments_score=-0.1,           
        description="Protests erupt across major cities in Europe following proposed reforms to pension laws, with demonstrators demanding fairer treatment."
    )

    create_user(
        id=24,
        timestamp="2025-01-15T12:50:45Z",
        author="Bloomberg",            
        sentiments_score=0.3,           
        description="Tesla's latest battery technology promises to double vehicle range while cutting production costs by 25%."
    )

    create_user(
        id=25,
        timestamp="2025-01-15T13:12:30Z",
        author="The Guardian",            
        sentiments_score=0.1,           
        description="The UK government has pledged an additional £2 billion to tackle homelessness, aiming to house 20,000 individuals by 2027."
    )

    create_user(
        id=26,
        timestamp="2025-01-15T14:07:21Z",
        author="CNBC",            
        sentiments_score=-0.2,           
        description="Oil prices hit a three-month low today as global demand slows, sparking concerns among energy producers."
    )

    create_user(
        id=27,
        timestamp="2025-01-15T15:22:14Z",
        author="CNN",            
        sentiments_score=0.4,           
        description="NASA successfully tests its new Mars rover prototype, designed to explore the planet's polar ice caps in search of water."
    )

    create_user(
        id=28,
        timestamp="2025-01-15T16:50:37Z",
        author="Forbes",            
        sentiments_score=0.2,           
        description="A new startup is disrupting the healthcare industry by offering AI-driven diagnostic tools that improve patient outcomes and reduce costs."
    )

    create_user(
        id=29,
        timestamp="2025-01-15T17:45:29Z",
        author="Wall Street Journal",            
        sentiments_score=0.0,           
        description="The Federal Reserve signals a potential pause in interest rate hikes, citing signs of cooling inflation and steady economic growth."
    )

    create_user(
        id=30,
        timestamp="2025-01-15T18:30:42Z",
        author="Hindustan Times",            
        sentiments_score=-0.1,           
        description="India experiences severe winter conditions, with record-low temperatures disrupting daily life in several northern states."
    )

    create_user(
        id=31,
        timestamp="2025-01-15T19:05:17Z",
        author="New York Times",            
        sentiments_score=0.3,           
        description="Advancements in renewable energy technologies have led to a significant decrease in carbon emissions globally, experts report."
    )

    create_user(
        id=32,
        timestamp="2025-01-15T20:12:11Z",
        author="The Times of India",            
        sentiments_score=0.4,           
        description="A historic cricket match ends with India defeating Australia in a thrilling last-over chase, delighting millions of fans."
    )
    

    # Example CRUD operations

    # Create a new user
    
   
    # Fetch news data
    #fetch_news_data(create_users_table)

    # Read user data
    #get_user(1)

    # Update user data
    #update_user(1, 'john1_doe_updated')

    # Delete the user
    #delete_user(4)

if __name__ == "__main__":
    main()