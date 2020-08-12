# The Fedex Economy
**The Problem:** The [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html) can turn the [FedEx SameDay bots](https://www.youtube.com/results?search_query=fedex+sameday+bot) into a new way to fund small businesses. We can build a token economy where startups thrive. 

**The Hack:** The [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html) allow the bots to make deliveries and accept FedEx tokens. The tokens fund startups. The startups are an engine for growth

**Potential Impact:** The bots become self-owning infrastructure that powers a small business ecosystem. The ecosystem generates block chain data that allow for new [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html).

**Watch the overview video...**

## Overview
FedEx unveiled the [SameDay Bot](https://www.youtube.com/results?search_query=fedex+sameday+bot)-- an autonomous vehicle for last-mile delivery. Using the [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html), we can transform the bots into a new way to fund small businesses. The [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html) allow the bots to make deliveries and accept FedEx tokens. The tokens fund startups. The startups are an engine for growth. This is the idea behind FedEx economy. 

The [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html) can do more than support apps. It can support a token economy where startups thrive.  And the resulting block chain data could make the FedEx APIs even more valuable.

## The Demo
The FedEx economy runs on FX tokens and is powered by a smart contract running on the block chain. Start by registering with the smart contract. You'll need FX tokens. You can buy them on the token exchange, you can earn them in the market, or they can be granted to you by FedEx (or anyone else with tokens.)

Let's start a business. Register in the marketplace. Create a profile and launch your startup. 

Let's buy something. Shop for products and services, place an order, and make a payment.

You can buy tokens on the exchange. You can sell your tokens on the exchange. Or, using your wallet, you can give your tokens away.

## The Design

We wrote a finite-state machine that extends the artificial intelligence of the FedEx Same-day bot. It turns the drone into self-owning infrastructure that earns FeX tokens by making deliveries and using those tokens to pay for its maintenance. The drone AI depends on the [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html) to validate delivery jobs sent by users of the marketplace. The drone is programmed to manage its own repairs. The drone determines when it needs maintenance, and can decide to hire a technician from the FedEx economy.  The drone uses the [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html) to locate a nearby FedEx office and arrange to meet the technician for repairs.

The smart contract automatically enforces the rules of the FedEx economy. It determines how to create and distribute FeX tokens. It keeps track of service providers, service consumers and the FeX balances of everyone participating in the FedEx economy. The drone interacts directly with the smart contract to take on delivery jobs and hire technicians for maintenance. Human users interact with the smart contract through the marketplace website.

The markteplace website is how allows entreprenuers to create a startup in the FedEx economy. Startups receive initial funding from FedEx in the form of FeX tokens. A startup can use those tokens to purchase services (like drone deliveries) needed for the business. They can also earn FeX by providing services to shoppers. The marketplace allows shoppers to purchase any service registered in the FedEx economy. Shoppers can browse service providers, read profiles, and make orders. Anyone registered in the marketplace can check their FeX balance and exchange dollars for FeX.

### The FedEx SameDay Bot

The finite-state machine is a Python/Flask web service running on Heroku. When initialized, the drone automatically connects with the smart contract and begins autonomous operations. The bot code communicates with the [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html) usign HTTP.

### The Smart Contract

The smart contract is a Python/Flask web service running on Heroku. We have written a version of the smart contract in both Python/Flask and Solidity. In production, we'll deploy the smart contract as solidity code running on the live Etherium block chain. For demonstration, we deployed the smart contract as a web service to avoid the cost and complication of running on a live block chain network.

### The FedEx Marketplace
 
The FedEx marketplace is a Python/Flask website that communicates with the smart contract. The client-side code runs Javascript and HTML5. The server-side code executes in Python on the Heroku server. Events like order and profile updates are communicated from the smart contract to the marketplace in real time using web sockets.

## Important Links

- Main presentation. Open this in presentation mode.
- Summary video
- The [FedEx Economy marketplace website](https://fedex-economy-market.herokuapp.com/)
- [The drone state machine code](https://github.com/jerryaoverton/fedex-economy-drone)
- [The smart contract (web service version)](https://github.com/jerryaoverton/fedex-economy-smartcontract)
- The smart contract (Solidity version)
- [The FedEx Economy marketplace website code](https://github.com/jerryaoverton/fedex-economy-market)
