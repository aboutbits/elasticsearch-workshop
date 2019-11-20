# Exercises

## Exercise 1 - Global Analyze API and Built-in Analyzers

Analyze the following text using the given analyzers. But don't create your own index, just try to analyze directly the text. Check the outputed tokens and how the analyzers work differently.

Text:

> The 4 programmers are thinking about new interesting features that they should implement using XP.

Analyzers:

- Standard Analyzer (standard)
- Simple Analyzer (simple)
- Whitespace Analyzer (whitespace)
- Stop Analyzer (stop)

## Exercise 2 - Index Analyzer API and Custom Analyzers

1. Create an index with the name `text-analysis-2` and the following details:

    - Custom Analyzer with the name `message_analyzer`:
        - Charater filter: HTML strip char filter (html_strip)
        - Tokenizer: Standard tokenizer (standard)
        - Token filter: Lowercase token filter (lowercase)
    - Mapping for the field `message`:
        - Type: `text`
        - Analyzer: `message_analyzer`

2. Analyze the following text by referencing the analyzer of the index:

    > The <b>CUSTOM</b> analyzers are awesome!

3. Analyze the same text by referencing the analyzer of the field `message`

## Exercise 3 - Custom Analyzer with Synonyms and Stopwords

1. Create an index with the name `text-analysis-3` and the following details:

    - Custom Analyzer with the name `message_analyzer`:
        - Tokenizer: Whitespace tokenizer (whitespace)
        - Token filter: Stopwords token filter (stop)
            - Built-in english stopwords
        - Token filter: Synonyms token filter (synonym)
            - :) should be converted to happy
            - :( should be converted to sad
    - Mapping for the field `message`:
        - Type: `text`
        - Analyzer: `message_analyzer`

2. Analyze the following text:

    > Today is a new day and I'm so :)

3. How is the text analyzed and what benefits / use cases could this analyzer have?

## Exercise 4 - Custom Analyzer with NGrams

1. Create an index with the name `text-analysis-4` and the following details:

    - Custom Analyzer with the name `message_analyzer`:
        - Tokenizer: Standard tokenizer (standard)
        - Token filter: Lowercase token filter (lowercase)
        - Token filter: NGram token filter (ngram)
            - min_gram: 3
            - max_gram: 3
    - Mapping for the field `message`:
        - Type: `text`
        - Analyzer: `message_analyzer`

2. Analyze the following text:

    > Apfelsaft ohne Zusatzstoffe

3. How is the text analyzed and what benefits / use cases could this analyzer have?

## Exercise 5 - Language Analyzers

Try out different built-in language anaylzers like `english`, `german` or `italian`. Analyze different texts with them. Try to find out what different components (charater filters, tokenizer, token filters) they are using under the hood.
