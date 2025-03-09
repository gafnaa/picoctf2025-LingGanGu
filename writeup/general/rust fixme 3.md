# rust fixme 3

## Description
Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag!
Download the Rust code [here](https://challenge-files.picoctf.net/c_verbal_sleep/dcdaf491b35c1d0f5075e9583edbbb7aaea1dffb6ad32bc000e4d87b5200ff7b/fixme3.tar.gz).

## Solution
**by s4nkya**

Fixing the code

### Error in ```Unsafe``` Usage
The code section commented out with ```unsafe``` is not really necessary.

```decrypted_buffer``` is already defined as ```Vec<u8>```, so it can be directly converted to ```String``` using ```String::from_utf8_lossy```.

### Error in ```XORCryptor``` Object Creation
```let res = XORCryptor::new(&key);```
Should be able to directly use ```.expect()``` or handled better.

### Error in ```XORCryptor::new``` function
Converting ```key``` to ```String``` → ```let key = String::from("CSUCKS");```

Passing ```&key``` reference to ```XORCryptor::new``` → ```let xrc = XORCryptor::new(&key).expect("Failed to create XORCryptor");```

The Correct code

```rust
use xor_cryptor::XORCryptor;

fn decrypt(encrypted_buffer: Vec<u8>, borrowed_string: &mut String) {
    // Key for decryption (ubah menjadi String)
    let key = String::from("CSUCKS");

    // Editing our borrowed value
    borrowed_string.push_str("PARTY FOUL! Here is your flag: ");

    // Create decryption object (gunakan referensi &key)
    let xrc = XORCryptor::new(&key).expect("Failed to create XORCryptor");

    // Decrypt the buffer
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);

    // Convert decrypted bytes to String safely
    let decrypted_str = String::from_utf8_lossy(&decrypted_buffer);
    borrowed_string.push_str(&decrypted_str);

    println!("{}", borrowed_string);
}

fn main() {
    // Encrypted flag values
    let hex_values = [
        "41", "30", "20", "63", "4a", "45", "54", "76", "12", "90", "7e", "53", "63", "e1", "01", "35",
        "7e", "59", "60", "f6", "03", "86", "7f", "56", "41", "29", "30", "6f", "08", "c3", "61", "f9", "35"
    ];

    // Convert the hexadecimal strings to bytes and collect them into a vector
    let encrypted_buffer: Vec<u8> = hex_values.iter()
        .map(|&hex| u8::from_str_radix(hex, 16).expect("Invalid hex value"))
        .collect();

    let mut party_foul = String::from("Using memory unsafe languages is a: ");
    decrypt(encrypted_buffer, &mut party_foul);
}
```

## Flag
    picoCTF{n0w_y0uv3_f1x3d_1h3m_411}