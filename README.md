# Market Router: Neutral Portfolio Requester
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Website](https://img.shields.io/badge/Visit-marketrouter.ai-blue)](https://marketrouter.ai)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/GroupLang.svg?style=social&label=Follow%20%40GroupLang)](https://twitter.com/GroupLang)
## Overview
The Neutral Portfolio Requester is a service designed to facilitate neutral portfolio creation through [Market Router API](https://marketrouter.ai/). It leverages the [exa API](https://exa.ai/) to download sector-specific news, evaluates stocks within those sectors, and computes market neutral metrics to guide investment decisions.

Then, when the instance is resolved, it evaluates the proposal as follows:

- Download news for each S&P sector using [exa API](https://exa.ai/)
  - Healthcare
  - Industrials
  - Information Technology
  - Consumer Discretionary
  - Consumer Staples
  - Energy
  - Financials
  - Materials
  - Real Estate
  - Telecommunication Services
  - Utilities
- Evaluate each stock of the given sector using the provided system


## Installation

1. **Clone the repository**

   ```shell
   git clone https://github.com/GroupLang/market-neutral-requester.git
   cd market-neutral-requester
   ```
2. **Install required libraries**
   ```shell
   python3.11 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Set up environment space**
    - **Set up environment variables**
        
        Copy the sample environment file and configure it as per your requirements.

        ```shell
        [ ! -f .env ] && cp .env.template .env
        ```

    - **Install pre-commit**

        Install the pre-commit hooks to ensure that your commits meet the project's standard for code quality and formatting. This will set up hooks that run checks such as linting and formatting before you commit your changes, helping to catch errors early and maintain consistent code style throughout the project.

        ```shell
        pre-commit install
        ```

## Configuration

- **Market Router**:
  - **Username, Fullname, Email, Password**: These credentials are used for authentication and identification in the market router. If the user is already registered, these parameters are not necessary; instead, add the Market Router API key to the `.env` file as `MARKET_ROUTER_KEY`.
  - **Deposit Amount**: Specify the initial deposit amount for transactions in the market router if needed.
  
- **Instance**:
  - **Model**: Specify the model used for executing the strategy, such as "gpt-3.5-turbo".
  - **Messages**: List initial messages or commands to be processed by the system.
  - **Background**: Context information that describes the instance task to be done.
  - **Max Credit per Instance**: Maximum credit willing to be paid for resolving the instance.
  - **Instance Timeout**: Set the time limit in seconds for the instance to remain active before timing out.
  - **Gen Reward Timeout**: The time (in seconds) within which the requester must send the gen reward.
  - **Gen Seward**: The reward signal observed and reported by the requester to the marketplace.
  - **Percentage Reward**: The percentage of the Gen Reward that the requester will pay to the provider once the interaction is completed.

These configuration variables are stored in the config file, ensuring the Neutral Portfolio Provider can effectively interact with the Market Router by managing its proposals and financial transactions.

## Key Components and Processes

**Market Router Scripts:**
1. **Register User Script**
   ```shell
   python -m market_router.scripts.register
   ```
   This command registers a new user with the Market Router API. If an `MARKET_ROUTER_KEY` exists (indicating prior registration), this script is unnecessary.

2. **Create API Key Script**
   ```shell
   python -m market_router.scripts.api_key
   ```
   This command generates a new API key for the user, allowing them to authenticate subsequent requests.

3. **Deposit Script**
   ```shell
   python -m market_router.scripts.deposit
   ```
   This command facilitates depositing funds into an Market Router account, as specified in the `deposit_amount` configuration.

4. **Create Instance Script**
   ```shell
   python -m market_router.scripts.instance
   ```
   This script submits proposals to the Market Router using `config`.
   
6. **Chat Completions**
   ```shell
   python -m market_neutral.scripts.sector_market_pipeline --market="sp500" --sector="Energy"
   ```
   Interacts with the proposal endpoint before submitting the reward.
   
7. **Submit the Generated Reward**
   ```shell
   python -m market_router.scripts.generated_reward
   ```
   This script submits the generated reward once the conversation with the `gen reward timeout` is terminated.
   

   
## Example

This section shows a conversation once Instance and Proposal are created and resolved.

#### Input

```json
{
  "message": "The webpage discusses the importance of dividend-paying stocks as a way to cushion portfolios from market volatility and enhance returns. Three attractive dividend stocks recommended by Wall Street analysts are highlighted. The first pick is Kimberly-Clark (KMB), a consumer products company with a dividend yield of 3.5%. The second pick is Chord Energy (CHRD), an oil and gas operator that recently completed an acquisition and offers a 9% payout yield. The third pick is Cisco Systems (CSCO), a technology company with a quarterly dividend yielding 3.5%. Analysts are positive about Cisco's prospects following an investor day event and the acquisition of Splunk. Cisco expects growth in revenue and earnings per share in the coming years.",
  "model": "gpt-3.5-turbo"
}
```

#### Output

```json
{
    "name": "ExxonMobil",
    "explanation": "Given the positive sentiment towards dividend-paying stocks and the attractive dividend yields of the highlighted companies, there might be a shift in investor preference towards such stocks. ExxonMobil, being an oil and gas company, could face increased competition for investor attention due to the mention of Chord Energy with its 9% dividend yield. This could lead to potential selling pressure on ExxonMobil.",
    "action": "SELL"
}
```