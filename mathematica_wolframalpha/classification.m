(* Mathematica Source File *)
(* Created by the Wolfram Language Plugin for IntelliJ, see http://wlplugin.halirutan.de/ *)
(* :Author: masgh003 *)
(* :Date: 2020-11-26 *)


(*Train a classifier on the Fisher iris dataset to predict the species of Iris:*)
c = Classify[
  ExampleData[{"MachineLearning", "FisherIris"}, "TrainingData"]]
(*Predict the species of Iris from a list of features:*)
c[{4.3, 3.1, 1.2, 0.3}]
(*Test the accuracy of the classifier on a test set:*)
cm = ClassifierMeasurements[c,
  ExampleData[{"MachineLearning", "FisherIris"}, "TestData"]]
cm["Accuracy"]
cm["ConfusionMatrixPlot"]

c = Classify[{1 -> "A", 2 -> "A", 3.5 -> "B", 4 -> "B"},
  AnomalyDetector -> Automatic]
c[6, AcceptanceThreshold -> 0.01]
c[6, AcceptanceThreshold -> 0.0001]
