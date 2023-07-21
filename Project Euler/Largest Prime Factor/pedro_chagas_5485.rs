fn solve(n: u64) -> u64{
    let mut i: u64 = 2;
    let mut n_mutable: u64 = n;
    while i * i <= n_mutable {
	if n_mutable % i != 0 {
	    i += 1;
	}else{
	    n_mutable = n_mutable/i;
	}
    }
    return n_mutable;

}

fn main(){
    let solution: u64 = solve(600851475143);
    println!("{}", solution);
}
