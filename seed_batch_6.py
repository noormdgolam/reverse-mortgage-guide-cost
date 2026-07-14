import os
import yaml

articles = [
    {
        "slug": "fha-initial-mortgage-insurance-premium-imip",
        "title": "Breaking Down the FHA Initial Mortgage Insurance Premium (IMIP)",
        "description": "Understand the largest closing cost associated with a reverse mortgage: the 2% FHA Initial Mortgage Insurance Premium.",
        "category": "costs",
        "date": "2024-02-08",
        "takeaways": [
            "The FHA IMIP is mandatory for all HECM reverse mortgages.",
            "It costs exactly 2.00% of your home's appraised value (or the FHA lending limit).",
            "This fee guarantees that the loan is non-recourse, protecting your heirs from debt."
        ],
        "content": """
When seniors receive their initial loan estimate for a Home Equity Conversion Mortgage (HECM), they are often shocked by the massive closing costs. The largest culprit is almost always the **Initial Mortgage Insurance Premium (IMIP)**.

Unlike private mortgage insurance (PMI) on a traditional loan, the IMIP is paid directly to the Federal Housing Administration (FHA) and serves a vastly different purpose.

## How Much Does the IMIP Cost?

The math for the IMIP is rigid and non-negotiable across all lenders. 

**The IMIP is exactly 2.00% of your home's appraised value, or 2.00% of the FHA Maximum Claim Amount limit, whichever is less.**

**Example 1:**
If your home appraises for $400,000, your IMIP will be **$8,000** ($400,000 x 0.02).

**Example 2:**
If your home appraises for $1,500,000, you hit the FHA cap. For 2024, the FHA lending limit is roughly $1.14 million. You will pay 2% of the $1.14 million limit, which is roughly **$22,996**. 

## Why Do You Have to Pay It?

Many seniors feel frustrated paying thousands of dollars for "insurance" when they already have homeowners insurance. 

The IMIP does not insure your house against fire or flood. **It insures the lender against the risk that you outlive your equity.**

Because a reverse mortgage is a "non-recourse" loan, the lender is never allowed to demand repayment from your other assets or from your heirs. If your loan balance grows to $500,000, but the housing market crashes and your home is only worth $300,000 when you die, the bank takes a $200,000 loss.

The IMIP fee goes into a massive federal insurance fund. When that $200,000 shortfall occurs, the FHA uses the fund to reimburse the lender. 

Without the IMIP, no bank on earth would issue a reverse mortgage because the risk of loss is mathematically guaranteed on long-lived loans. You are paying the IMIP to buy the peace of mind that your children will never inherit a massive debt.
"""
    },
    {
        "slug": "negotiate-reverse-mortgage-origination-fees",
        "title": "How to Negotiate Reverse Mortgage Origination Fees",
        "description": "Lender origination fees are capped by law, but they are still negotiable. Learn how to get the lender to lower their fees.",
        "category": "costs",
        "date": "2024-02-10",
        "takeaways": [
            "FHA law caps the origination fee at $6,000.",
            "Lenders will often waive the origination fee entirely in exchange for a higher interest rate.",
            "Always get Good Faith Estimates from at least three different lenders to force them to compete."
        ],
        "content": """
A reverse mortgage is a specialized financial product, and the loan officers who originate them expect to be compensated for their time and expertise. This compensation comes in the form of an Origination Fee.

Unlike the FHA Mortgage Insurance Premium, the Origination Fee is entirely negotiable. 

## The FHA Legal Cap on Origination Fees

To prevent predatory lending, the federal government placed strict mathematical limits on how much a lender can charge you to originate a HECM. 

The formula is:
- **2% of the first $200,000** of your home's value.
- **1% of the remaining value.**
- **Absolute Maximum Cap:** $6,000.
- **Absolute Minimum:** $2,500.

If you have a $300,000 home, the maximum fee is $5,000. If your home is worth $500,000 or more, the fee hits the hard $6,000 cap. 

## How to Negotiate the Fee to Zero

While $6,000 is the legal maximum, very few savvy borrowers actually pay it. 

The reverse mortgage industry is highly competitive. If you present a lender with a competing quote from another bank, they will almost always negotiate. 

The most common negotiation tactic is the **Lender Credit**. 

The lender will offer to waive your $6,000 origination fee entirely. In exchange, you agree to accept a slightly higher interest rate on your loan (for example, taking a 7.5% rate instead of a 7.0% rate). 

Because the lender makes more money on the back-end over time through the higher interest rate, they are willing to absorb the upfront cost of the origination fee.

If you plan to live in the home for 20 years, taking the higher rate is mathematically worse in the long run. If you only plan to live in the home for 3 years, wiping out the $6,000 upfront fee via a higher rate is a brilliant mathematical move.
"""
    },
    {
        "slug": "who-pays-for-title-insurance-reverse-mortgage",
        "title": "Who Pays for Title Insurance on a Reverse Mortgage?",
        "description": "Why you must purchase a new Lender's Title Insurance policy when getting a reverse mortgage.",
        "category": "costs",
        "date": "2024-02-12",
        "takeaways": [
            "The borrower pays for the Lender's Title Insurance policy at closing.",
            "This policy protects the bank from undisclosed liens or ownership disputes.",
            "The cost varies wildly by state but is typically $1,000 to $2,500."
        ],
        "content": """
When you close on a reverse mortgage, you will see a massive line item on your closing disclosure for "Lender's Title Insurance." Many seniors are confused by this, assuming that because they already bought title insurance when they originally purchased the house 30 years ago, they shouldn't have to pay for it again.

Unfortunately, the real estate industry does not work that way.

## Owner's vs. Lender's Title Insurance

When you bought your home, you likely purchased an **Owner's Title Insurance Policy**. This policy lasts for as long as you own the home and protects *you* if someone claims they have a legal right to your property.

When you take out a reverse mortgage, the bank is giving you hundreds of thousands of dollars and using your house as collateral. The bank needs a guarantee that they are in the "first lien position"—meaning no other creditor can take the house before they do. 

Therefore, the bank requires a brand new **Lender's Title Insurance Policy**. This policy strictly protects the bank, not you. However, as the borrower seeking the loan, it is your responsibility to pay the premium for it at closing.

## What Does Title Insurance Protect the Lender From?

The title company will do an exhaustive search of county public records before the loan closes. They are looking for:
- Unpaid contractor liens (Mechanic's Liens).
- Undisclosed second mortgages.
- Delinquent county property tax liens.
- IRS federal tax liens.
- Fraudulent deed transfers involving estranged family members.

If the title company misses one of these, and the IRS suddenly forecloses on the home, the title insurance policy will reimburse the reverse mortgage lender for their massive financial loss. 

## The Cost

The cost of a Lender's Title Policy is regulated by the state, not the federal government. Depending on where you live and the value of your home, expect this fee to range between $1,000 and $2,500. Like almost all reverse mortgage closing costs, you do not have to write a check for this; it is simply rolled into the starting balance of the loan.
"""
    },
    {
        "slug": "cost-of-hud-counseling-reverse-mortgage",
        "title": "The Cost of Independent HUD Counseling (and Fee Waivers)",
        "description": "Mandatory HUD counseling prevents predatory lending, but it isn't free. Learn what it costs and how to get a waiver.",
        "category": "costs",
        "date": "2024-02-14",
        "takeaways": [
            "HUD counseling is a strict federal requirement for all HECM applicants.",
            "The session typically costs between $125 and $200.",
            "Counseling agencies are required to offer fee waivers to seniors experiencing severe financial hardship."
        ],
        "content": """
Before you are allowed to sign an application or pay for an appraisal for a reverse mortgage, federal law requires you to complete a counseling session with an independent, HUD-approved housing counseling agency. 

This requirement was put in place to ensure that seniors fully understand the severe financial implications of a reverse mortgage and to prevent predatory loan officers from tricking vulnerable retirees.

While the counseling is mandatory, the counselors are not government employees. They work for non-profit agencies that rely on fees to keep their doors open.

## How Much Does It Cost?

The cost of a HUD reverse mortgage counseling session typically ranges from **$125 to $200**. 

Unlike origination fees or title insurance, **the counseling fee cannot be rolled into the loan.** You must pay this fee out-of-pocket directly to the counseling agency, usually via a credit card or check, before the session begins. 

This is done intentionally to ensure the counselor remains completely independent from the lender. If the lender paid the counselor, there would be a massive conflict of interest. 

## What Happens During the Session?

The session is usually conducted over the phone and lasts between 60 to 90 minutes. The counselor will:
- Review your current income and expenses.
- Explain the risks of compounding interest and negative amortization.
- Ensure you understand that you must continue paying property taxes.
- Discuss alternatives to a reverse mortgage (like downsizing or state property tax deferral programs).

Once the session is complete, the counselor will issue you a **Certificate of HECM Counseling**. You must give this certificate to your lender; the loan process cannot move forward without it.

## Hardship Fee Waivers

If you are pursuing a reverse mortgage because you are absolutely destitute and facing imminent foreclosure, finding $150 to pay a counselor can be impossible.

By law, HUD requires counseling agencies to provide their services regardless of a client's ability to pay. If your income falls below a certain poverty threshold (usually based on federal guidelines relative to your household size), you can request a **Fee Waiver** or a heavily subsidized rate.

When you call agencies to schedule your appointment, be upfront about your financial situation and ask if they offer hardship waivers. 
"""
    },
    {
        "slug": "closing-costs-rolled-into-loan-balance",
        "title": "Can Closing Costs Be Rolled Into the Reverse Mortgage Balance?",
        "description": "Discover how seniors pay for $15,000+ in reverse mortgage closing costs without actually writing a check.",
        "category": "costs",
        "date": "2024-02-16",
        "takeaways": [
            "Almost all reverse mortgage closing costs can be financed (rolled into the loan).",
            "This prevents house-rich, cash-poor seniors from having to drain their savings to get the loan.",
            "Counseling fees and the initial appraisal fee are the only costs you usually pay out-of-pocket."
        ],
        "content": """
When a senior receives an itemized closing disclosure for a reverse mortgage, the total closing costs can be terrifying. Between the FHA Mortgage Insurance Premium, the origination fee, title insurance, and recording fees, the total bill often exceeds $15,000.

If a senior is getting a reverse mortgage because they are broke, how on earth are they supposed to pay $15,000 to close the loan?

The answer is **financing the costs**. 

## Rolling Costs into the Loan

The FHA designed the HECM program specifically for "house-rich, cash-poor" individuals. Therefore, the program allows you to roll almost every single closing cost into the starting balance of the loan itself.

**Here is how the math works:**
- You qualify for a maximum loan advance of **$100,000**.
- Your total closing costs are **$15,000**.
- At the closing table, you do not write a check for $15,000.
- Instead, the lender subtracts the $15,000 from your available funds.
- Your starting loan balance is now $15,000.
- You have **$85,000** left over to draw as cash, a line of credit, or monthly income.

You essentially paid the closing costs using the equity from your own home.

## The Costs You MUST Pay Out-of-Pocket

While 95% of the costs are financed, there are two specific fees you generally must pay out of your own checking account before the loan closes:

1. **HUD Counseling Fee ($125 - $200):** This must be paid to the independent counseling agency before the lender can even process your application. 
2. **The FHA Appraisal Fee ($500 - $800):** The appraiser is an independent third party. They require payment when they inspect the house. Because the loan has not closed yet, the lender cannot use your home equity to pay them. You must pay this out of pocket. *(Note: If the loan closes successfully, some lenders will reimburse you for the appraisal fee by crediting it back on the closing disclosure, but you must front the cash initially).*

By rolling the massive fees into the loan balance, seniors can access their equity without draining their limited liquid savings. 
"""
    },
    {
        "slug": "reverse-mortgage-appraisals-cost-more",
        "title": "Why Reverse Mortgage Appraisals Cost More Than Traditional Ones",
        "description": "Understand why FHA HECM appraisers charge a premium and why they are incredibly strict regarding home repairs.",
        "category": "costs",
        "date": "2024-02-18",
        "takeaways": [
            "FHA appraisals require a much deeper inspection of the home's structural and safety condition.",
            "The appraiser acts as the eyes and ears of the federal government.",
            "Expect to pay $500 to $800, which is higher than a standard conventional appraisal."
        ],
        "content": """
When you apply for a traditional conventional mortgage to buy a house, the bank sends an appraiser to determine if the house is worth the purchase price. Their primary concern is the mathematical value of the real estate.

When you apply for a reverse mortgage, the Federal Housing Administration (FHA) sends an appraiser. The FHA appraiser is vastly more strict, their inspection takes longer, and as a result, they charge a significantly higher fee.

## The Scope of an FHA Appraisal

An FHA appraiser is not just looking at the value of the home; they are executing a strict **health, safety, and structural integrity audit** on behalf of the federal government.

Because the FHA is insuring the loan, they demand the collateral (the house) be in excellent condition. The appraiser is required to actively search for:
- **Lead-Based Paint:** Peeling or chipping paint on homes built before 1978 will cause an immediate failure.
- **Roof Life:** The roof must have at least two years of physical life remaining. If it looks degraded, the appraiser will demand a roof inspection.
- **Water Intrusions:** Active leaks in the basement, attic, or crawlspace must be documented.
- **Safety Hazards:** Missing handrails on stairs, exposed electrical wiring, or broken windows will be flagged.
- **Heating Systems:** The home must have a functional, permanent heat source.

## The Premium Cost

Because an FHA appraiser is required to take dozens of specific photos, test appliances, crawl into the attic, and fill out a massive federal reporting document, the appraisal takes significantly more time. 

As a result, FHA reverse mortgage appraisals typically cost between **$500 and $800**, compared to the $400 you might pay for a standard conventional appraisal. 

Furthermore, if the appraiser flags safety issues (like peeling paint), you will have to fix them. Once fixed, you have to pay the appraiser a **Re-inspection Fee** (usually $150 to $200) to come back to the house, verify the repairs were made, and clear the file for closing.

Seniors must budget for this out-of-pocket expense early in the process.
"""
    },
    {
        "slug": "understanding-the-monthly-servicing-fee",
        "title": "Understanding the Monthly Servicing Fee",
        "description": "Some reverse mortgages charge a monthly servicing fee. Learn what it covers and why many lenders now waive it.",
        "category": "costs",
        "date": "2024-02-20",
        "takeaways": [
            "The servicing fee pays the company that manages your loan statements and line of credit.",
            "FHA rules cap the maximum fee at $30 to $35 per month.",
            "Due to intense market competition, most modern lenders do not charge a servicing fee."
        ],
        "content": """
When reading through the dense legal disclosures of a Home Equity Conversion Mortgage (HECM), you may notice a line item mentioning a "Monthly Servicing Fee." 

For seniors who are taking out a reverse mortgage specifically to eliminate monthly payments, seeing a new monthly fee can be alarming. 

## What Does the Servicer Do?

The company that originates your loan (the broker or the bank) rarely holds onto it. They sell the loan to a massive Wall Street aggregator, who then hires a "Servicing Company" to manage the day-to-day operations of the loan for the next 20 years. 

The servicer's job is highly complex:
- They must mail you monthly statements showing your compounding interest.
- They must process your requests when you want to draw cash from your line of credit.
- They must monitor your county property tax records to ensure you aren't delinquent.
- They must process your annual occupancy certificate.

The monthly servicing fee is designed to pay this company for their ongoing administrative work.

## The FHA Cap

Because the FHA heavily regulates the reverse mortgage industry, they place a strict limit on how much a servicer can charge you:
- **$30 per month** for loans with a fixed interest rate or an annually adjusting rate.
- **$35 per month** for loans with a monthly adjusting rate.

Crucially, **you do not write a check for this fee.** The $30 is simply added to your loan balance every month, compounding with the rest of your interest.

## The Good News: The Fee is Disappearing

In the early 2000s, almost every reverse mortgage charged a servicing fee. 

Today, the industry is incredibly competitive. To win your business, **the vast majority of modern lenders waive the servicing fee entirely.** They have realized that the margin they make on the interest rate is more than enough to cover the administrative costs. 

If you receive a Good Faith Estimate from a lender and it includes a $35 monthly servicing fee, you should absolutely demand they remove it, or tell them you will take your business to a competitor who does not charge one.
"""
    },
    {
        "slug": "what-is-a-lender-credit",
        "title": "What is a 'Lender Credit' on a Reverse Mortgage?",
        "description": "A lender credit can wipe out thousands in closing costs, but it comes at a steep price: a higher interest rate.",
        "category": "costs",
        "date": "2024-02-22",
        "takeaways": [
            "A lender credit is money the bank gives you to cover your closing costs.",
            "In exchange, you must accept a higher interest rate on your loan.",
            "It is a brilliant strategy for short-term loans, but devastating for long-term loans."
        ],
        "content": """
Reverse mortgages are famous for their exorbitant closing costs, which frequently exceed $15,000. 

While you can roll these costs into the loan balance, doing so instantly evaporates $15,000 of your hard-earned home equity. To avoid this, many seniors use a highly effective negotiation tactic: The **Lender Credit**.

## How the Lender Credit Works

A lender credit (often called "Premium Pricing" in the mortgage industry) is a tradeoff. 

The lender agrees to pay some, or all, of your closing costs out of their own pocket. They might wipe out your $6,000 origination fee, and they might even pay your title insurance.

In exchange for giving you this free money upfront, **the lender requires you to accept a higher ongoing interest rate on your reverse mortgage.**

For example:
- **Option A:** You accept a 6.50% interest rate, and you pay $15,000 in closing costs from your equity.
- **Option B:** You accept a 7.25% interest rate, and the lender gives you a massive credit, reducing your closing costs to $0. 

## When is a Lender Credit a Good Idea?

Choosing the lender credit is entirely a math equation based on **how long you plan to live in the home.**

**The Short-Term Strategy (Take the Credit):**
If you are 82 years old and you only plan to stay in the home for another 4 years before moving to an assisted living facility, **take the lender credit.** The higher interest rate will not have enough time to compound and catch up to the massive $15,000 upfront savings. You win the math game.

**The Long-Term Strategy (Avoid the Credit):**
If you are 62 years old, perfectly healthy, and plan to live in the home for another 25 years, **never take the lender credit.** 
Paying a 7.25% interest rate instead of a 6.50% interest rate for 25 years will cause your loan balance to explode, destroying hundreds of thousands of dollars in equity due to decades of negative amortization. In this scenario, it is much cheaper to pay the $15,000 upfront to secure the lower long-term rate.

Always ask your loan officer to run an amortization schedule comparing the two options so you can see exactly when the math flips.
"""
    },
    {
        "slug": "flood-certification-and-hazard-insurance",
        "title": "Flood Certification and Hazard Insurance Requirements",
        "description": "Understand the strict insurance rules the FHA enforces to protect the collateral securing your reverse mortgage.",
        "category": "costs",
        "date": "2024-02-24",
        "takeaways": [
            "You must maintain a comprehensive homeowners insurance policy at all times.",
            "If your home is in a FEMA flood zone, you must purchase expensive federal flood insurance.",
            "Failure to maintain these policies will result in immediate foreclosure."
        ],
        "content": """
When you take out a reverse mortgage, you retain the title to your home. However, the Federal Housing Administration (FHA) and your lender hold a massive lien against the property. 

Because the house is the sole collateral guaranteeing the loan, the FHA demands absolute assurance that the house will not be destroyed by a disaster, leaving the bank with a worthless piece of land. 

This requires two strict insurance protocols: Hazard Insurance and Flood Certification.

## The Hazard Insurance Requirement

You are required to maintain a comprehensive **Homeowners Insurance (Hazard Insurance)** policy for the entire life of the reverse mortgage. 

The policy must cover the replacement cost of the physical structure. At closing, the lender will require you to provide a "declaration page" from your insurance agent proving that the policy is active and that the premium is paid for the next 12 months.

If you ever let this policy lapse because you forgot to pay the bill, the lender will instantly implement "Forced Placed Insurance"—an incredibly expensive policy they buy on your behalf and charge to your loan balance. If you refuse to insure the home, they will foreclose.

## The Flood Certification

During the underwriting process, you will be charged a tiny fee (usually $15 to $20) for a **Flood Certification**. 

The lender hires a third-party company to check your exact property address against the latest FEMA flood maps. 
- If your home is in a designated "Zone X" (low risk), you are fine.
- If your home is located in a Special Flood Hazard Area (SFHA), usually designated as Zone A or Zone V, **you are legally required to purchase National Flood Insurance.**

Federal flood insurance is notoriously expensive, often costing thousands of dollars a year. Standard homeowners insurance does not cover flood damage. If the Flood Certification flags your property, you cannot get the reverse mortgage until you provide proof that you have purchased a flood policy. 

Furthermore, you must pass the Financial Assessment proving you have enough ongoing income to afford that massive flood insurance premium every year for the rest of your life.
"""
    },
    {
        "slug": "recording-fees-and-mortgage-taxes",
        "title": "Recording Fees and Mortgage Taxes by State",
        "description": "Learn about the unavoidable government fees and taxes required to legally record a reverse mortgage at the county courthouse.",
        "category": "costs",
        "date": "2024-02-26",
        "takeaways": [
            "Recording fees pay the county clerk to officially file the mortgage lien in public records.",
            "Several states impose massive Mortgage Recording Taxes on the total loan amount.",
            "These fees are set by the government and cannot be negotiated with the lender."
        ],
        "content": """
When reviewing the closing disclosure for a reverse mortgage, borrowers often spot fees that the lender claims they have absolutely no control over. These are the government recording fees and state mortgage taxes.

Because a reverse mortgage is a massive real estate transaction, it must be officially recognized by the local government.

## County Recording Fees

When you sign your reverse mortgage documents, the title company must physically (or electronically) deliver the new mortgage lien to the County Clerk or County Recorder's office.

The clerk officially stamps the document, making the lender's lien a matter of public record. The county charges a **Recording Fee** for this administrative service.

Depending on the county, this fee is usually based on the number of pages in the legal document. For a massive reverse mortgage contract, recording fees typically range from **$150 to $300**. You cannot negotiate this; it is a fixed municipal cost.

## The Danger of Mortgage Recording Taxes

While recording fees are a minor annoyance, **Mortgage Recording Taxes** can be devastating. 

Several states view the issuance of a massive new mortgage as a taxable event and charge a percentage-based tax on the total loan amount. 

The worst offenders include:
- **New York:** The mortgage recording tax in parts of New York can approach 2.00% of the loan amount. On a large reverse mortgage, this tax alone can cost $10,000.
- **Florida:** Florida charges a Documentary Stamp Tax (0.35%) and an Intangible Tax (0.20%) on new mortgages.
- **Maryland & Virginia:** Both states impose significant recordation taxes based on county rates.

Because a reverse mortgage has a "Maximum Claim Amount" (often 150% of the home's value) that the lien secures, some aggressive tax jurisdictions attempt to tax that massive maximum amount rather than the actual cash you are drawing at closing.

If you live in a high-tax state, you must ask your loan officer to calculate the exact state and county recording taxes *before* you pay for an appraisal, as these taxes can easily wipe out the financial benefit of getting the loan.
"""
    }
]

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
        f.write('---\n')
        yaml.dump(frontmatter, f, sort_keys=False)
        f.write('---\n\n')
        f.write(article['content'].strip())

print("Created 10 new articles for Batch 6.")
