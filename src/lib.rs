pub mod ustr_extern;
pub use ustr_extern::*;


#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        use ustr::ustr;
        let u_apple = ustr("apple");
        let u_bravo = ustr("bravo");
        let u_charlie = ustr("charlie");
        let u_delta = ustr("delta");

        let mut v = vec![u_delta, u_bravo, u_charlie, u_apple];
        v.sort();
        assert_eq!(v, vec![u_apple, u_bravo, u_charlie, u_delta]);
    }
}
