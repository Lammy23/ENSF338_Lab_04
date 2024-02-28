`elapsed_time = timeit.timeit(lambda: fibonacci(1000), number=100)`

`times = timeit.repeat(lambda: fibonacci(1000), repeat =5, number=10)`


## Dealing with Noise: `timeit.timeit` vs `timeit.repeat`

When running code, a lot of factors can influence the execution speed such as background processes, caching and so on. Both `timeit.timeit` and `timeit.repeat` have different strategies for dealing with noise.

`timeit.timeit` runs a piece of code a specific number of times and returns the total time. The 'number' parameter helps in specifying the granularity of measurement and can provide more stable results in short duration operations.

`timeit.repeat` runs a piece of code a specific number of times, returns the total time and then repeats this process by the value in the 'repeat' argument. This function is useful because by restarting/repeating the measurements, it can further reduce the chance of noise being a factor in measurements. 

## When the use each

Use `timeit.timeit` when:
* You want to measure the average time taken per execution of a piece of code.
* The code being measured has a consistent execution time and doesn't vary significantly between runs.


Use `timeit.repeat` when:
* You want to mitigate the impact of external factors and obtain a more reliable measurement of the code's performance.
* The code's execution time is variable, and you want to account for this variability by taking the best result among multiple repetitions.

## Aggregate statistics

For `timeit.timeit`:

* The appropriate statistic to apply is the average. This is because timeit.timeit already performs multiple measurements (number times) and returns the total time taken. To get the average time per execution, you would divide this total time by the number of executions.


For `timeit.repeat`:

* The appropriate statistics to apply are min and max, along with possibly average. This is because timeit.repeat runs the code multiple times (repeat times) and returns a list of the times taken for each repetition. Taking the minimum and maximum provides insight into the best and worst-case scenarios, while the average can give an overall understanding of typical performance.