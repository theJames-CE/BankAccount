# BankAccount

<h1>Assignment: BankAccount</h1>

<b>Learning Objectives:</b><br>

<li>Students will follow specifications for creating a class.</li><br>

<li>Students will implement default arguments in parameters for attributes that can be assigned on instantiation.</li><br>

<li>Students will use basic programmatic logic to implement the functionality of a bank account</li><br>

<li>Students will handle edge-cases, such as insufficient funds, with the appropriate control structure (if-else, code flow, or early exit)</li><br>

<li>Students will demonstrate proficiency in creating and update attributes of an object instance, from within the class using <i>self</i> .</li><br>

<li>Students will thoroughly test the functionality of their class by creating instances and calling methods with different test data and scenarios.</li><br>

![image](https://github.com/theJames-CE/BankAccount/assets/124546382/60d867c0-5cf4-486a-8b64-7af5acfaea22)

If you imagine a banking system, and how the data is modeled, you may think, well, everything should be tied to the customer, in other words, the user. But users have accounts, and accounts have balances. This gives us the idea that maybe an account is its own class apart from the user class. But as we stated, it is not completely independent of the User class; accounts only exist because users open them.<br>

<i>For this assignment, don't worry about putting any user information in the BankAccount class. We'll take care of that in the next lesson!</i><br>

Let's first just get some more practice writing classes by writing a new BankAccount class.<br>

The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)<br>

The class should also have the following methods:<br>

<li><b>deposit(self, amount)</b> - increases the account balance by the given amount</li><br>

<li><b>withdraw(self, amount)</b> - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5</li><br>

<li><b>display_account_info(self)</b> - print to the console: eg. "Balance: $100"</li><br>

<li><b>yield_interest(self)</b> - increases the account balance by the current balance * the interest rate (as long as the balance is positive)</li><br>

This means we need a class that looks something like this:

![image](https://github.com/theJames-CE/BankAccount/assets/124546382/29025ccf-37d6-4dce-aa95-6911b4508cef)

![image](https://github.com/theJames-CE/BankAccount/assets/124546382/6d1c7b6d-d1a1-4f0a-b397-deb4d20e95e3)

#CodingDojo
