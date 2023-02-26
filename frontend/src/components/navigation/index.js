import React from 'react'
import { Menubar } from 'primereact/menubar';
const Navigation = () => {
    const navlist = [
        {label: 'Home', icon: 'pi pi-fw pi-home', command: () => {
            window.location.href='/';
        }},
        {label: 'Visualization', icon: 'pi pi-fw pi-map', command: () => {
            window.location.href='/viz';
        }},
        {label: 'Analysis', icon: 'pi pi-fw pi-search-plus', command: () => {
            window.location.href='/analysis';
        }},
        {label: 'Sources', icon: 'pi pi-fw pi-database', command: () => {
            window.location.href='/sources';
        }},
        {label: 'About', icon: 'pi pi-fw pi-calendar', command: () =>{
            window.location.href='/about'
        }},
        { label: 'Contact', icon: 'pi pi-fw pi-phone', command: () =>{
            window.location.href='/contact'
        }}
      ]
  return (
    <div>
           <header>
              <nav>
                <ul>
                    <Menubar model={navlist}/>
                </ul>
              </nav>
           </header>
        </div>
  )
}

export default Navigation