s=open("build.py").read()
def rep(a,b):
    global s
    assert a in s, a[:50]
    s=s.replace(a,b,1)
defs='''AUTHOR="Mansoor Khan"   # change to your real name
BIO="builds free online finance tools and writes plain-English guides about car loans, payments and budgeting. Every example in these guides is calculated with the standard loan payment formula."
AD_URL="https://www.profitableratecpmnetwork.com/fdi39i9ey?key=4be333bc82ce1e57d7cc0aa318245d4a"
AD=f'<aside class="ad" aria-label="Advertisement"><p>Advertisement</p><iframe src="{AD_URL}" title="Advertisement" width="100%" height="250" loading="lazy" referrerpolicy="no-referrer" sandbox="allow-scripts allow-popups allow-popups-to-escape-sandbox"></iframe></aside>'
BYL=lambda rel:f'<p class="byline">By <a href="{rel}about.html">{AUTHOR}</a> · Published <time datetime="2026-11-09">November 9, 2026</time> · Updated <time datetime="2026-11-09">November 9, 2026</time></p>'
AUTHBOX=lambda rel:f'<div class="author-box"><strong>About the author</strong><p>{AUTHOR} {BIO} <a href="{rel}about.html">More about the author</a>.</p></div>'
'''
rep("FONTS='<link",defs+"FONTS='<link")
rep("FOOT=lambda rel:f'''<footer>","FOOT=lambda rel:AD+f'''<footer>")
rep('<a href="{rel}articles/how-car-loan-payments-are-calculated.html">How payments work</a> · <a href="{rel}articles/how-much-car-can-i-afford.html">How much car can I afford</a>','<a href="{rel}index.html#articles">All guides</a> · <a href="{rel}about.html">About</a> · <a href="{rel}privacy.html">Privacy</a>')
rep('<p>Free, private, and built on the same formula lenders use.</p></div>','<p>Free, private, and built on the same formula lenders use.</p>{BYL("")}</div>')
rep('"applicationCategory":"FinanceApplication",','"applicationCategory":"FinanceApplication","datePublished":"2026-11-09","dateModified":"2026-11-09","author":{"@type":"Person","name":AUTHOR},')
rep('<h1>{t}</h1><img','<h1>{t}</h1>{BYL("../")}<img')
rep('<p>Next: <a href="{other[0]}.html">{other[1]}</a></p></article>','<h2>Related guides</h2><ul>{related}</ul>{AUTHBOX("../")}</article>')
rep('    page=head(','    related="".join(f\'<li><a href="{a[0]}.html">{a[1]}</a></li>\' for a in arts if a[0]!=slug)\n    page=head(')
rep('"author":{"@type":"Organization","name":"CarLoanCalc"}','"author":{"@type":"Person","name":AUTHOR,"url":BASE+"/about.html"}')
rep('urls=["",','urls=["","about.html","privacy.html",')
rep('Every extra $1,000 down cuts your payment and your interest.','Every extra $1,000 down cuts your payment and your interest (<a href="articles/how-much-down-payment-on-a-car.html">how much to put down</a>).')
rep('A 48-month loan costs far less interest than an 84-month loan.','A 48-month loan costs far less interest than an 84-month loan (<a href="articles/car-loan-term-48-60-72-84-months.html">compare loan terms</a>).')
s+='''
# ---- about, privacy, llms.txt ----
sch=json.dumps({"@context":"https://schema.org","@type":"Person","name":AUTHOR,"url":BASE+"/about.html","description":AUTHOR+" "+BIO,"worksFor":{"@type":"Organization","name":"CarLoanCalc","url":BASE+"/"}})
open("about.html","w").write(head("About the author | CarLoanCalc","About the author of CarLoanCalc and how the car loan calculator and guides are made.","about.html","",sch)+f'<main class="wrap prose"><h1>About CarLoanCalc</h1><p>{AUTHOR} {BIO}</p><p>CarLoanCalc is free. The calculator runs in your browser and does not send or store what you type. Results are estimates; your lender’s final offer may differ.</p><p>Last updated <time datetime="2026-11-09">November 9, 2026</time>. <a href="index.html">Use the car loan calculator</a>.</p></main>'+FOOT(""))
open("privacy.html","w").write(head("Privacy policy | CarLoanCalc","How CarLoanCalc handles your data, cookies, fonts and advertising.","privacy.html","",'{}')+'<main class="wrap prose"><h1>Privacy policy</h1><p>The calculator works entirely in your browser. The numbers you enter are not sent to us or stored.</p><p>This site loads fonts from Google Fonts. It also shows an advertisement from a third-party ad network, which may use cookies or similar technology to show ads and measure results. We do not control those practices. You can limit cookies in your browser settings.</p><p>Last updated <time datetime="2026-11-09">November 9, 2026</time>. <a href="index.html">Back to the calculator</a>.</p></main>'+FOOT(""))
open("llms.txt","w").write("# CarLoanCalc\\n\\n> Free car loan calculator and plain-English guides. Estimates monthly payment, total interest and a yearly payoff schedule from price, down payment, trade-in, APR, term, sales tax and fees.\\n\\n## Tool\\n- [Car loan calculator]("+BASE+"/): the main calculator\\n\\n## Guides\\n"+"".join(f"- [{a[1]}]({BASE}/articles/{a[0]}.html): {a[2]}\\n" for a in arts)+"\\n## About\\n- [About the author]("+BASE+"/about.html)\\n- [Privacy]("+BASE+"/privacy.html)\\n\\nAuthor: "+AUTHOR+". Updated 2026-11-09. Figures are estimates and not financial advice.\\n")
'''
open("build.py","w").write(s)
