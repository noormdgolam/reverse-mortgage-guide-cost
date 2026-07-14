import os
import yaml

articles = [
    {
        "slug": "why-reverse-mortgage-appraisals-cost-more",
        "title": "Why Reverse Mortgage Appraisals Cost More Than Traditional Ones",
        "description": "Understand why FHA reverse mortgage appraisals often have higher fees than conventional appraisals and what the appraiser is looking for.",
        "category": "fees",
        "date": "2023-10-20",
        "takeaways": [
            "Reverse mortgage appraisals must strictly follow FHA guidelines, which are more rigorous.",
            "Appraisers must check for safety, security, and structural soundness, not just market value.",
            "Fees generally range from $450 to $700 and must be paid upfront."
        ],
        "content": """
If you've bought or sold a home recently, you might expect an appraisal to cost around $300 to $400. However, when you apply for a reverse mortgage, you might be surprised to find the appraisal fee quoted at $500, $600, or even $700. 

Why the sudden markup? Are lenders just price-gouging seniors? The answer lies in the strict federal requirements governing Home Equity Conversion Mortgages (HECMs).

## The FHA Appraisal Standard

Almost all reverse mortgages are insured by the Federal Housing Administration (FHA). Because the FHA is taking on the risk of guaranteeing the loan, they require a specific type of appraisal known as an **FHA Appraisal**.

A conventional appraisal simply determines the current market value of your property so the lender knows how much collateral they have. 

An FHA appraisal does that, *plus* it serves as a rigorous health and safety inspection. The appraiser is required to ensure the property meets the HUD Minimum Property Standards (MPS).

## What Extra Things Does the Appraiser Check?

Because they must act as both an appraiser and a quasi-inspector, FHA-approved appraisers spend more time on the property and have more liability, hence the higher fee. They will look closely at:

- **The Roof:** Does it have at least three years of remaining economic life? Are there active leaks?
- **The Foundation:** Are there severe cracks or water damage?
- **Systems:** Do the heating, plumbing, and electrical systems function properly and safely?
- **Paint:** For homes built before 1978, is there any chipping or peeling paint that could be a lead-based paint hazard?
- **Safety:** Are there handrails on staircases? Is there safe egress from bedrooms?

## What Happens if the House Fails?

If the appraiser notes that the house does not meet FHA standards, the reverse mortgage **can still proceed**, but with conditions. 

The lender will require that the necessary repairs be made. If the repairs are relatively minor (like installing a handrail or fixing a broken window), the lender might allow the cost of those repairs to be paid out of the reverse mortgage proceeds after closing. This is known as a "repair set-aside." 

If the repairs are major (like a failing foundation), you may be required to fix them out of pocket before the loan can be approved.

## Who Pays for the Appraisal?

The appraisal is one of the few closing costs that you must typically pay out of pocket, upfront, directly to the appraisal management company. It generally cannot be rolled into the loan balance, though if your loan successfully closes, some lenders offer promotions where they will credit the cost back to you.
        """
    },
    {
        "slug": "understanding-monthly-servicing-fee",
        "title": "Understanding the Monthly Servicing Fee on a Reverse Mortgage",
        "description": "Learn what the reverse mortgage servicing fee covers, how much it typically costs, and why it is added to your loan balance.",
        "category": "fees",
        "date": "2023-10-21",
        "takeaways": [
            "Servicing fees cover the administrative costs of maintaining your loan over time.",
            "They are capped by HUD at $30 to $35 per month.",
            "The fee is not paid out of pocket; it is added to your loan balance each month."
        ],
        "content": """
When reviewing the estimated costs for a reverse mortgage, you might notice a recurring charge called the **Servicing Fee**. While upfront fees like origination and title insurance make sense, many borrowers wonder why they need to pay an ongoing monthly fee just to keep the loan open.

## What is Loan Servicing?

After your reverse mortgage closes, the original lender will often sell the loan on the secondary market. A "loan servicer" takes over the day-to-day management of your account. 

Even though you aren't making monthly mortgage payments, the servicer still has a lot of ongoing administrative work to do. Their responsibilities include:

- Sending you monthly account statements.
- Disbursing your requested line of credit funds or monthly tenure payments.
- Monitoring your property tax and homeowners insurance payments to ensure you remain in compliance.
- Calculating and applying the ongoing interest and mortgage insurance premiums to your balance.
- Handling the eventual payoff and lien release when the loan becomes due.

The servicing fee compensates the company for these ongoing administrative duties.

## How Much is the Fee?

HUD strict caps how much a servicer can charge for a Home Equity Conversion Mortgage (HECM).
- For loans with an annually adjusting interest rate, the cap is **$30 per month**.
- For loans with a monthly adjusting interest rate, the cap is **$35 per month**.

Many modern lenders actually waive the servicing fee entirely as a competitive feature, effectively rolling the cost into the interest rate margin. If you see a high servicing fee on your estimate, it is worth asking the lender if they have a "no servicing fee" option.

## How Do You Pay It?

The servicing fee is designed so that it does not impact your monthly cash flow. **You do not write a check for the servicing fee.** 

Instead, the $30 or $35 is simply added to your loan balance every month, just like the accrued interest. 

## The Servicing Fee Set-Aside

Because the fee is guaranteed to the servicer for the life of the loan, HUD requires lenders to create a "Servicing Fee Set-Aside" at closing. 

The lender calculates the expected total cost of the servicing fee over your projected lifespan and "sets aside" that portion of your equity to guarantee the servicer gets paid. 

For example, if your life expectancy is 20 more years, the lender might set aside $7,200 ($30 x 12 months x 20 years) from your available funds. This money is *not* a lump sum charge; it is simply a portion of your equity that is walled off and unavailable for you to withdraw. As the months pass, the $30 is deducted from the set-aside and added to your loan balance.
        """
    },
    {
        "slug": "what-is-a-lender-credit-reverse-mortgage",
        "title": "What is a Lender Credit on a Reverse Mortgage?",
        "description": "A comprehensive guide to understanding lender credits, how they can eliminate your closing costs, and the mathematical trade-offs involved.",
        "category": "fees",
        "date": "2023-10-22",
        "takeaways": [
            "A lender credit is money the lender gives you to cover your upfront closing costs.",
            "You receive this credit in exchange for accepting a higher interest rate.",
            "It is highly beneficial if you only plan to keep the reverse mortgage for a few years."
        ],
        "content": """
If you are shopping around for a reverse mortgage, you might encounter a loan officer offering you a "zero closing cost" or "no origination fee" loan. Given that reverse mortgages are notorious for high upfront costs, this sounds too good to be true. 

Usually, this is achieved through a financial mechanism called a **Lender Credit**. 

## How a Lender Credit Works

In the mortgage industry, interest rates and upfront costs are inversely related. 

If you want the absolute lowest interest rate possible, you have to pay all the upfront fees (origination, title, appraisal, etc.). 

If you do not want to pay those upfront fees, the lender will pay them for you—but they will charge you a higher interest rate on the loan to recoup their money over time. This tradeoff is the lender credit.

The lender is essentially saying: *"We will give you a $6,000 credit today to cover your origination fee, but in exchange, your interest rate will be 7.5% instead of 6.5%."*

## The Mathematics of the Tradeoff

Deciding whether to take a lender credit comes down to one primary factor: **How long do you plan to keep the loan?**

Because a reverse mortgage is a negatively amortizing loan (meaning the balance grows over time), a higher interest rate causes the debt to compound faster. 

### Scenario A: Short-Term Horizon (1 to 5 Years)
If you are getting a reverse mortgage as a short-term bridge—perhaps you plan to sell the house in three years and move to an assisted living facility—**taking the lender credit is usually the smartest move.** 
The extra interest accrued over just three years will likely be far less than the $6,000 to $10,000 you saved upfront in closing costs. 

### Scenario B: Long-Term Horizon (10+ Years)
If you are 65 years old and plan to stay in the home for the rest of your life, **taking the lowest interest rate and paying the upfront fees is usually better.** 
Over a 20-year period, a 1% higher interest rate on a large loan balance will cost you tens of thousands of dollars in compounded debt, far exceeding the initial savings of the lender credit.

## How to Compare Offers

When comparing loan estimates from different lenders, you must look at both the upfront costs *and* the interest rate margin. 
- Lender A might offer a $0 origination fee but a 3.0% margin.
- Lender B might charge a $5,000 origination fee but offer a 2.0% margin.

Ask your loan officer to run an amortization schedule for both options showing what the loan balance will be in 5, 10, and 15 years so you can visually see the breakeven point.
        """
    },
    {
        "slug": "flood-certification-hazard-insurance",
        "title": "Flood Certification and Hazard Insurance Requirements",
        "description": "Understand why lenders require flood certifications and specific hazard insurance levels for reverse mortgages to protect their collateral.",
        "category": "requirements",
        "date": "2023-10-23",
        "takeaways": [
            "Lenders require a flood certification to determine if your home is in a high-risk flood zone.",
            "You must maintain adequate hazard (homeowners) insurance for the life of the loan.",
            "Failure to maintain insurance can lead to forced-placed insurance or foreclosure."
        ],
        "content": """
Among the minor closing costs on your reverse mortgage estimate, you will likely see a small charge (usually under $20) for a "Flood Certification." While inexpensive, this certification triggers one of the most critical ongoing requirements of your reverse mortgage: maintaining adequate property insurance.

## The Flood Certification

Before approving your loan, the lender will hire a third-party company to pull FEMA flood maps and determine exactly where your property lies. This is the Flood Certification.

- **If you are not in a Special Flood Hazard Area (SFHA):** You are not required by law to carry flood insurance (though it is often still a good idea).
- **If you are in an SFHA:** Federal law dictates that you **must** obtain and maintain a separate flood insurance policy for the life of the loan. The coverage must equal the replacement cost of the property or the maximum limit offered by the National Flood Insurance Program (NFIP), whichever is less.

## The Hazard Insurance Requirement

Whether you are in a flood zone or not, you are absolutely required to maintain standard hazard insurance (your everyday homeowners insurance policy). 

Because the lender is handing you a large sum of money secured only by the house, they need an absolute guarantee that if the house burns down, their collateral is protected. The FHA requires that your insurance coverage equal at least 100% of the replacement cost of the property.

## The Danger of Lapsing Insurance

Maintaining your homeowners insurance is not just a suggestion; it is a primary covenant of the reverse mortgage contract. 

If you fail to pay your insurance premiums and the policy lapses, the lender will receive a notice from the insurance company. The lender will then take drastic action to protect their asset:

1. **Forced-Placed Insurance:** The lender will buy a new insurance policy for the home on your behalf and add the cost to your loan balance. Forced-placed insurance is notoriously expensive (often double or triple standard market rates) and only protects the lender's interest, not your personal belongings.
2. **Default and Foreclosure:** If you refuse to reinstate your own insurance policy, the lender can declare the loan in default for failing to meet the terms of the agreement. This can trigger the loan becoming due and payable, ultimately leading to foreclosure.

When you take out a reverse mortgage, you must budget to pay your property taxes and homeowners insurance every single year without fail.
        """
    },
    {
        "slug": "recording-fees-mortgage-taxes",
        "title": "Recording Fees and Mortgage Taxes by State",
        "description": "Learn about county recording fees and state mortgage taxes, how they impact your reverse mortgage closing costs, and why they vary so wildly.",
        "category": "fees",
        "date": "2023-10-24",
        "takeaways": [
            "Recording fees are charged by your local county to officially register the new mortgage lien.",
            "Some states charge massive mortgage taxes that can add thousands to your closing costs.",
            "These fees are set by the government and cannot be negotiated with the lender."
        ],
        "content": """
When reviewing the final closing disclosure for a reverse mortgage, you will see a section dedicated to "Taxes and Other Government Fees." Unlike lender origination fees, which are highly negotiable, these government fees are set in stone by your local and state municipalities. 

Depending on where you live, these fees can be a minor annoyance or a massive financial hurdle.

## County Recording Fees

When you take out a reverse mortgage, the lender places a lien on your property. This lien must be officially registered into the public record at your county clerk or recorder's office. 

The county charges a fee for this administrative service, known as a recording fee. 
- In most counties, this is a relatively minor flat fee ranging from **$50 to $200**.
- The fee covers the cost of physically or digitally archiving the deed of trust and the mortgage documents.

Because a reverse mortgage actually involves two liens (one for the lender and a second backup lien for HUD), recording fees are sometimes slightly higher than traditional mortgages because there is double the paperwork to file.

## State Mortgage Taxes (The Big Expense)

While recording fees are a drop in the bucket, **mortgage taxes** (also known as mortgage recording taxes, intangible taxes, or documentary stamp taxes) can be brutal. 

Certain states view the origination of a new mortgage as a taxable event. The tax is calculated as a percentage of the total loan amount (or in the case of a reverse mortgage, the maximum claim amount).

### High-Tax States
If you live in states like **New York or Florida**, be prepared for sticker shock. 
- In New York, the mortgage recording tax can easily exceed 1.0% to 1.92% of the loan amount, depending on the county. On a $500,000 home, that can be a tax bill of **$5,000 to $9,000**.
- In Florida, the documentary stamp tax and intangible tax combined total 0.55% of the loan amount, costing thousands of dollars.

### Zero-Tax States
Conversely, many states do not charge any mortgage taxes at all. If you live in **Texas, California, or Ohio**, you will only pay the nominal county recording fees and skip the massive tax bill entirely.

## Can These Be Financed?

Yes. Both recording fees and state mortgage taxes can be rolled into the reverse mortgage loan balance. You do not need to write a check to the county or the state out of your own bank account. However, just like all financed closing costs, they will reduce the total amount of equity available to you and will accrue interest over time.

Because these fees are strictly government-mandated, lenders have zero control over them and cannot negotiate them away.
        """
    }
]

import os

for article in articles:
    filepath = os.path.join('_src', '_content', 'articles', f"{article['slug']}.md")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    frontmatter = {
        'title': article['title'],
        'description': article['description'],
        'slug': article['slug'],
        'category': article['category'],
        'date': article['date'],
        'takeaways': article['takeaways']
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('---\\n')
        yaml.dump(frontmatter, f, sort_keys=False)
        f.write('---\\n\\n')
        f.write(article['content'].strip() + '\\n')

print("Created Batch 6 Part 2 (5 articles).")
