fn read_lines(filename: &str) -> Vec<String> {
   use std::fs::read_to_string;

   let mut result = Vec::new();

   for line in read_to_string(filename).unwrap().lines() {
      result.push(line.to_string())
   }
   result
}
fn main() {
   let lines = read_lines("D:/Advent-Of-Code/Rust-2023/inputs/in_09.txt");
   let histories: Vec<Vec<i128>> = lines.iter().map(|c| c.split_whitespace().map(|x| x.parse().unwrap()).collect()).collect();
   
   let mut sum: i128 = 0;
   let mut part2_sum: i128 = 0;
   for hist in histories {
      let mut seq = hist;
      let mut last_nums: Vec<i128> = Vec::new() ;
      let mut first_nums: Vec<i128> = Vec::new() ;
      loop {
         let next_seq: Vec<i128> = seq
         .windows(2)
         .map(|window| window[1] - window[0])
         .collect();

         last_nums.push(*seq.last().unwrap());
         first_nums.push(*seq.first().unwrap());

         if next_seq.iter().all(|&x| x==0) {
            break;
         } 
         seq = next_seq;
      }
      sum += last_nums.iter().sum::<i128>();
      
      first_nums.reverse();
      let mut prev = first_nums[0];
      for num in first_nums[1..].iter() {
         prev = num - prev;
      }

      part2_sum += prev;

   }
   println!("{:#?}", sum);
   println!("{:#?}", part2_sum);
}