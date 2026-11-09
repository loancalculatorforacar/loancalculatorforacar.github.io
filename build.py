import re
BASE="https://loancalculatorforacar.github.io"
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;700&family=Source+Serif+4:wght@400;600&display=swap" rel="stylesheet">'
def head(title,desc,path,rel,schema,img="images/hero-car.svg",typ="website"):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}/{path}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="{typ}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{BASE}/{path}"><meta property="og:image" content="{BASE}/{img}">
<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#1f4e79">
<link rel="icon" href="{rel}images/favicon.svg" type="image/svg+xml">{FONTS}
<link rel="stylesheet" href="{rel}css/style.css">
<script type="application/ld+json">{schema}</script></head><body>
<header class="site"><div class="wrap"><a class="brand" href="{rel}index.html">CarLoanCalc</a><nav aria-label="Main"><a href="{rel}index.html#calculator">Calculator</a><a href="{rel}index.html#articles">Guides</a><a href="{rel}index.html#faq">FAQ</a></nav></div></header>'''
FOOT=lambda rel:f'''<footer><div class="wrap"><p>&copy; 2026 CarLoanCalc. Estimates are for information only and are not financial advice. Your lender’s offer may differ.</p><p><a href="{rel}index.html">Car loan calculator</a> · <a href="{rel}articles/how-car-loan-payments-are-calculated.html">How payments work</a> · <a href="{rel}articles/how-much-car-can-i-afford.html">How much car can I afford</a></p></div></footer></body></html>'''

# ---------- HOME ----------
faq=[("How do I calculate a car loan payment?","Subtract your down payment and trade-in from the vehicle price, add sales tax and fees, then divide the loan into equal monthly payments that include interest. Our car loan calculator does this instantly using the standard amortization formula."),
("What is a good interest rate for a car loan?","Rates depend on your credit score, loan term, and whether the car is new or used. Borrowers with strong credit usually get the lowest rates, so compare offers from a bank, a credit union, and the dealer before you sign."),
("What is the best loan term for a car?","Shorter terms such as 36 to 60 months cost less interest overall. Longer terms of 72 to 84 months lower the monthly payment but increase total interest and the risk of owing more than the car is worth."),
("How much should I put down on a car?","Many buyers aim for about 20% on a new car and 10% on a used car. A bigger down payment reduces your loan, your monthly payment, and the interest you pay."),
("Does this calculator include sales tax and fees?","Yes. Enter your local sales tax rate and any documentation or registration fees. They are added to the amount you borrow."),
("Is the car loan calculator free?","Yes. It is free, needs no sign-up, and runs entirely in your browser. Nothing you type is sent or stored.")]
import json
faqld=json.dumps({"@context":"https://schema.org","@graph":[
 {"@type":"WebApplication","name":"Car Loan Calculator","url":BASE+"/","applicationCategory":"FinanceApplication","operatingSystem":"Any","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}},
 {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}]})
faqhtml="".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)
home=head("Car Loan Calculator: Estimate Your Monthly Payment (Free)","Free loan calculator for a car. Enter price, down payment, trade-in, rate, term and tax to see your monthly payment, total interest and a yearly payoff schedule.","index.html","",faqld)+f'''
<main class="wrap">
<div class="hero"><div><h1>Loan calculator for a car</h1><p>See what a car will really cost each month. Enter the price, your down payment and the interest rate. The result updates as you type.</p><p>Free, private, and built on the same formula lenders use.</p></div>
<img src="images/hero-car.svg" width="600" height="360" alt="Illustration of a yellow sedan next to a monthly car loan payment estimate"></div>
<section id="calculator" aria-label="Car loan calculator"><div class="calc">
<form id="calc-form" novalidate><div class="fields">
<div class="f"><label for="price">Vehicle price ($)</label><input id="price" type="number" inputmode="decimal" min="0" value="30000"></div>
<div class="f"><label for="down">Down payment ($)</label><input id="down" type="number" inputmode="decimal" min="0" value="5000"></div>
<div class="f"><label for="trade">Trade-in value ($)</label><input id="trade" type="number" inputmode="decimal" min="0" value="0"></div>
<div class="f"><label for="rate">Interest rate (APR %)</label><input id="rate" type="number" inputmode="decimal" min="0" step="0.01" value="6.5"></div>
<div class="f"><label for="term">Loan term</label><select id="term"><option value="24">24 months (2 years)</option><option value="36">36 months (3 years)</option><option value="48">48 months (4 years)</option><option value="60" selected>60 months (5 years)</option><option value="72">72 months (6 years)</option><option value="84">84 months (7 years)</option></select></div>
<div class="f"><label for="tax">Sales tax (%)</label><input id="tax" type="number" inputmode="decimal" min="0" step="0.01" value="7"></div>
<div class="f"><label for="fees">Fees and registration ($)</label><input id="fees" type="number" inputmode="decimal" min="0" value="500"></div>
</div><button class="btn" type="reset" id="reset">Reset to example</button></form>
<div class="result" aria-live="polite"><h2>Estimated monthly payment</h2><div class="big" id="monthly">$0</div><p class="sub">for the full loan term</p>
<div class="bar"><i id="bar-p"></i></div><div class="legend"><span id="l-p"></span><span id="l-i"></span></div>
<dl><dt>Amount you borrow</dt><dd id="r-loan"></dd><dt>Sales tax</dt><dd id="r-tax"></dd><dt>Total interest</dt><dd id="r-interest"></dd><dt>Total of all payments</dt><dd id="r-total"></dd><dt>Total cost with down payment</dt><dd id="r-all"></dd></dl></div></div>
<h2>Yearly payoff schedule</h2><div class="tablebox"><table><caption class="sr" style="display:none">Yearly car loan amortization</caption><thead><tr><th>Year</th><th>Principal paid</th><th>Interest paid</th><th>Balance left</th></tr></thead><tbody id="sched"></tbody></table></div></section>

<section class="prose"><h2>How a car loan calculator works</h2>
<p>A car loan calculator turns five numbers into one answer: what you will pay every month. It first works out how much you need to borrow. That is the vehicle price plus sales tax and fees, minus your down payment and trade-in.</p>
<p>It then spreads that amount over the loan term at your interest rate. Early payments are mostly interest. Later payments are mostly principal, which is why the yearly schedule above shows interest shrinking each year.</p>
<h3>The car loan payment formula</h3><div class="formula">M = P × r ÷ (1 − (1 + r)<sup>−n</sup>)</div>
<p><strong>M</strong> is the monthly payment, <strong>P</strong> the amount borrowed, <strong>r</strong> the monthly rate (APR ÷ 12), and <strong>n</strong> the number of monthly payments. Example: borrowing $26,000 at 6.5% for 60 months gives a payment of about $509.</p></section>

<section class="prose"><h2>Ways to lower your car payment</h2><ul>
<li><strong>Put more down.</strong> Every extra $1,000 down cuts your payment and your interest.</li>
<li><strong>Improve your rate.</strong> Get pre-approved at a bank or credit union, then ask the dealer to beat it.</li>
<li><strong>Choose a shorter term if you can.</strong> A 48-month loan costs far less interest than an 84-month loan.</li>
<li><strong>Negotiate the price, not the payment.</strong> A lower price helps in every line of the calculator.</li>
<li><strong>Use your trade-in.</strong> In many states it also lowers the amount that is taxed.</li></ul></section>

<section id="articles"><h2>Car loan guides</h2><div class="cards">
<a class="card" href="articles/how-car-loan-payments-are-calculated.html"><img src="images/article-formula.svg" width="600" height="320" loading="lazy" alt="Diagram showing principal and interest in a car loan payment"><div><h3>How car loan payments are calculated</h3><p>The formula, an example, and why interest comes first.</p></div></a>
<a class="card" href="articles/how-much-car-can-i-afford.html"><img src="images/article-afford.svg" width="600" height="320" loading="lazy" alt="Budget illustration showing how much car you can afford"><div><h3>How much car can I afford?</h3><p>Simple budget rules before you visit a dealer.</p></div></a></div></section>

<section id="faq"><h2>Car loan calculator FAQ</h2>{faqhtml}</section></main>'''+FOOT("")+'<script src="js/calculator.js" defer></script>'
home=home.replace("</body></html><script","<script")+"</body></html>" if False else home
open("index.html","w").write(home.replace('</body></html><script src="js/calculator.js" defer></script>','<script src="js/calculator.js" defer></script></body></html>'))

# ---------- ARTICLE IMAGES ----------
def svg(t,sub,col):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 320"><rect width="600" height="320" rx="16" fill="{col}"/><rect x="40" y="200" width="520" height="14" rx="7" fill="#f2a900"/><rect x="40" y="200" width="330" height="14" rx="7" fill="#fff"/><text x="40" y="110" font-family="Arial" font-size="40" font-weight="700" fill="#fff">{t}</text><text x="40" y="150" font-family="Arial" font-size="22" fill="#dbe8f3">{sub}</text></svg>'
open("images/article-formula.svg","w").write(svg("M = P × r ÷ (1 − (1+r)⁻ⁿ)","Car loan payment formula","#1f4e79"))
open("images/article-afford.svg","w").write(svg("The 20/4/10 rule","20% down, 4 years, 10% of income","#173b5c"))
open("images/favicon.svg","w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#1f4e79"/><path d="M5 20l3-7h16l3 7v3H5z" fill="#f2a900"/></svg>')

# ---------- ARTICLES ----------
arts=[("how-car-loan-payments-are-calculated","How Car Loan Payments Are Calculated (Formula and Example)","Learn the car loan payment formula, see a worked example, and understand how principal and interest change over time.","article-formula.svg","Diagram showing principal and interest in a car loan payment",
'''<p>Your car loan payment looks like one number, but it is two things added together: repayment of the money you borrowed (principal) and the lender’s charge for lending it (interest). Understanding the split helps you borrow smarter.</p>
<h2>Step 1: Work out the amount you borrow</h2><p>Start with the vehicle price. Add sales tax and fees. Subtract your down payment and trade-in. The result is the principal, <em>P</em>.</p>
<h2>Step 2: Apply the formula</h2><div class="formula">M = P × r ÷ (1 − (1 + r)<sup>−n</sup>)</div><p>Here <em>r</em> is your APR divided by 12 and <em>n</em> is the number of months.</p>
<h2>Worked example</h2><p>You borrow $26,000 at 6.5% APR for 60 months. The monthly rate is 0.065 ÷ 12 = 0.005417. The formula gives a payment of about $509. Over five years you pay roughly $30,540, so interest costs about $4,540.</p>
<h2>Why early payments are mostly interest</h2><p>Interest is charged on the balance you still owe. At the start the balance is highest, so most of each payment goes to interest. As the balance falls, more goes to principal. Paying extra early in the loan saves the most.</p>
<h2>What changes the payment most</h2><ul><li><strong>Term:</strong> longer terms lower the payment but raise total interest.</li><li><strong>Rate:</strong> one extra percentage point adds hundreds of dollars over a five-year loan.</li><li><strong>Down payment:</strong> borrowing less reduces everything else.</li></ul>'''),
("how-much-car-can-i-afford","How Much Car Can I Afford? A Simple Budget Guide","Use the 20/4/10 rule and a car loan calculator to find a car price and monthly payment that fit your budget.","article-afford.svg","Budget illustration showing how much car you can afford",
'''<p>The sticker price is not the real question. What matters is whether the monthly payment, insurance, fuel and repairs fit comfortably in your budget.</p>
<h2>The 20/4/10 rule</h2><ul><li><strong>20%</strong> down payment, so you start with equity in the car.</li><li><strong>4 years</strong> (48 months) or less for the loan term.</li><li><strong>10%</strong> or less of your gross monthly income on total car costs, including insurance.</li></ul>
<h2>Example</h2><p>If you earn $5,000 a month before tax, 10% is $500 for the payment and insurance together. With $150 insurance, aim for a payment near $350. Use the calculator to try prices until the monthly figure lands there.</p>
<h2>Costs people forget</h2><p>Sales tax, registration, insurance increases, fuel, maintenance and tires can add hundreds per month. Add them before you decide.</p>
<h2>Get pre-approved first</h2><p>Ask your bank or credit union for a pre-approved rate. You will know your real APR, and you can compare the dealer’s offer fairly.</p>''')]
exec(open("articles_extra.py").read())
for slug,t,d,im,alt,body in arts:
    path=f"articles/{slug}.html"
    sch=json.dumps({"@context":"https://schema.org","@type":"Article","headline":t,"description":d,"image":f"{BASE}/images/{im}","datePublished":"2026-11-09","dateModified":"2026-11-09","author":{"@type":"Organization","name":"CarLoanCalc"},"mainEntityOfPage":f"{BASE}/{path}"})
    other=[a for a in arts if a[0]!=slug][0]
    page=head(t+" | CarLoanCalc",d,path,"../",sch,"images/"+im,"article")+f'''
<div class="wrap crumbs"><a href="../index.html">Car loan calculator</a> / Guides</div>
<article class="post"><h1>{t}</h1><img src="../images/{im}" width="600" height="320" alt="{alt}">{body}
<div class="cta"><strong>Try it with your numbers.</strong> Use the <a href="../index.html#calculator">free car loan calculator</a> to see your monthly payment.</div>
<p>Next: <a href="{other[0]}.html">{other[1]}</a></p></article>'''+FOOT("../")
    open(path,"w").write(page)

# ---------- ROBOTS / SITEMAP ----------
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
urls=["",*[f"articles/{a[0]}.html" for a in arts]]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{BASE}/{u}</loc><lastmod>2026-11-09</lastmod></url>" for u in urls)+"</urlset>")
open("404.html","w").write(head("Page not found | CarLoanCalc","Page not found.","404.html","",'{}').replace('<meta name="robots" content="index, follow, max-image-preview:large">','<meta name="robots" content="noindex">')+'<main class="wrap"><h1>Page not found</h1><p><a href="index.html">Go to the car loan calculator</a></p></main></body></html>')
open("README.md","w").write("# Car loan calculator site\n\n1. Open `build.py`, set `BASE` to your GitHub Pages URL (e.g. https://name.github.io/repo), run `python3 build.py`.\n2. Push all files to a GitHub repo; Settings > Pages > Deploy from branch `main` / root.\n3. Submit `sitemap.xml` in Google Search Console.\n")

# ---- add new article cards to home page ----
h=open("index.html").read()
new="".join(f'<a class="card" href="articles/{a[0]}.html"><img src="images/{a[3]}" width="600" height="320" loading="lazy" alt="{a[4]}"><div><h3>{a[1]}</h3><p>{a[2][:95]}…</p></div></a>' for a in arts[2:])
h=h.replace('</div></a></div></section>','</div></a>'+new+'</div></section>',1)
open("index.html","w").write(h)
