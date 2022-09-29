# electionanalysis

## Project Overview
A Colorado Board of Elections employee has provided the following tasks to complete the election audit of a recent local congressional election.

1. Calculate total votes cast
2. Get a complete list of candidates who received votes
3. Calculate total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

Additionally the employee asked to see the following:
1. Voter turnout for each county
2. Percentage of votes from each county
3. The county with the highest turnout

## Election Audit Results
The analysis of the election show that:
-There were 369,711 votes cast in the election
-The candidates were:
  Charles Casper Stockham
  Diana DeGette
  Raymon Anthony
The candidate results were:
  Charles Casper Stockham: 23.0% (85,213)
  Diana DeGette: 73.8% (272,892)
  Raymon Anthony Doane: 3.1% (11,606)
The winner of the election was:
  Diana DeGette
  Winning Vote Count: 272,892
  Winning Percentage: 73.8%
The county with the largest voter turnout was "Denver"
The county results were:
  Jefferson: 10.5% (38,855)
  Denver: 82.8% (306,055)
  Arapahoe: 6.7% (24,801)
  
## Election Audit Summary
This script provides summary data on election results for candidates within Jefferson, Denver, and Arapahoe counties. This script also equips individuals with the necessary tools to analyze additional elections at a larger scale. For instance, this script could be applied to local, state, and national elections to analyze election results and determine winners based on the popular vote. Uploading a data source that contains additonal data at the aformenetioned levels would allow indidivudals to easily count and produce election results and reduce potential errors through an automated process. By switching "county" references to the "state" level, election results for races, including gubernatorial and state senate, can be tabulated to identify winners. 

This script could also be used to identify where specific candidates saw greater success. For instance, by measuring where candidates achieved a higher percentage of votes at the county level compared to counties where they didn't perform as well, individual candidates could use findings to identify targeted areas for future campaigns should they diecide to run again. This same analysis could also help potential winners strategically target areas where they should increase their campaign efforts for re-election bids. An ecample could be Diana DeGetter targeting Jefferson county for future campaign efforts. Similarly this analysis could also assist in identifying areas where voter turnout was low. By targeting these specific counties, campaign groups could use the data from this analysis to identify methods to encourage a greater voter turnout or even increase voter registration numbers. 

## Resources
-Data Source. election_results.csv
-Software: Python 3.9.12, Vusual Studio 1.71.2
