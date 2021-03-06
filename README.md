# The FedEx Economy
**The Problem:** The [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html) can turn the [FedEx SameDay bots](https://www.youtube.com/results?search_query=fedex+sameday+bot) into a new way to fund small businesses. We can build a token economy where large and small businesses connect and startups thrive. 

**The Hack:** The [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html) allow the bots to make deliveries and accept FedEx tokens. The tokens (supported by an ecosystem of large and small businesses) fund startups. The startups are an engine for growth.

**Potential Impact:** The bots become self-owning infrastructure that powers a business ecosystem. The ecosystem generates block chain data that allow for new [FedEx APIs](https://www.fedex.com/en-ca/resources-tools/api.html).

**Watch the overview video...**

## Overview
FedEx unveiled the [SameDay Bot](https://www.youtube.com/results?search_query=fedex+sameday+bot)-- an autonomous vehicle for last-mile delivery. Using the FedEx APIs, we can transform the bots into a new way to fund small businesses. The FedEx APIs allow the bots to make deliveries and accept FedEx tokens. The tokens fund startups. The startups are an engine for growth. This is the idea behind FedEx economy. 

The FedEx APIs can do more than support apps. It can support a token economy where startups thrive.  And the resulting block chain data could make the FedEx APIs even more valuable.

## The Demo
The enclosed video provides a demo of the [FedEx economy](https://fedex-economy-market.herokuapp.com/) functionality. It covers:
1. Registering with the smart contract. 
1. Buying, earning and exchanging FEx tokens
1. Launching business
1. Shopping for products and services (including FedEx SameDay Bot deliveries)


## The Design

We wrote a finite-state machine that extends the artificial intelligence of the FedEx SameDay Bot. It turns the drone into self-owning infrastructure that earns FEx tokens by making deliveries and using those tokens to pay for its maintenance. The drone AI depends on the FedEx APIs to validate delivery jobs sent by users of the marketplace. The drone is programmed to manage its own repairs. The drone determines when it needs maintenance and can decide to hire a technician from the FedEx Economy.  The drone uses the FedEx APIs to locate a nearby FedEx office and arrange to meet the technician for repairs.

The smart contract automatically enforces the rules of the FedEx Economy. It determines how to create and distribute FEx tokens. It keeps track of service providers, service consumers and the FEx balances of everyone participating in the FedEx Economy. The drone interacts directly with the smart contract to take on delivery jobs and hire technicians for maintenance. Human users interact with the smart contract through the [marketplace website](https://fedex-economy-market.herokuapp.com/).

The [marketplace website](https://fedex-economy-market.herokuapp.com/) is how allows entrepreneurs to create a startup in the FedEx economy. Startups receive initial funding from FedEx in the form of FEx tokens. A startup can use those tokens to purchase services (like drone deliveries) needed for the business. They can also earn FEx by providing services to shoppers. The marketplace allows shoppers to purchase any service registered in the FedEx economy. Shoppers can browse service providers, read profiles, and make orders. Anyone registered in the marketplace can check their FEx balance and exchange dollars for FEx.

### The FedEx SameDay Bot

The finite-state machine is a Python/Flask web service running on Heroku. When initialized, the drone automatically connects with the smart contract and begins autonomous operations. The bot code communicates with the FedEx APIs using HTTP.

### The Smart Contract

The smart contract is a Python/Flask web service running on Heroku. We have written a version of the smart contract in both Python/Flask and Solidity. In production, we'll deploy the smart contract as solidity code running on the live [Etherium](https://www.coindesk.com/learn/ethereum-101/what-is-ethereum) block chain. For demonstration, we deployed the smart contract as a web service to avoid the cost and complication of running on a live block chain network.

### The FedEx Marketplace
 
The FedEx marketplace is a Python/Flask website that communicates with the smart contract. The client-side code runs JavaScript and HTML5. The server-side code executes in Python on the Heroku server. Events like order and profile updates are communicated from the smart contract to the marketplace in real time using web sockets.

## Installing the Applications

The drone, smart contract, and web site are all Python applications. Each should be installed and run as follows:
1. [Download and install Python](https://www.python.org/downloads/)
1. Use the requirements.txt file to install dependent packages by [running pip: -r requirements.txt](https://note.nkmk.me/en/python-pip-install-requirements/)
1. Use the command line to [run the Python script](https://realpython.com/run-python-scripts/)

Start the smart contract first, then the website, then the drone. The local URL for accessing each component will be given in the command line after successful execution.

## Important Links

- Main presentation. Open this in presentation mode.
- Summary video
- The [FedEx Economy marketplace website](https://fedex-economy-market.herokuapp.com/)
- [The drone state machine code](https://github.com/jerryaoverton/fedex-economy-drone)
- [The smart contract (web service version)](https://github.com/jerryaoverton/fedex-economy-smartcontract)
- [The smart contract (Solidity version)](https://github.com/jerryaoverton/fedex-api-hackathon-2020/tree/master/Code/Solidity%20Smart%20Contract)
- [The FedEx Economy marketplace website code](https://github.com/jerryaoverton/fedex-economy-market)
