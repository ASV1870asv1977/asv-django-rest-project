import logo from './logo.svg';
import './App.css';
import React from "react";
import AuthorItem from "./components/Authors";
import AuthorList from "./components/Authors";
import axios from "axios";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': []
        };
    }

    componentDidMount() {
        // const authors = [
        //     {
        //         'first_name': "Иван",
        //         'last_name': "Иванов",
        //         'birthday_year': 1990
        //     },
        //     {
        //         'first_name': "Сергей",
        //         'last_name': "Сергеев",
        //         'birthday_year': 1970
        //     }
        // ]

        // this.setState(
        //     this.state = {
        //         'authors': authors
        //     }
        // )

        axios
            .get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors
                    }
                )
            })
            .catch(error => console.log(error))

    }

    render() {
        return (
            // <div>Main App</div>
            // <AuthorItem author={{
            //     'first_name': "Иван",
            //     'last_name': "Иванов",
            //     'birthday_year': 1990
            // }}/>

            <AuthorList authors={this.state.authors}/>
        )
    }
}


// function App() {
//   return (
//     <div className="App">
//       <h2>Hello world</h2>
//     </div>
//   );
// }

export default App;
