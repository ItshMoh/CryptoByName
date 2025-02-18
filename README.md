# CryptoByName

A natural language crypto payment automation tool.

## Overview

CryptoByName lets you send cryptocurrency using simple natural language commands. Instead of dealing with complex wallet addresses, just type commands like "transfer 3 ETH to Shweta" - making crypto transactions as easy as sending a text message.

## Features

- Natural language processing for crypto transfers
- Send to recipients by name instead of addresses
- Currently works with Oasis Network (configurable)
- Simple CLI interface

## Setup

1. Configure a MongoDB database to store recipient names and addresses
2. Set up your private key for transaction signing
3. Configure your preferred network (default: Oasis Network)

## Usage

After setup, simply run the application and use natural language commands in the terminal:

```
transfer 3 eth to Shweta
```

The system looks up Shweta's wallet address from your contacts database and handles the transaction automatically.

## Requirements

- MongoDB
- Private key for signing transactions
- Network configuration

## Important Note

This project is still under development - please only use with test networks and test coins. Do not use with real cryptocurrency at this stage.

## Future Development

- Feature for getting information about the blockchain with interactive graphs to track the progress.
- Transaction history and tracking
- Improved security features

## Contributing

Contributions welcome! This is a proof-of-concept that's actively being developed into a full product.
