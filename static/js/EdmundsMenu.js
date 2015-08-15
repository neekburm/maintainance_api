

// tutorial13.js

// var ModelMenu = React.createClass({
//   getInitialState: function() {
//     return {data: []};
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
    return {data: []};
  },
  componentDidMount: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  render: function() {
    return (
      <div className="makeMenu">
        <h1>Select Make and Model</h1>
        <MakeSelect data={this.state.data} />
      </div>
    );
  }
});

var MakeSelect = React.createClass({
  render: function() {
    var commentNodes = this.props.data.map(function (comment) {
      return (
        <MakeOption niceName={comment.niceName}>
          {comment.name}
        </MakeOption>
      );
    });
    return (
      <select className="makeSelect">
        {commentNodes}
      </select>
    );
  }
});

var MakeOption = React.createClass({
  render: function() {
    return (
        <option class="makeOption" value="{this.props.niceName}">{this.props.children}</option>
    );
  }
});

React.render(
  <MakeMenu url="_get_makes"/>,
  document.getElementById('content')
);
