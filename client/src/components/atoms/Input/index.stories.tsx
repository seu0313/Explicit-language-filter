import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import Input, { Props } from "./index";

export default {
  title: "Atoms/Input",
  component: Input,
};

const Template: Story<Props> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <Input {...args} />
  </GlobalThemeProvider>
);

export const InputStory = Template.bind({});

InputStory.args = {
  type: "text",
  accept: "",
  width: "311px",
  height: "43px",
  fontSize: "13px",
  placeholder: "제목을 입력하세요*",
};
