use core::cmp::max;

fn read_lines(filename: &str) -> Vec<String> {
   use std::fs::read_to_string;

   let mut result = Vec::new();

   for line in read_to_string(filename).unwrap().lines() {
      result.push(line.to_string())
   }
   result
}

fn main() {
   let (red, green, blue) = (12, 13, 14);
   let mut sum = 0;
   let mut power_sum = 0;
   let mut indx = 0;

   let lines = read_lines("D:/Advent-Of-Code/Rust-2023/inputs/in_02.txt");
   for line in lines {
      indx += 1;
      let mut possible = true;
      let (mut max_r,mut max_g,mut max_b) = (0, 0, 0);

      let groups: Vec<&str> =  line.split(": ").collect();
      let second = groups[1];
      let sets: Vec<&str> = second.split(";").collect();
      for set in sets {
         let (mut r,mut g,mut b) = (0, 0, 0);

         let colors: Vec<&str> = set.split(", ").collect();
         for color in colors {
            let num_and_color: Vec<&str> = color.split_whitespace().collect();
            let num: i32 = num_and_color.first().unwrap().parse().unwrap();
            let color_text = num_and_color.get(1).unwrap().to_string();
            
            match color_text.as_str() {
               "red" => r += num,
               "green" => g += num,
               "blue" => b += num,
               _ => panic!()
            }
         }
         if !(r <= red && b <= blue && g <= green) {
            possible = false;
         }
         (max_r, max_g, max_b) = (max(r, max_r), max(g, max_g), max(b, max_b));
      }
      if possible {
         sum += indx;
      }
      power_sum += max_r * max_g * max_b
      
   }
   println!("part1: {sum}");
   println!("part2: {power_sum}");
}