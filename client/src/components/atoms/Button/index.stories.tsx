import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import Button, { Props } from "./index";

export default {
  title: "Atoms/Button",
  component: Button,
};

const Template: Story<Props> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <Button {...args} />
  </GlobalThemeProvider>
);

export const ButtonStory = Template.bind({});

ButtonStory.args = {
  type: "submit",
  width: "311px",
  height: "43px",
  value: "제출",
  fontSize: "16px",
};
