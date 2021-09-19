# Software Design Patterns

[Link to the materials](https://hse-scicomp.gitlab.io/schedule/06-software-design.html)

[Reading Assignment]()

### Exercise: 
What if you wanted just the sum column, and didn't need the original table? Write an awk command that takes a two column table and outputs just the sum column.
```bash
    paste <(seq 1 10) <(seq 11 20) | awk '{$3 = $1 + $2; print $3}'
```
### Exercise:
Write a python program stats-sum which reads a newline-separated list of floating-point numbers from standard input. When it reaches the end of standard input, it prints the sum, and exits.

The [stats-sum](stats-sum) file


### Exercise:
Write similar "aggregator" programs computing stats-mean, stats-median, stats-variance, stats-stddev (standard deviation), stats-mad (median absolute deviation). Feel free to use the standard library, but do not use any third-party python packages.

* [stats-mean](stats-mean)
* [stats-median](stats-median) 
* [stats-variance](stats-variance) 
* [stats-stddev](stats-stddev)
* [stats-mad](stats-mad)