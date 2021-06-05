import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import HamburgerBtn, { Props } from "./index";

export default {
  title: "Atoms/HamburgerBtn",
  component: HamburgerBtn,
};

const Template: Story<Props> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <HamburgerBtn {...args} />
  </GlobalThemeProvider>
);

export const HamburgerBtnStory = Template.bind({});

HamburgerBtnStory.args = {
  isMenuClicked: false,
};
