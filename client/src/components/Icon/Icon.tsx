import React from "react";
import * as svg from "../../assets/icon";

export type TSvg = keyof typeof svg;
type IconProps = {
  name: TSvg;
};

const Icon = ({ name }: IconProps): JSX.Element => {
  return React.createElement(svg[name], {
    width: "1.2rem",
    height: "1.2rem",
  });
};

export default Icon;
