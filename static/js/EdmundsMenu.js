

// tutorial13.js

// var ModelMenu = React.createClass({
//   getInitialState: function() {
//     return {makes: []};
//   }
//
//   render: function() {
//     return (
//       <div className="ModelMenu">
//         <ModelSelect data={this.state.data} />
//       </div>>
//     );
//   }
// });

var MakeMenu = React.createClass({
  getInitialState: function() {
    return {makes: [],
            models: [],
            url1: this.props.url1,
            url2: this.props.url2};
  },
  componentDidMount: function() {
    $.ajax({
      url: this.state.url1,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({makes: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url1, status, err.toString());
      }.bind(this)
    });
    $.ajax({
      url: this.state.url2,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({models: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url2, status, err.toString());
      }.bind(this)
    });
  },
  handleMakeChange: function(event) {
    this.setState({chosenMake: event.target.selected});
    this.setState({url2: this.props.url2 + chosenMake});
    $.ajax({
      url: this.state.url2,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({models: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url2, status, err.toString());
      }.bind(this)
    });
  },
  render: function() {
    return (
      <div className="makeMenu">
        <h1>Select Make and Model</h1>
        <MakeSelect data={this.state.makes} onChange={this.handleMakeChange}/>
        <ModelSelect data={this.state.models} />
      </div>
    );
  }
});

var MakeSelect = React.createClass({
  render: function() {
    var makeNodes = this.props.data.map(function (make) {
      return (
        <MakeOption niceName={make.niceName}>
          {make.name}
        </MakeOption>
      );
    });
    return (
      <select className="makeSelect">
        {makeNodes}
      </select>
    );
  }
});

var ModelSelect = React.createClass({
  render: function() {
    var modelNodes = this.props.data.map(function (model) {
      return (
        <MakeOption niceName={model.niceName}>
          {model.name}
        </MakeOption>
      );
    });
    return (
      <select className="modelSelect">
        {modelNodes}
      </select>
    );
  }

});

var MakeOption = React.createClass({
  render: function() {
    return (
        <option className="makeOption" value="{this.props.niceName}">{this.props.children}</option>
    );
  }
});

React.render(
  <MakeMenu url1="_get_makes" url2="_get_models/am-general"/>,
  document.getElementById('content')
);
