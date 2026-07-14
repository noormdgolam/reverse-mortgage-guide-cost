import os
import yaml

articles = [
    {
        "slug": "are-reverse-mortgage-proceeds-taxable",
        "title": "Are Reverse Mortgage Proceeds Taxable?",
        "description": "Learn why the IRS does not consider reverse mortgage proceeds as income and how this affects your annual tax return.",
        "category": "taxes",
        "date": "2023-12-01",
        "takeaways": [
            "The IRS categorizes reverse mortgage payouts as loan advances, not taxable income.",
            "Lump sum, monthly, and line of credit draws are all tax-free.",
            "You still must pay your local property taxes to avoid foreclosure."
        ],
        "content": """
One of the most common concerns for seniors considering a Home Equity Conversion Mortgage (HECM) is whether the cash they receive will trigger a massive tax bill in April. 

Fortunately, the Internal Revenue Service (IRS) has very clear guidelines regarding how reverse mortgage proceeds are classified.

## Loan Advances, Not Income

The fundamental rule to remember is that **reverse mortgage proceeds are not considered income by the IRS.** 

When you take out a reverse mortgage, you are borrowing against the equity you have already built up in your home. You are not earning new money; you are simply taking an advance on an asset you already own. Because it is a loan that eventually must be repaid (with interest), the IRS does not tax it.

This tax-free status applies regardless of how you choose to receive your funds:
- **Lump Sum Disbursement:** Tax-free.
- **Monthly Tenure or Term Payments:** Tax-free.
- **Line of Credit Draws:** Tax-free.

## Impact on Income Taxes

Because the proceeds are not income, receiving money from a reverse mortgage will not push you into a higher federal income tax bracket. 

If you are currently in a 12% tax bracket based on your pension and Social Security, drawing $50,000 from a reverse mortgage will not suddenly bump you into a 22% bracket. Your taxable income remains exactly the same.

## The Property Tax Requirement

While you do not owe *income* tax on the money you receive, you are still strictly obligated to pay your local county **property taxes**. 

A reverse mortgage does not exempt you from property taxes. In fact, failing to pay your property taxes is a violation of the loan terms and will result in the lender foreclosing on your home. If you struggle to afford your property taxes, your lender may require a Life Expectancy Set-Aside (LESA) to automatically pay them from your loan proceeds.

*(Disclaimer: We are not CPAs. Always consult with a licensed tax professional regarding your specific financial situation.)*
"""
    },
    {
        "slug": "reverse-mortgage-and-social-security",
        "title": "How Reverse Mortgages Affect Social Security Benefits",
        "description": "Will taking out a reverse mortgage reduce or suspend your Social Security retirement benefits? We explain the rules.",
        "category": "taxes",
        "date": "2023-12-03",
        "takeaways": [
            "Standard Social Security retirement benefits are not affected by a reverse mortgage.",
            "Medicare benefits are completely unaffected.",
            "Supplemental Security Income (SSI) can be suspended if you hold proceeds as liquid assets."
        ],
        "content": """
A significant portion of retirees rely heavily on Social Security to cover their monthly living expenses. Consequently, seniors are often terrified that drawing a large sum of cash from a reverse mortgage will cause the government to slash or suspend their Social Security checks.

The answer depends entirely on *which* type of Social Security benefit you receive.

## Standard Social Security Retirement Benefits

If you receive standard Social Security retirement benefits (based on your lifelong work history and earnings record), **a reverse mortgage will have zero impact on your benefits.**

Standard Social Security is an entitlement program. It is not "means-tested." This means the Social Security Administration (SSA) does not care how much money you have in the bank, how much your house is worth, or whether you take out a loan. You paid into the system, and you are entitled to your check regardless of your net worth.

## Medicare Benefits

Similarly, standard Medicare (Parts A and B) is an age-based entitlement program. Taking out a reverse mortgage will not affect your eligibility for Medicare, nor will it cause you to lose your coverage.

## The Exception: Supplemental Security Income (SSI)

The danger arises if you receive **Supplemental Security Income (SSI)**. 

SSI is a strictly means-tested program designed for low-income individuals. To qualify for SSI, you must have very few liquid assets (usually capped at $2,000 for an individual or $3,000 for a couple).

While the reverse mortgage loan advance itself is not considered income, **if you keep that cash in your bank account past the end of the calendar month, it becomes a countable liquid asset.**

If you draw $10,000 to fix a roof but leave it in your checking account when the month rolls over, the SSA will see that you have $10,000 in liquid assets. This violates the $2,000 limit, and your SSI benefits will be immediately suspended until you spend the money down.

If you rely on SSI, you must strategically manage your reverse mortgage draws, taking only exactly what you need and spending it within the same calendar month.
"""
    },
    {
        "slug": "reverse-mortgages-and-capital-gains-tax",
        "title": "Reverse Mortgages vs. Capital Gains Tax When Selling",
        "description": "Understand how capital gains taxes work if you decide to sell a home that has an active reverse mortgage on it.",
        "category": "taxes",
        "date": "2023-12-05",
        "takeaways": [
            "Selling a home with a reverse mortgage triggers the same capital gains rules as a normal home sale.",
            "Most seniors qualify for the $250k/$500k primary residence exclusion.",
            "The loan payoff amount does not reduce your gross capital gain."
        ],
        "content": """
If you take out a reverse mortgage, you retain ownership of your home. This means that if you decide to sell the home five years later to move closer to your children, you are the one selling it, not the bank.

But how does the IRS calculate capital gains taxes on a home that has a rapidly growing reverse mortgage balance?

## The Primary Residence Exclusion

The good news is that homes with a reverse mortgage are treated exactly the same as homes with a traditional mortgage or no mortgage at all.

Under Section 121 of the IRS tax code, if you have lived in the home as your primary residence for at least two of the last five years, you can exclude a massive portion of the profit from capital gains taxes:
- **$250,000 exclusion** for single filers.
- **$500,000 exclusion** for married couples filing jointly.

For the vast majority of seniors, this exclusion is large enough to completely wipe out any potential capital gains tax liability.

## How Capital Gains Are Calculated

It is critical to understand that **your mortgage balance has nothing to do with your capital gains calculation.**

Capital gains are calculated based on your *profit*, which is the final sale price minus your adjusted "basis" (what you originally paid for the home plus major improvements).

**Example Scenario:**
- You bought the home in 1990 for $100,000.
- You sell the home today for $400,000.
- Your gross profit (capital gain) is $300,000.
- You have a reverse mortgage balance of $250,000.

Even though you only walk away from the closing table with $150,000 in cash (because $250,000 went to pay off the reverse mortgage), the IRS considers your capital gain to be $300,000. 

If you are a single filer, your exclusion is $250,000. You would owe capital gains tax on the remaining $50,000, regardless of the fact that the bank took most of the cash. 

Always calculate your adjusted basis carefully before selling a highly appreciated property.
"""
    },
    {
        "slug": "deducting-reverse-mortgage-interest",
        "title": "Deducting Reverse Mortgage Interest on Your Tax Return",
        "description": "Can you write off the interest charged on a reverse mortgage? We explain the IRS rules for deductibility.",
        "category": "taxes",
        "date": "2023-12-08",
        "takeaways": [
            "Interest on a reverse mortgage is only deductible when it is actually paid.",
            "Since reverse mortgages don't require monthly payments, you usually can't deduct interest annually.",
            "The deduction is typically claimed as a lump sum when the loan is finally paid off."
        ],
        "content": """
For decades, homeowners with traditional mortgages have enjoyed the tax benefit of deducting their mortgage interest on Schedule A of their federal tax returns. 

Because reverse mortgages charge interest, many seniors wonder if they can claim this same lucrative deduction. The answer is yes, but the timing is completely different.

## The Rule of "Actual Payment"

The IRS rule for deducting mortgage interest is simple: **You can only deduct interest in the year it is actually paid to the lender.**

With a traditional mortgage, you make a payment every month. A portion of that payment goes toward interest. At the end of the year, the bank sends you a Form 1098 detailing exactly how much interest you *paid*, which you then deduct.

With a Home Equity Conversion Mortgage (HECM), you do not make monthly payments. The interest accrues and is simply added to your loan balance. Because you haven't actually handed any cash to the lender, **you cannot deduct the accrued interest on your annual tax return.**

## When Can You Deduct It?

You (or your estate) can only claim the reverse mortgage interest deduction in the year the loan is actually paid off. This usually happens in three scenarios:

1. **You Sell the Home:** When you sell the home and the proceeds are used to pay off the reverse mortgage balance, the massive amount of accrued interest is officially "paid." You can deduct it on that year's tax return.
2. **You Refinance:** If you refinance the reverse mortgage, the old loan is paid off, triggering the deduction.
3. **You Pass Away:** If your heirs sell the home to pay off the loan, the accrued interest is paid. Your estate can often claim this deduction on the final estate tax return, which can be highly beneficial if the estate faces tax liabilities.

## Voluntary Payments

There is one exception. A reverse mortgage *allows* you to make voluntary payments at any time without penalty. If you choose to write a check to your lender for $5,000 in December, the lender applies it to your accrued interest first. You can then deduct that $5,000 on that year's tax return.

*Consult a CPA before attempting to use voluntary reverse mortgage payments as a tax strategy.*
"""
    },
    {
        "slug": "reverse-mortgage-medicare-part-b-irmaa",
        "title": "How a Reverse Mortgage Affects Medicare Part B Premiums",
        "description": "Learn how reverse mortgage proceeds bypass the IRMAA surcharge and keep your Medicare Part B premiums low.",
        "category": "taxes",
        "date": "2023-12-10",
        "takeaways": [
            "High income can trigger IRMAA surcharges on Medicare premiums.",
            "Because reverse mortgage proceeds are not income, they do not trigger IRMAA.",
            "Using a reverse mortgage instead of withdrawing from a 401(k) can save you thousands in Medicare costs."
        ],
        "content": """
Many affluent seniors are unpleasantly surprised when they discover the **Income-Related Monthly Adjustment Amount (IRMAA)**. 

IRMAA is a surcharge added to your Medicare Part B and Part D premiums if your Modified Adjusted Gross Income (MAGI) exceeds certain thresholds set by the government. 

## The IRMAA Trap

Let's say you need $40,000 to renovate your kitchen. If you pull that $40,000 out of a traditional pre-tax 401(k) or IRA, that withdrawal is treated as taxable ordinary income. 

Not only will you pay income tax on that $40,000, but that extra "income" will spike your MAGI for the year. Two years later (since IRMAA has a two-year lookback period), you may receive a letter from the Social Security Administration stating that your Medicare Part B premiums are doubling or tripling because your income was too high.

## The Reverse Mortgage Solution

This is where a reverse mortgage becomes a highly strategic financial planning tool for affluent seniors.

Because the IRS classifies reverse mortgage proceeds as a loan advance rather than taxable income, **drawing money from a reverse mortgage has absolutely no impact on your MAGI.**

If you draw $40,000 from a reverse mortgage line of credit to fund that same kitchen renovation, your taxable income remains identical to the previous year. You bypass the IRMAA surcharge entirely, keeping your Medicare Part B and Part D premiums at their standard base rates.

Financial advisors increasingly recommend setting up a HECM line of credit specifically to fund large, one-off retirement expenses (like a new car, a roof repair, or a dream vacation) to protect a client's tax brackets and avoid IRMAA penalties.
"""
    },
    {
        "slug": "asset-protection-can-a-reverse-mortgage-be-garnished",
        "title": "Asset Protection: Can Reverse Mortgage Proceeds Be Garnished?",
        "description": "Can creditors seize the funds from your reverse mortgage line of credit? Understand your asset protection rights.",
        "category": "legal",
        "date": "2023-12-12",
        "takeaways": [
            "Creditors generally cannot touch funds while they remain in the HECM line of credit.",
            "Once funds are deposited into your personal checking account, they lose protection.",
            "State laws regarding homestead exemptions play a massive role in creditor protection."
        ],
        "content": """
Seniors who face overwhelming medical debt or civil judgments often worry that aggressive creditors will force them to sell their homes or seize their bank accounts. 

If you have an active reverse mortgage line of credit, how protected is that money from debt collectors?

## Protection Inside the Line of Credit

The safest place for your money is inside the Home Equity Conversion Mortgage (HECM) line of credit itself. 

While the funds are sitting untouched in the line of credit, they technically still belong to the lender (HUD/FHA). Because the money is not yet a liquid asset in your personal possession, **ordinary unsecured creditors (like credit card companies or hospitals) cannot garnish or seize your available line of credit.** 

You cannot be legally compelled by an unsecured creditor to draw from your reverse mortgage to pay them.

## The Danger of Your Checking Account

The legal shield vanishes the moment you transfer the funds. 

If you request a $15,000 draw from your reverse mortgage and the lender deposits it into your personal Wells Fargo checking account, that money immediately becomes a personal liquid asset. If a creditor has a valid court judgment against you, they can freeze your checking account and garnish those funds.

Therefore, if you are actively dodging creditors, you should never take a massive lump-sum draw from a reverse mortgage.

## The Exception: The IRS and the Federal Government

While standard debt collectors cannot touch your line of credit, the federal government plays by different rules. 

If you owe massive back taxes to the IRS, or if you have defaulted on federal student loans, the federal government can place a tax lien on your property. A federal tax lien takes precedence over almost everything. If a tax lien is placed on your home, your reverse mortgage lender will likely freeze your line of credit until the lien is resolved, as the lien jeopardizes the lender's first-position claim on the property.

*Always consult with a bankruptcy or asset-protection attorney if you are facing severe debt collection efforts.*
"""
    },
    {
        "slug": "reverse-mortgages-and-bankruptcy",
        "title": "Reverse Mortgages and Bankruptcy: What You Need to Know",
        "description": "How filing for Chapter 7 or Chapter 13 bankruptcy affects an existing reverse mortgage, and vice versa.",
        "category": "legal",
        "date": "2023-12-15",
        "takeaways": [
            "Filing for bankruptcy temporarily halts all foreclosure actions on a reverse mortgage.",
            "A bankruptcy judge must approve any new draws from a HECM line of credit.",
            "You generally cannot get a *new* reverse mortgage while in an active bankruptcy."
        ],
        "content": """
Financial hardship can strike at any age. If a senior with a reverse mortgage finds themselves overwhelmed by unsecured debt and forced to file for bankruptcy, they face a very complex intersection of federal housing policy and federal bankruptcy law.

## Existing Reverse Mortgages in Bankruptcy

If you already have a Home Equity Conversion Mortgage (HECM) and you file for Chapter 7 or Chapter 13 bankruptcy, your home and your loan are subject to the jurisdiction of the bankruptcy court.

**The Automatic Stay:**
The moment you file for bankruptcy, an "automatic stay" goes into effect. This stops all collection actions. If your reverse mortgage lender was attempting to foreclose on you because you fell behind on your property taxes, the bankruptcy filing immediately halts the foreclosure process, buying you time to reorganize.

**Frozen Lines of Credit:**
If you have an available HECM line of credit, the lender will freeze it the moment they receive notice of your bankruptcy. Why? Because taking a draw from the line of credit creates new debt. Under bankruptcy rules, you are not allowed to incur new debt without the explicit permission of the bankruptcy trustee and the judge. You will have to petition the court to allow the lender to unfreeze the line.

## Getting a New Reverse Mortgage During Bankruptcy

What if you are currently in an active Chapter 13 bankruptcy (which involves a 3 to 5 year repayment plan) and you want to take out a reverse mortgage to pay off the bankruptcy early?

This is incredibly difficult, but not impossible. 
1. The FHA allows lenders to approve a HECM for someone in a Chapter 13 bankruptcy, provided the borrower has made all their bankruptcy payments on time for at least 12 months.
2. However, the bankruptcy judge must explicitly approve the reverse mortgage transaction. The judge must agree that taking out the loan is in the best interest of both you and your creditors.

You generally cannot obtain a new reverse mortgage if you are in the middle of an active Chapter 7 (liquidation) bankruptcy until the debts are officially discharged by the court.
"""
    },
    {
        "slug": "paying-off-credit-card-debt-reverse-mortgage",
        "title": "Paying Off Credit Card Debt with a Reverse Mortgage",
        "description": "Is it a good idea to use home equity to eliminate high-interest credit card debt? Pros and cons explained.",
        "category": "alternatives",
        "date": "2023-12-18",
        "takeaways": [
            "Paying off 25% APR credit cards with a 7% HECM can save thousands in interest.",
            "It drastically improves monthly cash flow by eliminating mandatory minimum payments.",
            "It converts unsecured debt into secured debt tied to your home."
        ],
        "content": """
American seniors are carrying more credit card debt than ever before. With average credit card interest rates exceeding 20%, keeping up with minimum monthly payments can quickly drain a fixed retirement income.

One of the most common reasons seniors take out a Home Equity Conversion Mortgage (HECM) is to wipe out this high-interest debt entirely. But is this a wise financial strategy?

## The Mathematical Argument (Pros)

From a pure cash-flow perspective, using a reverse mortgage to consolidate credit card debt is highly effective.

**1. Massive Interest Rate Reduction:** 
Credit cards charge exorbitant rates (often 20% to 29%). A reverse mortgage currently charges significantly less (usually 6% to 8%). Moving $30,000 of debt from a 25% credit card to a 7% reverse mortgage saves you a tremendous amount of compounding interest.

**2. Improved Monthly Cash Flow:** 
If you have $30,000 in credit card debt, your minimum monthly payments are likely around $900. By paying off the cards with a reverse mortgage, that $900 mandatory payment disappears completely. You instantly free up $900 a month to spend on groceries, healthcare, or quality of life.

## The Strategic Risks (Cons)

While the math looks great, there are behavioral and structural risks to consider.

**1. Converting Unsecured Debt to Secured Debt:** 
Credit card debt is "unsecured." If you stop paying a credit card, the company can damage your credit score and annoy you with phone calls, but they cannot take your house. A reverse mortgage is "secured" debt tied directly to your home. 

**2. The Behavioral Trap:** 
The biggest risk of paying off credit cards with a reverse mortgage is behavioral. If a senior pays off $30,000 in debt but does not change their spending habits, they will simply rack up another $30,000 on the newly cleared credit cards over the next three years. 
Now, they have maxed-out credit cards *and* a growing reverse mortgage balance. They have effectively doubled their debt.

If you choose to use a reverse mortgage for debt consolidation, financial advisors strongly recommend physically cutting up the credit cards immediately after they are paid off to prevent a devastating cycle of re-borrowing.
"""
    },
    {
        "slug": "true-cost-compounding-interest-reverse-mortgage",
        "title": "The True Cost of Compounding Interest Over 20 Years",
        "description": "See the actual math behind how compounding interest affects a reverse mortgage balance over a 20-year retirement.",
        "category": "rates",
        "date": "2023-12-20",
        "takeaways": [
            "Reverse mortgages use negative amortization (the balance grows).",
            "Interest is charged on the principal, plus previously accrued interest, plus the FHA MIP.",
            "A $100,000 loan can grow to over $350,000 in 20 years at current rates."
        ],
        "content": """
The most defining feature of a reverse mortgage is that you do not have to make monthly payments. While this provides incredible relief for your monthly budget, it invokes a powerful mathematical force: **Negative Amortization**.

Because you aren't paying the interest every month, the lender simply adds it to your loan balance. The next month, you are charged interest on the original amount *plus* the interest from the previous month. This is compounding interest.

Let's look at the raw math to understand what happens to a reverse mortgage over a 20-year retirement.

## The Mathematical Model

Assume the following scenario:
- You borrow a lump sum of **$100,000**.
- The fully indexed interest rate is **7.00%**.
- The ongoing FHA Mortgage Insurance Premium (MIP) is **0.50%** annually.
- Total compounding rate = **7.50%**.
- You make absolutely no voluntary payments.

### Year 1
- Starting Balance: $100,000
- Interest & MIP added: $7,763 (compounded monthly)
- **End of Year 1 Balance: $107,763**

### Year 5
- You are now paying 7.5% interest on the new, larger balance.
- **End of Year 5 Balance: $145,329**

### Year 10
- The compounding effect begins to accelerate aggressively. 
- **End of Year 10 Balance: $211,206** (Your debt has more than doubled).

### Year 15
- **End of Year 15 Balance: $306,945**

### Year 20
- **End of Year 20 Balance: $446,081**

## What This Means for Your Heirs

As you can see, borrowing $100,000 at age 65 means your loan balance will be nearly $450,000 by the time you are 85. 

If your home only appreciates at 2% a year, the loan balance will eventually eclipse the value of the home. 

This is why the **Non-Recourse Guarantee** is so vital. If you pass away in Year 20 and the home is only worth $300,000, your heirs are completely protected. They hand the keys to the bank, and the FHA insurance fund absorbs the $146,081 loss. Your heirs will not inherit a penny of that debt.

However, if you hope to leave significant home equity as an inheritance to your children, a reverse mortgage is usually the wrong financial tool, as compounding interest will inevitably consume that equity over a long retirement.
"""
    },
    {
        "slug": "reverse-mortgages-in-trust",
        "title": "Reverse Mortgages in Trust: Can You Hold the Home in a Revocable Trust?",
        "description": "Learn the FHA rules for keeping your home in a Living Trust while obtaining a reverse mortgage.",
        "category": "legal",
        "date": "2023-12-22",
        "takeaways": [
            "Yes, you can get a reverse mortgage if your home is in a Revocable Living Trust.",
            "Irrevocable trusts are generally not allowed by the FHA.",
            "The lender must review the trust documents before closing."
        ],
        "content": """
Many seniors place their primary residence into a trust as an estate planning tool to avoid probate court and ensure a smooth transfer of assets to their children upon death. 

A frequent question is: *If my house is in a trust, do I have to take it out to get a reverse mortgage?*

The short answer is **no**, provided the trust is structured correctly according to FHA guidelines.

## Revocable vs. Irrevocable Trusts

The Federal Housing Administration (FHA) distinguishes heavily between the two main types of trusts.

**Revocable Living Trusts (Allowed):**
A revocable trust is one that you can change, amend, or dissolve at any time while you are alive. The FHA allows homes held in a revocable trust to qualify for a Home Equity Conversion Mortgage (HECM). Because you retain full control of the asset, you still meet the FHA's strict homeownership requirements.

**Irrevocable Trusts (Generally Prohibited):**
An irrevocable trust is one that cannot be easily changed once signed. You permanently surrender ownership of the assets to the trust. Because you no longer legally own or control the home, the FHA will not insure a reverse mortgage on a property held in an irrevocable trust.

## The Lender Review Process

If your home is in a revocable trust, you must notify the reverse mortgage lender immediately during the application process.

The lender's underwriting and legal teams must review the complete trust document. They are checking for specific requirements:
1. **Primary Beneficiary:** The senior applying for the loan must be the primary beneficiary of the trust.
2. **Occupancy Right:** The trust must explicitly guarantee the senior the right to live in the home for the rest of their life.
3. **Signatory Authority:** The trust must grant the trustee (usually the senior) the legal authority to encumber the property with debt (i.e., the power to sign a mortgage).

## Does It Delay Closing?

Yes, slightly. Because the lender's legal department must review the trust documents to ensure compliance with federal law and state-specific trust statutes, it typically adds an extra week to the underwriting timeline.

If the trust is poorly written or lacks the explicit power to borrow against the property, the lender may require you to have your estate attorney draft an amendment to the trust before they will approve the loan.

In summary, having a revocable living trust is excellent for estate planning and does not disqualify you from accessing your equity via a reverse mortgage.
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

print("Created 10 new articles for Batch 3.")
