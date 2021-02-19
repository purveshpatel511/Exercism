pub fn square(s: u32) -> u64 {
    if s <= 0 || s >= 65 {
        panic!("Square must be between 1 and 64");
    }
    else {
        if s == 1u32 {
            1
        }
        else {
            let (grain, _total_grain) = count_grain(s);
            grain
        }
    }
}


fn count_grain(s: u32) -> (u64,u64) {
    let mut grain: u64 = 1u64;
    let mut total_grain: u64 = 1u64;
    for _i in 2u32..s+1 {
        grain *= 2;
        total_grain += grain;
    }
    (grain,total_grain)   
}

pub fn total() -> u64 {
    let (_grain, total_grain) = count_grain(64);
    total_grain
}
