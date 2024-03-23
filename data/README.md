## Scenario

Howdy fellow developer, we have been tasked by our Product Owner to create an API (**but not a web page**) that 
exposes the following functionalities:

1. As a user, I can retrieve the list of signals
   * I get all the information about each signal
   * I get the keyword names (but not their description) for each signal
2. As a user, I can retrieve a specific signal given its `node_id`

The available signals have been given to us in a plain CSV file named `signals.csv`

## Instructions

- There are very few rules, feel free to use the technologies you fancy (altough most of the time, the team chooses to 
  use 
  Java, Kotlin or Python);
- Our application must run in a container (e.g. docker, k8s, podman, etc.);
- Data must be persisted in a database (also running in a container);
- Our Product Owner expressed very basic needs, but would be very happy if some additional features are baked in;
- Tests should be added if necessary;
- We can't modify the `signals.csv` or the `keywords.csv` input files 
  - (signals.csv md5 hash: `b4394a28720b8173372b0ce2e0352be2`)
  - (keywords.csv md5 hash: `ca8a9c8aff57261fb798e9c33367ce6c`)
- We have to demonstrate our application to the Product Owner and explain our implementation choices.

