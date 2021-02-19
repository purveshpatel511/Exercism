pub fn raindrops(n: u32) -> String {
    let mut output_string = String::new();
    if n % 3 == 0 {
        output_string.push_str("Pling");
    }
    if n % 5 == 0 {
        output_string.push_str("Plang");
    }
    if n % 7 == 0 {
        output_string.push_str("Plong");
    }

    if output_string.len() != 0 {
        return output_string;
    }
    else{
        return n.to_string();
    }
}
