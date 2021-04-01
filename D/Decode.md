# Decode

## What is decoding?
A bytes object is converted to a string object.

## Code example
[decode_ex.py](https://github.com/pratikshapaudyal/A-Z_of_Python/blob/develop/D/decode_ex.py)

Running the example in an interactive python terminal:

``` bash
>>> bytes_object = b'\xf0\x9f\x98\x80\xf0\x9f\x98\x80\xf0\x9f\x98\x80'
>>> bytes_object.decode("utf-8")
u'\U0001f600\U0001f600\U0001f600'
>>> print(bytes_object)
😀😀😀
```

## Further References
[This is a must read.](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)