import React, {useState} from 'react'
import {Button, TextField } from '@material-ui/core'
import axios from 'axios'
import { makeStyles } from '@material-ui/core/styles';
import DeleteIcon from '@material-ui/icons/Delete';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import KeyboardVoiceIcon from '@material-ui/icons/KeyboardVoice';
import Icon from '@material-ui/core/Icon';
import SaveIcon from '@material-ui/icons/Save';

const useStyles = makeStyles((theme) => ({
    root: {
        '& > *': {
          margin: theme.spacing(1),
          width: '25ch',
        },
    },
    button: {
      margin: theme.spacing(1),
    },
  }));
  

const FileUploader = () => {
    const classes = useStyles();
    const [title, setTitle] = useState("");
    const [video, setVideo] = useState(undefined);
    const [fileName, setFileName] = useState("UPLOAD FILE")

    const handleChange = (e) => {
        setTitle(e.target.value)
    }

    const handleFileChange = (e) => {
        setVideo(e.target.files[0])
        setFileName(e.target.files[0]['name'])
    }

    const fileSubmit = async (e) => {
        e.preventDefault();
        let form_data = new FormData();
        form_data.append('title', title)
        form_data.append('video_file', video)
    
        let url = 'http://localhost:8000/deeps/';

        await axios.post(url, form_data, {
                headers: {
                    'content-type': "multipart/form-data"
                }})
                .then(res => {
                    console.log(res.data);
                    setTitle("")
                    setVideo(undefined)
                    setFileName("UPLOAD FILE")
                })
                .catch(err => console.log(err))
    }

    return (
        <div>
            <form method='POST' onSubmit={fileSubmit}>
                <TextField id="outlined-basic" label="Title" variant="outlined" type='text' placeholder='Please input title' fullWidth value={title} onChange={handleChange}/>
                <Button variant="contained" component="label">
                    {fileName}
                    <input type="file" style={{ display: "none" }} accept='video/mp4, video/avi, video/mov' name="video" onChange={handleFileChange} required/>
                </Button>
                <Button variant="contained"
                        color="default"
                        className={classes.button}
                        startIcon={<CloudUploadIcon />}
                        type='submit'>
                    upload
                </Button>
            </form>
        </div>
    )
}

export default FileUploader;
