import yfinance as yf

def trading_bot():
    print("MY TRADING BOT STARTED")

    markets = {
        "Bitcoin": "BTC-USD",
        "Ethereum": "ETH-USD",
        "Apple Stock": "AAPL"
    }

    for name, symbol in markets.items():
        try:
            data = yf.download(
                symbol,
                period="3mo",
                interval="1d",
                auto_adjust=True,
                progress=False
            )

            close = data["Close"].squeeze().dropna()
            ema20 = close.ewm(span=20).mean()
            ema50 = close.ewm(span=50).mean()

            if ema20.iloc[-1] > ema50.iloc[-1]:
                signal = "BUY"
            elif ema20.iloc[-1] < ema50.iloc[-1]:
                signal = "SELL"
            else:
                signal = "HOLD"

            print(name, ":", signal)

        except Exception as error:
            print(name, ": Data unavailable")

trading_bot()
