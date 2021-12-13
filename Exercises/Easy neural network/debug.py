def get_sum_metrics(predictions, metrics= None):
    if metrics is None:
        metrics = []
        j= 0
    else:
        j =-len(metrics)
    for i in range(3):
        metrics.append(lambda x: x + j)

    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(predictions)
        j += 1
    return sum_metrics


def main():
    #breakpoint()
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9
    print(get_sum_metrics(3, [lambda x: x]))  # Should be (3) + (3 + 0) + (3 + 1) + (3 + 2) = 15
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9
    print(get_sum_metrics(3, [lambda x: x, lambda x: x**2]))  # Should be (3) + (3 + 0) + (3 + 1) + (3 + 2) = 15

if __name__ == "__main__":
    main()