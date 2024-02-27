# HKUST(GZ) Academic Network Optimization - Clash Rules Generator

## Overview

This repository contains a Python script designed to address a specific need within the HKUST(GZ) academic community. With the activation of the academic network, it has been observed that access to certain nodes has been optimized by the school, eliminating the need to route traffic through these nodes for access. The provided script automates the process of converting an optimized website list into clash rules, facilitating seamless access to these resources without unnecessary routing.

## Purpose

The primary goal of this script is to streamline the user experience for HKUST(GZ) community members by generating clash rules for already optimized websites. This ensures that the academic network is utilized efficiently, with optimized access paths being leveraged where available.

## How It Works

The script reads a text file containing a list of URLs, each representing an optimized website. It processes each URL according to the following logic:

1. If a URL is prefixed with "*.", this prefix is removed, and the URL is marked with a "DOMAIN-SUFFIX" type.
2. If a URL does not have this prefix, it is processed as a "DOMAIN" type.
3. Each processed URL is then formatted into a clash rule, specifying the channel as "🎯 全球直连". (Could be alternated with your own subscription)

The output is a new text file containing the generated clash rules, ready to be integrated into your Clash configuration.

## Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Save the script as `generate_clash_rules.py`.
3. Run the script from the command line, providing the path to your list of optimized websites as follows:

```bash
python generate_clash_rules.py <path_to_your_file>