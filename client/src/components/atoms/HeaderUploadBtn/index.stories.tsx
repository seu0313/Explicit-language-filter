import React from "react";
import { Story } from "@storybook/react";
import cloud from "assets/image/cloud.png";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import HeaderUploadBtn, { HeaderUploadBtnProps } from "./index";

export default {
  title: "Atoms/HeaderUploadBtn",
  component: HeaderUploadBtn,
};

const Template: Story<HeaderUploadBtnProps> = (args) => (
  <GlobalThemeProvider>
    <HeaderUploadBtn {...args} />
  </GlobalThemeProvider>
);

export const HeaderUploadBtnStory = Template.bind({});

HeaderUploadBtnStory.args = {
  src: cloud,
  isUploadClicked: false,
};
