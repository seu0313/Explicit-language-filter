import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import UploadModalFileInput, { UploadModalFileInputProps } from "./index";

export default {
  title: "Atoms/UploadModalFileInput",
  component: UploadModalFileInput,
};

const Template: Story<UploadModalFileInputProps> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <UploadModalFileInput {...args} />
  </GlobalThemeProvider>
);

export const UploadModalFileInputStory = Template.bind({});
