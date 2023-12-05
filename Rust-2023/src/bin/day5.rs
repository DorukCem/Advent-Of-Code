use std::cmp::min;
use std::fs::read_to_string;
use std::time::Instant;

fn get_location(map : &[Vec<i128>], location : i128) -> i128 {
   for line in map {
      match line[..] {
         [dest, source, range] => {
            if source <= location && location < source+range {
               return dest + (location - source);
            }
         },
         _ => panic!(),
      }   
   }

   return location;
}


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

   
   let mut locations : Vec<i128> = Vec::new();
   for seed in &seeds {
      let mut current = *seed;
      for map in &maps {
         current = get_location(&map, current)
      }
      locations.push(current);
   }
   
   let part1 = locations.iter().min().unwrap();


   println!("part1: {part1}");
   
   let start = Instant::now(); // Measure Time

   let mut location : i128 = i128::MAX;
   for chunk in seeds.chunks(2) {
      let first = *chunk.get(0).unwrap();
      let second = *chunk.get(1).unwrap();
      for seed in first..first+ second {
         let mut current = seed;
         for map in &maps {
            current = get_location(&map, current)
         }
         location = min(location, current);
      }
   }
   
   let part2 = location;
   println!("part2: {part2}");

   let duration = start.elapsed();
   println!("Time elapsed in brute force is: {:?}", duration);

}