import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import ModalContainer, { ModalContainerProps } from "./index";

export default {
  title: "Modules/ModalContainer",
  component: ModalContainer,
};

const Template: Story<ModalContainerProps> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <ModalContainer {...args} />
  </GlobalThemeProvider>
);

export const ModalContainerStory = Template.bind({});

ModalContainerStory.args = {
  isUploadClicked: false,
  isMenuClicked: false,
  isNotification: false,
};
