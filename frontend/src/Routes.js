import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Auth from './Components/Auth/Auth'
import Upload from './Components/Upload/Upload';
import View from './Components/View/View';

export const Switches = () =>{
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Auth />} />
                <Route path="/upload" element={<Upload />} />
                <Route path="/view" element={<View />} />
            </Routes>
        </Router>
    )
}