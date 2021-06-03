import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import HeaderText, { HeaderTextProps } from "./index";

export default {
  title: "Atoms/HeaderText",
  component: HeaderText,
};

const Template: Story<HeaderTextProps> = (args) => (
  <GlobalThemeProvider>
    <HeaderText {...args} />
  </GlobalThemeProvider>
);

export const HeaderTextStory = Template.bind({});

HeaderTextStory.args = {
  text: "LINGO FILTER",
};
