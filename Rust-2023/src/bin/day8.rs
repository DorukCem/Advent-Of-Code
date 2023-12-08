use std::collections::HashMap;

use itertools::Itertools;

fn read_lines(filename: &str) -> Vec<String> {
   use std::fs::read_to_string;

   let mut result = Vec::new();

   for line in read_to_string(filename).unwrap().lines() {
      result.push(line.to_string())
   }
   result
}

fn main() {
   let lines = read_lines("D:/Advent-Of-Code/Rust-2023/inputs/in_08.txt");
   let filtered = lines.iter().map(|c| c.chars().filter(|x| x.is_alphabetic() || x == &' ').collect::<String>()).collect::<Vec<_>>();
   let instructions = &filtered[0];
   let tuples = &filtered[2..]
      .iter()
      .map(|c| c.split_whitespace().collect_tuple::<(_, _, _)>().unwrap())
      .collect::<Vec<_>>();

   let mut nodes: HashMap<&str, (&str, &str)> = HashMap::new();

   for tuple in tuples.iter() {
      let key = tuple.0;
      let values = (tuple.1, tuple.2);

      nodes
         .entry(key) 
         .or_insert_with(|| values);
   }
   // part1
   
   let mut ins_indx = 0;
   let mut steps = 0;
   let mut current = "AAA";

   loop {
      if current == "ZZZ" {
         break;
      }
      steps += 1;

      let instruction = instructions.chars().nth(ins_indx).unwrap();
      ins_indx += 1;
      ins_indx %= instructions.len();

      let paths = nodes.get(current).unwrap();
      let next_node = if instruction == 'L' {paths.0} else {paths.1};
      current = next_node
   }
   println!("{}", steps);

}