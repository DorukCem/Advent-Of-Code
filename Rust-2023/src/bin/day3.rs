use std::collections::{HashSet, HashMap};

fn read_lines(filename: &str) -> Vec<String> {
   use std::fs::read_to_string;

   let mut result = Vec::new();

   for line in read_to_string(filename).unwrap().lines() {
      let mut line = line.to_string();
      line.push('.');
      result.push(line); // ! carefull
   }
   result
}

fn check_surroundings(symb : &HashSet<(i32, i32)>, gears : &mut HashMap<(i32, i32), Vec<i32>>, num :i32, left: i32, right: i32, h : i32) -> bool 
{  
   let mut flag = false;
   for indx in left-1..right+2 {
      for j in h-1..h+2 {
         if let Some(gear) = gears.get_mut(&(j, indx)) {
            gear.push(num);
         }
         
         if symb.contains( &(j, indx) ) {
            flag =  true;
         }
      }
   }

   return flag;
}

fn main() {
   let lines : Vec<String> = read_lines("D:/Advent-Of-Code/Rust-2023/inputs/in_03.txt");
   let mut symbols: HashSet<(i32, i32)> = HashSet::new();
   let mut gears: HashMap<(i32, i32), Vec<i32>> = HashMap::new();
   
   let mut i = 0;
   // First iteration find symbols
   for line in lines.clone() {
      let char_vec: Vec<char> = line.chars().collect();
      let mut j = -1;
      for c in char_vec {
         j+=1;
         if c.is_digit(10) || c == '.' {
            continue;
         }
         symbols.insert((i,j)); 
         if c == '*' {
            gears
            .entry((i, j))
            .or_insert_with(Vec::new);
      }
   }
   i+=1;
}


i = 0;
let mut sum = 0;
use regex::Regex;
for line in lines {
   let pattern = Regex::new(r"\d+").unwrap();
   for num in pattern.find_iter(&line.clone())
   {  
      let number: i32 = num.as_str().parse().unwrap();
      let start_index = i32::try_from(num.start()).unwrap();
      let end_index = i32::try_from(num.end()).unwrap();
      
      if check_surroundings(&symbols, &mut gears, number, start_index, end_index-1, i) {
         sum += number;
      }
      }
      
      i+=1;
   }
   
   println!("part1: {sum}");

   let mut gear_sum: i32 = 0;
   for nums in gears.values() {
      if nums.len() == 2 {
         gear_sum += nums.iter().product::<i32>();
      }
   }

   println!("part2: {gear_sum}");
   

}