import React from "react";
import thumbnail from "assets/image/thumbnail.png";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import MainVideo, { MainVideoProps } from "./index";

export default {
  title: "Modules/MainVideo",
  component: MainVideo,
};

const Template: Story<MainVideoProps> = (args) => (
  <GlobalThemeProvider>
    <MainVideo {...args} />
  </GlobalThemeProvider>
);

export const MainVideoStory = Template.bind({});

MainVideoStory.args = {
  id: "1",
  text: "Mountains | Beautiful Chill Mix WAAAAA~",
  date: "2021-06-04T14:05:46.384Z",
  src: thumbnail,
};
