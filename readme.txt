claude --dangerously-skip-permissions

claude-fast    # "Add a stop-loss column to the trades table"
claude-smart   # "Debug why my 0DTE bot double-enters positions"
claude-max     # "Analyze my entire codebase and optimize the backtesting system"

I made some changes in the code.  Please
 PUSH ALL CHANGES TO GITHUB. Make sure you push all 
changes, as I've had other conversations going on 
with different AIs.

We do not yet have a git repo for this algorithm.  
Use agent "C:\Users\worth\.claude\agents\git-agent.md" to 
Set up GIT.

Zip project with zip agent: "C:\Users\worth\.claude\agents\zip-agent.md"

codex
npm install -g @openai/codex@latest



Do not summarize. Expand every point with implementation details, edge cases, historical context, and failure
modes. Prioritize completeness over conciseness.

 Clearly identify root causes, requirements, and goals.
   - Plan a strategic, thoughtful approach before implementation.

Evaluate: What is excellent? What is missing? What should be reinforced? Which expert concepts could be added? Which instructions should be clarified? Improve it again based on your critique.
 — PRODUCE THE ULTIMATE PROMPT


perfect this prompt: 

* Please create a presentation for this backtest in html. One chart per trade, please. 
Include exact tweet signal price and the discounted limit order as well as profit 
tiers in the visual chart. Also add overall performance metrics, Strategy parameters, 
Execution statistics, Risk analysis, backtest summary and performance summary. 
daily_return= needs to be prominently displayed in the overall performance metrics 
near the top next to total return%. daily_return= is our most important metric. *

Create an HTML presentation that describes in detail how my algo performed.  
All one document.  NO multiple slides.  

pip install -r requirements_gui.txt

Ctrl + Shift + ` = New terminal
To run: 
python gui.py

Shift + Tab = choose mode 
 ※ Tip: Use /agents to create context-efficient experts for specific tasks. Eg. Code Reviewer, Software Architect,
 Data Scientist

/terminal-setup

Shift + Tab = choose mode 
 ※ Tip: Use /agents to create context-efficient experts for specific tasks. Eg. Code Reviewer, Software Architect,
 Data Scientist

/terminal-setup

Shift + Enter  = Increases Input Box Height

create a .bat for one-click opening the program with a terminal.

create a .pyw for one-click opening the program without a terminal.

Create a single .vbs launcher file that opens the GUI      
without showing any terminal/console window. Use
pythonw.exe for cleanest execution.  Use the same prefix as the 
.bat file.  Use underscores between the words for proper file naming.  
Make sure the .bat file has underscores between the words.  Make sure
the .bat file and the .vbs file have the same prefix.    

create a desktop icon that uses the .vbs to open the program
by double clicking on the icon and here is the icon I want
you to use: 

create a desktop icon that uses the .pyw to open the program
by double clicking on the icon and here is the icon I want
you to use: 

Please remove any unnecessary files and folders. 
---------------
*******************************************
  
  Prompt:

  I need to set a custom .ico file as the icon for both the Windows taskbar (system tray) and the      
  title bar in my PyQt5 application. The icon file is located at:

  Requirements:
  1. The icon must appear in the application's title bar (upper-left corner)
  2. The icon must appear in the Windows taskbar when the app is running
  3. The icon must persist and not revert to the default Python icon
  4. Use proper Windows AppUserModelID to ensure taskbar icon persistence
  5. Set the icon on both QApplication (for taskbar) and QMainWindow (for title bar)
  6. The icon should be set BEFORE creating the main window for best Windows compatibility

  Please provide Python code using PyQt5 that properly implements this Windows icon system with best    
   practices for icon persistence.

----------------------

---------------

RUT, NDX, and SPX options are all cash-settled index options → 
qualify for 60/40 tax treatment under Section 1256.

Summary
The 60/40 rule applies to Section 1256 contracts.
-Those include:
Futures
Options on futures
Broad-based index options (like SPX)
-It does not apply to:
Stock options
ETF options (SPY, QQQ, IWM)
Individual equity or crypto trades

60/40 Tax Treatment (Section 1256):
Cash-Settled:

SPX (S&P 500 Index options)
NDX (Nasdaq-100 Index options)
RUT (Russell 2000 Index options)
VIX (Volatility Index options/futures)
DJX (Dow Jones Index options)
XSP (Mini-SPX options)
ES (E-mini S&P 500 futures)
NQ (E-mini Nasdaq-100 futures)
RTY (E-mini Russell 2000 futures)
YM (E-mini Dow futures)

Physically-Settled:

Currency futures
Commodity futures (gold, oil, etc.)
Treasury futures

🟢 Cash-Settled, 60/40 Treatment Applies (Section 1256)
Instrument	Type	Tax Treatment	Notes
SPX	S&P 500 Index Options	✅ 60/40	Cash-settled, European-style
NDX	Nasdaq-100 Index Options	✅ 60/40	Cash-settled, European-style
RUT	Russell 2000 Index Options	✅ 60/40	Cash-settled, European-style
DJX	Dow Jones Index Options	✅ 60/40	Cash-settled
XSP	Mini-SPX Options	✅ 60/40	Cash-settled, same as SPX but smaller
VIX	Volatility Index Options/Futures	✅ 60/40	CBOE confirmed Section 1256 treatment
ES	E-mini S&P 500 Futures	✅ 60/40	CME futures, always under §1256
NQ	E-mini Nasdaq-100 Futures	✅ 60/40	Same
RTY	E-mini Russell 2000 Futures	✅ 60/40	Same
YM	E-mini Dow Futures	✅ 60/40	Same
🟡 Physically-Settled (Still §1256)
Instrument	Type	Tax Treatment	Notes
Currency Futures	Physically-settled	✅ 60/40	FX futures are §1256 contracts
Commodity Futures (Gold, Oil, etc.)	Physically-settled	✅ 60/40	Listed futures are §1256 contracts
Treasury Futures	Physically-settled	✅ 60/40	CME Treasury futures qualify under §1256
⚙️ Summary

✅ All listed cash-settled and physically-settled futures are treated under Section 1256.

✅ All receive 60/40 blended tax treatment.

❌ Exceptions would include single-stock options or ETF options (like SPY, QQQ, IWM) — these 
are not §1256 and are 100% short-term unless held >1 year.

--------

🧭 Index Options Ticker Symbols by Broker — TL;DR

Interactive Brokers

Uses standardized cash-settled index symbols.

Index         Ticker     Exchange
S&P 500       SPX        CBOE
NASDAQ-100    NDX        NASDAQ
Dow Jones     INDU       NYSE
Russell 2000  RUT        CBOE

Charles Schwab

Uses DJX for Dow Jones instead of INDU.

Index         Ticker
S&P 500       SPX
NASDAQ-100    NDX
Dow Jones     DJX
Russell 2000  RUT

Symbols often appear as $SPX, $NDX, etc., but you trade
without $.

Tradier

Uses CBOE standard symbols; also supports weekly
variants.

Index         Ticker
S&P 500       SPX / SPXW
NASDAQ-100    NDX
Dow Jones     DJI / INDU
Russell 2000  RUT / RUTW

Alpaca

❌ No direct index options trading.

Only supports stocks, ETFs, crypto.

Use ETFs for index exposure: SPY, QQQ, DIA, IWM.

💡 Key Takeaways

Standardized symbols (SPX, NDX, RUT) across brokers
due to CBOE listing.

Weekly options supported via SPXW and RUTW.

Alpaca limitation: no index options—use ETFs instead.

As part of extended trading hours the following symbols are traded until 16:15 ET.

AUM, AUX, BACD, BPX, BRB, BSZ, BVZ, CDD, CITD, DBA, DBB, DBC, DBO, DBS, DIA, DJX, 
EEM, EFA, EUI, EUU, GAZ, GBP, GSSD, IWM, IWN, IWO, IWV, JJC, JPMD, KBE, KRE, MDY, 
MLPN, MNX, MOO, MRUT, MSTD, NDO, NDX, NZD, OEF, OEX, OIL, PZO, QQQ, RUT, RVX, SFC, 
SKA, SLX, SPX, SPX (PM Expiration), SPY, SVXY, UNG, UUP, UVIX, UVXY, VIIX, VIX, VIXM, 
VIXY, VXEEM, VXST, VXX, VXZ, XEO, XHB, XLB, XLE, XLF, XLI, XLK, XLP, XLU, XLV, XLY, 
XME, XRT, XSP, XSP (AM Expiration), & YUK

     Lukas Frohlich (The Short Bear)
	-Core Trading Philosophy
Agenda Trading - Understanding why something should happen with high probability. For Lucas, this meant reading SEC filings to understand when small caps needed to raise money (dilution plays). The combination of technical setup + fundamental agenda gave him confidence to size up.
	-Quantitative Approach to Setups
Create "buckets" for specific setups you can scan for
Track average moves: high-of-day from open, open-to-close, high-to-low
Build expectancy based on historical data for that bucket
Stop loss based on divergence from average pattern behavior

	-Pyramiding Strategy
Start with base position at likely rejection level
Cut quickly if wrong (he'd take 2-3 small losses)
Once trade confirms, add size as it moves in favor
Move stop to lock in the adds while maintaining edge
