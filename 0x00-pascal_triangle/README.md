# Pascal's Triangle

A Python algorithm to generate Pascal's Triangle of given depth.

### Testing

```python
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

Output:

```bash
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```
