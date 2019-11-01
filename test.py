from bs4 import BeautifulSoup
from textblob import TextBlob

file_list = {
    "the-intensifying-impacts-of-the-innovation-economy": "./POSTS/the-intensifying-impacts-of-the-innovation-economy.html",
    "optimize-your-insurance-engine-with-data-consortiums": "./POSTS/optimize-your-insurance-engine-with-data-consortiums.html",
    "3-detours-taking-your-data-strategy-off-track": "./POSTS/3-detours-taking-your-data-strategy-off-track.html",
    "the-nature-of-risk-is-changing-what-does-that-mean-for-leadership": "./POSTS/the-nature-of-risk-is-changing-what-does-that-mean-for-leadership.html",
    "data-is-insurances-ultimate-equalizer": "./POSTS/data-is-insurances-ultimate-equalizer.html",
    "changing-nature-of-risk-what-does-it-mean-for-leadership": "./POSTS/changing-nature-of-risk-what-does-it-mean-for-leadership.html",
    "whats-your-analytics-story": "./POSTS/whats-your-analytics-story.html",
    "commercial-autos-wild-ride-continues": "./POSTS/commercial-autos-wild-ride-continues.html",
    "little-things-olympians-can-teach-executives": "./POSTS/little-things-olympians-can-teach-executives.html",
    "secret-ingredient-highly-innovative-teams-change-game": "./POSTS/secret-ingredient-highly-innovative-teams-change-game.html",
    "first-conference-features-innovators-winter-fun-vail": "./POSTS/first-conference-features-innovators-winter-fun-vail.html",
    "real-momentum-building-data-analytics-property-casualty": "./POSTS/real-momentum-building-data-analytics-property-casualty.html",
    "valens-2014-outlook-commercial-lines": "./POSTS/valens-2014-outlook-commercial-lines.html",
    "underwriter-future": "./POSTS/underwriter-future.html",
    "predictive-analytics-helps-insurance-agents-customers": "./POSTS/predictive-analytics-helps-insurance-agents-customers.html",
    "5-top-challenges-carriers-face-rapidly-changing-industry": "./POSTS/5-top-challenges-carriers-face-rapidly-changing-industry.html",
    "misclassified-payroll-matters-tune-76-8-billion": "./POSTS/misclassified-payroll-matters-tune-76-8-billion.html",
    "tackling-underwriting-profitability-head": "./POSTS/tackling-underwriting-profitability-head.html",
    "what-makes-underwriter-adoption-of-predictive-analytics-challenging": "./POSTS/what-makes-underwriter-adoption-of-predictive-analytics-challenging.html",
    "change-doesnt-have-to-be-painful": "./POSTS/change-doesnt-have-to-be-painful.html",
    "it-is-all-about-price": "./POSTS/it-is-all-about-price.html",
    "you-need-more-visibility": "./POSTS/you-need-more-visibility.html",
    "welcome-to-this-week-in-analytics": "./POSTS/welcome-to-this-week-in-analytics.html",
    "goosebump-moments-career": "./POSTS/goosebump-moments-career.html",
    "market-share-consolidation-moves-quickly": "./POSTS/market-share-consolidation-moves-quickly.html",
    "clock-strikes-midnight": "./POSTS/clock-strikes-midnight.html",
    "beauty-model-maintenance-told-davinci": "./POSTS/beauty-model-maintenance-told-davinci.html",
    "four-things-im-thankful": "./POSTS/four-things-im-thankful.html",
    "3-takeaways-insuretech-connect": "./POSTS/3-takeaways-insuretech-connect.html",
    "back-basics-predictive-analytics-reducing-loss-ratio": "./POSTS/back-basics-predictive-analytics-reducing-loss-ratio.html",
    "race-bottom-myth": "./POSTS/race-bottom-myth.html",
    "pursuing-better-rating-predictive-analytics-can-help": "./POSTS/pursuing-better-rating-predictive-analytics-can-help.html",
    "the-magic-bullet": "./POSTS/the-magic-bullet.html",
    "two-critical-concerns-work-comp-insurers": "./POSTS/two-critical-concerns-work-comp-insurers.html",
    "the-power-of-the-underwriter": "./POSTS/the-power-of-the-underwriter.html",
    "5-must-dos-data-collection": "./POSTS/5-must-dos-data-collection.html",
    "commercial-autos-wild-ride": "./POSTS/commercial-autos-wild-ride.html",
    "meet-bob-claims-superhero": "./POSTS/meet-bob-claims-superhero.html",
    "market-leaving-behind-valens-roi-study-showcases-insurers-leading-work-comp": "./POSTS/market-leaving-behind-valens-roi-study-showcases-insurers-leading-work-comp.html",
    "davids-data-analytics-slingshot": "./POSTS/davids-data-analytics-slingshot.html",
    "insurtech-disruption-end-distribution": "./POSTS/insurtech-disruption-end-distribution.html",
    "sometimes-you-have-to-say-no-to-the-data": "./POSTS/sometimes-you-have-to-say-no-to-the-data.html",
    "distraction-danger": "./POSTS/distraction-danger.html",
    "industry-talent-crisis": "./POSTS/industry-talent-crisis.html",
    "3-insurance-industry-lessons-2016": "./POSTS/3-insurance-industry-lessons-2016.html",
    "insuretech-adaptation-not-just-disruption": "./POSTS/insuretech-adaptation-not-just-disruption.html",
    "3-reasons-insurers-lack-strong-pricing-helps-thrive": "./POSTS/3-reasons-insurers-lack-strong-pricing-helps-thrive.html",
    "half-work-comp-policies-include-payroll-errors": "./POSTS/half-work-comp-policies-include-payroll-errors.html",
"valen-analytics-2016-scholarship-award-winner": "./POSTS/valen-analytics-2016-scholarship-award-winner.html",
    "insurance-consumers-want-innovation": "./POSTS/insurance-consumers-want-innovation.html",
    "best-time-implement-insurance-predictive-model": "./POSTS/best-time-implement-insurance-predictive-model.html",
    "will-predictive-analytics-replace-underwriters": "./POSTS/will-predictive-analytics-replace-underwriters.html",
    "innovators-dilemma-a-constant-across-every-industry-even-insurance": "./POSTS/innovators-dilemma-a-constant-across-every-industry-even-insurance.html",
    "severe-implications-of-payroll-misclassification-premium-fraud": "./POSTS/severe-implications-of-payroll-misclassification-premium-fraud.html",
    "the-perfect-pair-human-judgement-and-analytics": "./POSTS/the-perfect-pair-human-judgement-and-analytics.html",
    "what-really-drives-insurance-market-cycles": "./POSTS/what-really-drives-insurance-market-cycles.html",
    "the-angst-of-an-insurance-industry-outlook-report": "./POSTS/the-angst-of-an-insurance-industry-outlook-report.html",
    "planning-for-a-predictive-analytics-implementation": "./POSTS/planning-for-a-predictive-analytics-implementation.html",
    "how-to-gain-organizational-buy-in-of-predictive-analytics": "./POSTS/how-to-gain-organizational-buy-in-of-predictive-analytics.html",
    "1st-step-in-a-predictive-analytics-implementation": "./POSTS/1st-step-in-a-predictive-analytics-implementation.html",
    "roadblocks-to-insurance-innovation": "./POSTS/roadblocks-to-insurance-innovation.html",
    "insurance-carriers-race-for-the-top-10-of-business": "./POSTS/insurance-carriers-race-for-the-top-10-of-business.html",
    "is-insurance-an-easy-target-for-criticism": "./POSTS/is-insurance-an-easy-target-for-criticism.html",
    "actuaries-vs-underwriters-who-wins": "./POSTS/actuaries-vs-underwriters-who-wins.html",
    "loss-ratio-suffers-in-insurance-if-you-do-this-wrong": "./POSTS/loss-ratio-suffers-in-insurance-if-you-do-this-wrong.html",
    "bringing-insurance-into-the-21st-century": "./POSTS/bringing-insurance-into-the-21st-century.html",
    "predictive-analytics-implementation-steps": "./POSTS/predictive-analytics-implementation-steps.html",
    "how-predictive-analytics-combats-adverse-selection": "./POSTS/how-predictive-analytics-combats-adverse-selection.html",
    "the-future-of-the-insurance-industry-is-now": "./POSTS/the-future-of-the-insurance-industry-is-now.html",
    "predictive-analytics-is-not-a-magic-bullet": "./POSTS/predictive-analytics-is-not-a-magic-bullet.html",
    "how-to-raise-a-predictive-model-you-can-live-with": "./POSTS/how-to-raise-a-predictive-model-you-can-live-with.html",
    "implementing-predictive-analytics-youre-wrong": "./POSTS/implementing-predictive-analytics-youre-wrong.html",
    "two-predictive-statistics-you-need-to-evaluate-your-model": "./POSTS/two-predictive-statistics-you-need-to-evaluate-your-model.html",
    "3-lessons-insurance-customers-taught-us": "./POSTS/3-lessons-insurance-customers-taught-us.html",
    "big-data-in-insurance-a-glimpse-into-2015": "./POSTS/big-data-in-insurance-a-glimpse-into-2015.html",
    "insurance-industry-most-exciting-in-2015": "./POSTS/insurance-industry-most-exciting-in-2015.html",
    "insurance-data-analytics-christmas-carol": "./POSTS/insurance-data-analytics-christmas-carol.html",
    "a-farewell-letter-to-traditional-insurance-loss-ratio": "./POSTS/a-farewell-letter-to-traditional-insurance-loss-ratio.html",
    "predictive-analytics-giving-thanks-in-2014": "./POSTS/predictive-analytics-giving-thanks-in-2014.html",
    "top-6-myths-about-predictive-modeling-and-analytics": "./POSTS/top-6-myths-about-predictive-modeling-and-analytics.html",
    "insurance-data-and-analytics-revolution": "./POSTS/insurance-data-and-analytics-revolution.html",
    "valen-summit-2015-announced-gold-rush": "./POSTS/valen-summit-2015-announced-gold-rush.html",
    "workers-compensation-underwriting-for-baldwin-lyons": "./POSTS/workers-compensation-underwriting-for-baldwin-lyons.html",
    "risk-score-big-news-for-insurance-industry": "./POSTS/risk-score-big-news-for-insurance-industry.html",
    "how-to-grow-profitably-and-avoid-adverse-selection": "./POSTS/how-to-grow-profitably-and-avoid-adverse-selection.html",
    "identify-loss-ratio-difference-between-loss-free-workers-compensation-policies": "./POSTS/identify-loss-ratio-difference-between-loss-free-workers-compensation-policies.html",
    "how-predictive-analytics-helps-insurance-company-competitors": "./POSTS/how-predictive-analytics-helps-insurance-company-competitors.html",
    "farm-bureau-financial-services-analytics-implementation": "./POSTS/farm-bureau-financial-services-analytics-implementation.html",
    "pricing-insurance-policies": "./POSTS/pricing-insurance-policies.html",
    "insurer-eulogy-adverse-selection": "./POSTS/insurer-eulogy-adverse-selection.html",
    "valen-recognized-vice-president-joe-biden-stem-education": "./POSTS/valen-recognized-vice-president-joe-biden-stem-education.html",
    "meet-tomorrows-talent-challenge-2014-scholarship-recipient": "./POSTS/meet-tomorrows-talent-challenge-2014-scholarship-recipient.html",
    "1-thing-carriers-forget-preventing-fraud-can-save-millions": "./POSTS/1-thing-carriers-forget-preventing-fraud-can-save-millions.html",
    "500m-work-comp-fraud-new-york-tip-iceberg": "./POSTS/500m-work-comp-fraud-new-york-tip-iceberg.html",
    "valen-promotes-insurance-careers-nations-top-business-leaders": "./POSTS/valen-promotes-insurance-careers-nations-top-business-leaders.html",
    "1-secret-success-advanced-analytics": "./POSTS/1-secret-success-advanced-analytics.html",
    "guest-post-todays-small-commercial-automation-enough": "./POSTS/guest-post-todays-small-commercial-automation-enough.html",
    "2014-outlook-personal-lines": "./POSTS/2014-outlook-personal-lines.html",
    "550-commercial-underwriters-cant-wrong": "./POSTS/550-commercial-underwriters-cant-wrong.html",
    "valen-welcomes-fhm-new-customer": "./POSTS/valen-welcomes-fhm-new-customer.html",
    "will-best-talent-choose-insurance": "./POSTS/will-best-talent-choose-insurance.html",
    "coolest-thing-weve-announced": "./POSTS/coolest-thing-weve-announced.html",
    "valens-new-product-helps-homeowners-carriers-chart-course-profitability": "./POSTS/valens-new-product-helps-homeowners-carriers-chart-course-profitability.html",
}

all_data = {}

def extract_blog(filename):
    post_data = {}
    with open(filename) as html_file:
        html_doc = html_file.read()
        soup = BeautifulSoup(html_doc, "html.parser")
        #-----------------------------------------------------------------------
        # GET CONTENT
        #-----------------------------------------------------------------------
        content = soup.find(class_="entry-content")
        #-----------------------------------------------------------------------
        # GET TITLE 
        #-----------------------------------------------------------------------
        title = soup.find(class_="entry-title")
        #-----------------------------------------------------------------------
        # GET AUTHOR 
        #-----------------------------------------------------------------------
        author = soup.find(class_="entry-meta")
        #-----------------------------------------------------------------------
        # SENTEMENT ANALYSIS 
        #-----------------------------------------------------------------------
        sa = TextBlob(content.text)
        #-----------------------------------------------------------------------
        # RETURN DATA 
        #-----------------------------------------------------------------------
        post_data = {
            "content": content.text,
            "title": title.text,
            "author": author.text,
            "polarity": sa.sentiment.polarity,
            "subjectivity": sa.sentiment.subjectivity,
        }
    return post_data

if __name__ == "__main__":
    all_data = {}
    for blog_file_name, blog_file_path in file_list.items():
        print(blog_file_name)
        data = extract_blog(blog_file_path)
        all_data[blog_file_name] = data
    import json
    with open("report.json", "w") as report:
        report.write(json.dumps(all_data))
