PageRank
========

Implementation of the Page Rank algorithm to compute Page Rank on a collection of 183,811 web documents.


PageRank works by counting the number and quality of links to a page to determine a rough estimate of how 
important the website is. 
The underlying assumption is that more important websites are likely to receive more links from other websites.

The in-links file for the WT2g collection (wt2g_inlinks.txt) is a 2GB crawl of a subset of the web with inlinks
to webpages in the format : A C F G - where A is the webpage and C,F,G are the pages with links to A.

Following Algorithm was used :

// P is the set of all pages; |P| = N
// S is the set of sink nodes, i.e., pages that have no out links
// M(p) is the set of pages that link to page p
// L(q) is the number of out-links from page q
// d is the PageRank damping/teleportation factor; use d = 0.85 as is typical

foreach page p in P
  PR(p) = 1/N                          /* initial value */

while PageRank has not converged do
  sinkPR = 0
  foreach page p in S                  /* calculate total sink PR */
    sinkPR += PR(p)
  foreach page p in P
    newPR(p) = (1-d)/N                 /* teleportation */
    newPR(p) += d*sinkPR/N             /* spread remaining sink PR evenly */
    foreach page q in M(p)             /* pages pointing to p */
      newPR(p) += d*PR(q)/L(q)         /* add share of PageRank from in-links */
  foreach page p
    PR(p) = newPR(p)

return PR

This iterative version of PageRank algorithm until PageRank values "converge". 
To test for convergence, the perplexity of the PageRank distribution is calculated at each iteration, 
where perplexity is simply 2 raised to the entropy of the PageRank distribution, i.e., 2H(PR). 
Perplexity is a measure of how "skewed" a distribution is --- the more "skewed" (i.e., less uniform) a distribution is, 
the lower its preplexity. Informally, you can think of perplexity as measuring the number of elements that have a
"reasonably large" probability weight; technically, the perplexity of a distribution with entropy h is the number of 
elements n such that a uniform distribution over n elements would also have entropy h. 
(Hence, both distributions would be equally "unpredictable".)

The program will run until 4 concecutive values for preplexity are constant, it will then stop and display the top 10
webpages.



