
# EMP: An Agent-Based Economic Simulation Platform - Project Overview

## Core Idea

EMP is an interactive economic simulation platform where users create a simplified economy, adjust economic variables, introduce shocks, and observe how the economy changes over time.

The purpose is to make economics more understandable and tangible by allowing users to experiment with economic decisions and directly see the consequences.

Instead of only learning economic theory, users can simulate it.


# Main Concept

The economy consists of different agents:

## Households:

* Earn wages
* Pay taxes
* Consume goods
* Save money
* Change spending behaviour depending on income, prices, and confidence
* May become unemployed

## Firms:

* Produce goods
* Hire workers
* Set prices
* Earn revenue
* Make profits or losses
* Adjust production depending on demand

## Government:

* Collects taxes
* Spends money
* Uses fiscal policy to influence demand

## Central bank:

* Controls interest rates
* Influences borrowing, saving, investment, and inflation

## User Experience

The user creates an economy by selecting variables such as:

* Number of households
* Number of firms
* Wage levels
* Tax rates
* Interest rates
* Government spending
* Productivity
* Consumer confidence
* Initial wealth distribution

# Key Outputs

## The dashboard displays:

* GDP/output
* Inflation
* Unemployment
* Average income
* Wealth inequality
* Firm profits
* Savings rates
* Consumption levels
* Government budget position

## Economic Shocks

Users can introduce events such as:

## Interest Rate Rise

Possible effects:

* Lower borrowing
* Lower consumption
* Reduced inflation
* Higher unemployment risk

## Tax Cut

Possible effects:

* Higher disposable income
* Increased demand
* Possible inflation increase

## Government Stimulus

Possible effects:

* Increased demand
* Higher output
* Lower unemployment

## Energy Price Shock

Possible effects:

* Higher production costs
* Higher prices
* Reduced purchasing power

## Productivity Increase

Possible effects:

* Higher output
* Economic growth

## Demand Crash

Possible effects:

* Lower spending
* Lower firm revenue
* Higher unemployment


## Simulation Process

Each time period:

1. Households receive income
2. Taxes are paid
3. Households decide how much to spend/save
4. Firms receive demand
5. Firms produce goods
6. Firms adjust prices
7. Firms hire/fire workers
8. Government collects and spends money
9. Central bank policy affects the economy
10. Economic indicators are updated

This repeats to show long-term economic behaviour.


## AI Explanation Layer

An AI system can explain simulation results by describing:

* What happened
* Why it happened
* Which variables caused the change
* Relevant economic theories
* Real-world examples
* Limitations of the model

Example:

“Inflation increased after an energy price shock because firms faced higher costs and passed these costs onto consumers. Lower purchasing power reduced consumption, causing firms to reduce hiring and increasing unemployment.”


# MVP Version

##The first version should focus on:

* Households
* Firms
* Basic spending behaviour
* Employment/unemployment
* Price changes
* Inflation calculation
* GDP calculation
* Data visualisation
* Two economic shocks:
    * Interest rate rise
    * Demand crash

Avoid making the first version too complex.


## Recommended Technology Stack

## Programming:

Python

## Data:

Pandas

## Visualisation:

Matplotlib / Plotly

## Dashboard:

Streamlit

## Development:

GitHub

## Future AI Integration:

LLM/API-based explanation system


# Project Structure

econsim/

* app.py
* simulation/
    * economy.py
    * household.py
    * firm.py
    * government.py
    * shocks.py
* analysis/
    * metrics.py
    * explanations.py
* visuals/
    * charts.py
* docs/
    * model assumptions
    * research report
    * limitations


## Research Question

“How can agent-based modelling be used to simulate the effects of economic shocks on inflation, unemployment, and inequality in a simplified economy?”

# Final Vision

### EMP becomes a realistic educational economic laboratory where users can experiment with economies, test policies, observe consequences, and understand why economic systems behave the way they do.

## The final product should demonstrate:

* Economic understanding
* Programming ability
* Mathematical modelling
* Data analysis
* Research skills

# Final Goal: 
Build a unique, interactive economic simulation platform that combines economics, computer science, mathematics, and systems modelling.
