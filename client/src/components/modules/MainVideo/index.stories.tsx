import React from "react";
import thumbnail from "assets/image/thumbnail.png";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import MainVideo, { Props } from "./index";

export default {
  title: "Modules/MainVideo",
  component: MainVideo,
};

const Template: Story<Props> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <MainVideo {...args} />
  </GlobalThemeProvider>
);

export const MainVideoStory = Template.bind({});

MainVideoStory.args = {
  id: "1",
  title: "Mountains | Beautiful Chill Mix WAAAAA~",
  createdAt: "2021-06-04T14:05:46.384Z",
  src: thumbnail,
};
