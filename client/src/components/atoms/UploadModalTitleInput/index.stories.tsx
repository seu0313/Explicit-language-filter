import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import UploadModalTitleInput, { UploadModalTitleInputProps } from "./index";

export default {
  title: "Atoms/UploadModalTitleInput",
  component: UploadModalTitleInput,
};

const Template: Story<UploadModalTitleInputProps> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <UploadModalTitleInput {...args} />
  </GlobalThemeProvider>
);

export const UploadModalTitleInputStory = Template.bind({});

UploadModalTitleInputStory.args = {};
