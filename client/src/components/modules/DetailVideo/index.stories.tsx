import React from "react";
import thumbnail from "assets/image/thumbnail.png";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import DetailVideo, { Props } from "./index";

export default {
  title: "Modules/DetailVideo",
  component: DetailVideo,
};

const Template: Story<Props> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <DetailVideo {...args} />
  </GlobalThemeProvider>
);

export const DetailVideoStory = Template.bind({});

DetailVideoStory.args = {
  id: "1",
  title: "Mountains | Beautiful Chill Mix WAAAAA~",
  createdAt: "2021-06-04T14:05:46.384Z",
  src: thumbnail,
};
