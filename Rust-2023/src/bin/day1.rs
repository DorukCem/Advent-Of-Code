use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
   let mut result = Vec::new();

   for line in read_to_string(filename).unwrap().lines() {
      result.push(line.to_string())
   }
   result
}

fn part1() {
   let mut sum = 0;
   let lines: Vec<String> = read_lines("D:/Advent-Of-Code/Rust-2023/inputs/in_01.txt");
   for line in lines {
      let mut digits : Vec<u32> = Vec::new();
      for c in line.chars() {
         if c.is_digit(10) {
            digits.push( c.to_digit(10).unwrap() )
         }
      }
      sum += digits[0] * 10 + digits[ digits.len()-1 ];
   }

   println!("{sum}");
} 

fn part2() {
   let lines: Vec<String> = read_lines("D:/Advent-Of-Code/Rust-2023/inputs/in_01.txt");
   let mut sum = 0;
   for line in lines {
      let replaced = line
         .replace("zero", "zero0zero")
         .replace("one", "one1one")
         .replace("two", "two2two")
         .replace("three", "three3three")
         .replace("four", "four4four")
         .replace("five", "five5five")
         .replace("six", "six6six")
         .replace("seven", "seven7seven")
         .replace("eight", "eight8eight")
         .replace("nine", "nine9nine");
      
      let digits  = replaced.chars().filter_map(|c| c.to_digit(10)).collect::<Vec<u32>>();
      
      sum += digits.first().unwrap() * 10 + digits.last().unwrap();

   }

   println!("{sum}")
}

fn main() {
   part1();
   part2();
}

