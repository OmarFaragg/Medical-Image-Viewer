import InsightViewer, { useImage } from '@lunit/insight-viewer'
import { useLocation  } from 'react-router-dom';
import './View.css';


export default function App() {
    let location = useLocation(); 
  const { image } = useImage({
    dicomfile: location.state.imageId,
  })
  console.log(location)

  return (
    <>
      <div className='image-container'>
        <InsightViewer image={image} />
      </div>
    </>
  )
}
