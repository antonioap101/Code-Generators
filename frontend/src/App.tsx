// src/App.tsx
import React from 'react';
import '@/App.css';
import AuthorLink from "./components/authorLink/AuthorLink.tsx";
import ThemeToggleButton from "./components/themeToggleButton/ThemeToggleButton.tsx";
import HelpButton from "./components/helpButton/helpButtonAndPopUp.tsx";
import {Route, Routes} from 'react-router-dom';
import GraphMLCodeGenerator from "./pages/graphml/GraphMLCodeGenerator.tsx";
import HomePage from "./pages/homePage/HomePage.tsx";
import NotFoundPage from "./pages/notFound/NotFoundPage.tsx";
import HomeButton from "./components/homeButton/HomeButton.tsx";

const App: React.FC = () => {
    return (
        <div className="app-container">
            <AuthorLink/>
            <HomeButton/>
            <div style={{
                zIndex: 1000
            }}>
            </div>
            <div style={{
                zIndex: 1000, position: 'fixed', top: 20, right: 20, display: 'flex', gap: '10px'
            }}>
                <ThemeToggleButton/>
                <HelpButton/>
            </div>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/graphml-code-generator" element={<GraphMLCodeGenerator/>}/>
                {/*<Route path="/crud-code-generator" element={<CRUDCodeGeneratorPage />} />*/}
                <Route path="*" element={<NotFoundPage/>}/>
            </Routes>

        </div>
    );
};

export default App;
