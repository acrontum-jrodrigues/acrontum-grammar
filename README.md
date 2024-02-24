# Acrontum Grammar

## Introduction

This is a substitute for Grammarly, which was blocked by the company due to data privacy concerns. It is a simple grammar checker that uses the [grammarly/coedit-large model](https://huggingface.co/grammarly/coedit-large) to check for grammar errors in a given text.

## Usage

To run the api server:

```bash
cd api && python3 app.py
```

Or with Docker:

```bash
docker build -t acrontum-grammar-api .
docker run -p 5000:5000 acrontum-grammar-api
```

To run the web app:

```bash
cd client && pnpm dev
```

## Limitations

Only the english language is supported.
