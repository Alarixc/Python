class Experiment:
    a=45


b=Experiment()
b.a=0
Experiment.a=1
print(b.a)
print(Experiment.a)



