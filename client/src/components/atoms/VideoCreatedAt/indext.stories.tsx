import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import VideoCreatedAt, { VideoCreatedAtProps } from "./index";

export default {
  title: "Atoms/VideoCreatedAt",
  component: VideoCreatedAt,
};

const Template: Story<VideoCreatedAtProps> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <VideoCreatedAt {...args} />
  </GlobalThemeProvider>
);

export const VideoCreatedAtStory = Template.bind({});

VideoCreatedAtStory.args = {
  date: "2021-06-04T14:05:46.384Z",
};
