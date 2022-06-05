#[macro_use]
extern crate timeit;

//use std::convert::identity;
//use std::boxed::Box;
use std::rc::Rc;

// static mut uparg: fn(i32) -> i32 = identity;

static mut uparg: Option<Box<dyn FnMut(i32)->i32>> = Option::None;

fn fast(v: i32) -> i32 {
	let mut z = v + 1;
	let f = move |x: i32| {
		z + x
	};
    unsafe {
	    uparg = Some(Box::new(f)); // just to take time
    }
	f(v)
}

fn slower(v: i32) -> i32 {
	let mut z = v + 1;
	let f = move |x: i32| {
		z + x
	};
    unsafe {
	    uparg = Some(Box::new(f)); // requires copy of z; hopefully just a copy as z is never modified
    }
	f(v)
}

fn slowest(v: i32) -> i32 {
	let mut z = v + 1;
	let mut f = move |x: i32| {
		z += x;
        z
	};
    unsafe {
	    uparg = Some(Box::new(f)); // requires copy of z; hopefully just a copy as z is never modified
    }
	f(v)
}


fn main() {
    print!("Fast: ");
	timeit!({
		fast(100);
	});

    print!("Slower: ");
	timeit!({
		slower(100);
	});

	print!("Slowest: ");
	timeit!({
		slowest(100);
	});
}
