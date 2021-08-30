import React from "react";
import * as S from "./style";

export interface Props {
  src: string;
  width?: string;
}

const VideoThumbnail: React.FC<Props> = ({
  src,
  width = "343px",
}): JSX.Element => {
  return <S.VideoThumbnail src={src} width={width} />;
};

export default VideoThumbnail;
