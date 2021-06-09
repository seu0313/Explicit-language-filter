import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import Label, { Props } from "./index";

export default {
  title: "Atoms/Label",
  component: Label,
};

const Template: Story<Props> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <Label {...args} />
  </GlobalThemeProvider>
);

export const LabelStory = Template.bind({});

LabelStory.args = {
  type: "text",
  width: "9rem",
  text: "LINGO FILTER",
  fontSize: "18px",
};
