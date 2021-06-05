import React from "react";
import { Story } from "@storybook/react";
import cloud from "assets/image/cloud.png";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import Header, { Props } from "./index";

export default {
  title: "Modules/Header",
  component: Header,
};

const Template: Story<Props> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <Header {...args} />
  </GlobalThemeProvider>
);

export const HeaderStory = Template.bind({});

HeaderStory.args = {
  src: cloud,
  text: "LINGO FILTER",
  isMenuClicked: false,
  isUploadClicked: false,
};
