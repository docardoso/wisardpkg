from wisardpkg import ClusWisard

print("\n\n")
print("### ClusWiSARD UNSUPERVISED ###")
print("### Input ###")

X = [
    [1,1,1,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,1],
    [0,0,0,0,0,1,1,1,1]
]

for i,d in enumerate(X):
    print("unknown",d)

print("\n")

addressSize = 3 # tamanho do endereçamento das rams
minScore = 0.1 # score mínimo do processo de treino
threshold = 10 # limite de treinos por discriminador
discriminatorLimit = 5 # limit de discriminadores por cluster
clus = ClusWisard(addressSize,minScore,threshold,discriminatorLimit)


print("training...")
clus.trainUnsupervised(X)

print("classifing...")
out=clus.classifyUnsupervised(X)

print("out:")
for i,d in enumerate(X):
    print(out[i],d)

print("### DONE ClusWiSARD UNSUPERVISED ###")
