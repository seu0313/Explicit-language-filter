import React from "react";
import Label from "components/atoms/Label";
import Text from "components/atoms/Text";
import { Player } from "video-react";
// import "node_modules/video-react/dist/video-react.css";
import VideoCreatedAt from "components/atoms/VideoCreatedAt";
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
      <Player key={id} width="343px" height="200px" src={src} />
      <S.MetaSection>
        <Label text={title} width="18.75rem" />
        <Text text={description} />
        <VideoCreatedAt createdAt={createdAt} />
      </S.MetaSection>
    </S.DetailVideo>
  );
};

export default DetailVideo;
