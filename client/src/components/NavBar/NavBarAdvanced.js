import React, { useState } from 'react';

// added
import { Link } from 'react-router-dom';

// design
import { Menu, Icon, Input, Form, Button } from 'semantic-ui-react';
import './NavBarAdvanced.scss';

// components


const NavBarAdvanced = () => {
    // state
    const [ActiveItem, setActiveItem] = useState('프로필')
    const [anchorEl, setAnchorEl] = React.useState(false);

    // func
    const handleItemClick = (e, { name }) => {
        setActiveItem(name)
    }

    const handleProfileMenuOpen = () => {
        setAnchorEl(!anchorEl);
    };


    const renderMenu = (
        <Menu
            size='small'
            pointing
            attached='top'
        >
            <Link to='/profile'>
                <Menu.Item
                    name='프로필'
                    active={ActiveItem === '프로필'}
                    onClick={handleItemClick}
                />
            </Link>
            <Link to='/account'>
                <Menu.Item
                    name='계정'
                    active={ActiveItem === '계정'}
                    onClick={handleItemClick}
                />
            </Link>

        </Menu>
    );

    return (
        <div>
            <Menu borderless className='top-menu' fixed='top'>
                <Menu.Item header className='logo'>
                    <Link to='/'><h2>: EIEO</h2></Link>
                </Menu.Item>
                <Menu.Menu className='nav-container'>
                    <Menu.Item className='search-input'>
                        <Form>
                            <Form.Field>
                                <Input placeholder='검색어를 입력하세요'
                                    size='big'
                                    action='검색'
                                />
                            </Form.Field>
                        </Form>
                    </Menu.Item>
                    <Menu.Menu position='right'>
                        <Menu.Item>
                            <Link to='/upload'>
                                <Button icon color='google plus'>
                                    <Icon className='header-icon' name='video camera' size='large'/>
                                </Button>
                            </Link>
                        </Menu.Item>
                        <Menu.Item>
                            {anchorEl ? renderMenu : null}
                        </Menu.Item>
                        <Menu.Item name='avatar'>
                            <Button icon color='twitter' onClick={handleProfileMenuOpen}>
                                <Icon name='user' size='large'/>
                            </Button>
                        </Menu.Item>
                    </Menu.Menu>
                </Menu.Menu>
            </Menu>
        </div>
    )
};

export default NavBarAdvanced;
