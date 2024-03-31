import '../Auth/Auth.css';
import { useDicomFile } from '@lunit/insight-viewer'
import { useNavigate } from 'react-router-dom';


const Upload = () => {
    const navigate = useNavigate();
    const { imageId, file, setImageIdByFile } = useDicomFile()

    const handleFileChange = (e) => {
        setImageIdByFile(e.target.files[0])
    };

    const handleUpload = () => {
        if (file) {
            navigate('/view', {state: {imageId}})
        } else {
            console.log('No file selected.');
        }
    };

    return (
        <div className='container'>
            <div className="submit-container">
                <input type="file" accept="application/dicom" onChange={handleFileChange} />
                <input type="text" value={file ? file.name : ''} readOnly />
            </div>
            <button className="submit" onClick={handleUpload}>Upload and View</button>
        </div>
    );
};

export default Upload;
