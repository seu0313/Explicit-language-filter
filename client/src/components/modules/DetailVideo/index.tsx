import React from "react";
import Label from "components/atoms/Label";
import { Player } from "video-react";
// import "node_modules/video-react/dist/video-react.css";
import VideoCreatedAt from "components/atoms/VideoCreatedAt";
import VideoThumbnail from "components/atoms/VideoThumbnail";
import * as S from "./style";

export interface Props {
  id: string;
  title: string;
  description: string;
  createdAt: string;
  src: string;
}

const DetailVideo: React.FC<Props> = ({
  id,
  title,
  description,
  createdAt,
  src,
}): JSX.Element => {
  return (
    <S.DetailVideo>
      <Player width="343px" height="200px" src={src} />
      <S.MetaSection>
        <Label text={title} width="18.75rem" />
        <Label text={description} width="18.75rem" />
        <VideoCreatedAt createdAt={createdAt} />
      </S.MetaSection>
    </S.DetailVideo>
  );
};

export default DetailVideo;
