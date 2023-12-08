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

fn get_step(nodes: &HashMap<&str, (&str, &str)>, instructions : &String, start: &str) -> i128 {
   let mut ins_indx = 0;
   let mut steps = 0;
   let mut current = start;

   loop {
      if current.chars().nth(2).unwrap() == 'Z'{
         break;
      }
      steps += 1;

      let instruction = instructions.chars().nth(ins_indx).unwrap();
      ins_indx += 1;
      ins_indx %= instructions.len();

      let paths = nodes.get(current).unwrap();
      current = if instruction == 'L' {paths.0} else {paths.1};
   }
   
   return steps;
}

fn gcd(mut a: i128, mut b: i128) -> i128 {
   while b != 0 {
      let temp = b;
      b = a % b;
      a = temp;
   }
   a
}

fn lcm(a: i128, b: i128) -> i128 {
   if a == 0 || b == 0 {  0 } 
   else { a * b / gcd(a, b) }
}

fn find_lcm(numbers: Vec<i128>) -> i128 {
   if numbers.is_empty() {
      return 0;
   }

   let mut result = numbers[0];
   for &num in &numbers[1..] {
      result = lcm(result, num);
   }
   result
}

fn main() {
   let lines = read_lines("D:/Advent-Of-Code/Rust-2023/inputs/in_08.txt");
   let filtered = lines.iter().map(|c| c.chars().filter(|x| x.is_alphanumeric() || x == &' ').collect::<String>()).collect::<Vec<_>>();
   let instructions = &filtered[0];
   let tuples = &filtered[2..]
      .iter()
      .map(|c| c.split_whitespace().collect_tuple::<(_, _, _)>().unwrap())
      .collect::<Vec<_>>();

   let mut nodes: HashMap<&str, (&str, &str)> = HashMap::new();
   let mut start_nodes : Vec<&str> = Vec::new();

   for tuple in tuples.iter() {
      let key = tuple.0;
      let values = (tuple.1, tuple.2);
      if key.chars().nth(2).unwrap() == 'A' {
         start_nodes.push(key);
      }

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
   println!("part1: {}", steps);

   //part2

   let steps : Vec<i128> = start_nodes.iter().map(|c| get_step(&nodes, instructions, c)).collect();
   let result = find_lcm(steps);
   println!("part2: {:#?}", result);

}