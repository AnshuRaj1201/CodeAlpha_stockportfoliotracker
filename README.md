# 📈 Stock Portfolio Tracker

A beginner-friendly Python command-line application that helps you track your stock investments. Enter stock names and quantities, and the program calculates your total portfolio value based on predefined prices — with an option to save results to a file.

---

## 🌟 Features

- 🔍 Look up stock prices from a built-in dictionary
- 📝 Input multiple stocks and quantities interactively
- 🧮 Automatically calculates total investment value per stock and overall
- 💾 Save your portfolio summary to a `.txt` file
- ⚠️ Validates stock symbols and guides you to available options

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Concepts used:** Dictionaries, loops, input/output, arithmetic, file handling

> No external libraries required — runs with pure Python!

---

## 📂 Project Structure

```
stock-portfolio-tracker/
│
├── stock_tracker.py    # Main program file
├── portfolio.txt       # Generated output file (created after running)
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed. Check by running:

```bash
python --version
```

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/stock-portfolio-tracker.git
   cd stock-portfolio-tracker
   ```

2. **Run the program**

   ```bash
   python stock_tracker.py
   ```

---

## 💻 Usage

When you run the program, it will:

1. Display available stock symbols
2. Prompt you to enter a stock name and quantity
3. Repeat until you type `done`
4. Show a full portfolio summary
5. Ask if you'd like to save the results to `portfolio.txt`

### Example Session

```
=== Stock Portfolio Tracker ===
Available stocks: ['AAPL', 'TSLA', 'GOOGL', 'AMZN', 'MSFT']

Enter stock name (or 'done' to finish): aapl
  How many shares of AAPL? 10

Enter stock name (or 'done' to finish): TSLA
  How many shares of TSLA? 5

Enter stock name (or 'done' to finish): done

--- Portfolio Summary ---
  AAPL  :  10 shares ×   $180 =    $1,800
  TSLA  :   5 shares ×   $250 =    $1,250

  Total Portfolio Value: $3,050

Save results to file? (yes/no): yes
✓ Saved to portfolio.txt
```

---

## 📊 Available Stocks

| Symbol | Company         | Price (USD) |
|--------|-----------------|-------------|
| AAPL   | Apple Inc.      | $180        |
| TSLA   | Tesla Inc.      | $250        |
| GOOGL  | Alphabet Inc.   | $140        |
| AMZN   | Amazon.com Inc. | $185        |
| MSFT   | Microsoft Corp. | $420        |

> To add more stocks, edit the `stock_prices` dictionary in `stock_tracker.py`.

---

## 🔧 Customization

Open `stock_tracker.py` and update the `stock_prices` dictionary to add your own stocks:

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 420,
    "NVDA": 875,   # ← add new stocks here
}
```

---

## 🗺️ Roadmap / Future Improvements

- [ ] Add error handling for invalid quantity input (`try/except`)
- [ ] Support saving as `.csv` format
- [ ] Allow updating quantity if the same stock is entered twice
- [ ] Fetch live stock prices using an API (e.g., `yfinance`)
- [ ] Add a simple GUI using `tkinter`

---

## 🧑‍💻 Anshu Raj
Github-https://github.com/AnshuRaj1201/CodeAlpha_stockportfoliotrackern

LinkedIn-www.linkedin.com/in/anshuraj1201




Built as a beginner Python project to practice:
- Dictionary operations
- `while` loops and user input
- Basic arithmetic
- File handling with `open()` and `with`

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- Inspired by beginner Python project ideas for learning core programming concepts
- Great next step after learning variables and functions!
