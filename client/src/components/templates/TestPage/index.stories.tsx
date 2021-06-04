import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import TestPage from "./index";

export default {
  title: "Templates/TestPage",
  component: TestPage,
};

const Template: Story = () => (
  <GlobalThemeProvider>
    <TestPage />
  </GlobalThemeProvider>
);

export const TestPageStory = Template.bind({});
