import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import VideoCreatedAt, { Props } from "./index";

export default {
  title: "Atoms/VideoCreatedAt",
  component: VideoCreatedAt,
};

const Template: Story<Props> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <VideoCreatedAt {...args} />
  </GlobalThemeProvider>
);

export const VideoCreatedAtStory = Template.bind({});

VideoCreatedAtStory.args = {
  createdAt: "2021-06-04T14:05:46.384Z",
};
