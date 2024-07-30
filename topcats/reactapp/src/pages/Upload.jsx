import React, { useState } from 'react';
import axios from "axios";

function Upload() {
  const [file, setFile] = useState(null);
  
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await axios.post('http://localhost:8000/api/upload/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        console.log(response.data);
    } catch (error) {
        console.error('Error uploading file:', error);
    }
};
    
    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>Submit a file</h1>
            <input type="file" accept=".pdf" onChange={handleFileChange} />
            <button className="form-button" type="submit">
                Upload
            </button>
        </form>
    );
}

export default Upload