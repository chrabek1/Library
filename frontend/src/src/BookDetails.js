import React from 'react';
import axios from 'axios'

export default class BookDetails extends React.Component {
  myHeaders = {"API_KEY": "H10JZ74AT8CBUY57TP87", 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': '*'}
  url = 'http://localhost:5001/'
  state = {
    rentals: null
  }
  onComponentDidMount() {
    this.getBookData()
  }
  getBookData() {
    axios.get(this.url+"book/"+this.props.data, {headers: this.myHeaders}).then(res => {
      this.setState({
        rentals: res.data["rentals"]
      })
    });
  }
  onRentHandle() {
    axios.post(this.url+"book/"+this.props.data+"/rent",{}, {headers: this.myHeaders}).then(res => {
      if (res.status == 200) {
        this.getRentalsData()
        console.log("GICIOR KSIĄŻKA WYPOŻYCZONA")
      }
    });
  }
  detailsRender() {
    let rentals = this.state.rentals.map((rental) => {
      return (
        <tr key={rental.rental_id}>
          <td>{rental.rental_id}</td>
          <br />
          <td>{rental.start_date}</td>
          <br />
          <td>{rental.end_date}</td>
          <br />
          <td>{rental.user_id}</td> 
        </tr>
      )
    });
    return (
      <tr>
        <button onClick={this.onRentHandle()}>Rent</button>
        <button onClick={this.onReturnHandle()}>Return</button>
        {rentals}
      </tr>

      )
  }
  onReturnHandle() {
    axios.post(this.url+"book/"+this.props.data+"/return",{}, {headers: this.myHeaders}).then(res => {
      if (res.status == 200) {
        this.getRentalsData()
        console.log("GICIOR KSIĄŻKA ODDANA")
      }
    });
  }
  render() {
    return (
      <div>
        {this.detailsRender()}
      </div>
      
    )
  }
}