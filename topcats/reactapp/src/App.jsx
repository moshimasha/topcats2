import React from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home"
import Upload from "./pages/Upload"
import NotFound from "./pages/NotFound"
import LearningView from "./pages/LearningView"
import ProtectedRoute from "./components/ProtectedRoute"
import LibraryView from "./pages/LibraryView"
import About from "./pages/About"

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />
        <Route path="/about" element={<About />} />
        <Route path="/login" element={<Login />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="/library" element={<LibraryView />} />
        <Route path="/learn/:fileName" element={<LearningView />} />
        
        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
