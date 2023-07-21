fn reverse_string(produto : &str) -> String {
    return produto.chars().rev().collect::<String>();
}

fn check_palindrom(produto : &str) -> bool {
    return produto == reverse_string(produto);
}

fn helper(p : u64, largest : u64) -> u64 {
    let pString : String = (p).to_string();
    if !check_palindrom(&pString) {
        return largest;
    }
    if p >= largest {
        return p
    }
    return largest;

}

fn solve() -> u64{
    let mut largest : u64 = 0;
    for i in 100 .. 1000 {
        for k in 100 .. 1000 {
            let p : u64 = i*k;
            largest = helper(p, largest);
        }
    }
    return largest;
}

fn main() {
    println!("{}",solve());

}
