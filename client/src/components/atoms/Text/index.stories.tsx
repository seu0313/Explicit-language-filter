import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import Text, { Props } from "./index";

export default {
  title: "Atoms/Text",
  component: Text,
};

const Template: Story<Props> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <Text {...args} />
  </GlobalThemeProvider>
);

export const TextStory = Template.bind({});

TextStory.args = {
  text: "Lorem description",
  fontSize: "16px",
};
