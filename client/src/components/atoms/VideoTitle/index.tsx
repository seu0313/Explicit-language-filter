import React from "react";
import * as S from "./style";

export interface VideoTitleProps {
  text: string;
}

const VideoTitle: React.FC<VideoTitleProps> = ({ text }): JSX.Element => {
  return (
    <S.Container>
      <S.VideoTitle>{text}</S.VideoTitle>
    </S.Container>
  );
};

export default VideoTitle;
