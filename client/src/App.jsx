import "./App.css";
import { HashRouter as Router, Routes, Route } from 'react-router-dom'
import { Home } from './pages/home'
import { Nav } from './pages/nav'
import { Fish } from './pages/fish'
import { Fossils } from './pages/fossils'
import { Insects } from './pages/insects'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/nav" element={<Nav/>}/>
        <Route path="/fish" element={<Fish/>}/>
        <Route path="/fossils" element={<Fossils/>}/>
        <Route path="/insects" element={<Insects/>}/>
      </Routes>
    </Router>
  )
}
export default App