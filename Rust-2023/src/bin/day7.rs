use std::{collections::HashMap, cmp::Ordering};
use itertools::Itertools;

fn read_lines(filename: &str) -> Vec<String> {
   use std::fs::read_to_string;

   let mut result = Vec::new();

   for line in read_to_string(filename).unwrap().lines() {
      result.push(line.to_string())
   }
   result
}

fn get_card_val(card: char) -> i32 {
   match card {
      '2'..='9' => card.to_digit(10).unwrap() as i32,
      'T' => 10,
      'J' => 11,
      'Q' => 12,
      'K' => 13,
      'A' => 14,
      _ => panic!(), // Handle invalid characters
   } 
}

fn find_rank(hand: &String) -> i32 {
   let letter_counts: HashMap<char, i32> =
      hand
         .chars()
         .fold(HashMap::new(), |mut map, c| {
            *map.entry(c).or_insert(0) += 1;
            map
         });
   
   let values: Vec<&i32> = letter_counts.values().sorted().rev().collect();
   match values[..] {
      [5] => return 7,
      [4,1] => return 6,
      [3,2] => return 5,
      [3,1,1] => return 4,
      [2,2,1] => return 3,
      [2,..] => return 2,
      _ => return 1,
   }
}

// part2 functions

fn get_card_val_joker(card: char) -> i32 {
   match card {
      'J' => 1,
      '2'..='9' => card.to_digit(10).unwrap() as i32,
      'T' => 10,
      'Q' => 12,
      'K' => 13,
      'A' => 14,
      _ => panic!(), // Handle invalid characters
   } 
}

fn find_rank_joker(hand: &String) -> i32 {
   let mut letter_counts: HashMap<char, i32> =
      hand
         .chars()
         .fold(HashMap::new(), |mut map, c| {
            *map.entry(c).or_insert(0) += 1;
            map
   });
   
   let num_js = letter_counts.get(&'J').cloned().unwrap_or(0);
   if num_js > 0 {
      letter_counts.insert('J', 0);
   }
   
   let mut values: Vec<i32> = letter_counts.values().sorted().rev().map(|c| c.to_owned()).collect();
   values[0] += num_js;
 

   match values[..] {
      [5,..] => return 7,
      [4,1,..] => return 6,
      [3,2,..] => return 5,
      [3,..] => return 4,
      [2,2,1,..] => return 3,
      [2,..] => return 2,
      _ => return 1,
   }
}

fn compare_hands(h1: &String, h2: &String) -> Ordering {
   let (r1, r2) = (find_rank(h1), find_rank(h2));
   
   if r1 > r2 {
      return Ordering::Greater;
   }

   if r2 > r1 {
      return Ordering::Less;
   }
   
   for (c1, c2) in std::iter::zip(h1.chars(), h2.chars()) {
      if get_card_val(c1) == get_card_val(c2) { 
         continue;
      } else {
         if get_card_val(c1) > get_card_val(c2) {
            return Ordering::Greater;
         } else {
            return Ordering::Less;
         }
      }
   }

   return Ordering::Equal;
}


fn compare_hands_joker(h1: &String, h2: &String) -> Ordering {
   let (r1, r2) = (find_rank_joker(h1), find_rank_joker(h2));
   
   if r1 > r2 {
      return Ordering::Greater;
   }

   if r2 > r1 {
      return Ordering::Less;
   }
   
   for (c1, c2) in std::iter::zip(h1.chars(), h2.chars()) {
      if get_card_val_joker(c1) == get_card_val_joker(c2) { 
         continue;
      } else {
         if get_card_val_joker(c1) > get_card_val_joker(c2) {
            return Ordering::Greater;
         } else {
            return Ordering::Less;
         }
      }
   }

   return Ordering::Equal;
}

fn main() {
   let lines = read_lines("D:/Advent-Of-Code/Rust-2023/inputs/in_07.txt");
   let mut hand_bids: Vec<(String ,i32)> = lines
      .iter()
      .map(|line| {
         let mut iter = line.split_whitespace();
         (
            iter.next().unwrap().to_string(),
            iter.next().unwrap().to_string().parse().unwrap(),
         )
      })
      .collect();

   hand_bids.sort_by(|(h1, _), (h2, _)| compare_hands(h1, h2));
   let part1: usize = hand_bids.iter().enumerate().map(|(i, e)| (i + 1) * e.1 as usize).sum();
   println!("{:#?}", part1);
   hand_bids.sort_by(|(h1, _), (h2, _)| compare_hands_joker(h1, h2));
   let part2: usize = hand_bids.iter().enumerate().map(|(i, e)| (i + 1) * e.1 as usize).sum();
   println!("{:#?}", part2);
   
}