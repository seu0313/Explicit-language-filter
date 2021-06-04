import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import UploadModalDescInput from "./index";

export default {
  title: "Atoms/UploadModalDescInput",
  component: UploadModalDescInput,
};

const Template: Story = (args): JSX.Element => (
  <GlobalThemeProvider>
    <UploadModalDescInput {...args} />
  </GlobalThemeProvider>
);

export const UploadModalDescInputStory = Template.bind({});

UploadModalDescInputStory.args = {};
