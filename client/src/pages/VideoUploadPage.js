import React, { useState } from "react";

// added
import axios from "axios";
import { Redirect } from "react-router-dom";

// design
import { Button, TextField } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import CloudUploadIcon from "@material-ui/icons/CloudUpload";
import { Modal, Dimmer, Loader, Image, Segment } from "semantic-ui-react";
import "./VideoUploadPage.scss";

// components

const useStyles = makeStyles((theme) => ({
  button: {
    margin: theme.spacing(1),
  },
}));

const VideoUploadPage = () => {
  // state
  const classes = useStyles();
  const [VideoTitle, setVideoTitle] = useState("");
  const [VideoDescription, setVideoDescription] = useState("");
  const [VideoFile, setVideoFile] = useState(undefined);
  const [TransferFailState, setTransferFailState] = useState(false);
  const [RedirectState, setRedirectState] = useState(false);
  const [value, setValue] = React.useState("GCP");

  // lifecycle

  // func
  const handleValueChange = (e) => {
    setValue(e.target.value);
  };

  const handleTitleChange = (e) => {
    setVideoTitle(e.currentTarget.value);
  };

  const handleDescChange = (e) => {
    setVideoDescription(e.currentTarget.value);
  };

  const handleFileChange = (e) => {
    setVideoFile(e.currentTarget.files[0]);
  };

  const stateInitialize = () => {
    setVideoTitle("");
    setVideoDescription("");
    setVideoFile(undefined);
    setValue("GCP");
  };

  const fileSubmit = (e) => {
    e.preventDefault();

    // create data form
    const formData = new FormData();
    formData.append("title", VideoTitle);
    formData.append("description", VideoDescription);
    formData.append("videoFile", VideoFile);
    formData.append("processMethod", value);

    let url = "http://localhost:8000/api/v1/deeps/";

    axios
      .post(url, formData, {
        headers: {
          "content-type": "multipart/form-data",
        },
      })
      .then((res) => {
        stateInitialize();
        setRedirectState(true);
      })
      .catch((err) => {
        console.log(err);
        setTransferFailState(true);
      });
  };

  // render
  if (!TransferFailState && RedirectState) {
    return <Redirect to="/" />;
  }

  return (
    <div className="upload">
      <div className="responsive-video-grid-container">
        <h2>업로드</h2>
        <form method="POST" onSubmit={fileSubmit}>
          <TextField
            id="outlined-basic"
            label="제목"
            variant="outlined"
            type="text"
            placeholder="영상의 제목을 입력해주세요"
            fullWidth
            value={VideoTitle}
            onChange={handleTitleChange}
          />
          <hr />
          <TextField
            id="outlined-basic"
            label="설명"
            variant="outlined"
            type="text"
            placeholder="영상의 설명을 입력해주세요"
            fullWidth
            value={VideoDescription}
            onChange={handleDescChange}
          />
          <hr />
          <Button
            size="large"
            color="primary"
            variant="contained"
            component="label"
          >
            <input
              type="file"
              accept="video/mp4, video/avi, video/mov"
              name="video"
              onChange={handleFileChange}
              required
            />
          </Button>
          <Modal
            trigger={
              <Button
                size="large"
                variant="contained"
                color="secondary"
                className={classes.button}
                startIcon={<CloudUploadIcon />}
                type="submit"
              >
                UPLOAD
              </Button>
            }
          >
            <Modal.Header>
              {VideoFile && !TransferFailState ? "비속어 처리 중.." : "경고!"}
            </Modal.Header>
            <Modal.Content image>
              {VideoFile && !TransferFailState ? (
                <Segment>
                  <Dimmer active>
                    <Loader />
                  </Dimmer>

                  <Image src="/images/wireframe/short-paragraph.png" />
                </Segment>
              ) : (
                "다시 시도해주십시오."
              )}
            </Modal.Content>
          </Modal>
          <FormControl component="fieldset">
            <FormLabel component="legend">Method</FormLabel>
            <RadioGroup
              aria-label="method"
              name="method1"
              value={value}
              onChange={handleValueChange}
            >
              <FormControlLabel value="GCP" control={<Radio />} label="GCP" />
              <FormControlLabel value="None" control={<Radio />} label="None" />
            </RadioGroup>
          </FormControl>
        </form>
      </div>
    </div>
  );
};

export default VideoUploadPage;
