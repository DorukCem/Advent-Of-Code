use std::fs::read_to_string;


fn main() {
   let input = read_to_string("D:/Advent-Of-Code/Rust-2023/inputs/ex_05.txt").unwrap();
   
   let binding = input
      .replace("seeds: ", "");
   
   let filtered : Vec<&str> = binding
      .split("\r\n")
      .filter(|c| !(c.contains("map"))) 
      .collect();
      
   let seeds: Vec<i32> = filtered.first().unwrap().split_whitespace().map(|c| c.parse().unwrap()).collect();

   let mut maps : Vec<Vec<Vec<i32>>> = Vec::new();
   let mut current : Vec<Vec<i32>> = Vec::new();
   for line in &filtered[2..] {
      if line != &"" {
         let triplet: Vec<i32> = line.split_whitespace().map(|c|c.parse().unwrap()).collect();
         current.push(triplet)
      } else {
         maps.push(current.clone());
         current.clear();
      }
   }
   maps.push(current.clone());

   println!("{:#?}", maps);
}