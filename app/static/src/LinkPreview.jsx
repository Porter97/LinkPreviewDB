import React, { useState } from 'react';
import Microlink from "@microlink/react";
import { makeStyles } from "@material-ui/core";
import ReactLoading from 'react-loading';

/* URL Input Field */
import { useDebounce } from './debounce';
import TextField from '@material-ui/core/TextField';
import InputAdornment from '@material-ui/core/InputAdornment';
import SearchIcon from '@material-ui/icons/Search';



const useStyles = makeStyles((theme) => ({
    mainContainer: {
        marginTop: '10%'
    },
    root: {
        display: 'flex',
        justifyContent: 'center',
        marginTop: theme.spacing(2)
    },
    InputField: {
        marginBottom: theme.spacing(3),
        width: '400px',
    },
    icon: {
        color: '#979797'
    }
}));

export default function LinkPreview() {
    const classes = useStyles();

    const [input, setInput] = useState(null);
    const debouncedQuery = useDebounce(input, 1000);

    const handleDelete = (event) => {
        if (event.keyCode === 8) {
            return setInput(null);
        }
    };

    const handleChange = (event) => {
        let input_string1 = event.target.value.match(/(([a-z]+:\/\/)?(([a-z0-9\-]+\.)+([a-z]{2}|aero|arpa|biz|com|coop|edu|gov|info|int|jobs|mil|museum|name|nato|net|org|pro|travel|local|internal))(:[0-9]{1,5})?(\/[a-z0-9_\-\.~]+)*(\/([a-z0-9_\-\.]*)(\?[a-z0-9+_\-\.%=&amp;]*)?)?(#[a-zA-Z0-9!$&'()*+.=-_~:@/?]*)?)(\s+|$)/gi);
		let input_string2 = event.target.value.match(/https?:\/\/\S+/gi);
		if (input_string1 !== null || input_string2 !== null) {
			if (input_string2 !== null) {
					return setInput(input_string2)
				}
			if (input_string1 !== null) {
				return setInput('https://' + input_string1)
			}
		}
	};


    return(
        <div className={classes.mainContainer}>
            <div className={classes.root}>
                <TextField
                    className={classes.inputField}
                    label='Search'
                    onChange={handleChange}
                    onKeyUp={handleDelete}
                    InputProps={{
                        endAdornment: (
                            <InputAdornment position="end">
                                <SearchIcon className={classes.icon} />
                            </InputAdornment>
                        )
                    }}
                    />
            </div>
            <div className={classes.root}>
                {(!!input && !debouncedQuery) &&
                    <div style={{top: '46%', left: '43%', position: 'absolute'}}>
                        <ReactLoading type={"cubes"} color={"#dc004e"}/>
                    </div>}
                {!!debouncedQuery &&
                    <Microlink
                        url={debouncedQuery}/>
                }
            </div>
        </div>
    )
}


