import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import UploadModal, { UploadModalProps } from "./index";

export default {
  title: "Modules/UploadModal",
  component: UploadModal,
};

const Template: Story<UploadModalProps> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <UploadModal {...args} />
  </GlobalThemeProvider>
);

export const UploadModalStory = Template.bind({});
