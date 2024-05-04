import "./MenuBurgerButton-style.css";
import hamburgerIcon from "@/assets/Hamburger_icon.svg.png";

export const MenuBurgerButton = (props: any) => {
    return (
        // It has two classNames networkInterfaces. Frame and the one passed.
        <div className={`frame ${props.className}`}>
            <img className="hamburger-icon" alt="Hamburger icon" src={hamburgerIcon} />
        </div>
    );
};