# Solana Arbitrage Bot   
[![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/6DTGbMNYuA)[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/playlist?list=PLMIFlNMah1MnCqDsEJ0P2QhDr93O9KYmF)[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/RudeLabs_io)

[![](https://dcbadge.limes.pink/api/server/6DTGbMNYuA)](https://discord.gg/6DTGbMNYuA)

### [Video Tutorial](https://www.youtube.com/playlist?list=PLMIFlNMah1MnCqDsEJ0P2QhDr93O9KYmF)

**Over $500k profit produced for users since March 2024!**

## Requirements
- Ubuntu >= 22 OS Server ([Nodestop](https://billing.nodestop.io/aff.php?aff=88) and [Tier.net](https://billing.tier.net/aff.php?aff=257) are good)
- 12 cores or more
- Baremetal/Dedicated server is suggested
- RPC + GRPC connections ([Pixel](https://discord.gg/RYnvkvqxbF), [Shyft](https://discord.gg/mkax7WUu3z), [Rift](https://discord.gg/riftnode), [Shark](https://discord.gg/kMEdGGfuqb))
- Profit scales with capital (larger trade sizes, larger profits)

### Ask [Claude](https://claude.ai/)/ChatGPT how to remote into your Ubuntu server
- This is different for every PC's Operating System
- You will receive the login credentials from your server provider
- For example, if your PC is Windows 10, you need ask [Claude](https://claude.ai/)/ChatGPT how you would remote into your Ubuntu server using Windows 10

## Installation on your Ubuntu >=22 Server

### New Server Setup
Run these commands sequentially:
```bash
sudo apt update && apt upgrade -y && apt install -y screen unzip && apt install python3-pip -y
```
```bash
pip3 install requests python-dotenv
```
```bash
wget https://github.com/AlexRubik/rude-bot-solana/releases/download/v3.2.0-alpha/rude-bot-alpha3_2_0.zip
```
```bash
unzip rude-bot-alpha3_2_0.zip
```
```bash
cd rude-bot-alpha3_2_0
```
Use the --help arg to see all the possible args and what they do:
```bash
./rude --help
```
Quickstart Guide to getting the bot running ASAP:
```bash
./rude --overview
```

3.2.0
