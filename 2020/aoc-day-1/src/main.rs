use std::fs;
use rand::Rng;

fn load_input(filename : &str) -> Vec<i32> {
    let mut output: Vec<i32> = Vec::new();

    println!("Trying to load file {}.", filename);
    let input = fs::read_to_string(filename)
        .expect("File not found.");

    let lines: Vec<&str> = input
        .lines()
        .collect();

    for line in lines {
        let value: i32 = match line.parse() {
            Ok(num) => num,
            Err(_) => panic!("Did not find valid data.")
        };
        output.push(value);
    }
    output
}

fn solve_part1(input: Vec<i32>){
    let length = input.len(); //Get the length of our input data.
    const sum_value : i32 = 2020;
    let solution : Vec<i32> = Vec::new(); //Here's where we want to store the two numbers that add up to 2020.
    let mut counter : usize = 0;

    'search: while solution.len() < 2{
        for n in 0..length{
            if n != counter && input[counter] + input[n] == sum_value { //Avoid adding the number with itself.
                println!("Found numbers that add to {}. {} and {}", sum_value, input[counter], input[n]);
                println!("Solution: {}", input[counter]*input[n]);
                break 'search;
            }
        }
        counter += 1;
        if counter == input.len(){
            println!("Unable to find the numbers that add up to 2020");
            break; //Just to prevent getting stuck in an infinite loop during debugging.
        }
    }
}

fn solve_part2(input: Vec<i32>) -> i32{
    let length = input.len(); //Get the length of our input data.
    const sum_value : i32 = 2020;
    let mut solution : i32 = 0;
    let mut i : usize = 0;

    while solution == 0{
        let mut rng = rand::thread_rng();
        let n1 : usize = rng.gen_range(0..length);
        let mut n2 : usize = rng.gen_range(0..length);
        while n2 == n1{
            n2 = rng.gen_range(0..length);
        }
        let mut n3 : usize = rng.gen_range(0..length);
        while n3 == n1 || n3 == n2 {
            n3 = rng.gen_range(0..length);
        }
        if input[n1]+input[n2]+input[n3] == sum_value {
            solution = (input[n1]*input[n2]*input[n3]);
        }
    }
    return solution;
}

fn main() {
    let input_data = load_input("./input.txt");
    let answer : i32 = solve_part2(input_data);
    println!("Solution is {}", answer);
}
