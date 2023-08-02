+++
title = "Customizing Blender's Video Editing Workspace"
date = 2022-11-25
lastmod = 2022-11-28
categories = ["blender", "VSE"]
+++
The default VSE workspace is already very user-friendly. As with most Blender components, you can heavily customize the UI.

Blender's video editor is a basic but robust editor; tightly integrated with the other parts of the Blender ecosystem. Upon opening Blender, the [splash screen](https://docs.blender.org/manual/en/dev/interface/window_system/splash.html) gives you the possibility to create a *Video Editing* project. Choosing this option takes you immediately into the Video Editing workspace.

{{<figure src="/blender/assets/blender-splash-screen.svg" caption="Figure 1: Splash screen of Blender LTS version 3.3.1" alt= "Splash screen" width="100%" class="mx-auto d-block" >}}

Workspaces are predefined window layouts aimed at a specific use case, for example video editing. Each Workspace consists of a set of *Areas* containing one or more *Editors*. The Video Editing workspace is a smart combination of five editors. Together they provide you with all the necessary tools to edit your videos.

{{<figure src="/blender/assets/_video-editing-workspace.svg" caption="Figure 1: Default Video Editing workspace  with 5 editors" alt= "Video Editing workspace" width="100%">}}

(1) File browser: you can navigate your file system for easily adding assets (clips, images, sounds, ...) to your timeline by dragging and dropping the files. If you select multiple files, they will be added one after the other to the timeline. You can customize (sorting, filtering, ...) the file browser, so that you have an optimal overview of your assets. Of course, there are more methods to add content to your timeline.

(2) & (4) Video Sequencer: the areas (2) and (4) both contain the Video Sequence Editor; respectively with type Preview and type Sequencer. The Preview is self-explanatory. It shows you the image of the current frame in the Sequencer Timeline. The Sequencer type is probably the area in the workspace that you'll use the most. The Sequence Editor has three view types: *Sequencer*, *Preview*, and *Sequencer & Preview*. You can switch easily between the Sequencer and the Preview with the {Ctrl + Tab} shortcut

(3) Properties: are organized into several categories, which can be chosen via tabs (the icons column to its left). Not all categories are relevant in the Video Sequencer. By default only the following are shown: Active Tool, Render Properties, View Layer Properties, Scene Properties, World Properties, and Texture Properties. Most of the time, you will use only the Render Properties.

(5) Timeline: only the header of this editor is visible; so you have to drag the horizontal top border to reveal the time units and eventual keyframes. The Timeline Editor is also used in other workspaces. The use of this Timeline Editor within the Video Editor workspace is rather limited and a case could be made to remove it from the workspace. Its functions can easily be overtaken by the Sequencer (see figure 2), which is right on top of it in the Video Editing Workspace.

The built-in Video Editing workspace is very handy and it can be customized easily. Each editor area can be sized, moved, replaced or removed from the workspace. As example, an alternative workspace with auto-installed add-ons can be download from [tin2tin's github](https://github.com/tin2tin/Sequence_Editing>). A screenshot is provided in figure 2.

{{< figure src="https://raw.githubusercontent.com/tin2tin/Sequence_Editing/main/Sequence_Editing.png" caption="Figure 2: A customized Video Editing Workspace." alt= "A customized Video Editing Workspace" width="100%">}}

Please, note that the Timeline editor -area (5) in figure 2- is removed and that the Playback controls are placed in the header of the Sequencer. Several add-ons are automatically installed (e.g. Transform tools), together with some new operators (e.g. Remove Gap after ...). Last but not least, the Properties editor is also removed and the project settings are placed in the Preview sidebar, where they can easily toggled on/off with the N-key.
