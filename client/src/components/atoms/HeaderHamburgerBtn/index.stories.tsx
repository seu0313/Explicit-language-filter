import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import HeaderHamburgerBtn, { HeaderHamburgerBtnProps } from "./index";

export default {
  title: "Atoms/HeaderHamburgerBtn",
  component: HeaderHamburgerBtn,
};

const Template: Story<HeaderHamburgerBtnProps> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <HeaderHamburgerBtn {...args} />
  </GlobalThemeProvider>
);

export const HeaderHamburgerBtnStory = Template.bind({});

HeaderHamburgerBtnStory.args = {
  isMenuClicked: false,
};
