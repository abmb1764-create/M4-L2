w=(1, 0, 0, 1, 1, 1, 0)
sunny=(w.count(0))
rainy=(w.count(1))
if sunny>rainy:
    print("The weather is going to be sunny")
else:
    print('The weather is going to be rainy')