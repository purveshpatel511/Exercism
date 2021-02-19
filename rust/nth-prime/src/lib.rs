pub fn nth(n: u16) -> u32 {
    let mut vec: Vec<u32> = Vec::new();
    vec.push(2);
    vec.push(3);
    vec.push(5);
    let mut counter: u16 = 3u16;

    let mut num: u32 = 6u32;
    while counter < n+1 {
        let mut flag:bool = false; 
        for i in vec.iter() {
            if num%i == 0 {
                flag = true;
                break
            }
        } 
        if flag != true {
            vec.push(num);
            counter += 1;
        }
        num += 1;
    }
    vec[usize::from(n)]
}
