# Write a function power(base, exponent=2) that:
# Returns base ** exponent.
# Works even if only base is provided.


def power(base, power=2):
    return base**power


both_args = power(2, 3)
only_base = power(2)

print(both_args, "\n", only_base)
