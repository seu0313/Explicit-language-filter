import React from "react";
import * as S from "./style";

export interface VideoCreatedAtProps {
  date: string;
}

const VideoCreatedAt: React.FC<VideoCreatedAtProps> = ({ date }) => {
  return (
    <S.Container>
      <S.VideoCreatedAt>
        <b>Created at:</b> {date}
      </S.VideoCreatedAt>
    </S.Container>
  );
};

export default VideoCreatedAt;
