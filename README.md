# ue-helper

 Very simple helper Addon for Blender For Unreal Engine addon (https://github.com/xavier150/Blender-For-UnrealEngine-Addons). 
 
 Main functionality is to mark multiple objects for export and preseve hierarchy of blender collection on unreal side.
 
 <img src="https://github.com/bbn777/ue-helper/blob/main/docs/02-mark.jpg">
 
 The addon serves those 2 purpouses:
 - Marking/unmarking selected objects for export to unreal (export type: Export Recursive)
 - Setting sub folder name to the one matched by collections

# What it does?

In my workflow I freuqently need to export multiple objects to Unreal Engine. And I want for the objects to appear in Unreal under the same hirerachy as in Blender.

Let's say you have bunch of objects and you want export subset of those to unreal with Blender For Unreal Engine addon. (⚠️the images are from early version and show ue-helper as separate n-panel. Now they are attached at the bottom of the BfUE addon.)

<img src="https://github.com/bbn777/ue-helper/blob/main/docs/01-init.jpg">


Select objects that you want to export and click "Mark selected for export" from "UE Helper. If you check "Rotate Z" option, it will add additional 90 degrees rotation on the Z axsis for the export (to match unreal's forward direction if your objects face -Y in Blender).

<img src="https://github.com/bbn777/ue-helper/blob/main/docs/02-mark.jpg">

After that selected objects are set to "Export recursive" with their sub folder names matching hierarchy:

<img src="https://github.com/bbn777/ue-helper/blob/main/docs/03-result.jpg">

Do note, that the code for traversing hierarchy is not the most efficient one and make take few seconds if you run it on hundrets of objcts.

# Download and installation instructions

0. Download and install Blender For Unreal Engine addon (https://github.com/xavier150/Blender-For-UnrealEngine-Addons) if you don't have it.
1. Download current release [from here](https://github.com/VertexMachine/ue-helper/releases).
2. In Blender: Open User Preferences and under Add-ons click Install from file. Navigate to the downloaded file in step 1 and select it.
3. It should now appear in the window with Add-ons. You can tick the checkbox to enable it. If the checkbox don't appear search for "ue-helper"

Note, for BfUE 0.4.1 use ue-helper version of 0.0.3. v0.0.4 and onwards are for 0.4.2 and newer.

# Ligtmap UV Generation

New feature: the addon can generate now lightmap UVs for objects using Blender's built in lightmap UV generation algorithm.

- Utilizes Blender's built-in lightmap UV generation with a quality setting of 30 and a margin of 0.2.
- Toggles the 'Generate Lightmap UVs' option in BfU.
- Effective only during the 'Mark for Export' process.
- Adds a second UV map exclusively for objects with only one existing UV map.
- ⚠️Use with care, as it might not be efficient in your case, see [BleuRaven wiki page](https://github.com/xavier150/Blender-For-UnrealEngine-Addons/wiki/Generate-UV-Light-Maps) for more in-depth explanation of what the problem with that method can be.
  
<img src="https://github.com/bbn777/ue-helper/blob/main/docs/LightmapUVs.jpg">

# Other

If you like this addon ping me on twitter at https://twitter.com/VertexRage

If you found some bug or would like to see some improvements to the addon please create an issue or join my [discord server](https://discord.gg/U56WakRzpM) (support/#ue-helper channel) 
