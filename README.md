# logic_synthesis
Consider a randomly generated boolean equation 

`((((G)&(!D))&((!A)&(((E)|(!C))|(E))))&(((((G)|(G))&((!D)&(!D)))&(H))&((!A)&((!A)&(((!D)|(E))&(!D))))))`

**Tree represenation of above equation**

![image](https://user-images.githubusercontent.com/54628243/180242100-61907327-049e-4b67-a23a-150720d449ad.png)

You can check the decomposition of the above with `k = 3` where k means decomposition with 3 unique variable.

Let us look at an example in diagram below for the meaning of k

![image](https://user-images.githubusercontent.com/54628243/180237140-54f5a26d-14ee-461c-b1e0-7df4bef21b68.png)


The yellow cut defines a decomposition with `k = 3` i.e the cut has 3 unique variables. For more details please have [here](https://docs.google.com/presentation/d/1NMPl3cNHcZt6KMU3oYGuRScfKRWLWBj7-lLKyWiVIc8/edit#slide=id.ge57ba949b7_0_6).

Overall if we do a normal decomposition of above boolean equation it would take around 4 decomposition. You can have look at these slides [here](https://docs.google.com/presentation/d/1NMPl3cNHcZt6KMU3oYGuRScfKRWLWBj7-lLKyWiVIc8/edit#slide=id.ge57ba949b7_0_6).

In our project we have developed a algorithm which can minimize this decomposition via properties of trees.

We manipulate the boolean equation which changes its tree respresentation without changing its meaning. Have a look at the change made by the our algorithm below.

![image](https://user-images.githubusercontent.com/54628243/180241581-4823bd7a-07d6-4dd4-a084-41fb78210243.png)

This representation allows us to reduce the no of decomposition into 2. Have a complete look [here](https://docs.google.com/presentation/d/1NMPl3cNHcZt6KMU3oYGuRScfKRWLWBj7-lLKyWiVIc8/edit#slide=id.ge57ba949b7_0_6).
