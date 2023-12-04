use std::collections::HashMap;

fn read_lines(filename: &str) -> Vec<String> {
   use std::fs::read_to_string;

   let mut result = Vec::new();

   for line in read_to_string(filename).unwrap().lines() {
      result.push(line.to_string())
   }
   result
}

fn part1(lines: &Vec<String> ) {
   let mut sum = 0;
   for line in lines {
      let nums = line.split(":").nth(1).unwrap();
      let punch_card: Vec<Vec<_>> = nums
         .split("|")
         .map(|c| c.split_whitespace().collect())
         .collect();

      let winning_nums = punch_card.first().unwrap();
      let my_nums = punch_card.last().unwrap();
      
      let count = winning_nums.iter().filter(|c| my_nums.contains(c)).count();
      let point = if count > 0 {1 << count-1} else {0} ;

      sum += point;
   }

   println!("part1: {sum}");
}

fn part2(lines: Vec<String> ) {
   let mut num_cards : HashMap<usize, i32> = HashMap::new();
   let mut sum = 0;
   for (i, line) in lines.iter().enumerate() {
      let nums = line.split(":").nth(1).unwrap();
      let punch_card: Vec<Vec<_>> = nums
         .split("|")
         .map(|c| c.split_whitespace().collect())
         .collect();
      
      let winning_nums = punch_card.first().unwrap();
      let my_nums = punch_card.last().unwrap();
      let count = winning_nums.iter().filter(|c| my_nums.contains(c)).count();
      
      let iter =  num_cards.get(&i).unwrap_or(&0);
      for _ in 0..iter+1 {
         sum += 1;
         for x in i+1..i+count+1 {
            *num_cards.entry(x).or_insert(0) += 1;
         }
      }
   }
   println!("part2: {:#?}", sum);
}

fn main(){
   let lines: Vec<String> = read_lines("D:/Advent-Of-Code/Rust-2023/inputs/in_04.txt");
   part1(&lines);
   part2(lines);
}
