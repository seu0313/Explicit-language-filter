import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import UploadModalFileInput from "./index";

export default {
  title: "Atoms/UploadModalFileInput",
  component: UploadModalFileInput,
};

const Template: Story = (args): JSX.Element => (
  <GlobalThemeProvider>
    <UploadModalFileInput {...args} />
  </GlobalThemeProvider>
);

export const UploadModalFileInputStory = Template.bind({});
