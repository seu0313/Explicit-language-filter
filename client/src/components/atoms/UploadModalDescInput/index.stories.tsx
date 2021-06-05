import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import UploadModalDescInput, { UploadModalDescInputProps } from "./index";

export default {
  title: "Atoms/UploadModalDescInput",
  component: UploadModalDescInput,
};

const Template: Story<UploadModalDescInputProps> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <UploadModalDescInput {...args} />
  </GlobalThemeProvider>
);

export const UploadModalDescInputStory = Template.bind({});

UploadModalDescInputStory.args = {};
