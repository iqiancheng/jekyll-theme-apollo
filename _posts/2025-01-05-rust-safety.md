---
title: "Why I Love Rust's Borrow Checker"
layout: post
date: 2025-01-05 12:00:00
tags: [Rust, Systems Programming, Safety]
---

I'm a systems programmer. I used to write C++, but memory leaks kept me up at night. Then I found Rust.

## Ownership and Borrowing

The borrow checker is your strict but fair friend. It ensures memory safety without a garbage collector.

```rust
fn main() {
    let s1 = String::from("hello");
    
    let len = calculate_length(&s1); // We pass a reference
    
    println!("The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

If I tried to modify `s` inside `calculate_length` without making it mutable, the compiler would stop me.

## Error Handling

Rust's `Result` type forces you to handle errors. No more unhandled exceptions crashing your production server.

```rust
use std::fs::File;

fn main() {
    let f = File::open("hello.txt");

    let f = match f {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the file: {:?}", error),
    };
}
```

![Rust Crab](https://loremflickr.com/800/400/metal,gear)

## A Theme for Code

I appreciate that this theme supports `rust` syntax highlighting perfectly. The lifetimes `'a` and types `String` are clearly distinguished.
