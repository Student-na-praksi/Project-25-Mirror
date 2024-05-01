import "./frame-style.css";
import hamburgerIcon from "./assets/Hamburger_icon.svg.png";

export const Frame = (props: any) => {
    return (
        <div className={`frame ${props.className}`}>
            <img className="hamburger-icon" alt="Hamburger icon" src={hamburgerIcon} />
        </div>
    );
};