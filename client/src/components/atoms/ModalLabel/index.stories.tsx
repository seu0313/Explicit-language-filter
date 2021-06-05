import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import ModalLabel, { ModalLabelProps } from "./index";

export default {
  title: "Atoms/ModalLabel",
  component: ModalLabel,
};

const Template: Story<ModalLabelProps> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <ModalLabel {...args} />
  </GlobalThemeProvider>
);

export const ModalLabelStory = Template.bind({});

ModalLabelStory.args = {
  text: "비속어 필터링 하기",
};
