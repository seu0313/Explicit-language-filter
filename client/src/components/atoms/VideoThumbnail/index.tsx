import React from "react";
import * as S from "./style";

export interface VideoThumbnailProps {
  src: string;
}

const VideoThumbnail: React.FC<VideoThumbnailProps> = ({ src }) => {
  return (
    <S.Container>
      <S.VideoThumbnail src={src} />
    </S.Container>
  );
};

export default VideoThumbnail;
