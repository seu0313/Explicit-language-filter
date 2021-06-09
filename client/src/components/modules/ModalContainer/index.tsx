import React, { useState } from "react";
import UploadModal from "components/modules/UploadModal";
import * as S from "./style";

export interface ModalContainerProps {
  isUploadClicked: boolean;
  setIsUploadClicked: (value: boolean) => void;
  isMenuClicked: boolean;
  setIsMenuClicked: (value: boolean) => void;
  renderHandler: () => void;
}

const ModalContainer: React.FC<ModalContainerProps> = ({
  isUploadClicked,
  setIsUploadClicked,
  isMenuClicked,
  setIsMenuClicked,
  renderHandler,
}): JSX.Element => {
  const [opacity, setOpacity] = useState(0);
  const [modalState, setModalState] = useState("");

  const toggleModal = () => {
    setOpacity(0);
    if (isUploadClicked) {
      setIsUploadClicked(!isUploadClicked);
    } else {
      setIsMenuClicked(!isMenuClicked);
    }
  };

  const beforeOpen = () => {
    if (isMenuClicked) {
      setModalState("menu");
    } else {
      setModalState("upload");
    }
  };

  const afterOpen = () => {
    setTimeout(() => {
      setOpacity(1);
    }, 100);
  };

  const beforeClose = () => {
    return new Promise((resolve) => {
      setOpacity(0);
      setTimeout(resolve, 300);
    });
  };

  return (
    // <S.Container>
    <S.ModalContainer
      // opacity={opacity}
      isOpen={isUploadClicked || isMenuClicked}
      beforeOpen={beforeOpen}
      afterOpen={afterOpen}
      beforeClose={beforeClose}
      onBackgroundClick={toggleModal}
      onEscapeKeydown={toggleModal}
      backgroundProps={{ opacity }}
    >
      {
        {
          menu: <div>menu</div>,
          upload: (
            <UploadModal
              isUploadClicked={isUploadClicked}
              setIsUploadClicked={setIsUploadClicked}
              renderHandler={renderHandler}
            />
          ),
        }[modalState]
      }
    </S.ModalContainer>
    // </S.Container>
  );
};

export default ModalContainer;
