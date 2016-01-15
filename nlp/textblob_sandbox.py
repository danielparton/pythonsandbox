#!/usr/bin/env python
# -*- coding: utf-8 -*-
from textblob import TextBlob
import re

website_texts = [
u"""What is high-fructose corn syrup? What are the health concerns?

Answers from Katherine Zeratsky, R.D., L.D.
High-fructose corn syrup is a common sweetener in sodas and fruit-flavored drinks. As use of high-fructose corn syrup has increased, so have levels of obesity and related health problems. Some wonder if there's a connection.

Research has shown that high-fructose corn syrup is chemically similar to table sugar. Controversy exists, however, about whether the body handles high-fructose corn syrup differently than table sugar.

At this time, there's insufficient evidence to say that high-fructose corn syrup is any less healthy than other types of sweeteners.

It is known, however, that too much added sugar of all kinds — not just high-fructose corn syrup — can contribute unwanted calories that are linked to health problems, such as weight gain, type 2 diabetes, metabolic syndrome and high triglyceride levels. All of these boost your risk of heart disease.

The American Heart Association recommends that most women get no more than 100 calories a day of added sugar from any source, and that most men get no more than 150 calories a day of added sugar. That's about 6 teaspoons of added sugar for women and 9 teaspoons for men.

If you're concerned about your health, the smart play is to cut back on added sugar, regardless of the type.
"""
]

hfcs_keywords = ['high', 'fructose', 'corn', 'syrup']

for website_text in website_texts:
    tb = TextBlob(website_text)
    hfcs_sentences = []
    for sentence in tb.sentences:
        if all([True if sentence.lower().find(keyword) > -1 else False for keyword in hfcs_keywords]):
            print sentence
            print sentence.sentiment
            hfcs_sentences.append(sentence)

