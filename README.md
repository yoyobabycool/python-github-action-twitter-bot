# Twitter bot

A GitHub Actions Repository for Automated Tweeting of Quotes Using Python.

## Overview

This project is a GitHub Actions repository that automates the process of tweeting quotes on Twitter. The repository runs a workflow every hour, which fetches a random quote from a `quotes.json` file and publishes it on Twitter (https://twitter.com/coronavirusbot0).

## Features

- Fetches a random quote from `quotes.json` every hour.
- Tweets the quote on Twitter automatically.

## Prerequisites

To use this GitHub Actions repository, you need to have the following:

- A Twitter Developer Account: Obtain API keys and access tokens from the Twitter Developer Portal.
- Add your API keys as secret keys in actions in secrets and variables in settings
- A `quotes.json` File: Create a JSON file containing a collection of quotes to be tweeted.

## Steps to add workflow
Go to Actions -> New Workflow -> Configure Python Application -> Edit python-app.yml based on requirement -> commit changes

## Customization

Feel free to customize this repository to suit your requirements. You can modify the workflow schedule, or enhance the tweet formatting.

## Contributions

Contributions to this project are welcome. If you have any ideas, bug fixes, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

