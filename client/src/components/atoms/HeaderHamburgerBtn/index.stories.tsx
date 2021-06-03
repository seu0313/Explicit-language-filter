import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import HeaderHamburgerBtn, { HeaderHamburgerProps } from "./index";

export default {
  title: "Atoms/HeaderHamburgerBtn",
  component: HeaderHamburgerBtn,
};

const Template: Story<HeaderHamburgerProps> = (args) => (
  <GlobalThemeProvider>
    <HeaderHamburgerBtn {...args} />
  </GlobalThemeProvider>
);

export const HeaderHamburger = Template.bind({});

HeaderHamburger.args = {
  isMenuClicked: false,
};
