import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import UploadModalBtn from "./index";

export default {
  title: "Atoms/UploadModalBtn",
  component: UploadModalBtn,
};

const Template: Story = (args): JSX.Element => (
  <GlobalThemeProvider>
    <UploadModalBtn {...args} />
  </GlobalThemeProvider>
);

export const UploadModalBtnStory = Template.bind({});
