use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
   let mut result = Vec::new();

   for line in read_to_string(filename).unwrap().lines() {
      result.push(line.to_string())
   }
   result
}

fn main() {
   let mut sum = 0;
   let lines = read_lines("inputs/in_01.txt");
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

