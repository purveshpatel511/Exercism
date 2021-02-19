extern crate unicode_segmentation;
use unicode_segmentation::UnicodeSegmentation;

pub fn reverse(input: &str) -> String {
    let string = input.to_string();
    let reverse_string = string.graphemes(true).rev().collect();
    reverse_string
}
