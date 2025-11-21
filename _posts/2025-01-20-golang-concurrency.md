---
title: "Mastering Goroutines: Concurrency in Go"
layout: post
date: 2025-01-20 08:00:00
tags: [Go, Golang, Concurrency, Backend]
---

I'm a backend engineer obsessed with performance. Go is my weapon of choice. I use this blog to share patterns and snippets.

## The Worker Pool Pattern

One of the most common patterns in Go is the worker pool. It allows you to limit the number of concurrent tasks.

```go
package main

import (
    "fmt"
    "time"
)

func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        fmt.Println("worker", id, "started  job", j)
        time.Sleep(time.Second)
        fmt.Println("worker", id, "finished job", j)
        results <- j * 2
    }
}

func main() {
    const numJobs = 5
    jobs := make(chan int, numJobs)
    results := make(chan int, numJobs)

    // Start 3 workers
    for w := 1; w <= 3; w++ {
        go worker(w, jobs, results)
    }

    for j := 1; j <= numJobs; j++ {
        jobs <- j
    }
    close(jobs)

    for a := 1; a <= numJobs; a++ {
        <-results
    }
}
```

## Why Syntax Highlighting Matters

Go code is dense. The **Atom One Light** theme used here makes keywords like `go`, `chan`, and `func` pop out, making the logic easier to follow.

![Gopher](https://loremflickr.com/800/400/code,screen)

## Conclusion

Concurrency is hard, but Go makes it easier. And this theme makes reading about it easier.
