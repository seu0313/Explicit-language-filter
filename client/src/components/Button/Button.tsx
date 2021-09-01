import React from "react";
import styled from "styled-components";
import theme from "../../styles/theme";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  className?: string;
  type?: "submit" | "button" | "reset" | undefined;
  style?: React.CSSProperties;
  children?: React.ReactNode;
  disabled?: boolean;
}

export default function Button({
  className,
  type = "button",
  style,
  children,
  disabled,
}: ButtonProps): JSX.Element {
  return (
    <ButtonElement
      type={type}
      className={className}
      style={style}
      disabled={disabled}
    >
      {children}
    </ButtonElement>
  );
}

const ButtonElement = styled.button<ButtonProps>`
  width: 20rem;
  height: 3rem;
  cursor: pointer;
  font-size: 1.1rem;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: 500;
  color: white;
  background-color: ${theme.color.basicColor};

  &:disabled {
    background-color: ${theme.color.disabled};
  }

  &:active {
    background-color: ${theme.color.press};
  }
`;
