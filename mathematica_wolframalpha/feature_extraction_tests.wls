#!/usr/bin/env wolframscript

(* Wolfram Script *)
(* Created by the Wolfram Language Plugin for IntelliJ, see http://wlplugin.halirutan.de/ *)
(* :Author: masgh003 *)
(* :Date: 2020-11-26 *)

Print["Hello World"];

(*IMAGE FEATURE TRACKING *)
(* Cell[BoxData[RowBox[{"ImageFeatureTrack", "[", RowBox[{RowBox[{"{", RowBox[{TagBox[FrameBox[SubscriptBox["image", "1"]], "Placeholder"], ",", TagBox[FrameBox[SubscriptBox["image", "2"]], "Placeholder"], ",", TagBox[FrameBox["…"], "Placeholder"], ",", TagBox[FrameBox[SubscriptBox["image", "n"]], "Placeholder"]}], "}"}], ",", TagBox[FrameBox["pts"], "Placeholder"]}], "]"}]], "Input", CellTags -> "ImageFeatureTrack_templates"] *)
images={1.jpg,2.jpg}; mask= little-white-box.jpg;
pts = ImageFeatureTrack[images,Masking->mask, MaxFeatures->15];
MapThread[HighlightImage,{images,pts}]

(*Image cropping/tripping*)
i = uncroppedImgwithFace.jpg;
ImageTrim[i,FindFaces[i]];
ImageResize[i, Scaled[3],Resampling->"Linear"];
(*First order interpolation that downsizes for better results for thin objects*)
ImageResize[i, 80, Resampling -> "Linear"];
(*Get a summary of estimated features*)
i2 = seconduncroppedimg.jpg;
FacialFeatures[i2]//Dataset;
(*estimate a feature on the faces detected in an image*)
FacialFeatures[i2,"EyePoints"];
ImageResize[MeanFilter[i2, 1], Scaled[0.5], Resampling -> "Linear"];

(*Neural net from the Wolfram Neural Net Repository to extract Facial features*)
CloudGet["https://www.wolframcloud.com/objects/731bd83b-35a9-4f29-982f-84ec047ba783"] (* Evaluate this cell to copy the example input from a cloud object *)
img = ;
net = NetModel["Vanilla CNN for Facial Landmark Regression"];
faces = FindFaces[img, "Image"];
MapThread[
 HighlightImage[#1, {PointSize[.1], #2},
   DataRange -> {1, 1}] &, {faces, net /@ faces}];
HighlightImage[img, {PointSize[0.04], landmarks},
 DataRange -> {{0, 1}, {0, 1}}];

findFacialLandmarks[img_Image] := Block[
  {crops, points},
  crops = ImageTrim[img, #] & /@ FindFaces[img];
  points = If[Length[crops] > 0, net[crops], {}];
  MapThread[<|"Crop" -> #1,
     "Landmarks" ->
      AssociationThread[{"LeftEye", "RightEye", "Nose", "LeftMouth",
        "RightMouth"}, #2]|> &, {crops, points}]
  ]
output = findFacialLandmarks[img]
colorCodes = <|"LeftEye" -> Hue[0.2], "RightEye" -> Hue[0.4],
   "Nose" -> Hue[0.6], "LeftMouth" -> Hue[0.8],
   "RightMouth" -> Hue[1]|>;
showLandmarks[data_] :=
 Table[HighlightImage[
   face["Crop"], {PointSize[0.04],
    Riffle[Values@colorCodes, Values@face["Landmarks"]]},
   DataRange -> {{0, 1}, {0, 1}}], {face, data}]
(*Separate 2D Face Alignment NN*)
NetModel["2D Face Alignment Net Trained on 300W Large Pose Data"]
(*Get landmarks using evaluation function: *)
netevaluation[img_] := Block[
  {heatmaps, posFlattened, posMat},
  heatmaps =
   NetModel["2D Face Alignment Net Trained on 300W Large Pose Data"][
    img];
  posFlattened =
   Map[First@Ordering[#, -1] &, Flatten[heatmaps, {{1}, {2, 3}}]];
  posMat = QuotientRemainder[posFlattened - 1, 64] + 1;
  1/64.*Map[{#[[2]], 64 - #[[1]] + 1} - 0.5 &, posMat]
  ]

(* Evaluate this cell to get the example input *) CloudGet["https://www.wolframcloud.com/obj/bf8852d2-bcd4-4148-b855-de24cea25639"]
groupings =
  Span @@@ {{1, 17}, {18, 22}, {23, 27}, {28, 36}, {37, 42}, {43,
     48}, {49, 60}, {61, 68}};
(* Evaluate this cell to get the example input *) CloudGet["https://www.wolframcloud.com/obj/b9db7852-bd64-4d2f-838f-b49f694b557a"]
HighlightImage[#Crop,
   Graphics@
    Riffle[Thread@Hue[Range[8]/8.],
     Map[Point, Function[p, Part[#Landmarks, p]] /@ groupings]],
   DataRange -> {{0, 1}, {0, 1}}, ImageSize -> 300] & /@ output

crops = Table[ImageCrop[img, s, Bottom], {s, 290, 500, 70}];
HighlightImage[#,
   Graphics@
    Riffle[Thread@Hue[Range[8]/8.],
     Map[Point, Function[p, Part[netevaluation[#], p]] /@ groupings]],
    DataRange -> {{0, 1}, {0, 1}}, ImageSize -> 250] & /@ crops