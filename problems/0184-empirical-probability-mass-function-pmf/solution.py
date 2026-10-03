def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    tot = len(samples)
    return [(i, samples.count(i)/tot) for i in set(samples)]