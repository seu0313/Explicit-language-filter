import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import VideoTitle, { VideoTitleProps } from "./index";

export default {
  title: "Atoms/VideoTitle",
  component: VideoTitle,
};

const Template: Story<VideoTitleProps> = (args) => (
  <GlobalThemeProvider>
    <VideoTitle {...args} />
  </GlobalThemeProvider>
);

export const VideoTitleStory = Template.bind({});

VideoTitleStory.args = {
  text: "Title",
};
