import React from "react";
import thumbnail from "assets/image/thumbnail.png";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import VideoThumbnail, { VideoThumbnailProps } from "./index";

export default {
  title: "Atoms/VideoThumbnail",
  component: VideoThumbnail,
};

const Template: Story<VideoThumbnailProps> = (args) => (
  <GlobalThemeProvider>
    <VideoThumbnail {...args} />
  </GlobalThemeProvider>
);

export const VideoThumbnailStory = Template.bind({});

VideoThumbnailStory.args = {
  src: thumbnail,
};
