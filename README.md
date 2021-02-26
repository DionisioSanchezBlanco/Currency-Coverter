<strong>Description</strong>

On this stage, you need to specify what currency you want to exchange. Imagine that you came to the bank with some money in your pocket. You want to choose the best currency to exchange your money for. First, read the currency to exchange, then read the currency you might exchange your money for and the amount of money you want to exchange. Notice that the input number can have a fractional part!

There is a different amount of currencies in different tests. Checking if input is empty might be really useful.
Parse the data from FloatRates. You can store it in any collection you want. It's called caching – a simple way to speed up the program. If we need to exchange the same currencies that we have already changed, we won't need to connect to the Internet, we only need to refer to the data in our cache.

Check the cache — the required currency might be already in there, print the result afterward. Output the amount of money that the bank employee should give you.

<strong>Objectives</strong>

You're in the bank. Think about how much and what kind of currency you have.

Take the currency code, the amount of money that you have, and the currency code that you want to receive as the user input.
Retrieve the data from FloatRates as in the previous exercises.
Save the exchange rates for USD and EUR.
Read the currency to exchange for and the amount of money.
Take a look at the cache. Maybe you already have what you need?
If you have the currency in your cache, calculate the amount.
If not, get it from the site, and calculate the amount.
Save all the information to your cache.
Repeat steps 3-7 until there is no currency left to process.
Print the results.
