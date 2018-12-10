use std::io;

fn main(){
    let mut numbers = String::new();
    io::stdin().read_line(&mut numbers).expect("Failed to read inputs");
    let mut iter = numbers.split_whitespace();
    let a = iter.next().unwrap();
    let b = iter.next().unwrap();
    println!("{}", a.parse::<i32>().unwrap() - b.parse::<i32>().unwrap());
}