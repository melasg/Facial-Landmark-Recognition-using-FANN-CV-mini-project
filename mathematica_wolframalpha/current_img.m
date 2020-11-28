(* Mathematica Source File *)
(* Created by the Wolfram Language Plugin for IntelliJ, see http://wlplugin.halirutan.de/ *)
(* :Author: masgh003 *)
(* :Date: 2020-11-26 *)

HighlightImage[CurrentImage[], FindFaces];

dev = DeviceOpen["Camera", $ImagingDevice];

f[i_Image] := HighlightImage[i, {"Boundary", FindFaces[i]}];
Dynamic[f[CurrentImage[]]]

i = img.jpg;
box = FindFaces[i];
FindFaces[i,{"Image","BoundingBox"}]
HighlightImage[i, {"Boundary",Blue,FindFaces[#]&}];
FindFaces[i, Method -> "LocalBinaryPatterns"]
FindFaces[i,
 Method -> {"LocalBinaryPatterns", "Haar", "SingleShotDetector"}]
