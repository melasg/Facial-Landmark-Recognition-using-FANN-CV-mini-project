(* Mathematica Source File *)
(* Created by the Wolfram Language Plugin for IntelliJ, see http://wlplugin.halirutan.de/ *)
(* :Author: masgh003 *)
(* :Date: 2020-11-26 *)
i = img.jpg;
dataset = {i};
nf = FeatureNearest[dataset]


(*----*)
(*Separate a given set of points  into different groups. This is done by finding the centers  for each group by minimizing , where  is a given local kernel and  is a given penalty parameter*)
x = Block[{t, n = 30},
   SeedRandom[12345]; t = RandomReal[{0, 1}, {2, n}]; Apply[Join, {
Transpose[t + {1/2, 1/2}],
RandomChoice[
Transpose[t + {-1.2, -1.2}], n],
RandomChoice[
Transpose[t + {-1.2, 1}], n],
RandomChoice[
Transpose[t + {0.5, -1.2}], n]}]];
{n, dim} = Dimensions[x];
centers = Array[c, n];
(*The kernel  is a -nearest neighbor () function such that , else . For this problem,  nearest neighbors are selected*)
kNN = Nearest[x -> Automatic][x, 10];
\[Kappa] =
  SparseArray[
   Join @@ Table[Thread[{i, kNN[[i]]}], {i, n}] -> 1, {n, n}];