use std::{fs::read_to_string, collections::HashMap};


fn main() {
   let input = read_to_string("D:/Advent-Of-Code/Rust-2023/inputs/in_05.txt").unwrap();
   
   let binding = input
      .replace("seeds: ", "");
   
   let filtered : Vec<&str> = binding
      .split("\r\n")
      .filter(|c| !(c.contains("map"))) 
      .collect();
      
   let seeds: Vec<i128> = filtered.first().unwrap().split_whitespace().map(|c| c.parse::<i128>().unwrap()).collect();

   let mut maps : Vec<Vec<Vec<i128>>> = Vec::new();
   let mut current : Vec<Vec<i128>> = Vec::new();
   for line in &filtered[2..] {
      if line != &"" {
         let triplet: Vec<i128> = line.split_whitespace().map(|c|c.parse().unwrap()).collect();
         current.push(triplet)
      } else {
         maps.push(current.clone());
         current.clear();
      }
   }
   maps.push(current.clone());

   
   let mut tables : Vec<HashMap<i128, i128>> = Vec::new();
   for map in maps {
      let mut current_table : HashMap<i128, i128> = HashMap::new();
      for line in map {
         match line[..] {
            [source, dest, range] => {
               for i in 0..range {
                  current_table.insert(dest+i, source+i); 
               }
            },
            _ => panic!(),
         }   
      }
      tables.push(current_table);
   }

   let mut locations : Vec<i128> = Vec::new();
   for seed in seeds {
      let mut current: &i128 = &seed;
      for table in &tables {
         let next_value = table.get(current).or_else(|| Some(current)).unwrap();
         current = next_value;
      }
      locations.push(*current);
   }
   
   let part1 = locations.iter().min().unwrap();
   
   println!("part1: {part1}");
   

   // TODO: Make a function that find if num is in given range
}