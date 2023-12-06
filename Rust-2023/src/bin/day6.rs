use std::iter::zip;

fn read_lines(filename: &str) -> Vec<String> {
   use std::fs::read_to_string;

   let mut result = Vec::new();

   for line in read_to_string(filename).unwrap().lines() {
      result.push(line.to_string())
   }
   result
}

fn racist(time: &i64, record_dist: &i64) -> i64{
   // * This is the quadratic formula
   let tf: f64 = *time as f64;
   let rf: f64 = *record_dist as f64;
   let th1 = ((tf + ((tf * tf - 4f64 * rf) as f64).sqrt() )/ 2f64).ceil() as i64;
   let th2 = ((tf - ((tf * tf - 4f64 * rf) as f64).sqrt() )/ 2f64).floor() as i64;
   
   let mut lower = 0;
   let mut upper = 0;
   
   for time_held in th2..th1 {
      let fin_dist = time_held * (time - time_held);
      if fin_dist > *record_dist {
         lower = time_held;
         break;
      }
   }

   for time_held in (th2..th1).rev() {
      let fin_dist = time_held * (time - time_held);
      if fin_dist > *record_dist {
         upper = time_held;
         break;
      }
   }

   let diff = upper-lower+1;
   return diff;
}


fn main() {
   let lines = read_lines("D:/Advent-Of-Code/Rust-2023/inputs/in_06.txt");
   let parsed  = lines.iter()
      .map(|c| c.split(":").nth(1).unwrap().split_whitespace().map(
         |num| num.parse().unwrap()).collect::<Vec<i64>>())
      .collect::<Vec<Vec<i64>>>();
   
   let mut product = 1;
   for (time, record_dist) in zip(&parsed[0], &parsed[1]) {
      product *= racist(time, record_dist);
   }
   println!("part1: {product}");
   
   // part2
   let single_race = lines.iter()
      .map(|c| c.split(":").nth(1).unwrap().chars().filter(|c| !c.is_whitespace()).collect::<String>().parse().unwrap())
      .collect::<Vec<i64>>();
        
   let part2 = racist(&single_race[0], &single_race[1]);
   println!("{part2:#?}");

}