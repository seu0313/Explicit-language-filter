import React, { Component } from 'react'
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import {Button, TextField } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios'

// const useStyles = makeStyles((theme) => ({
//     root: {
//         '& > *': {
//           margin: theme.spacing(1),
//           width: '25ch',
//         },
//     },
//     button: {
//       margin: theme.spacing(1),
//     },
// }));

class FileUploader extends Component {
    constructor(props){
        super(props)
        this.state = {
            title: "",
            video: undefined,
            fileName: "UPLOAD FILE",
        }
    }
    
    handleTitleChange = (e) => {
        this.setState({title: e.target.value})
    }

    handleFileChange = (e) => {
        this.setState({
            video: e.target.files[0],
            fileName: e.target.files[0]['name']
        })
    }

    // 파일 전송 Form
    fileSubmit = async (e) => {
        e.preventDefault();
        const form_data = new FormData();
        form_data.append('title', this.state.title)
        form_data.append('video_file', this.state.video)
    
        let url = 'http://localhost:8000/deeps/';

        await axios.post(url, form_data, {
                headers: {
                    'content-type': "multipart/form-data"
                }
            })
            .then(res => {
                console.log(res.data);
                this.setState({
                    title: "",
                    video: undefined,
                    fileName: "UPLOAD FILE"
                })
                this.props._renderData()

                console.log(this.state.fileName + this.state.title, this.state.video)
            })
            .catch(err => console.log(err))
    }

    render() {
        // const classes = useStyles();
        return (
            <div>
                <form method='POST' onSubmit={this.fileSubmit}>
                    <TextField id="outlined-basic" label="Title" variant="outlined" type='text' placeholder='Please input title' fullWidth value={this.state.title} onChange={this.handleTitleChange}/>
                    <Button variant="contained" component="label">
                        {this.state.fileName}
                        <input type="file" style={{ display: "none" }} accept='video/mp4, video/avi, video/mov' name="video" onChange={this.handleFileChange} required/>
                    </Button>
                    <Button variant="contained"
                            color="default"
                            // className={classes.button}
                            startIcon={<CloudUploadIcon />}
                            type='submit'>
                        upload
                    </Button>
                </form>
            </div>
        )
    }
}

export default FileUploader
