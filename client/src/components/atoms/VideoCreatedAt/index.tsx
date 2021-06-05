import React from "react";
import * as S from "./style";

export interface Props {
  createdAt: string;
}

const VideoCreatedAt: React.FC<Props> = ({ createdAt }): JSX.Element => {
  return (
    <S.VideoCreatedAt>
      <b>Created at:</b> {createdAt}
    </S.VideoCreatedAt>
  );
};

export default VideoCreatedAt;
