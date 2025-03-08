# Rust fixme 1

## Description


## Solution

Install rust
```sh
$ sudo apt install cargo
$ sudo apt install rustup
```

Install cargo
```sh
 $ rustup default stable
```

Fix the code
```rust
use xor_cryptor::XORCryptor;

fn main() {
    // Key for decryption
    let key = String::from("CSUCKS"); // End statements with a semicolon in Rust

    // Encrypted flag values
    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "7f", "5a", "60", "50", "11", "38", "1f", "3a", "60", "e9", "62", "20", "0c", "e6", "50", >

    // Convert the hexadecimal strings to bytes and collect them into a vector
    let encrypted_buffer: Vec<u8> = hex_values.iter()
        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
        .collect();

    // Create decryption object
    let res = XORCryptor::new(&key);
    if res.is_err() {
        return; // Use `return` to exit the function early in Rust
    }
    let xrc = res.unwrap();

    // Decrypt flag and print it out
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
    println!(
        "{}", // Use `{}` to print out a variable in the println function
        String::from_utf8_lossy(&decrypted_buffer)
    );
}
```
Run the code
```sh
$ cargo run
```

## Flag
    picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}